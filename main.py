# main.py
import os

def call_me():
    # Safely grab the secret from the env
    api_key = os.environ.get("CALL_ME")
    if not api_key:
        print("Environment variable CALL_ME is not set.")
    else:
        print(f"CALL_ME = the key exist no problem at all")

if __name__ == "__main__":
    call_me()
