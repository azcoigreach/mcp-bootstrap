# MCP Client Bootstrap Demo

This is a minimal working demo of an MCP client using the Model Context Protocol Python SDK.

## Table of Contents
- [Purpose](#purpose)
- [How to Run](#how-to-run)
- [Files](#files)
- [Demonstrated Calls](#demonstrated-calls)
- [Advanced Usage](#advanced-usage)
- [Documentation](#documentation)

## Purpose
This project demonstrates how to connect to an MCP server, list all available prompts, resources, and tools, and call each of them using the Python SDK. It shows how to interact with echo, query_db, user, and project endpoints. Use this as a starting point for building an MCP client applications.

## How to Run

1. Install dependencies:
   ```sh
   pip install "mcp[cli]"
   ```
2. Run the client demo:
   ```sh
   python client.py
   ```
   The client will connect to a local MCP server (see the server bootstrap demo) and demonstrate all available calls.

## Files
- `client.py`: Main entry point for the MCP client demo. Lists and calls all available prompts, resources, and tools from the server, including echo, query_db, user, and project endpoints.
- `streamable_http_example.py`: Advanced example showing how to connect to an MCP server using the streamable HTTP transport.
- `oauth_example.py`: Advanced example showing how to use OAuth authentication with the MCP client.
- `requirements.txt`: Python dependencies for the client demo.

## Demonstrated Calls
The client will automatically:
- List all available prompts, resources, and tools from the server
- Call each prompt (e.g., `echo_prompt`)
- Call each resource, including:
  - `echo://{message}` (e.g., `echo://hello-client`)
  - `user://{user_id}` (e.g., `user://1`)
  - `project://{project_id}` (e.g., `project://101`)
- Call each tool, including:
  - `echo_tool` (echoes a message)
  - `query_db` (queries the fake database for users or projects)

See the output of `python client.py` for example results.

## Advanced Usage

### Streamable HTTP Example
See `streamable_http_example.py` for an example of connecting to an MCP server using the streamable HTTP transport. This is useful for connecting to remote servers over HTTP.

### OAuth Authentication Example
See `oauth_example.py` for an example of using OAuth authentication with the MCP client. This is useful for connecting to protected MCP servers that require authentication.

## Documentation
- [MCP Python SDK Documentation](https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#adding-mcp-to-your-python-project)
- [Model Context Protocol Specification](https://modelcontextprotocol.io)

## Contributing
Contributions are welcome! Please see the MCP Python SDK repository for guidelines. 