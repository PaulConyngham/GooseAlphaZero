import requests
from mcp.server.fastmcp import FastMCP
from mcp.shared.exceptions import McpError
from mcp.types import ErrorData, INTERNAL_ERROR, INVALID_PARAMS

mcp = FastMCP("alphazero")

#BASE_URL = "http://localhost:5000"
BASE_URL = "http://52.9.199.91:8000"

@mcp.tool()
def state(user_id: str = "default_user") -> dict:
    try:
        r = requests.get(f"{BASE_URL}/state", params={"user_id": user_id})
        r.raise_for_status()
        return r.json()
    except Exception as e:
        raise McpError(ErrorData(INTERNAL_ERROR, f"Failed to get user state: {e}"))

@mcp.tool()
def lesson(module_id: str, lesson_id: str, act: int) -> dict:
    if not module_id or not lesson_id or not isinstance(act, int):
        raise McpError(ErrorData(INVALID_PARAMS, "Invalid module_id, lesson_id, or act"))
    try:
        r = requests.get(f"{BASE_URL}/lesson/{module_id}/{lesson_id}/{act}")
        r.raise_for_status()
        return r.json()
    except Exception as e:
        raise McpError(ErrorData(INTERNAL_ERROR, f"Failed to get lesson content: {e}"))

@mcp.tool()
def answer(module_id: str, lesson_id: str, user_answer: str, user_id: str = "default_user") -> dict:
    if not module_id or not lesson_id or not user_answer:
        raise McpError(ErrorData(INVALID_PARAMS, "Missing module_id, lesson_id, or user_answer"))
    try:
        payload = {
            "module_id": module_id,
            "lesson_id": lesson_id,
            "user_answer": user_answer,
            "user_id": user_id,
        }
        r = requests.post(f"{BASE_URL}/answer", json=payload)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        raise McpError(ErrorData(INTERNAL_ERROR, f"Failed to submit answer: {e}"))

if __name__ == "__main__":
    mcp.run()
