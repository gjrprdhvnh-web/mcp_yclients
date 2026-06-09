"""Common tools for YCLIENTS MCP Server."""

import json
from typing import Any
from ..client import yclients_client
from datetime import datetime
import pytz


def register_common_tools(mcp):
    """Register common tools."""

    @mcp.tool()
    async def get_current_date() -> str:
        """Get current date in YYYY-MM-DD format"""
        tz = pytz.timezone('Europe/Moscow')
        now = datetime.now(tz)

        return now.strftime("%Y-%m-%d")