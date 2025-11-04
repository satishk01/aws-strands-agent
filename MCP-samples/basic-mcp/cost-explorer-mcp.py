from strands import Agent
from strands.tools.mcp import MCPClient
from mcp import stdio_client, StdioServerParameters
from strands.models import BedrockModel

aws_docs_client = MCPClient(
    lambda: stdio_client(StdioServerParameters(command="uvx", args=["awslabs.cost-explorer-mcp-server@latest"]))
)

bedrock_model = BedrockModel(
  model_id="us.amazon.nova-pro-v1:0",
  temperature=0.3,
  streaming=True, # Enable/disable streaming
)

with aws_docs_client:
   agent = Agent(model=bedrock_model, tools=aws_docs_client.list_tools_sync())
   response = agent("Analyze the cost for the last quarter and let me know in each month of the quarter what was the top 3 servies adding to cost")   