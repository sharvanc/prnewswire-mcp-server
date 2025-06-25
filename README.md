# PRNewswire Press Release Fetcher
A Model Context Protocol (MCP) server that fetches and processes press releases from PRNewswire based on specified topics.

## Overview
This project provides an MCP server that allows AI assistants to retrieve recent press releases from PRNewswire. It scrapes press release content based on user-specified topics and returns structured data containing the title, date, and content of each press release.

## Features
- Search for press releases by topic
- Filter results by date range (default: last 7 days)
- Extract structured data from press releases
- Seamless integration with AI assistants via MCP

## Available Tools
get_press_releases(topic)
Fetches press releases from PRNewswire based on the specified topic.

Parameters:

- topic (str): The topic to search for (e.g., "artificial intelligence", "healthcare", "finance")
Returns:

- A list of dictionaries, each containing:
  - title: The title of the press release
  - date: The publication date
  - content: The full text content of the press release

## Dependencies
- bs4 - For HTML parsing
- httpx - HTTP client
- mcp - Model Context Protocol framework
- pandas - For date handling
- requests - For HTTP requests

### Important:
This project is for educational purposes only. It is not intended for commercial use.