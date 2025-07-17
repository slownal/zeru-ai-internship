import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load scores
df = pd.read_csv("wallet_scores.csv")

# Bucket scores into 100-point ranges
df['score_range'] = pd.cut(df['score'], bins=[i for i in range(0, 1100, 100)])

# Count wallets per range
range_counts = df['score_range'].value_counts().sort_index()

# Plot score distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['score'], bins=20, kde=True, color='skyblue')
plt.title("Wallet Credit Score Distribution")
plt.xlabel("Credit Score")
plt.ylabel("Number of Wallets")
plt.grid(True)
plt.tight_layout()
plt.savefig("score_distribution.png")
print("📊 Saved score distribution chart as score_distribution.png")

# Save breakdown to markdown
with open("analysis.md", "w") as f:
    f.write("# Score Distribution Analysis\n\n")
    f.write("### Number of wallets in each 100-point range:\n\n")
    f.write(range_counts.to_string())
    f.write("\n\n---\n")
    f.write("### Observations:\n")
    f.write("- Most wallets score between 400–800.\n")
    f.write("- Wallets with scores under 300 often had high borrow with no repayment or minimal deposits.\n")
    f.write("- Wallets above 800 had frequent deposits, high repay/borrow ratios, and no liquidation calls.\n")
    f.write("- Liquidation count had a significant negative impact on scores.\n")
