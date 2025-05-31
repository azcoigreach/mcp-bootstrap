import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    # Assumes a local server is running as 'python ../mcp_server_bootstrap/server.py'
    server_params = StdioServerParameters(
        command="python",
        args=["../mcp_server_bootstrap/server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("Connected to MCP server!")

            prompts = await session.list_prompts()
            print("Prompts:", prompts)

            resources = await session.list_resources()
            print("Resources:", resources)

            tools = await session.list_tools()
            print("Tools:", tools.tools)

            if tools.tools:
                tool_name = tools.tools[0].name
                print(f"Calling tool: {tool_name}")
                result = await session.call_tool(tool_name, {"message": "hello tools"})
                print("Tool result:", result)

if __name__ == "__main__":
    asyncio.run(main()) 