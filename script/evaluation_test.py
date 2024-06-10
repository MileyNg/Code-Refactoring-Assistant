import requests
import pandas as pd
import matplotlib.pyplot as plt
import time

BASE_URL = "http://127.0.0.1:5000"

def get_initial_metrics(code):
    response = requests.post(f"{BASE_URL}/analyze", json={'code': code})
    return response.json()

def refactor_code(code):
    response = requests.post(f"{BASE_URL}/refactor", json={'code': code})
    return response.json()['refactored_code']

def refactor_code_again(original_code, refactor_history):
    response = requests.post(f"{BASE_URL}/refactor_again", json={
        'original_code': original_code,
        'refactor_history': refactor_history
    })
    return response.json()['further_refactored_code']

def run_experiment(code, iterations):
    data = []
    original_metrics = get_initial_metrics(code)
    refactor_history = [refactor_code(code)]

    for i in range(1, iterations + 1):
        metrics = get_initial_metrics(refactor_history[-1])
        data.append({
            'iteration': i,
            'cyclic_complexity': metrics['cyclic_complexity'],
            'loc': metrics['loc'],
            'maintainability_index': metrics['maintainability_index'],
            'halstead_volume': metrics['halstead_volume'],
            'halstead_difficulty': metrics['halstead_difficulty'],
            'halstead_effort': metrics['halstead_effort']
        })
        if i < iterations:
            refactor_history.append(refactor_code_again(code, refactor_history))
        time.sleep(1)  # Optional: Sleep to avoid rapid consecutive requests

    df = pd.DataFrame(data)
    df.to_csv('refactor_results.csv', index=False)
    return df

def plot_results(df):
    plt.figure(figsize=(14, 8))
    
    plt.subplot(2, 3, 1)
    plt.plot(df['iteration'], df['cyclic_complexity'], marker='o')
    plt.title('Cyclomatic Complexity')
    plt.xlabel('Iteration')
    plt.ylabel('Complexity')

    plt.subplot(2, 3, 2)
    plt.plot(df['iteration'], df['loc'], marker='o')
    plt.title('Lines of Code')
    plt.xlabel('Iteration')
    plt.ylabel('LOC')

    plt.subplot(2, 3, 3)
    plt.plot(df['iteration'], df['maintainability_index'], marker='o')
    plt.title('Maintainability Index')
    plt.xlabel('Iteration')
    plt.ylabel('Index')

    plt.subplot(2, 3, 4)
    plt.plot(df['iteration'], df['halstead_volume'], marker='o')
    plt.title('Halstead Volume')
    plt.xlabel('Iteration')
    plt.ylabel('Volume')

    plt.subplot(2, 3, 5)
    plt.plot(df['iteration'], df['halstead_difficulty'], marker='o')
    plt.title('Halstead Difficulty')
    plt.xlabel('Iteration')
    plt.ylabel('Difficulty')

    plt.subplot(2, 3, 6)
    plt.plot(df['iteration'], df['halstead_effort'], marker='o')
    plt.title('Halstead Effort')
    plt.xlabel('Iteration')
    plt.ylabel('Effort')

    plt.tight_layout()
    plt.savefig('refactor_metrics.png')
    plt.show()

if __name__ == "__main__":
    initial_code = """
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
        return calculate_discount(price, rate)
    else:
        return calculate_fee(price, rate)

original_price = 100
discount_rate = 0.1
fee_rate = 0.05

discounted_price = calculate_discount(original_price, discount_rate)
print(f"Discounted price: {discounted_price}")

fee_added_price = calculate_fee(original_price, fee_rate)
print(f"Price after fee added: {fee_added_price}")

processed_price = process_transaction(original_price, discount_rate, is_discount=True)
print(f"Processed price with discount: {processed_price}")

processed_price = process_transaction(original_price, fee_rate, is_discount=False)
print(f"Processed price with fee: {processed_price}")
"""
    iterations = 5
    df = run_experiment(initial_code, iterations)
    plot_results(df)