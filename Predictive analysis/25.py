# Given data
data = [24, 15, 20, 29, 19, 18, 22, 25, 27, 9, 17, 20, 15, 7]
median_h0 = 21.5

# Count positive and negative signs
positive_signs = sum(1 for x in data if x > median_h0)
negative_signs = sum(1 for x in data if x < median_h0)
n = positive_signs + negative_signs  # Total samples excluding ties

# Significance level
alpha = 0.01

# Critical value approximation for binomial distribution
critical_value = round(n * 0.5 + 2.33 * ((n * 0.5 * 0.5) ** 0.5))  # Normal approximation

# Print results
print(f"Positive Signs (S⁺) = {positive_signs}")
print(f"Negative Signs (S⁻) = {negative_signs}")
print(f"Total Valid Samples (n) = {n}")
print(f"Critical Value (α=0.01) ≈ {critical_value}")

# Decision
if positive_signs > critical_value:
    print("Reject H0: The median sulfur oxide emission is significantly greater than 21.5.")
else:
    print("Fail to Reject H0: No significant evidence that the median is greater than 21.5.")