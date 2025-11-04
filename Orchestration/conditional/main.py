from strands import Agent
from strands.multiagent import GraphBuilder
from config import get_model, RETRIEVER_PROMPT, BUY_PROMPT, SELL_PROMPT
from tools import stock_price_calculator
from utils import submit_buy, submit_sell, extract_clean_results

def create_agents():
    """Create and configure all agents."""
    model = get_model()
    
    retriever_agent = Agent(
        model=model,
        tools=[stock_price_calculator],
        system_prompt=RETRIEVER_PROMPT
    )
    
    buy_agent = Agent(
        model=model,
        system_prompt=BUY_PROMPT
    )
    
    sell_agent = Agent(
        model=model,
        system_prompt=SELL_PROMPT
    )
    
    return retriever_agent, buy_agent, sell_agent

def build_conditional_graph():
    """Build the conditional edge graph."""
    retriever_agent, buy_agent, sell_agent = create_agents()
    
    builder = GraphBuilder()
    
    # Add nodes
    builder.add_node(retriever_agent, "retriever")
    builder.add_node(buy_agent, "buyer")
    builder.add_node(sell_agent, "seller")
    
    # Add conditional edges
    builder.add_edge("retriever", "buyer", condition=submit_buy)
    builder.add_edge("retriever", "seller", condition=submit_sell)
    
    # Set entry point
    builder.set_entry_point("retriever")
    
    return builder.build()

def run_graph(task):
    """Execute the graph with given task."""
    graph = build_conditional_graph()
    result = graph(task)
    return result

def main():
    """Main execution function."""
    task = "I want to see what to do with Tesla stock, get the stock price and make a decision to buy or sell."
    result = run_graph(task)
    
    # Method 1: Using helper function for clean parsing
    clean_results = extract_clean_results(result)
    
    print("\n" + "="*50)
    print("📊 CLEAN GRAPH RESULTS")
    print("="*50)
    print(f"📈 Status: {clean_results['status']}")
    print(f"🔄 Execution Order: {clean_results['execution_order']}")
    print(f"✅ Completed: {clean_results['completed_count']} | ❌ Failed: {clean_results['failed_count']}")
    
    # Show stock price and decision
    stock_price = clean_results['node_results']['retriever']
    print(f"\n💰 Stock Price: ${stock_price}")
    
    if 'buyer' in clean_results['node_results']:
        print(f"🟢 Decision: BUY")
        print(f"📝 Details: {clean_results['node_results']['buyer']}")
    elif 'seller' in clean_results['node_results']:
        print(f"🔴 Decision: SELL") 
        print(f"📝 Details: {clean_results['node_results']['seller']}")
    
    print(f"\n⏱️ Execution Time: {clean_results['total_execution_time']}ms")
    print(f"💸 Tokens Used: {clean_results['total_tokens']}")
    print("="*50)

if __name__ == "__main__":
    main() 