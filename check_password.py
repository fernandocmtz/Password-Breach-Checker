import requests
import hashlib
import sys

def check_password(password):
    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if suffix in response.text:
        print("⚠️ Your password has been leaked! Consider changing it.")
    else:
        print("✅ Your password is safe.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_password.py <your_password>")
    else:
        check_password(sys.argv[1])
