import os
from dotenv import load_dotenv
import requests
import time
import pandas as pd

load_dotenv(dotenv_path="./app/.env")

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
    }, timeout=5)
     
    if response.status_code == 200:
        print("Login successfull.")
        return response.cookies
    else:
        print(f"Login failed with status code {response.status_code}.")
        return None

def get_submission_records():
    header = [
        "judge_id", "user_id", "problem_id", "language", "accuracy",
        "status", "cpu_time", "memory", "code_size", "submission_date", "judge_date"
    ]
    df_submissions = pd.read_csv(csv_file_path, names=header)

    return df_submissions

def get_problem_id(judge_id, submission_records):
    record = submission_records[(submission_records["judge_id"].astype(str).str.strip() == judge_id)]
    if not record.empty:
        return record.iloc[0]["problem_id"]
    return None


def submit_code(problem_id, source_code, cookies, judge_id):
    response = requests.post(f"{judge_api}/submissions", json={
        "problemId": problem_id.strip(),
        "language": "Python3",
        "sourceCode": f"""{source_code}"""
    }, cookies=cookies, timeout=10)

    if response.status_code == 200:
        return response.json()["token"]
    elif response.status_code == 404:
        print(f"Problem not found for judge_id {judge_id}. Skipping this submission.")
        return None
    else:
        print(f"An error occurred with status code {response.status_code}")
        return None

def check_submission_status(token, cookies):
    response = requests.get(f"{judge_api}/submission_records/recent", cookies=cookies, timeout=5)
    records = response.json()
    for record in records:
        if record["token"] == token:
            return record["status"] == 4
    return False

def read_test_codes_from_folder(folder_path):
    test_codes = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".py"):
            with open(os.path.join(folder_path, filename), "r") as file:
                test_codes[filename] = file.read()
    return test_codes

def validate_code_files():
    cookies = login_to_judge()    
    if not cookies:
        print("Validation aborted due to login failure.")
        return []
    submission_records = get_submission_records()
    test_codes = read_test_codes_from_folder(test_code_folder)

    validation_results = []
        
    for filename, code in test_codes.items():
        judge_id = os.path.splitext(filename)[0]
        problem_id = get_problem_id(judge_id, submission_records)
        if problem_id is None:
            print(f"Problem ID for judge_id {judge_id} not found.")
        else:
            token = submit_code(problem_id, code, cookies, judge_id)
            if token is None:
                is_accepted = False
            else:
                time.sleep(3)  # Wait for the submission to be judged
                is_accepted = check_submission_status(token, cookies)
                if not is_accepted:
                    print(f"Error: Submission for judge_id {judge_id} was not accepted.")
            
            validation_results.append({
                "filename": filename,
                "judge_id": judge_id,
                "problem_id": problem_id,
                "status": "ACCEPTED" if is_accepted else "REJECTED",
            })
            
    return validation_results

if __name__ == "__main__":

    results = validate_code_files()
    for result in results:
        print(f"File: {result['filename']} - Status: {result['status']} - Problem ID: {result['problem_id']}")