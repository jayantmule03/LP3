
def fractional_knapsack(capacity, items):
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    total_value = 0

    for value, weight in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)
            break

    return total_value

n = int(input("Enter number of items: "))
items = []

for i in range(n):
    value = int(input("Enter value: "))
    weight = int(input("Enter weight: "))
    items.append((value, weight))

capacity = int(input("Enter knapsack capacity: "))
print("Maximum value:", fractional_knapsack(capacity, items))
