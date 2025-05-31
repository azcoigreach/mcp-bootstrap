"""
Advanced MCP Client Example: OAuth Authentication

This example demonstrates how to use OAuth authentication with the MCP client.
"""
import asyncio
from mcp.client.auth import OAuthClientProvider, TokenStorage
from mcp.client.session import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from mcp.shared.auth import OAuthClientInformationFull, OAuthClientMetadata, OAuthToken

class CustomTokenStorage(TokenStorage):
    """Simple in-memory token storage implementation."""
    def __init__(self):
        self.tokens = None
        self.client_info = None
    async def get_tokens(self) -> OAuthToken | None:
        return self.tokens
    async def set_tokens(self, tokens: OAuthToken) -> None:
        self.tokens = tokens
    async def get_client_info(self) -> OAuthClientInformationFull | None:
        return self.client_info
    async def set_client_info(self, client_info: OAuthClientInformationFull) -> None:
        self.client_info = client_info

oauth_auth = OAuthClientProvider(
    server_url="https://api.example.com",
    client_metadata=OAuthClientMetadata(
        client_name="My Client",
        redirect_uris=["http://localhost:3000/callback"],
        grant_types=["authorization_code", "refresh_token"],
        response_types=["code"],
    ),
    storage=CustomTokenStorage(),
    redirect_handler=lambda url: print(f"Visit: {url}"),
    callback_handler=lambda: ("auth_code", None),
)

async def main():
    async with streamablehttp_client(
        "https://api.example.com/mcp", auth=oauth_auth
    ) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("Authenticated session ready!")

if __name__ == "__main__":
    asyncio.run(main()) 