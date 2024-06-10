import os
import shutil
import pandas as pd

# raw data of AOJ code archive
source_codes_directory = "./documents/009"

# AOJ submission records
csv_file_path = "./documents/_submission_records_0000000_0999999.csv"

# new directory for the test programs that will be used
new_directory = './test_code'
if not os.path.exists(new_directory):
    os.makedirs(new_directory)

header = [
    "judge_id", "user_id", "problem_id", "language", "accuracy",
    "status", "cpu_time", "memory", "code_size", "submission_date", "judge_date"
]

# load csv data
df = pd.read_csv(csv_file_path, names=header)

# filter only functional python programs 
filtered_df = df[(df["language"].str.strip() == "Python") & (df["status"].str.strip() == "Accepted")]
judge_ids = filtered_df["judge_id"].astype(str).str.strip().str.replace('.txt', '', regex=False).tolist()

# change all the filtered program endings .txt to .py and copy to test_code directory
for filename in os.listdir(source_codes_directory):
    judge_id = os.path.splitext(filename)[0]
    if judge_id == "99999":
        print(judge_id)
    if judge_id in judge_ids:
        new_filename =  judge_id + ".py"
        source_path = os.path.join(source_codes_directory, filename)
        destination_path = os.path.join(new_directory, new_filename)
        try:
            shutil.copy2(source_path, destination_path)
        except OSError as e:
            print(f"Copy and renaming of {filename} to {new_filename} failed: {e}")

# Zählen der .py-Dateien im Verzeichnis
py_files_count = len([f for f in os.listdir(source_codes_directory) if f.endswith(".py")])
py_files_count_new = len([f for f in os.listdir(new_directory)])

# Vergleichen der Anzahl der judge_id"s mit der Anzahl der .py-Dateien
judge_ids_count = len(judge_ids)

print(f"Anzahl der judge_ids in der Liste: {judge_ids_count}")
print(f"Anzahl der .py-Dateien im Verzeichnis: {py_files_count}")
print(f"Anzahl der .py-Dateien im Verzeichnis: {py_files_count_new}")
