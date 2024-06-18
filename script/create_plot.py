import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read each CSV file into a separate DataFrame
df_1 = pd.read_csv("../documents/analysis_results1.csv")
df_2 = pd.read_csv("../documents/analysis_results2.csv")
df_3 = pd.read_csv("../documents/analysis_results3.csv")
df_4 = pd.read_csv("../documents/analysis_results4.csv")
df_5 = pd.read_csv("../documents/analysis_results5.csv")
df_6 = pd.read_csv("../documents/analysis_results6.csv")
df_7 = pd.read_csv("../documents/analysis_results7.csv")
df_8 = pd.read_csv("../documents/analysis_results8.csv")
df_9 = pd.read_csv("../documents/analysis_results9.csv")
df_10 = pd.read_csv("../documents/analysis_results10.csv")

# combined DataFrame
combined_df = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10], keys=['Run1', 'Run2', 'Run3', 'Run4', 'Run5', 'Run6', 'Run7', 'Run8', 'Run9', 'Run10'], names=['Run', 'Index']).reset_index(level='Run')
filenames = combined_df['filename'].unique()

# list of metrics
metrics = ['cyclic_complexity', 'loc', 'maintainability_index', 'halstead_volume', 'halstead_difficulty', 'halstead_effort']

# plotting improvements across iterations for given metric and filename
def plot_improvement_by_filename(metric, filename):
    plt.figure(figsize=(12, 8))
    sns.lineplot(data=combined_df[combined_df['filename'] == filename], x='iteration', y=metric, hue='Run', marker='o', estimator=None)
    plt.title(f"{metric.title()} across iterations for {filename}")
    plt.xlabel("Iteration")
    plt.ylabel(metric)
    plt.legend(title='Run', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

# Generate plots for each metric
#for metric in metrics:
 
    #plot_improvement(metric)
    #print(df_1["validation_status"])

for metric in metrics:
    plot_improvement_by_filename(metric, filenames[1])

# # Compare metrics before and after refactoring
# def compare_metrics(metric):
#     original_metric = original_results.set_index('filename')[metric]
#     refactored_metric = refactored_results.groupby('filename')[metric].last()
    
#     comparison_df = pd.DataFrame({
#         'original': original_metric,
#         'refactored': refactored_metric
#     }).dropna()

#     print(f"\nComparison of {metric} before and after refactoring:")
#     print(comparison_df.describe())
    
#     sns.boxplot(data=comparison_df, orient='h')
#     plt.title(f"Comparison of {metric} before and after refactoring")
#     plt.xlabel(metric)
#     plt.show()

# # List of metrics to compare
# metrics = ['cyclic_complexity', 'loc', 'maintainability_index', 'halstead_volume', 'halstead_difficulty', 'halstead_effort']

# for metric in metrics:
#     compare_metrics(metric)

# # Identify patterns in validation status
# validation_counts = df['validation_status'].value_counts()
# print("\nValidation status counts:")
# print(validation_counts)

# sns.countplot(data=df, x='validation_status')
# plt.title("Validation Status Counts")
# plt.xlabel("Validation Status")
# plt.ylabel("Count")
# plt.xticks(rotation=45)
# plt.show()

# # Plotting improvements across iterations
# def plot_improvement(metric):
#     sns.lineplot(data=df, x='iteration', y=metric, hue='filename', marker='o')
#     plt.title(f"Improvements in {metric} Across Iterations")
#     plt.xlabel("Iteration")
#     plt.ylabel(metric)
#     plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
#     plt.show()

# for metric in metrics:
#     plot_improvement(metric)
