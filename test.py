def calculate_discount(price, discount_rate):
    if price <= 0:
        return 0
    discount = price * discount_rate
    final_price = price - discount
    return final_price

def calculate_fee(price, fee_rate):
    if price <= 0:
        return 0
    fee = price * fee_rate
    final_price = price + fee
    return final_price

def process_transaction(price, rate, is_discount=True):
    if is_discount:
        if price <= 0:
            return 0
        discount = price * rate
        final_price = price - discount
        return final_price
    else:
        if price <= 0:
            return 0
        fee = price * rate
        final_price = price + fee
        return final_price

# Example usage
original_price = 100
discount_rate = 0.2
fee_rate = 0.05

discounted_price = calculate_discount(original_price, discount_rate)
print(f"Discounted price: {discounted_price}")

fee_added_price = calculate_fee(original_price, fee_rate)
print(f"Price after fee added: {fee_added_price}")

# Process transaction can handle both cases with a single function call
processed_price = process_transaction(original_price, discount_rate, is_discount=True)
print(f"Processed price with discount: {processed_price}")
processed_price = process_transaction(original_price, fee_rate, is_discount=False)
print(f"Processed price with fee: {processed_price}")
