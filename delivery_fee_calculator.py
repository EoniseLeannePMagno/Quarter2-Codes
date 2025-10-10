def calculate_delivery_fee(distance, rate_per_kilometer):
    return distance * rate_per_kilometer
a = int(input("Enter distance in kilometers: "))
b = float(input("Enter rate per kilometer (₱): "))
c = calculate_delivery_fee(a, b)
print("Total delivery fee: ₱", c)