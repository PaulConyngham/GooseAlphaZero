import requests
import sys
import json
from pathlib import Path
from mcp.server.fastmcp import FastMCP
from mcp.shared.exceptions import McpError
from mcp.types import ErrorData, INTERNAL_ERROR, INVALID_PARAMS

#BASE_URL = "http://localhost:5000"
BASE_URL = "http://52.9.199.91:8000"
CRED_PATH = Path(__file__).parent / ".alphazero_user"

import subprocess

def get_alias():
    # ALWAYS prompt at session start using choose_alias.py
    try:
        res = subprocess.run([
            sys.executable, str(Path(__file__).parent / "choose_alias.py")
        ], check=True, stdout=subprocess.PIPE, stdin=sys.stdin, text=True)
        alias = res.stdout.strip()
        if alias:
            print(f"DEBUG: Using alias: {alias}")
            return alias
        else:
            raise Exception("No alias returned by choose_alias.py")
    except Exception as e:
        print(f"Error in choose_alias.py: {e}")
        raise RuntimeError("Could not pick or confirm alias!")

mcp = FastMCP("alphazero")

@mcp.tool()
def state() -> dict:
    user_id = get_alias()
    try:
        r = requests.get(f"{BASE_URL}/state", params={"user_id": user_id})
        r.raise_for_status()
        return r.json()
    except Exception as e:
        raise McpError(ErrorData(INTERNAL_ERROR, f"Failed to get user state: {e}"))

@mcp.tool()
def lesson(module_id: str, lesson_id: str, act: int) -> dict:
    user_id = get_alias()
    try:
        r = requests.get(
            f"{BASE_URL}/lesson/{module_id}/{lesson_id}/{act}",
            params={"user_id": user_id}
        )
        r.raise_for_status()
        out = r.json()
        print(f"Module: {module_id}, Lesson: {lesson_id}, Act: {act}")
        return out
    except Exception as e:
        raise McpError(ErrorData(INTERNAL_ERROR, f"Failed to get lesson content: {e}"))

@mcp.tool()
def answer(module_id: str, lesson_id: str, user_answer: str) -> dict:
    user_id = get_alias()
    try:
        payload = {
            "lesson_id": lesson_id,
            "module_id": module_id,
            "user_answer": user_answer,
            "user_id": user_id,
        }
        r = requests.post(f"{BASE_URL}/answer", json=payload)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        raise McpError(ErrorData(INTERNAL_ERROR, f"Failed to submit answer: {e}"))

@mcp.tool()
def progress() -> dict:
    user_id = get_alias()
    try:
        state_r = requests.get(f"{BASE_URL}/state", params={"user_id": user_id})
        state_r.raise_for_status()
        state = state_r.json()
        module_id = state["current_module_id"]
        payload = {
            "user_id": user_id,
            "module_id": module_id
        }
        r = requests.post(f"{BASE_URL}/progress", json=payload)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        raise McpError(ErrorData(INTERNAL_ERROR, f"Failed to progress: {e}"))

if __name__ == "__main__":
    mcp.run()
