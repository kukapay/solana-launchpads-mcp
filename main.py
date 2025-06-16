from mcp.server.fastmcp import FastMCP
import httpx
import os
from dotenv import load_dotenv
import pandas as pd

# Load environment variables
load_dotenv()

# Initialize MCP server
mcp = FastMCP(
    name="Solana Launchpads",
    dependencies=["httpx", "python-dotenv", "pandas"]
)

# Configuration
DUNE_API_KEY = os.getenv("DUNE_API_KEY")
BASE_URL = "https://api.dune.com/api/v1"
HEADERS = {"X-Dune-API-Key": DUNE_API_KEY}

def get_latest_result(query_id: int, limit: int = 1000) -> list:
    """
    Fetch the latest results from a Dune Analytics query.

    Args:
        query_id (int): The ID of the Dune query to fetch results from.
        limit (int, optional): Maximum number of rows to return. Defaults to 1000.

    Returns:
        list: A list of dictionaries containing the query results, or an empty list if the request fails.

    Raises:
        httpx.HTTPStatusError: If the API request fails due to a client or server error.
    """
    url = f"{BASE_URL}/query/{query_id}/results"
    params = {"limit": limit}
    with httpx.Client() as client:
        response = client.get(url, params=params, headers=HEADERS, timeout=300)
        response.raise_for_status()
        data = response.json()
        
    result_data = data.get("result", {}).get("rows", [])
    return result_data

@mcp.tool()
def get_daily_tokens_deployed(return_percent: bool = False, limit: int = 1000) -> str:
    """
    Retrieve the daily count of tokens deployed by Solana memecoin launchpads.

    This tool fetches data from a Dune Analytics query and pivots it to show the number of tokens
    deployed per day by each platform. Optionally, it can return the data as percentages of the
    total daily deployments.

    Args:
        return_percent (bool, optional): If True, returns the data as percentages of total daily
            deployments for each platform. Defaults to False.
        limit (int, optional): Maximum number of rows to fetch from the Dune query. Defaults to 1000.

    Returns:
        str: A markdown-formatted table of daily token deployments by platform, or an error message
            if the query fails.
    """
    try:
        data = get_latest_result(4010816, limit=limit)
        df = pd.DataFrame(data)
        df['date'] = pd.to_datetime(df['date_time']).dt.date
        pivot_df = df.pivot(index='date', columns='platform', values='daily_token_count')
        pivot_df = pivot_df.sort_index(ascending=False)
        if return_percent:
            pivot_df = pivot_df.div(pivot_df.sum(axis=1), axis=0).round(3)
        return pivot_df.to_markdown()
    except Exception as e:
        return str(e)

@mcp.tool()
def get_daily_graduates(limit: int = 1000) -> str:
    """
    Fetch the daily number of graduates from Solana memecoin launchpads.

    This tool retrieves data from a Dune Analytics query and pivots it to show the number of
    successful graduates (e.g., completed token sales or projects) per day by each platform.

    Args:
        limit (int, optional): Maximum number of rows to fetch from the Dune query. Defaults to 1000.

    Returns:
        str: A markdown-formatted table of daily graduates by platform, or an error message if the
            query fails.
    """
    try:
        data = get_latest_result(5131612, limit=limit)
        df = pd.DataFrame(data)
        df['block_date'] = pd.to_datetime(df['block_date']).dt.date
        pivot_df = df.pivot(index="block_date", columns="platform", values="daily_graduates")
        pivot_df = pivot_df.sort_index(ascending=False)
        return pivot_df.to_markdown()
    except Exception as e:
        return str(e)

@mcp.tool()
def get_daily_graduation_rate(limit: int = 1000) -> str:
    """
    Fetch the daily graduation rate of Solana memecoin launchpads.

    This tool retrieves data from a Dune Analytics query and pivots it to show the graduation rate
    (e.g., percentage of projects that successfully complete their goals) per day by each platform.

    Args:
        limit (int, optional): Maximum number of rows to fetch from the Dune query. Defaults to 1000.

    Returns:
        str: A markdown-formatted table of daily graduation rates by platform, or an error message
            if the query fails.
    """
    try:
        data = get_latest_result(5129526, limit=limit)
        df = pd.DataFrame(data)
        df['block_date'] = pd.to_datetime(df['block_date']).dt.date
        pivot_df = df.pivot(index="block_date", columns="platform", values="graduation_rate")
        pivot_df = pivot_df.sort_index(ascending=False)
        return pivot_df.to_markdown()
    except Exception as e:
        return str(e)

@mcp.tool()
def get_daily_active_addresses(limit: int = 1000) -> str:
    """
    Fetch the daily count of active wallet addresses interacting with Solana memecoin launchpads.

    This tool retrieves data from a Dune Analytics query and pivots it to show the number of unique
    active wallets per day by each platform.

    Args:
        limit (int, optional): Maximum number of rows to fetch from the Dune query. Defaults to 1000.

    Returns:
        str: A markdown-formatted table of daily active wallets by platform, or an error message if
            the query fails.
    """
    try:
        data = get_latest_result(5002622, limit=limit)
        df = pd.DataFrame(data)
        df['date_time'] = pd.to_datetime(df['date_time']).dt.date
        pivot_df = df.pivot(index="date_time", columns="platform", values="daily_active_wallets")
        pivot_df = pivot_df.sort_index(ascending=False)
        return pivot_df.to_markdown()
    except Exception as e:
        return str(e)

# Run the server
if __name__ == "__main__":
    mcp.run()