import sys
import os
import json
from mcp_bridge import state, lesson, progress

if __name__ == "__main__":
    # Optionally allow ALPHAZERO_ALIAS for bridge
    alias = os.environ.get("ALPHAZERO_ALIAS")
    if alias:
        sys.alias_cli = alias  # for patched bridge CLI logic

    # Advance progress on "continue" or "next lesson"
    st = progress()
    lesson_id = st.get("current_lesson_id")
    act = st.get("current_act")
    print(lesson_id)
    print(act)
    # Uncomment if debugging
    # print(f"Advanced state: lesson_id={lesson_id}, act={act}")
    # content = lesson(lesson_id, act)
    # print(f"Lesson content for {lesson_id} act {act}:")
    # print(json.dumps(content, indent=2))
