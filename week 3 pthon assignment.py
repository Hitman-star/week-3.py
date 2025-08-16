def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying discount.
    If discount is 20% or more, apply it, otherwise return original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

try:
    original_price = float(input("original price ( 1000): "))
    discount = float(input("discount percentage ( 20): "))

    final_price = calculate_discount(original_price, discount)

    if discount >= 20:
        print(f"The final price after a {discount}% discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: {final_price:.2f}")
except ValueError:
    print("valid numbers for price and discount.")