# Ep 2: variables, types and math, the AI way
# A spam filter checked 200 emails. How good is it really?

model_name = "Spam filter v1"   # str: text
total = 200                     # int: whole number
correct = 172                   # int
is_ready = False                # bool: True or False

accuracy = correct / total      # float: / always gives a float
print(model_name, "accuracy:", accuracy)
print(f"{model_name}: {accuracy:.1%} accurate")

is_ready = accuracy >= 0.9
print("Ready to ship?", is_ready)

# The lazy model: it says "not spam" for every email
spam = 20
not_spam = total - spam
lazy_accuracy = not_spam / total
print(f"Lazy model: {lazy_accuracy:.1%} accurate, spam caught: 0 of {spam}")

# Where Spam filter v1 was right and wrong
tp = 14    # spam, caught
fn = 6     # spam, missed
fp = 22    # normal email, wrongly flagged
tn = 158   # normal email, left alone

accuracy = (tp + tn) / total
recall = tp / (tp + fn)
print(f"Accuracy: {accuracy:.1%}  Recall: {recall:.1%}")
