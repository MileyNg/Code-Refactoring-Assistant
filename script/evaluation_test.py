import os
from dotenv import load_dotenv
import requests
import time
import pandas as pd
from validate_test_code import login_to_judge, get_submission_records, get_problem_id, submit_code, check_submission_status, read_test_codes_from_folder

load_dotenv(dotenv_path="./app/.env")

judge_api = "https://judgeapi.u-aizu.ac.jp"
APP_URL = os.getenv("APP_URL")
USERNAME = os.getenv("AOJ_USERNAME")
PASSWORD = os.getenv("AOJ_PASSWORD")
test_code_folder = "./test_code/selected"
result_csv_file = "./documents/analysis_results6.csv"

def analyze_code(code):
    response = requests.post(f"{APP_URL}/analyze", json={"code": code}, timeout=30)
    return response.json()

def refactor_code(code):
    response = requests.post(f"{APP_URL}/refactor", json={"code": code}, timeout=60)
    return response.json()["refactored_code"]

def refactor_code_again(original_code, refactor_history):
    response = requests.post(f"{APP_URL}/refactor_again", json={"original_code": original_code, "refactor_history": refactor_history}, timeout=60)
    return response.json()["further_refactored_code"], response.json()["analysis"]

def evaluate_prototype():
    cookies = login_to_judge()
    if not cookies:
        print("Validation aborted due to login failure.")
        return
    submission_records = get_submission_records()
    test_codes = read_test_codes_from_folder(test_code_folder)
    results = []

    for filename, code in test_codes.items():
        print(f"Evaluating {filename}...")
        judge_id = os.path.splitext(filename)[0]
        problem_id = get_problem_id(judge_id, submission_records)
        if problem_id is None:
            print(f"Problem ID for judge_id {judge_id} not found.")
            continue

        initial_analysis = analyze_code(code)
        results.append({
            "filename": filename,
            "iteration": 0,
            "cyclic_complexity": initial_analysis["cyclic_complexity"],
            "loc": initial_analysis["loc"],
            "maintainability_index": initial_analysis["maintainability_index"],
            "halstead_volume": initial_analysis["halstead_volume"],
            "halstead_difficulty": initial_analysis["halstead_difficulty"],
            "halstead_effort": initial_analysis["halstead_effort"],
            "validation_status": "ACCEPTED"
        })
        refactor_history = []
        current_code = code

        # refactoring repetition for 5 times
        for i in range(5):
            refactored_code = refactor_code(current_code)
            refactor_history.append(refactored_code)
            analysis = analyze_code(refactored_code)

            # validate refactored code
            token = submit_code(problem_id, refactored_code, cookies, judge_id)
            if token:
                time.sleep(3)  # wait for the submission to be judged
                is_accepted = check_submission_status(token, cookies)
            else:
                is_accepted = False

            results.append({
                "filename": filename,
                "iteration": i + 1,
                "cyclic_complexity": analysis["cyclic_complexity"],
                "loc": analysis["loc"],
                "maintainability_index": analysis["maintainability_index"],
                "halstead_volume": analysis["halstead_volume"],
                "halstead_difficulty": analysis["halstead_difficulty"],
                "halstead_effort": analysis["halstead_effort"],
                "validation_status": "ACCEPTED" if is_accepted else "REJECTED"
            })

            if not is_accepted:
                break

            current_code = refactored_code

    df = pd.DataFrame(results)
    df.to_csv(result_csv_file, index=False)
    print(f"Results saved to {result_csv_file}")

if __name__ == "__main__":
    evaluate_prototype()
