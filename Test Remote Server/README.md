# Test Remote Server

This folder is a starter project intended to evolve into a remote MCP server.
Right now, it contains a minimal Python script and project config, making it a clean base for experimentation.

## Current Status

- `main.py` currently prints a simple message.
- MCP is not yet wired in this folder.
- No external dependencies are required at the moment.

## Files

- `main.py`: entry script (placeholder behavior).
- `pyproject.toml`: project metadata (`python >= 3.11`).
- `README.md`: this guide.

## Intended Architecture (Target)

```text
+-------------------------+
| MCP Client              |
| (Codex/Desktop/Agent)   |
+------------+------------+
             |
             | Remote MCP calls
             v
+------------+------------+
| Remote MCP Server       |
| (this folder)           |
| FastMCP app             |
+------------+------------+
             |
             v
+------------+------------+
| Domain Tools            |
| - utility tools         |
| - data tools            |
| - ML helper tools       |
+-------------------------+
```

## Why Keep This Folder Separate?

- You can prototype remote-only behavior without changing the calculator example.
- It helps compare local MCP and remote MCP approaches side by side.
- It is useful for revision: one folder shows working tools, one folder shows scaffold-to-production progression.

## Suggested MCP Conversion Steps

1. Install `fastmcp`.
2. Replace print-based `main.py` with a `FastMCP` app.
3. Add 2 to 3 focused tools.
4. Add input validation and clear error handling.
5. Add logging for observability.
6. Connect with an MCP client and test tool calls end to end.

## Example Direction for Educational Use Cases

- Remote calculator API for distributed teams.
- Dataset profile tools for ML notebooks.
- Unit conversion and preprocessing services.
- Safe internal automation tools with controlled interfaces.

## Run Current Placeholder

```powershell
cd "Test Remote Server"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python main.py
```

Expected output:

```text
Hello from test-remote-server!
```

## Next Practical Upgrade

Convert `main.py` into a minimal remote MCP server with:

- `health_check()` tool
- `add_numbers(a, b)` tool
- structured errors and basic logging

That gives you a complete learning path from scaffold to functional remote MCP service.
