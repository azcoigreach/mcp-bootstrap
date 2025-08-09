"""MCP Client Bootstrap Demo.

This script demonstrates how to interact with the demo MCP server using the
Model Context Protocol Python SDK.  It lists every available prompt, resource
and tool exposed by the server and exercises them one by one.

The module is intentionally lightweight so it can be imported without having
the ``mcp`` package installed.  The heavy imports occur inside :func:`main` so
that documentation tools or static analysers do not need the dependency.
"""

from __future__ import annotations

import asyncio
from pathlib import Path


def print_header(title: str) -> None:
    """Print a formatted section header."""

    print(f"\n=== {title} ===")


def _print_resource_result(name: str, result) -> None:
    """Print the contents of a resource result."""

    if result.contents:
        for content in result.contents:
            if hasattr(content, "text"):
                print(f"{name} resource result:", content.text)
            elif hasattr(content, "blob"):
                print(f"{name} resource result: <binary content>")
    else:
        print(f"{name} resource result: <no content>")


async def main() -> None:
    """Connect to the demo MCP server and exercise all endpoints."""

    # Import MCP components only when ``main`` runs.  This allows the module to
    # be imported without the dependency being present, which is handy for
    # documentation generation or static analysis.
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client

    server_script = (
        Path(__file__).resolve().parent.parent
        / "mcp_server_bootstrap"
        / "server.py"
    )

    server_params = StdioServerParameters(
        command="python",
        args=[str(server_script)],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print_header("Connected to MCP server!")

            prompts = await session.list_prompts()
            print_header("Prompts")
            print(prompts)
            for prompt in prompts.prompts:
                result = await session.get_prompt(
                    prompt.name, {"message": f"Test message for {prompt.name}"}
                )
                print(f"Prompt '{prompt.name}' result:")
                for msg in result.messages:
                    content = msg.content
                    if getattr(content, "type", None) == "text":
                        print(f"  [{msg.role}] {content.text}")
                    elif getattr(content, "type", None) == "image":
                        print(
                            f"  [{msg.role}] <image content, {getattr(content, 'mimeType', 'unknown type')}>"
                        )
                    elif getattr(content, "type", None) == "resource":
                        print(f"  [{msg.role}] <embedded resource>")
                    else:
                        print(f"  [{msg.role}] <unknown content type>")

            resources = await session.list_resources()
            print_header("Resources")
            print(resources)
            echo_res = await session.read_resource("echo://hello-client")
            _print_resource_result("Echo", echo_res)
            user_res = await session.read_resource("user://1")
            _print_resource_result("User", user_res)
            project_res = await session.read_resource("project://101")
            _print_resource_result("Project", project_res)

            tools = await session.list_tools()
            print_header("Tools")
            print(tools.tools)
            for tool in tools.tools:
                if tool.name == "echo_tool":
                    result = await session.call_tool(
                        tool.name, {"message": "hello tools"}
                    )
                elif tool.name == "query_db":
                    result = await session.call_tool(
                        tool.name,
                        {"arguments": {"table": "users", "filter": {"name": "Alice"}}},
                    )
                else:
                    result = await session.call_tool(tool.name, {})
                print(f"Tool '{tool.name}' result:", result)


if __name__ == "__main__":
    asyncio.run(main())

