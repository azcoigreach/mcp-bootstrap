# MCP Server Bootstrap Demo

This is a minimal working demo of an MCP server using the Model Context Protocol Python SDK.

## Table of Contents
- [Purpose](#purpose)
- [How to Run](#how-to-run)
- [Files](#files)
- [Available Endpoints](#available-endpoints)
- [Advanced Usage](#advanced-usage)
- [Documentation](#documentation)

## Purpose
This project demonstrates how to create a simple MCP server that exposes multiple resources, tools, and prompts using the Python SDK. The server provides echo, query_db, user, and project endpoints. Use this as a starting point for building your own MCP server applications.

## How to Run

1. Install dependencies:
   ```sh
   pip install "mcp[cli]"
   ```
2. Run the server demo:
   ```sh
   python server.py
   ```
   The server will start and expose all available endpoints for client interaction.
3. Run the lifespan example to see resource setup/teardown:
   ```sh
   python lifespan_example.py
   ```

## Files
- `server.py`: Main entry point for the MCP server demo. Exposes echo, query_db, user, and project endpoints as resources, tools, and prompts.
- `lifespan_example.py`: Advanced example showing how to use the MCP server lifespan API for resource management (e.g., database connections). Run with `python lifespan_example.py`.
- `requirements.txt`: Python dependencies for the server demo.

## Available Endpoints
The server exposes the following endpoints:

### Resources
- `echo://{message}`: Echoes the message as a resource.
- `user://{user_id}`: Returns a user record from the fake database.
- `project://{project_id}`: Returns a project record from the fake database.

### Tools
- `echo_tool`: Echoes a message as a tool.
- `query_db`: Queries the fake database for users or projects. Example: `{ "table": "users", "filter": { "name": "Alice" } }`

### Prompts
- `echo_prompt`: Returns a prompt string including the provided message.

## Advanced Usage

### Lifespan API Example
See `lifespan_example.py` for an example of managing resources (like database connections) during server startup and shutdown using the MCP lifespan API. Run it with `python lifespan_example.py` to observe initialization and cleanup of a resource that persists for the server's lifetime.

### Adding More Resources, Tools, and Prompts
You can add more resources, tools, and prompts by defining new functions and registering them with the MCP server instance using the appropriate decorators or registration methods.

## Documentation
- [MCP Python SDK Documentation](https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#adding-mcp-to-your-python-project)
- [Model Context Protocol Specification](https://modelcontextprotocol.io)

## Contributing
Contributions are welcome! Please see the MCP Python SDK repository for guidelines. 
