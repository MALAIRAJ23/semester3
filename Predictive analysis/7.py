
day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
passengers = [10353, 92051, 10079, 10235, 10656, 10628, 11311, 96806, 86811, 99194]
period = 3
avg = []

for i in range(len(passengers)):
    if i < 1 or i > len(passengers) - 2:  
        avg.append(None) 
    else:
        avg.append((passengers[i - 1] + passengers[i] + passengers[i + 1]) / period)

valid_days = [day[i] for i in range(len(avg)) if avg[i] is not None] 
valid_smoothed = [value for value in avg if value is not None]

difference = [valid_smoothed[i + 1] - valid_smoothed[i] for i in range(len(valid_smoothed) - 1)]
trend_value = sum(difference) / len(difference)

predicted_value = valid_smoothed[-1] + trend_value
print(valid_smoothed)
print(difference)
print(trend_value)
print("Day\tPassengers\t Smoothed")
for i in range(len(day)):
    smoothed_value = avg[i] if avg[i] is not None else "-"
    print(f"{day[i]}\t{passengers[i]}\t\t{smoothed_value}")

print(f"\nPredicted passengers for the 11th day: {predicted_value}")
