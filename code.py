foods = ["Biriyani", "Ice Cream", "Gobi Manchurian", "Red Velvet", "Waffles", "Burger", "Pizza"]

n = len(foods)  # sorting my favourite foods by their name length using bubble sort
for i in range(n):
    for j in range(0, n - i - 1):
        if len(foods[j]) > len(foods[j + 1]):
            foods[j], foods[j + 1] = foods[j + 1], foods[j]

print("Foods sorted by length:", foods)
