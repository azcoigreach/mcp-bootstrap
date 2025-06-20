"""
MCP Client Bootstrap Demo

This is a minimal working demo of an MCP client using the Model Context Protocol Python SDK.

Demonstrates:
- Listing and calling all available prompts, resources, and tools from the server.
- Interacting with echo, query_db, user, and project endpoints.

See also:
- Advanced examples: streamable_http_example.py, oauth_example.py
- MCP Python SDK documentation: https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#adding-mcp-to-your-python-project
"""
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

def print_header(title: str) -> None:
    """Print a formatted section header."""
    print(f"\n=== {title} ===")

async def main() -> None:
    """
    Connect to a local MCP server using stdio, list and call all available prompts, resources, and tools.
    Demonstrates echo, query_db, user, and project endpoints.
    """
    # Assumes a local server is running as 'python ../mcp_server_bootstrap/server.py'
    server_params = StdioServerParameters(
        command="python",
        args=["../mcp_server_bootstrap/server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print_header("Connected to MCP server!")

            prompts = await session.list_prompts()
            print_header("Prompts")
            print(prompts)
            # Call all prompts
            for prompt in prompts.prompts:
                result = await session.get_prompt(prompt.name, {"message": f"Test message for {prompt.name}"})
                # Print all messages in the prompt result
                print(f"Prompt '{prompt.name}' result:")
                for msg in result.messages:
                    content = msg.content
                    if hasattr(content, "type") and content.type == "text":
                        print(f"  [{msg.role}] {content.text}")
                    elif hasattr(content, "type") and content.type == "image":
                        print(f"  [{msg.role}] <image content, {getattr(content, 'mimeType', 'unknown type')}>")
                    elif hasattr(content, "type") and content.type == "resource":
                        print(f"  [{msg.role}] <embedded resource>")
                    else:
                        print(f"  [{msg.role}] <unknown content type>")

            resources = await session.list_resources()
            print_header("Resources")
            print(resources)
            # Call echo resource
            echo_res = await session.read_resource("echo://hello-client")
            if echo_res.contents:
                for content in echo_res.contents:
                    if hasattr(content, "text"):
                        print("Echo resource result:", content.text)
                    elif hasattr(content, "blob"):
                        print("Echo resource result: <binary content>")
            else:
                print("Echo resource result: <no content>")
            # Call user resource
            user_res = await session.read_resource("user://1")
            if user_res.contents:
                for content in user_res.contents:
                    if hasattr(content, "text"):
                        print("User resource result:", content.text)
                    elif hasattr(content, "blob"):
                        print("User resource result: <binary content>")
            else:
                print("User resource result: <no content>")
            # Call project resource
            project_res = await session.read_resource("project://101")
            if project_res.contents:
                for content in project_res.contents:
                    if hasattr(content, "text"):
                        print("Project resource result:", content.text)
                    elif hasattr(content, "blob"):
                        print("Project resource result: <binary content>")
            else:
                print("Project resource result: <no content>")

            tools = await session.list_tools()
            print_header("Tools")
            print(tools.tools)
            # Call all tools
            for tool in tools.tools:
                if tool.name == "echo_tool":
                    result = await session.call_tool(tool.name, {"message": "hello tools"})
                elif tool.name == "query_db":
                    result = await session.call_tool(tool.name, {"arguments": {"table": "users", "filter": {"name": "Alice"}}})
                else:
                    result = await session.call_tool(tool.name, {})
                print(f"Tool '{tool.name}' result:", result)

if __name__ == "__main__":
    asyncio.run(main()) 