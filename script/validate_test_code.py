import os
from dotenv import load_dotenv
import requests
import time
import pandas as pd

load_dotenv(dotenv_path="../app/.env")

judge_api = "https://judgeapi.u-aizu.ac.jp"
APP_URL = os.getenv("APP_URL")
USERNAME = os.getenv("AOJ_USERNAME")
PASSWORD = os.getenv("AOJ_PASSWORD")
test_code_folder = "./test_code/selected"
csv_file_path = "./documents/_submission_records_0000000_0999999.csv"

def login_to_judge():
    response = requests.post(f"{judge_api}/session", json={
        "id": USERNAME,
        "password": PASSWORD
    })
    return response.cookies

def get_submission_records():
    header = [
        "judge_id", "user_id", "problem_id", "language", "accuracy",
        "status", "cpu_time", "memory", "code_size", "submission_date", "judge_date"
    ]   
    return pd.read_csv(csv_file_path, names=header)

def get_problem_id(judge_id, submission_records):
    record = submission_records[submission_records["judge_id"].str.strip() == judge_id]
    if not record.empty:
        return record.iloc[0]["problem_id"]
    return None


def submit_code(problem_id, source_code, cookies):
    response = requests.post(f"{judge_api}/submissions", json={
        "problemId": problem_id,
        "language": "Python3",
        "sourceCode": source_code
    }, cookies=cookies)
    return response.json()["token"]

def check_submission_status(cookies):
    response = requests.get(f"{judge_api}/submission_records/users/{USERNAME}", cookies=cookies)
    records = response.json()
    if not records:
        return None
    latest_submission = records[0]
    return latest_submission["status"] == 4, latest_submission

def read_test_codes_from_folder(folder_path):
    test_codes = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".py"):
            with open(os.path.join(folder_path, filename), "r") as file:
                test_codes[filename] = file.read()
    return test_codes

def validate_code_files():
    cookies = login_to_judge()
    submission_records = get_submission_records()
    test_codes = read_test_codes_from_folder(test_code_folder)

    validation_results = []

    for filename, code in test_codes.items():
        judge_id = filename
        problem_id = get_problem_id(judge_id, submission_records).str.strip()
        
        if problem_id is None:
            print(f"Problem ID for judge_id {judge_id} not found.")
            continue
        token = submit_code(problem_id, code, cookies)
        time.sleep(5)  # Wait for the submission to be judged
        is_accepted, submission_details = check_submission_status(cookies)

        validation_results.append({
            'filename': filename,
            'judge_id': judge_id,
            'problem_id': problem_id,
            'status': 'ACCEPTED' if is_accepted else 'REJECTED',
            'submission_details': submission_details
        })

    return validation_results

if __name__ == "__main__":
    results = validate_code_files()
    for result in results:
        print(f"File: {result['filename']} - Status: {result['status']} - Problem ID: {result['problem_id']}")
