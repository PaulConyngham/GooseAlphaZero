import sys
import os
import json
from mcp_bridge import state, lesson

if __name__ == "__main__":
    # Optionally allow ALPHAZERO_ALIAS for bridge
    alias = os.environ.get("ALPHAZERO_ALIAS")
    if alias:
        sys.alias_cli = alias  # for patched bridge CLI logic

    # Fetch current user state (auto-registers user)
    st = state()
    lesson_id = st.get("current_lesson_id")
    act = st.get("current_act")
    if not lesson_id:
        lesson_id = "rl_fundamentals_01"
    if not act:
        act = 1
    # Print just the right info for Goose and lesson driver
    print(lesson_id)
    print(act)
    # Optionally: actually call and print lesson content
    # content = lesson(lesson_id, act)
    # print(json.dumps(content, indent=2))
