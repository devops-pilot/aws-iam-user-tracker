import boto3
from datetime import datetime, timezone, timedelta
from tabulate import tabulate
from colorama import Fore, Style

iam = boto3.client("iam")

def get_days_since(date_str):
    if not date_str:
        return None
    dt = date_str.replace(tzinfo=timezone.utc)
    return (datetime.now(timezone.utc) - dt).days

def get_user_last_used(username):
    try:
        response = iam.get_user(UserName=username)
        last_used = response["User"].get("PasswordLastUsed")
        return last_used
    except Exception:
        return None

def fetch_users():
    paginator = iam.get_paginator("list_users")
    users = []

    for page in paginator.paginate():
        for user in page["Users"]:
            username = user["UserName"]
            created = user["CreateDate"]
            last_used = get_user_last_used(username)

            # Attached policies
            policies_resp = iam.list_attached_user_policies(UserName=username)
            attached_policies = [p["PolicyName"] for p in policies_resp.get("AttachedPolicies", [])]

            # Inline policies
            inline_resp = iam.list_user_policies(UserName=username)
            inline_policies = inline_resp.get("PolicyNames", [])

            days_unused = get_days_since(last_used) if last_used else "N/A"
            status = ""

            if days_unused != "N/A" and days_unused > 90:
                status = f"{Fore.YELLOW}❌ Inactive > 90d{Style.RESET_ALL}"
            elif "AdministratorAccess" in attached_policies:
                status = f"{Fore.RED}⚠️ Admin Access{Style.RESET_ALL}"
            else:
                status = f"{Fore.GREEN}✔️ Active{Style.RESET_ALL}"

            users.append([
                username,
                created.strftime("%Y-%m-%d"),
                last_used.strftime("%Y-%m-%d") if last_used else "Never",
                len(attached_policies),
                len(inline_policies),
                status
            ])
    return users

if __name__ == "__main__":
    print(f"\n🔍 Fetching IAM Users...\n")
    table = fetch_users()
    headers = ["Username", "Created", "Last Used", "Attached Policies", "Inline Policies", "Status"]
    print(tabulate(table, headers=headers, tablefmt="pretty"))
