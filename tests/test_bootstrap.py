"""Tests for the MCP bootstrap demo."""

import asyncio

import pytest

from mcp_server_bootstrap import server
from mcp_client_bootstrap import client


def test_echo_resource():
    assert server.echo_resource("hi") == "Resource echo: hi"


def test_echo_tool():
    assert server.echo_tool("hello") == "Tool echo: hello"


def test_echo_prompt():
    assert server.echo_prompt("foo") == "Please process this message: foo"


def test_query_db_happy_path():
    res = server.query_db({"table": "users", "filter": {"name": "Alice"}})
    assert res == {
        "results": [
            {"id": 1, "name": "Alice", "email": "alice@example.com"}
        ]
    }


def test_query_db_error_cases():
    assert server.query_db("bad") == {"error": "Arguments must be a dictionary."}
    assert server.query_db({"filter": {}})["error"].startswith("Missing required")
    assert server.query_db({"table": "users", "filter": "no"}) == {
        "error": "'filter' must be a dictionary if provided."
    }
    assert server.query_db({"table": "missing"}) == {
        "error": "Table missing not found."
    }


def test_user_resource():
    assert server.user_resource(1)["name"] == "Alice"
    assert server.user_resource(999)["error"] == "User not found."


def test_project_resource():
    assert server.project_resource(101)["title"] == "Demo Project"
    assert server.project_resource(999)["error"] == "Project not found."


def test_client_main_runs():
    pytest.importorskip("mcp")
    asyncio.run(client.main())

