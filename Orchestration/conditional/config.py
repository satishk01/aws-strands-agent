from strands.models import BedrockModel

# Model configuration
MODEL_CONFIG = {
    ###"model_id": "us.anthropic.claude-sonnet-4-20250514-v1:0",
    "model_id": "us.anthropic.claude-3-5-sonnet-20241022-v2:0",
    "region_name": "us-east-1"
}

def get_model():
    """Get configured Bedrock model instance."""
    return BedrockModel(**MODEL_CONFIG)

# Agent prompts
RETRIEVER_PROMPT = """You are a stock retriever agent. You are given a stock name and you use the stock_price_calculator tool to get a mock price of the stock.

You then return the price in a message, don't give any other information or recommendations.
"""

BUY_PROMPT = """You are a buy agent. You receive a stock price from the retriever agent and should recommend BUYING the stock. 

Use the price that was provided by the previous agent and make a buy recommendation. Don't worry about real-world prices - just use the retriever's price data to make your buy decision, no need to mention any reasoning or details.

Output Format: Recommend BUY for [STOCK] at $[PRICE].
"""

SELL_PROMPT = """You are a sell agent. You receive a stock price from the retriever agent and should recommend SELLING the stock.

Use the price that was provided by the previous agent and make a sell recommendation. Don't worry about real-world prices - just use the retriever's price data to make your sell decision, no need to mention any reasoning or details.

OutputFormat: Recommend SELL for [STOCK] at $[PRICE].
"""
