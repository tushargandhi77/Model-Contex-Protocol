# Model Context Protocol (MCP) Learning Repository

This repository is a hands-on MCP learning workspace built for education and revision.
It contains one working MCP server (`Calculator MCP Server`) and one starter project (`Test Remote Server`) that can be expanded into a remote MCP service.

## Learning Goals

- Understand how an MCP server is structured in Python.
- Learn how tools are exposed to an MCP client (for example, Codex/Desktop clients).
- Practice extending tool sets from simple math operations to real workflows.
- Use this repo as quick revision material before interviews, demos, or project work.

## Repository Structure

```text
Model-Contex-Protocol/
|-- README.md                         # This file (full repo guide)
|-- image.png
|-- Image_main.jpg
|-- Calculator MCP Server/
|   |-- main.py                       # FastMCP server and tool definitions
|   |-- pyproject.toml                # Project metadata + dependencies
|   |-- uv.lock                       # Resolved dependency lock file
|   `-- README.md                     # Local project README
`-- Test Remote Server/
    |-- main.py                       # Starter script (currently non-MCP)
    |-- pyproject.toml                # Minimal Python project config
    `-- README.md                     # Remote server notes and expansion plan
```

## What Is MCP (Quick Revision)

Model Context Protocol (MCP) is a standard for connecting AI applications to external capabilities in a structured and safe way.

In practical terms:

- MCP Client: The AI app that wants to use external tools.
- MCP Server: Your application that exposes tools/resources/prompts.
- Transport Layer: How client and server communicate (local stdio or network/remote transport).
- Tool Invocation: The client requests a named tool with arguments; server executes and returns structured results.

## Architecture in This Repository

```text
+---------------------------+
| MCP Client (LLM App)      |
| e.g., Codex/Desktop       |
+-------------+-------------+
              |
              | MCP request: tool name + arguments
              v
+-------------+-------------+
| FastMCP Server            |
| Calculator MCP Server     |
| (main.py)                 |
+-------------+-------------+
              |
              | Python function execution
              v
+-------------+-------------+
| Tools                      |
| - roll_dice                |
| - add_numbers              |
| - subtract_numbers         |
| - multiply_numbers         |
| - divide_numbers           |
| - modulus_numbers          |
+---------------------------+
```

## Current Implementation Summary

### 1) Calculator MCP Server (`Calculator MCP Server/main.py`)

This is the main MCP implementation.

- Creates a `FastMCP` server instance named `DEMO Server`.
- Registers tools using `@mcp.tool`.
- Exposes arithmetic operations and a random dice tool.
- Starts server with `mcp.run()` in the main entrypoint.

Available tools:

- `roll_dice(n_dice: int = 1) -> list[int]`
- `add_numbers(a: float, b: float) -> float`
- `subtract_numbers(a: float, b: float) -> float`
- `multiply_numbers(a: float, b: float) -> float`
- `divide_numbers(a: float, b: float) -> float` (raises `ValueError` for divide-by-zero)
- `modulus_numbers(a: int, b: int) -> int`

### 2) Test Remote Server (`Test Remote Server/main.py`)

This is currently a starter script and prints:

- `Hello from test-remote-server!`

It is a good place to build your remote MCP experiments without affecting the calculator example.

## Setup and Run

Python requirement for both projects: `>=3.11`

### Option A: Run Calculator MCP Server

```powershell
cd "Calculator MCP Server"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install fastmcp
python main.py
```

### Option B: Run Starter Remote Server

```powershell
cd "Test Remote Server"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python main.py
```

## MCP Use Cases (Relevant to This Repo)

Use this calculator server pattern as a template for:

- Data preprocessing tools for ML workflows.
- Statistical utility tools (mean/std/normalization checks).
- Feature engineering helpers exposed as MCP tools.
- Internal operations assistant (validated business calculations).
- Educational sandboxes to teach AI tool-calling.

## Concepts to Revise from This Codebase

1. Tool registration via decorators (`@mcp.tool`).
2. Typed signatures and automatic schema generation.
3. Deterministic tools (`add_numbers`) vs non-deterministic tools (`roll_dice`).
4. Error handling and tool safety (`divide_numbers`).
5. Separation of concern: MCP wiring vs business logic.
6. Local-first development before remote deployment.

## Suggested Next Improvements

1. Add input validation for all math tools (ranges, type guards).
2. Add unit tests for each tool function.
3. Add logging and structured error responses.
4. Convert `Test Remote Server` into a real remote MCP server.
5. Add resources/prompts support (not only tools) for broader MCP learning.

## Example Extension Path (Remote MCP)

To convert `Test Remote Server` into a remote MCP service:

1. Initialize a `FastMCP` instance.
2. Define at least one `@mcp.tool` function.
3. Configure run mode for remote transport.
4. Add auth, request limits, and logging.
5. Test using an MCP-capable client.

## Troubleshooting Notes

- `ModuleNotFoundError: fastmcp`: install dependency in active virtual environment.
- Wrong Python version: confirm `python --version` is 3.11+.
- Tool errors: check function signatures and edge cases (for example divide by zero).

## Revision Checklist

Use this before interviews or practical sessions:

- Explain MCP client-server flow in 30 seconds.
- Describe how `@mcp.tool` exposes Python functions.
- Discuss one safety concern and one mitigation.
- Extend one tool and test it locally.
- Explain how local MCP differs from remote MCP deployment.

---

If you want, the next step can be adding a production-style remote MCP server in `Test Remote Server` with authentication, logging, and a few ML-oriented tools.
