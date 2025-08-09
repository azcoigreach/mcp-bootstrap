"""Lifespan API example for FastMCP.

This script demonstrates using FastMCP's ``lifespan`` parameter to manage
resources during server startup and shutdown. A fake database connection is
created when the server starts and cleaned up when the server stops.

Run with::

    python lifespan_example.py
"""

from contextlib import asynccontextmanager
from typing import AsyncIterator, Dict, Any

from mcp.server.fastmcp import Context, FastMCP


@asynccontextmanager
async def lifespan(app: FastMCP) -> AsyncIterator[Dict[str, Any]]:
    """Manage the lifespan of a fake database connection."""
    # Setup phase - create resource
    db = {"connected": True, "items": []}
    print("Lifespan startup: opened fake database connection")
    try:
        yield db  # Make the resource available to endpoints via lifespan context
    finally:
        # Teardown phase - clean up resource
        db["connected"] = False
        print("Lifespan shutdown: closed fake database connection")


mcp = FastMCP(
    "Lifespan Example Server",
    lifespan=lifespan,
)


@mcp.tool()
def add_item(item: str, ctx: Context) -> Dict[str, Any]:
    """Add an item to the fake database and return all items."""
    db = ctx.request_context.lifespan_context
    db["items"].append(item)
    return {"items": db["items"]}


if __name__ == "__main__":
    mcp.run()
