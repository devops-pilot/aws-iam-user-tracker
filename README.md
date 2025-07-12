# 🔐 AWS IAM User Tracker

Track and audit your AWS IAM users — spot inactive accounts, privileged users, and potential risks.

---

## 🔍 Features

- Lists all IAM users in your AWS account
- Shows:
  - Username
  - Created Date
  - Last Console/API/CLI Use
  - Count of Attached & Inline Policies
- Flags:
  - ❌ Inactive users (90+ days)
  - ⚠️ Admin access
- Color-coded CLI output

---

## 📁 Project Structure
```
aws-iam-user-tracker/
├── tracker.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Usage

### 1. Install dependencies

```bash
pip install -r requirements.txt
```
## 2. Configure AWS credentials
##### Make sure you’re authenticated via:
```
aws configure
```
#### Or via a profile:
```
export AWS_PROFILE=your-profile
```
## 3. Run the script
```
python3 tracker.py
```
## 🧪 Sample Output
```
🔍 Fetching IAM Users...

+----------------+------------+------------+-------------------+-----------------+-----------------------+
| Username       | Created    | Last Used  | Attached Policies | Inline Policies | Status                |
+----------------+------------+------------+-------------------+-----------------+-----------------------+
| alice          | 2022-12-01 | 2023-12-28 | 1                 | 0               | ✔️ Active              |
| dev-admin      | 2021-03-03 | Never      | 1                 | 2               | ⚠️ Admin Access        |
| intern-user    | 2021-01-01 | 2021-05-01 | 0                 | 0               | ❌ Inactive > 90d      |
+----------------+------------+------------+-------------------+-----------------+-----------------------+
```
## 🧠 Notes
- Doesn't delete or modify anything — safe to run
- Supports AWS profiles and default credential chain
- Extendable: Add MFA check, group memberships, etc.
## 📝 License
- MIT
## 🙌 Contributions
- Star it ⭐ — Fork it 🍴 — PRs welcome!
