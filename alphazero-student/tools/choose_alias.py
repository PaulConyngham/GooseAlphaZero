import os
import json
from pathlib import Path

CRED_PATH = Path(__file__).parent / ".alphazero_user"


def prompt_for_alias(old_alias=None):
    if old_alias:
        print(f"Your last alias was '{old_alias}'.")
        use_old = input("Would you like to use this alias again? (y/n): ").strip().lower()
        if use_old == 'y':
            print(f"Continuing as {old_alias}.")
            return old_alias
    # Else
    alias = input("Enter a new alias (username): ").strip()
    while not alias:
        alias = input("Alias cannot be empty. Please enter a new alias: ").strip()
    return alias

def main():
    old_alias = None
    if CRED_PATH.exists():
        try:
            with CRED_PATH.open("r") as f:
                data = json.load(f)
                old_alias = data.get("alias")
        except Exception:
            old_alias = None

    alias = prompt_for_alias(old_alias)

    # Always overwrite file with current alias
    with CRED_PATH.open("w") as f:
        json.dump({"alias": alias}, f)

    print(alias)  # print the chosen alias (for shell/parent)

if __name__ == "__main__":
    main()
