price = float(input("Enter the total amount: "))
discount = float(input("Enter the discount percentage: "))

discount_value = (price * discount) / 100
final_price = price - discount_value

print("Discount is", discount_value)
print("Discounted price is", final_price)