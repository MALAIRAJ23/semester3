n = int(input("Enter the packets of seeds: "))
c = int(input("Enter the number of companies: "))
mean_list=[]
mode_list=[]
for k in range(1, c + 1):
    l = []
    print("\n--- Company", k, "---")
    for i in range(1, n + 1):
        j = float(input("Enter the number of plants for packet " + str(i) + ": "))
        l.append(j)

    # Mean
    mean = sum(l) / len(l)
    print("The mean of the number of plants that grew from seeds of company", k, ":", mean)
    mean_list.append(mean)
    # Median
    sorted_l = sorted(l)
    if n % 2 != 0:
        median = sorted_l[n // 2]
    else:
        i1 = sorted_l[n // 2]
        i2 = sorted_l[(n // 2) - 1]
        median = (i1 + i2) / 2
    print("The median of the number of plants that grew from seeds of company", k, ":", median)
    
    # Mode
    freq = {}
    for value in sorted_l:
        freq[value] = freq.get(value, 0) + 1
    mode = max(freq, key=freq.get)
    print("The mode of the number of plants that grew from seeds of company", k, ":", mode)
    mode_list.append(mode)
    # Range
    range_num = max(l) - min(l)
    print("The range of the number of plants that grew from seeds of company", k, ":", range_num)
print("-Company with best mean-")
if mean_list[0] > mean_list[1]:
    print("Company 1 has a higher mean than Company 2.")
elif mean_list[0] < mean_list[1]:
    print("Company 2 has a higher mean than Company 1.")
else:
    print("Both companies have the same mean.")
print("-Company with best mode-")
if mode_list[0] > mode_list[1]:
    print("Company 1 has a higher mode than Company 2.")
elif mode_list[0] < mode_list[1]:
    print("Company 2 has a higher mode than Company 1.")
else:
    print("Both companies have the same mode.")