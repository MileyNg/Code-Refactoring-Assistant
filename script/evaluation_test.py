import os
from dotenv import load_dotenv
import requests
import pandas as pd
import time


load_dotenv(dotenv_path="../app/.env")

JUDGE_API_APP_URL = "https://judgeapi.u-aizu.ac.jp"
APP_URL = os.getenv("APP_URL")
USERNAME = os.getenv("AOJ_USERNAME")
PASSWORD = os.getenv("AOJ_PASSWORD")

def get_initial_metrics(code):
    response = requests.post(f"{APP_URL}/analyze", json={"code": code})
    return response.json()

def refactor_code(code):
    response = requests.post(f"{APP_URL}/refactor", json={"code": code})
    return response.json()["refactored_code"]

def refactor_code_again(original_code, refactor_history):
    response = requests.post(f"{APP_URL}/refactor_again", json={
        "original_code": original_code,
        "refactor_history": refactor_history
    })
    return response.json()["further_refactored_code"]

def login_to_judge():
    response = requests.post(f"{JUDGE_API_APP_URL}/session", json={
        "id": USERNAME,
        "password": PASSWORD
    })
    return response.cookies

def submit_code(problem_id, language, source_code, cookies):
    response = requests.post(f"{JUDGE_API_APP_URL}/submissions", json={
        "problemId": problem_id,
        "language": language,
        "sourceCode": source_code
    }, cookies=cookies)
    return response.json()["token"]

def check_submission_status(cookies):
    response = requests.get(f"{JUDGE_API_APP_URL}/submission_records/users/{USERNAME}", cookies=cookies)
    records = response.json()
    if not records:
        return None
    latest_submission = records[0]
    return latest_submission["status"] == 4, latest_submission["token"]

def run_experiment(code, problem_id, iterations):
    cookies = login_to_judge()
    data = []
    original_metrics = get_initial_metrics(code)
    refactor_history = [refactor_code(code)]

    for i in range(1, iterations + 1):
        metrics = get_initial_metrics(refactor_history[-1])
        token = submit_code(problem_id, "Python3", refactor_history[-1], cookies)
        time.sleep(5)  # Wait for the submission to be judged
        is_accepted, submission_token = check_submission_status(cookies)

        data.append({
            "iteration": i,
            "cyclic_complexity": metrics["cyclic_complexity"],
            "loc": metrics["loc"],
            "maintainability_index": metrics["maintainability_index"],
            "halstead_volume": metrics["halstead_volume"],
            "halstead_difficulty": metrics["halstead_difficulty"],
            "halstead_effort": metrics["halstead_effort"],
            "status": "ACCEPTED" if is_accepted else "REJECTED",
            "token": submission_token
        })

        if i < iterations:
            if is_accepted:
                refactor_history.append(refactor_code_again(code, refactor_history))
            else:
                # If the refactored code is not accepted, stop further refactoring
                break

        time.sleep(1)  # Optional: Sleep to avoid rapid consecutive requests

    df = pd.DataFrame(data)
    df.to_csv("refactor_results.csv", index=False)
    return df

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
    problem_id = "ITP1_1_A"
    df = run_experiment(initial_code, problem_id, iterations)
