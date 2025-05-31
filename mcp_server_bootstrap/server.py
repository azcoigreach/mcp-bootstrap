"""
MCP Server Bootstrap Demo

This is a minimal working demo of an MCP server using the Model Context Protocol Python SDK.

Demonstrates:
- Echo resource, tool, and prompt endpoints
- Fake database query tool
- User and project resource endpoints

See also:
- Advanced examples: lifespan_example.py
- MCP Python SDK documentation: https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#adding-mcp-to-your-python-project
"""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "Demo Server",
    description="A minimal MCP server demo for Cursor integration.",
    version="0.1.0"
)

def echo_resource(message: str) -> str:
    """
    Echo a message as a resource.

    Args:
        message (str): The message to echo.
    Returns:
        str: The echoed message.
    Example:
        GET echo://hello -> "Resource echo: hello"
    """
    return f"Resource echo: {message}"

# Register the echo resource endpoint (echo://{message})
mcp.resource("echo://{message}")(echo_resource)

def echo_tool(message: str) -> str:
    """
    Echo a message as a tool.

    Args:
        message (str): The message to echo.
    Returns:
        str: The echoed message.
    Example:
        call_tool("echo_tool", {"message": "hi"}) -> "Tool echo: hi"
    """
    return f"Tool echo: {message}"

# Register the echo tool endpoint
mcp.tool()(echo_tool)

def echo_prompt(message: str) -> str:
    """
    Create an echo prompt.

    Args:
        message (str): The message to include in the prompt.
    Returns:
        str: The prompt string.
    Example:
        call_prompt("echo_prompt", {"message": "foo"}) -> "Please process this message: foo"
    """
    return f"Please process this message: {message}"

# Register the echo prompt endpoint
mcp.prompt()(echo_prompt)

# Fake in-memory database for demonstration
FAKE_DATABASE = {
    "users": [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"}
    ],
    "projects": [
        {"id": 101, "title": "Demo Project", "status": "active"}
    ]
}

def query_db(arguments: dict) -> dict:
    """
    Query the fake database.

    Args:
        arguments (dict): Should contain 'table' (str) and optional 'filter' (dict).
    Returns:
        dict: Query results or error message.
    Example:
        call_tool("query_db", {"arguments": {"table": "users", "filter": {"name": "Alice"}}})
    """
    table = arguments.get("table")
    filter_ = arguments.get("filter", {})
    if table not in FAKE_DATABASE:
        return {"error": f"Table {table} not found."}
    results = FAKE_DATABASE[table]
    for key, value in filter_.items():
        results = [row for row in results if row.get(key) == value]
    return {"results": results}

# Register the query_db tool endpoint
mcp.tool()(query_db)

def user_resource(user_id: int) -> dict:
    """
    Retrieve a user by user_id from the fake database.

    Args:
        user_id (int): The user ID to look up.
    Returns:
        dict: The user record or error message.
    Example:
        GET user://1 -> {"id": 1, "name": "Alice", ...}
    """
    for user in FAKE_DATABASE["users"]:
        if user["id"] == user_id:
            return user
    return {"error": "User not found."}

# Register the user resource endpoint (user://{user_id})
mcp.resource("user://{user_id}")(user_resource)

def project_resource(project_id: int) -> dict:
    """
    Retrieve a project by project_id from the fake database.

    Args:
        project_id (int): The project ID to look up.
    Returns:
        dict: The project record or error message.
    Example:
        GET project://101 -> {"id": 101, "title": "Demo Project", ...}
    """
    for project in FAKE_DATABASE["projects"]:
        if project["id"] == project_id:
            return project
    return {"error": "Project not found."}

# Register the project resource endpoint (project://{project_id})
mcp.resource("project://{project_id}")(project_resource)

if __name__ == "__main__":
    mcp.run() 