import sys
from user_session import save_alias

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python write_alias.py <alias>")
        sys.exit(1)
    save_alias(sys.argv[1])
    print(f"Alias '{sys.argv[1]}' saved to ~/.alphazero_user.")
