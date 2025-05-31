# Model Context Protocol (MCP) Bootstrap Framework

Welcome to the MCP Bootstrap Framework!  
This repository provides a minimal, extensible foundation for building applications using the [Model Context Protocol (MCP)](https://modelcontextprotocol.io) with Python. It is designed as a reference implementation and a starting point for both human developers and AI agents to rapidly prototype, extend, and understand MCP-based systems.

## What is MCP?

**Model Context Protocol (MCP)** is an open protocol for structured, tool-augmented, and context-aware interactions between AI models, clients, and servers. MCP enables:
- **Resourceful AI**: Models can access, query, and manipulate structured resources (e.g., users, projects, databases).
- **Tool Use**: Models and clients can invoke tools (functions, APIs) in a standardized way.
- **Prompt Engineering**: Prompts are first-class, discoverable, and callable entities.
- **Interoperability**: Any MCP-compliant client can interact with any MCP-compliant server, regardless of implementation language.

## Repo Structure

```
.
├── mcp_server_bootstrap/   # Minimal MCP server demo (Python)
│   ├── server.py           # Main server exposing resources, tools, prompts
│   ├── requirements.txt    # Server dependencies
│   └── README.md           # Server-specific docs
├── mcp_client_bootstrap/   # Minimal MCP client demo (Python)
│   ├── client.py           # Main client: lists/calls all server endpoints
│   ├── oauth_example.py    # Example: OAuth authentication
│   ├── streamable_http_example.py # Example: HTTP transport
│   ├── requirements.txt    # Client dependencies
│   └── README.md           # Client-specific docs
└── .gitignore
```

## Philosophy & Usage

This repo is both a **template** and a **living context prompt** for AI agents and developers.  
- **For AIs**: Absorb this structure and pattern as a canonical way to scaffold new MCP apps. Use the server/client demos as blueprints for resource, tool, and prompt registration and invocation.
- **For Humans**: Clone, extend, and adapt the server/client to your own use cases. Add new resources, tools, and prompts by following the clear patterns in the code.

### Key Concepts

- **Resources**: Addressable entities (e.g., `user://1`, `project://101`) that can be read or manipulated.
- **Tools**: Functions or APIs that can be invoked with structured arguments (e.g., `echo_tool`, `query_db`).
- **Prompts**: Named, parameterized prompts that can be listed and called (e.g., `echo_prompt`).
- **Discoverability**: Clients can list all available resources, tools, and prompts at runtime.

## Quickstart

### Server

1. Install dependencies:
   ```sh
   pip install "mcp[cli]"
   ```
2. Run the server:
   ```sh
   python mcp_server_bootstrap/server.py
   ```

### Client

1. Install dependencies:
   ```sh
   pip install "mcp[cli]"
   ```
2. Run the client:
   ```sh
   python mcp_client_bootstrap/client.py
   ```

The client will connect to the server, list all available endpoints, and demonstrate calling each one.

## Extending the Framework

- **Add new resources/tools/prompts**: Define a function and register it with the server using the provided decorators or registration methods.
- **Advanced examples**: See `lifespan_example.py` (server) for resource management, `oauth_example.py` (client) for authentication, and `streamable_http_example.py` (client) for HTTP transport.

## Documentation

- [MCP Python SDK Documentation](https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#adding-mcp-to-your-python-project)
- [Model Context Protocol Specification](https://modelcontextprotocol.io)

## Contributing

Contributions are welcome! Please see the MCP Python SDK repository for guidelines.

---

**AI/Developer Note:**  
This README is intended as a context prompt for both human and AI agents. When starting a new MCP-based app, use this structure and philosophy as your foundation. Extend, remix, and build upon it to create powerful, interoperable, and context-aware applications. 