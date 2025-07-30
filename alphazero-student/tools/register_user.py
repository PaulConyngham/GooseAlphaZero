import sys
import os
sys.path.insert(0, os.path.dirname(__file__))  # Ensure local import resolution
from mcp_bridge import state

if __name__ == "__main__":
    try:
        s = state()
        print("User registered/checked in backend:", s)
    except Exception as e:
        print("Could not register user:", e)
