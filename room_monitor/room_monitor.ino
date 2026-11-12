/*
 * Code Mind – ESP32 Room Monitor
 * Reads a DHT22 and serves temperature/humidity on a local web page.
 *
 * Wiring
 *   DHT22 pin      ESP32 pin      Wire colour (suggested)
 *   + (VCC)        3V3            Red
 *   OUT (Data)     GPIO 4 (D4)    Yellow
 *   - (GND)        GND            Black
 */

#include <WiFi.h>
#include <WebServer.h>
#include <DHT.h>

#include "secrets.h"   // WIFI_SSID / WIFI_PASS — copy secrets.example.h to secrets.h

#define DHTPIN  4
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);
WebServer server(80);

float temperature = NAN;
float humidity    = NAN;
unsigned long lastRead = 0;

const char PAGE[] = R"rawliteral(
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Room Monitor</title>
  <style>
    body  { font-family: sans-serif; background: #0f172a; color: #e2e8f0;
            text-align: center; margin: 0; padding: 24px; }
    .card { background: #1e293b; border-radius: 16px; padding: 20px;
            margin: 16px auto; max-width: 320px; }
    .val  { font-size: 48px; font-weight: bold; }
    .lbl  { color: #94a3b8; }
  </style>
</head>
<body>
  <h2>Code Mind Room Monitor</h2>

  <div class="card">
    <div class="lbl">Temperature</div>
    <div class="val" id="t">--</div>
  </div>

  <div class="card">
    <div class="lbl">Humidity</div>
    <div class="val" id="h">--</div>
  </div>

  <script>
    async function update() {
      try {
        const r = await fetch('/data');
        const d = await r.json();
        document.getElementById('t').textContent =
          d.t === null ? 'Error' : d.t.toFixed(1) + ' °C';
        document.getElementById('h').textContent =
          d.h === null ? 'Error' : d.h.toFixed(1) + ' %';
      } catch (e) {}
    }
    update();
    setInterval(update, 2000);
  </script>
</body>
</html>
)rawliteral";

void handleRoot() {
  server.send(200, "text/html", PAGE);
}

void handleData() {
  String json = "{\"t\":";
  json += isnan(temperature) ? "null" : String(temperature, 1);
  json += ",\"h\":";
  json += isnan(humidity) ? "null" : String(humidity, 1);
  json += "}";
  server.send(200, "application/json", json);
}

void setup() {
  Serial.begin(115200);
  dht.begin();

  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASS);

  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();
  Serial.print("Open this on your phone: http://");
  Serial.println(WiFi.localIP());

  server.on("/", handleRoot);
  server.on("/data", handleData);
  server.begin();
}

void loop() {
  server.handleClient();

  // DHT22 needs at least 2 seconds between readings
  if (millis() - lastRead >= 2500) {
    lastRead = millis();

    float t = dht.readTemperature();
    float h = dht.readHumidity();

    if (!isnan(t) && !isnan(h)) {
      temperature = t;
      humidity    = h;
    } else {
      Serial.println("DHT22 read failed");
    }
  }
}
