import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the results from the CSV file
results_csv_file = "../documents/analysis_results1.csv"
df = pd.read_csv(results_csv_file)

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Convert appropriate columns to numeric, coercing errors and handling NaN values
numeric_columns = ['cyclic_complexity', 'loc', 'maintainability_index', 'halstead_volume', 'halstead_difficulty', 'halstead_effort']

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors='coerce')

# Fill NaN values with a placeholder (e.g., -1) to avoid issues during sorting and analysis
df[numeric_columns] = df[numeric_columns].fillna(-1)

# Ensure 'filename' and 'validation_status' are treated as categorical data
df['filename'] = df['filename'].astype(str)
df['validation_status'] = df['validation_status'].astype(str)

# Descriptive statistics for each metric
print("\nDescriptive Statistics for each metric:")
print(df.describe())

# Separate original and refactored results
original_results = df[df['iteration'] == 0]
refactored_results = df[df['iteration'] > 0]

# Compare metrics before and after refactoring
def compare_metrics(metric):
    original_metric = original_results.set_index('filename')[metric]
    refactored_metric = refactored_results.groupby('filename')[metric].last()
    
    comparison_df = pd.DataFrame({
        'original': original_metric,
        'refactored': refactored_metric
    }).dropna()

    print(f"\nComparison of {metric} before and after refactoring:")
    print(comparison_df.describe())
    
    sns.boxplot(data=comparison_df, orient='h')
    plt.title(f"Comparison of {metric} before and after refactoring")
    plt.xlabel(metric)
    plt.show()

# List of metrics to compare
metrics = ['cyclic_complexity', 'loc', 'maintainability_index', 'halstead_volume', 'halstead_difficulty', 'halstead_effort']

for metric in metrics:
    compare_metrics(metric)

# Identify patterns in validation status
validation_counts = df['validation_status'].value_counts()
print("\nValidation status counts:")
print(validation_counts)

sns.countplot(data=df, x='validation_status')
plt.title("Validation Status Counts")
plt.xlabel("Validation Status")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Plotting improvements across iterations
def plot_improvement(metric):
    sns.lineplot(data=df, x='iteration', y=metric, hue='filename', marker='o')
    plt.title(f"Improvements in {metric} Across Iterations")
    plt.xlabel("Iteration")
    plt.ylabel(metric)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

for metric in metrics:
    plot_improvement(metric)
