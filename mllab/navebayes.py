# Sample data
data = [
    ['sunny', 'hot', 'high', 'false', 'no'], ['sunny', 'hot', 'high', 'true', 'no'],
    ['overcast', 'hot', 'high', 'false', 'yes'], ['rainy', 'mild', 'high', 'false', 'yes'],
    ['rainy', 'cool', 'normal', 'false', 'yes'], ['rainy', 'cool', 'normal', 'true', 'no'],
    ['overcast', 'cool', 'normal', 'true', 'yes'], ['sunny', 'mild', 'high', 'false', 'no'],
    ['sunny', 'cool', 'normal', 'false', 'yes'], ['rainy', 'mild', 'normal', 'false', 'yes'],
    ['sunny', 'mild', 'normal', 'true', 'yes'], ['overcast', 'mild', 'high', 'true', 'yes'],
    ['overcast', 'hot', 'normal', 'false', 'yes'], ['rainy', 'mild', 'high', 'true', 'no']
]

# Count occurrences
class_counts = {}
feature_counts = {}

for row in data:
    label = row[-1]  # Class label ('yes' or 'no')

    # Count class occurrences
    class_counts[label] = class_counts.get(label, 0) + 1

    # Count feature occurrences per class
    if label not in feature_counts:
        feature_counts[label] = [{} for _ in range(len(row) - 1)]

    for i, feature in enumerate(row[:-1]):
        feature_counts[label][i][feature] = feature_counts[label][i].get(feature, 0) + 1

# Print probabilities
print("Class Probabilities:")
for label, count in class_counts.items():
    print(f"P({label}) = {count / len(data):.4f}")

print("\nFeature Probabilities:")
for label, features in feature_counts.items():
    print(f"\nFor Class = {label}:")
    for i, feature_values in enumerate(features):
        for feature, count in feature_values.items():
            print(f"P({feature} | {label}) = {count / class_counts[label]:.4f}")