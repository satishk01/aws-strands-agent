import random
from strands import tool

@tool
def stock_price_calculator(stock_name: str) -> dict:
    """Calculate mock stock price for given stock name."""
    print(f"Calculating stock price for {stock_name}")
    stock_price = random.randint(100, 1000)
    return {f"Current price of {stock_name}": stock_price} 