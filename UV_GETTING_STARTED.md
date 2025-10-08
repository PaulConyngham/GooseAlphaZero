# Getting Started with uv

Quick setup guide for running GooseAlphaZero with [uv](https://github.com/astral-sh/uv) - a fast Python package manager.

**Requirements**: Internet connection, Python 3.10+ (uv can install this)

---

## Step 1: Install uv

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify: `uv --version`

---

## Step 2: Ensure Python 3.10+

Check: `python3 --version`

**If you have 3.10+:** Skip to Step 3

**If you have older Python (or none):**
```bash
uv python install 3.12
```

---

## Step 2.1 next run the following command:

```bash
uv sync
```
---

## Step 3: Run the MCP Server

Get your command and run it:

```bash
cd /path/to/GooseAlphaZero
./get-uvx-command.sh
```

Copy and run the command it outputs. That's it!

---

## Goose Desktop Integration

1. Get your command: `cd /path/to/GooseAlphaZero && ./get-uvx-command.sh`
2. Open **Goose Desktop** → **Settings** → **Extensions** → **Add Custom Extension**
3. Fill in:
   - **Name**: `alphazeroapi`
   - **Type**: `STDIO`
   - **Command**: Paste the command from step 1
4. Use your recipe URL to start

---

## Troubleshooting

### Issue: `uv: command not found`

**Solution**: Make sure uv is in your PATH. Restart your terminal or run:

```bash
# macOS/Linux
source ~/.bashrc  # or ~/.zshrc

# Windows
refreshenv
```

### Issue: Python version too old

**Problem**: You see an error like:
```
Because mcp>=1.12.0 depends on Python>=3.10...
```

**Solution**: This project requires Python 3.10 or higher. Let uv install it:

```bash
uv python install 3.12
```

Then try running the MCP server again with uvx.

### Issue: uvx command doesn't work

**Solution**: Make sure you're using the full absolute path from `./get-uvx-command.sh`:

```bash
cd /path/to/GooseAlphaZero
./get-uvx-command.sh
```

Copy the full command it outputs (with your actual project path) and run that.

### Issue: Backend API not responding

**Problem**: The MCP server starts but can't connect to the backend.

**Solution**: The backend API at `http://52.9.199.91:8000` must be online. Test connectivity:

```bash
curl http://52.9.199.91:8000/
```

If this fails, the backend may be down - contact your instructor or the maintainer.

---


## Quick Reference

```bash
# 1. Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Install Python 3.12 (if needed)
uv python install 3.12

# 3. Get and run command
cd /path/to/GooseAlphaZero
./get-uvx-command.sh
# Copy and run the output
```

---

**Need help?** See [Troubleshooting](#troubleshooting) above.
