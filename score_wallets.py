import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load features
df = pd.read_csv("wallet_features.csv")

print("📥 Loaded wallet features:")
print(df.head())

# Columns to use for scoring (you can tune this)
features = [
    'repay_to_borrow_ratio',
    'deposit_sum',
    'num_active_days',
    'redeem_to_deposit_ratio',
    'num_txn',
    'liquidationcall_count'
]

# Replace any NaNs or infinite values (safe cleanup)
df = df.replace([float('inf'), -float('inf')], 0).fillna(0)

# Normalize features
scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df[features])

# Define weights for scoring (you can tune these)
# [repay/borrow, deposit sum, active days, redeem ratio, txn count, liquidation count]
weights = [0.25, 0.2, 0.2, 0.15, 0.1, -0.5]  # Negative for liquidation

# Compute weighted score and scale to 0–1000
df['raw_score'] = df_scaled.dot(weights)
df['score'] = MinMaxScaler(feature_range=(0, 1000)).fit_transform(df[['raw_score']])

# Round for presentation
df['score'] = df['score'].round(2)

# Preview results
print("\n📊 Sample Wallet Scores:")
print(df[['wallet', 'score']].head())

# Save to CSV
df[['wallet', 'score']].to_csv("wallet_scores.csv", index=False)
print("\n✅ Saved scores to wallet_scores.csv")
