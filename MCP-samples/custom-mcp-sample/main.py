from mcp.server.fastmcp import FastMCP

# for more structured data
from pydantic import BaseModel, Field

# create a MCP server
mcp = FastMCP("demo-mcp-py")


class FetchData(BaseModel):
    """data structure"""

    age: int = Field(description="Age of the person")
    phone_no: str = Field(description="phone number of the person")
    realtion: str = Field(description="realtion of the person")
    activity: list[str] = Field(description="Interests of the person")

# random people list
people_db: dict[str, FetchData] = {
    "Hobes":  FetchData(age=30, phone_no="9911939394",   realtion="Companion", activity=["Hunting", "Sleeping"]),
    "Calvin":FetchData(age=33, phone_no="9911939395",   realtion="Thinker",   activity=["HUnting", "Troubling"]),
    "Sylvester": FetchData(age=44, phone_no="9911939396", realtion="Cat",  activity=["RatCatching", "HUnting"]),
    "Tweety": FetchData(age=55, phone_no="9911939397", realtion="Bird",   activity=["Swinging", "Running"])
}

# return biodata tool using pydantic model and people list (mock database)
@mcp.tool()
def return_FetchData(name: str) -> FetchData:
    """Return details for a known person name."""
    try:
        return people_db[name]
    except KeyError:
        # MCP hosts will display this as a tool error
        raise ValueError(f"Person '{name}' not found in database")

if __name__ == "__main__":
    mcp.run(transport="stdio")