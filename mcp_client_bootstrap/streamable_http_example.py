"""
Advanced MCP Client Example: Streamable HTTP

This example demonstrates how to connect to an MCP server using the streamable HTTP transport.
"""
import asyncio
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession

async def main():
    # Replace with your actual MCP server URL
    async with streamablehttp_client("http://localhost:8000/mcp") as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("Connected to MCP server via HTTP!")
            # Example: Call a tool named 'echo' with a message
            result = await session.call_tool("echo", {"message": "Hello via HTTP!"})
            print("Tool result:", result)

if __name__ == "__main__":
    asyncio.run(main()) 