import os

def call_me():
    # Read the environment variable CALL_ME
    call_me_key = os.environ.get("CALL_ME")
    if call_me_key is None:
        print("Environment variable CALL_ME is not set.")
    else:
        print(f"CALL_ME = {call_me_key}")

if __name__ == "__main__":
    call_me()
