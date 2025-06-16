# Solana Launchpads MCP

An MCP server that tracks daily activity and graduate metrics across multiple Solana launchpads.

![GitHub License](https://img.shields.io/github/license/kukapay/solana-launchpads-mcp) 
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

## Features

- **MCP Tools**: Four tools to retrieve daily metrics:
  - Token deployments.
  - Successful graduates (completed projects).
  - Graduation rates.
  - Active wallet addresses.
- **Markdown Output**: Data is formatted as markdown tables for easy readability.

## Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) (recommended package manager)
- A [Dune Analytics API key](https://dune.com/docs/api/getting-started/#authentication)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/solana-launchpads-mcp.git
   cd solana-launchpads-mcp
   ```

2. **Install dependencies**:
   ```bash
   uv sync
   ```

3. **Installing to Claude Desktop**:

    Install the server as a Claude Desktop application:
    ```bash
    uv run mcp install main.py --name "Solana Launchpads"
    ```

    Configuration file as a reference:

    ```json
    {
       "mcpServers": {
           "Solana Launchpads": {
               "command": "uv",
               "args": [ "--directory", "/path/to/solana-launchpads-mcp", "run", "main.py" ],
               "env": { "DUNE_API_KEY": "dune_api_key"}               
           }
       }
    }
    ```
    Replace `/path/to/solana-launchpads-mcp` with your actual installation path, and `dune_api_key` with your API key from Dune Analytics.

## Tools

| Tool Name                     | Description                                                                 | Parameters                              |
|-------------------------------|-----------------------------------------------------------------------------|-----------------------------------------|
| `get_daily_tokens_deployed`   | Retrieves daily token deployments by platform, optionally as percentages.   | `return_percent: bool` (default: False)<br>`limit: int` (default: 1000) |
| `get_daily_graduates`         | Fetches daily successful graduates by platform.                             | `limit: int` (default: 1000)           |
| `get_daily_graduation_rate`   | Retrieves daily graduation rates by platform.                               | `limit: int` (default: 1000)           |
| `get_daily_active_addresses`  | Fetches daily active wallet addresses by platform.                          | `limit: int` (default: 1000)           |


## Example Usage

To use the MCP server, start it and interact with its tools and prompt via an LLM client (e.g., Claude Desktop or or MCP Inspector). Below are examples for each tool and the prompt, using natural language inputs.

### Get Daily Token Deployments 

**Prompt**: 
```
Show me the number of tokens launched on Solana memecoin launchpads each day for the past week.
```

**Output**:
```markdown
| date       | LaunchLabs | LetsBonk | Pump.fun | Boop | Bags | Believeapp | Moonshot | Sunpump.meme |
|------------|------------|----------|----------|------|------|------------|----------|--------------|
| 2025-06-15 | 50         | 20       | 120      | 10   | 15   | 5          | 30       | 25           |
| 2025-06-14 | 45         | 18       | 110      | 8    | 12   | 4          | 25       | 20           |
| ...        | ...        | ...      | ...      | ...  | ...  | ...        | ...      | ...          |
```

### Get Daily Graduates

**Prompt**: 
```
How many projects successfully graduated from Solana memecoin launchpads daily over the last 10 days?
```

**Output**:
```markdown
| block_date | LaunchLabs | LetsBonk | Pump.fun | Boop | Bags | Believeapp | Moonshot | Sunpump.meme |
|------------|------------|----------|----------|------|------|------------|----------|--------------|
| 2025-06-15 | 10         | 5        | 15       | 2    | 3    | 1          | 5        | 4            |
| 2025-06-14 | 8          | 4        | 12       | 1    | 2    | 0          | 4        | 3            |
| ...        | ...        | ...      | ...      | ...  | ...  | ...        | ...      | ...          |
```

### Get Daily Graduation Rate

**Prompt**: 
```
What’s the success rate of projects on Solana memecoin launchpads for the past 5 days?
```

**Output**:
```markdown
| block_date | LaunchLabs | LetsBonk | Pump.fun | Boop | Bags | Believeapp | Moonshot | Sunpump.meme |
|------------|------------|----------|----------|------|------|------------|----------|--------------|
| 2025-06-15 | 0.20       | 0.25     | 0.30     | 0.15 | 0.18 | 0.10       | 0.22     | 0.19         |
| 2025-06-14 | 0.18       | 0.22     | 0.28     | 0.12 | 0.15 | 0.08       | 0.20     | 0.17         |
| ...        | ...        | ...      | ...      | ...  | ...  | ...        | ...      | ...          |
```


### Get Daily Active Addresses

**Prompt**: 
```
Tell me how many wallets were active on Solana memecoin launchpads each day for the last week.
```

**Output**:
```markdown
| date_time  | LaunchLabs | LetsBonk | Pump.fun | Boop | Bags | Believeapp | Moonshot | Sunpump.meme |
|------------|------------|----------|----------|------|------|------------|----------|--------------|
| 2025-06-15 | 2000       | 800      | 5000     | 300  | 400  | 100        | 1200     | 900          |
| 2025-06-14 | 1800       | 700      | 4800     | 250  | 350  | 80         | 1100     | 800          |
| ...        | ...        | ...      | ...      | ...  | ...  | ...        | ...      | ...          |
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

