import requests
from datetime import datetime

print("=" * 50)
print("        GITHUB PROFILE ANALYZER")
print("=" * 50)

username = input("Enter GitHub Username: ")

url = f"https://api.github.com/users/{username}"

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    print("\n" + "=" * 50)

    print("Username            :", data["login"])
    print("Name                :", data["name"])
    print("Bio                 :", data["bio"])
    print("Location            :", data["location"])

    print("\n--- Profile Statistics ---")
    
    created_at = datetime.strptime(
        data["created_at"],
        "%Y-%m-%dT%H:%M:%SZ"
    )

    today = datetime.now()

    account_age = today.year - created_at.year

    print("Followers           :", data["followers"])
    print("Following           :", data["following"])
    print("Public Repositories :", data["public_repos"])

    print("\n--- Account Details ---")

    print("Account Created     :", created_at.date())
    print("Account Age         :", account_age, "Year(s)")

    print("\nProfile URL:")
    print(data["html_url"])

    print("=" * 50)

else:
    print("\nUser Not Found!")