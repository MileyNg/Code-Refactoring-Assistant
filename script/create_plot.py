import pandas as pd
import matplotlib.pyplot as plt

def plot_results(csv_file):
    df = pd.read_csv(csv_file)
    
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
    plot_results('refactor_results.csv')
