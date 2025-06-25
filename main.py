from mcp.server.fastmcp import FastMCP
from pr_utils import get_links_prnewswire, get_article_content

mcp = FastMCP("PRNewswire")

@mcp.tool()
def get_press_releases(topic) -> list[dict]:
    '''
    Fetches press releases from PRNewswire based on the topic and date range.

    Args:
        topic (str): The topic to search for.

    Returns:
        list: A list of dictionaries containing the title, date, and content of the press releases.
    '''
    links = get_links_prnewswire(topic)
    press_releases = []
    for link in links:
        article = get_article_content(link)
        if article:
            press_releases.append(article)

    return press_releases


if __name__ == "__main__":
    mcp.run(transport="stdio") # for local use
