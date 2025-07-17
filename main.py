import json
import pandas as pd
from tqdm import tqdm

# Load JSON data
def load_data(path):
    print("📥 Loading JSON...")
    with open(path, 'r') as f:
        data = json.load(f)
    print(f"✅ Loaded {len(data)} transactions.")
    return pd.DataFrame(data)

# Feature engineering per wallet
def extract_wallet_features(df):
    print("🛠️ Extracting features per wallet...")

    df.rename(columns={'userWallet': 'user'}, inplace=True)  # if not already done
    df['amount'] = pd.to_numeric(df['actionData'].apply(lambda x: x.get('amount', 0)), errors='coerce').fillna(0)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s', errors='coerce')

    wallet_stats = []

    for user, user_df in tqdm(df.groupby('user'), desc="Processing wallets"):
        stats = {}
        stats['wallet'] = user
        stats['num_txn'] = len(user_df)
        stats['num_active_days'] = user_df['timestamp'].dt.date.nunique()
        stats['avg_amount_per_txn'] = user_df['amount'].mean()

        # For each action
        for action in ['deposit', 'borrow', 'repay', 'redeemunderlying', 'liquidationcall']:
            action_df = user_df[user_df['action'] == action]
            stats[f'{action}_count'] = len(action_df)
            stats[f'{action}_sum'] = action_df['amount'].sum()

        # Ratios
        stats['repay_to_borrow_ratio'] = (
            stats['repay_sum'] / stats['borrow_sum']
            if stats['borrow_sum'] > 0 else 0
        )
        stats['redeem_to_deposit_ratio'] = (
            stats['redeemunderlying_sum'] / stats['deposit_sum']
            if stats['deposit_sum'] > 0 else 0
        )

        wallet_stats.append(stats)

    return pd.DataFrame(wallet_stats)

# Main
if __name__ == '__main__':
    df = load_data("user_transactions.json")
    wallet_df = extract_wallet_features(df)

    print("\n📊 Sample Wallet Features:")
    print(wallet_df.head())

    wallet_df.to_csv("wallet_features.csv", index=False)
    print("\n✅ Saved wallet features to wallet_features.csv")
