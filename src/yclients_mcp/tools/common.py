"""Common tools for YCLIENTS MCP Server."""

import json
from typing import Any
from ..client import yclients_client
from datetime import datetime
import zoneinfo import ZoneInfo


def register_common_tools(mcp):
    """Register common tools."""

    @mcp.tool()
    async def get_current_date() -> str:
        """Get current date"""
        return datetime.now(ZoneInfo('Europe/Moscow')).date()