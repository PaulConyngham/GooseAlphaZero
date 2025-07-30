import json
import sys
from pathlib import Path

CRED_PATH = Path.home() / ".alphazero_user"

def get_stored_alias():
    if CRED_PATH.exists():
        try:
            with CRED_PATH.open("r") as f:
                creds = json.load(f)
                return creds.get("alias", None)
        except Exception:
            return None
    return None

def save_alias(alias):
    with CRED_PATH.open("w") as f:
        json.dump({"alias": alias}, f)

def prompt_for_alias():
    if sys.stdin.isatty():
        print("Welcome! Please enter your alias (username) for progress tracking.\n(Leave blank to reuse previous or enter a new one to switch.)")
        alias = input("Alias: ").strip()
        if alias:
            save_alias(alias)
            return alias
        else:
            prev = get_stored_alias()
            if prev:
                print(f"Using previously saved alias: {prev}")
                return prev
            else:
                print("No alias set yet—please enter one.")
                return prompt_for_alias()
    else:
        raise RuntimeError("Alias is not set and cannot prompt for input in non-interactive mode. Please provide user_id from agent or set ~/.alphazero_user.")

def resolve_user_id(user_id=None):
    if user_id:
        save_alias(user_id)
        return user_id
    alias = get_stored_alias()
    if alias:
        return alias
    return prompt_for_alias()

def logout_alias():
    if CRED_PATH.exists():
        CRED_PATH.unlink()
