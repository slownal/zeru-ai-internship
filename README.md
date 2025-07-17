# Zeru Credit Score

This repository is part of the Zeru AI Engineer Internship Assignment. The aim is to create a machine learning-driven system that assesses the creditworthiness of wallets (scored from 0 to 1000) using raw DeFi transaction data from the Aave V2 protocol.

---

## 🚀 Problem Statement

You are given 100,000 raw transaction-level JSON records of wallets interacting with the Aave V2 protocol through the following actions:

- `deposit`
- `borrow`
- `repay`
- `redeemunderlying`
- `liquidationcall`

Your objectives are:
- Engineer insightful features for each wallet
- Develop a scoring mechanism to determine the risk or safety of every wallet
- Produce a normalized credit score (0–1000) for each wallet
- Examine the score distribution and interpret the patterns

---

## 🛠️ Project Structure

```
zeru-credit-score/
│
├── main.py                  # Loads JSON and extracts features per wallet
├── score_wallets.py         # Calculates credit scores using normalized features
├── analyze_scores.py        # Visualizes score distribution and summarizes insights
│
├── user_transactions.json   # Input dataset (~100K records)
├── wallet_features.csv      # Engineered wallet-level features
├── wallet_scores.csv        # Final credit scores for each wallet
├── score_distribution.png   # Histogram of score distribution
├── analysis.md              # Insights and patterns from scoring results
└── requirements.txt         # Python dependency list (optional)
```

🔍 Features Engineered per Wallet
| Feature                   | Description                                        |
| ------------------------- | -------------------------------------------------- |
| `num_txn`                 | Total number of transactions                       |
| `num_active_days`         | Number of unique days the wallet was active        |
| `deposit_sum`             | Aggregate deposit volume                          |
| `borrow_sum`              | Aggregate borrow volume                           |
| `repay_sum`               | Aggregate repay volume                            |
| `redeemunderlying_sum`    | Aggregate redemption volume                       |
| `liquidationcall_count`   | Count of liquidation events                       |
| `repay_to_borrow_ratio`   | Repay-to-borrow volume ratio (risk indicator)     |
| `redeem_to_deposit_ratio` | Ratio of redeemed to deposited (capital cycling)  |

🎯 Scoring Logic
Credit scores are determined by a weighted combination of normalized features:
Score = 
    + 0.25 * (repay_to_borrow_ratio)
    + 0.20 * (deposit_sum)
    + 0.20 * (num_active_days)
    + 0.15 * (redeem_to_deposit_ratio)
    + 0.10 * (txn_count)
    - 0.50 * (liquidation_count)
All features are normalized using MinMaxScaler, and the resulting scores are scaled to the [0, 1000] range.

📈 Score Distribution
Scores typically range from about 200 to 950.

The majority of wallets score between 400 and 800.

Higher scores are linked to responsible behaviors:

- High repay/borrow ratios
- Absence of liquidations
- Regular deposits and redemptions

Lower scores are associated with:

- Minimal or no repayments
- High borrowing activity
- Presence of liquidation events

For a comprehensive breakdown, refer to analysis.md and score_distribution.png.

💻 How to Run
1. Set up your environment:

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

2. Execute the pipeline:

```bash
python main.py           # Step 1: Extract features from raw JSON
python score_wallets.py  # Step 2: Score wallets based on features
python analyze_scores.py # Step 3: Analyze and plot results
```

📄 Requirements
You may install dependencies individually or use:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn tqdm
```

📬 Submission
Your final submission should include:

- Source code (GitHub link)
- wallet_scores.csv, score_distribution.png, analysis.md, and README.md
- Submission via the provided Google Form

👤 Author
G Om Sai
B.Tech (CSE) | Applicant for AI Engineer Internship @ Zeru

---