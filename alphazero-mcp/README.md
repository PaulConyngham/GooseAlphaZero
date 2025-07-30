# AlphaZero MCP Extension (Maintainers/Developers)

This project is the official Model Context Protocol (MCP) server for the AlphaZero RL curriculum. It serves as a bridge between the Goose AI agent and the backend lesson server.

## Contents
- `src/alphazero_mcp/server.py` — MCP SDK server. Exposes tools for state, lesson content, validation.
- `pyproject.toml` — Project/dependency definition
- Example usage and integration described below.

## Usage
1. Install dependencies in your preferred Python 3.9+ environment:
   ```bash
   pip install mcp[cli] requests
   ```

2. Run the server (usually launched via Goose, but can also be tested manually):
   ```bash
   python src/alphazero_mcp/server.py
   ```
3. For CLI/GUI integration, set Goose's extension config to use the full path to this script as a StandardIO extension.

## Maintenance
- For server/maintainer/developer use only.

## Developer Contact
See the main project repo or contact your lead developer/instructor.
