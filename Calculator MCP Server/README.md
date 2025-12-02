**Overview**

This is a minimal Example "Calculator" MCP (Model Context Protocol) server implemented with `fastmcp`. It exposes a couple of simple tools (functions) — `add_numbers` and `roll_dice` — that you can run locally, test, and debug.

**Prerequisites**

- **Python**: Python 3.11 or newer is required. Confirm with `python --version`.
- **Network / Port access**: If you run the server on a publicly reachable interface, ensure the host/port are reachable and firewall rules allow access.

**Files of interest**

- `main.py`: The server implementation and entry point.
- `pyproject.toml`: Project metadata and dependency (`fastmcp`).

**Quick Start (Windows PowerShell)**

- **Create a virtual environment** and activate it:

```powershell
python -m venv .venv
; .\.venv\Scripts\Activate.ps1
```

- **Install dependencies**:

```powershell
python -m pip install --upgrade pip
python -m pip install fastmcp
# or install the project in editable mode (if you want to import it):
python -m pip install -e .
```

- **Run the server**:

```powershell
python "Calculator MCP Server\main.py"
```

This starts the MCP server using the default settings in `main.py`. If you want the server to listen on a specific host or port, edit `main.py` to pass arguments to `mcp.run(host=..., port=...)`.

**Testing the functions locally (fast turnaround)**

- You can unit-test the tools without starting the MCP server by importing them directly from `main.py`:

```powershell
python - <<'PY'
from Calculator_MCP_Server import main as server_main
from importlib import import_module
mod = import_module('Calculator MCP Server.main')
print(mod.add_numbers(1.5, 2.25))
print(mod.roll_dice(3))
PY
```

Note: If you prefer a simple Python REPL test:

```powershell
python
>>> from importlib import import_module
>>> mod = import_module('Calculator MCP Server.main')
>>> mod.add_numbers(1,2)
>>> mod.roll_dice(2)
```

**Debugging**

- **Enable Python logging**: Add log setup near the top of `main.py` before calling `mcp.run()` to see detailed runtime information:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# ... existing code ...
if __name__ == '__main__':
		mcp.run()
```

- **Run with an environment variable (PowerShell)** to mark intent or pass options to your startup scripts:

```powershell
$env:LOG_LEVEL = 'DEBUG'; python "Calculator MCP Server\main.py"
```

- **Use VS Code debugging**: Create or update `.vscode/launch.json` with a configuration similar to the following (place in workspace root):

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Launch Calculator MCP",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/Calculator MCP Server/main.py",
      "console": "integratedTerminal",
      "justMyCode": false
    }
  ]
}
```

- **Breakpoints & inspection**: Set breakpoints inside `add_numbers` or `roll_dice` and run the VS Code launch configuration. The `justMyCode: false` option ensures library calls are also viewable if needed.

**Collecting logs for troubleshooting**

- Run the server with logging enabled (see above) and capture console output.
- To write logs to a file, configure `logging` in `main.py`:

```python
import logging
logging.basicConfig(level=logging.DEBUG, filename='mcp-server.log', filemode='a', format='%(asctime)s %(levelname)s %(message)s')
```

Then reproduce the issue and attach `mcp-server.log` when requesting help.

**Common issues & fixes**

- **Wrong Python version**: Confirm `python --version` is 3.11+ and your virtual environment is active.
- **Dependency not installed**: If you see `ModuleNotFoundError: fastmcp`, run `python -m pip install fastmcp` in the active venv.
- **Port already in use**: If the server fails to start due to address-in-use, change the port in `mcp.run(port=XXXX)` in `main.py` or stop the conflicting process.
- **Code changes not reflected**: If you installed the package into the environment using `pip install .` (not editable), re-install with `pip install -e .` or run `python main.py` directly for active development.

**Development tips**

- Keep `main.py` small — use separate modules to host business logic and keep `main.py` responsible only for wiring the MCP and registering tools.
- Add unit tests that import the functions directly rather than exercising the network layer. This makes iteration faster.

**How to get help**

- When reporting a problem, include:
  - Python version (`python --version`)
  - Exact commands run
  - Full console output or `mcp-server.log` if available
  - A minimal reproduction snippet if possible

---

If you want, I can also:

- add a ready-to-use `.vscode/launch.json` to the repo,
- add a `requirements.txt` or `tox`/`pytest` scaffolding for tests, or
- add a simple client example that calls this MCP server.

Please tell me which of those you'd like next.
