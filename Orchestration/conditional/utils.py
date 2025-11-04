import re

def submit_buy(state):
    """Conditional function to route to buy agent if stock price < 750."""
    #print(state)
    stock_retriever_result = state.results.get("retriever")
    if not stock_retriever_result:
        return False
    
    # Get the text content from the AgentResult
    agent_result = stock_retriever_result.result
    text_content = agent_result.message['content'][0]['text']
    #print(f"Text content: {text_content}")
    
    # Parse the price from the text (handle both $973 and plain 973)
    price_matches = re.findall(r'\$?(\d+)', text_content)
    
    if price_matches:
        result = int(price_matches[0])
        if result < 750:
            print(f"🟢 Routing to BUYER: Stock price ${result} < $750")
            return True
        return False
    
    return False


def submit_sell(state):
    """Conditional function to route to sell agent if stock price > 750."""
    #print(state)
    stock_retriever_result = state.results.get("retriever")
    if not stock_retriever_result:
        return False
    
    # Get the text content from the AgentResult
    agent_result = stock_retriever_result.result
    text_content = agent_result.message['content'][0]['text']
    #print(f"Text content: {text_content}")
    
    # Parse the price from the text (handle both $973 and plain 973)
    price_matches = re.findall(r'\$?(\d+)', text_content)
    
    if price_matches:
        result = int(price_matches[0])
        if result > 750:
            print(f"🔴 Routing to SELLER: Stock price ${result} > $750")
            return True
        return False
    
    return False

def extract_clean_results(graph_result):
    """
    Clean result extraction using Strands GraphState properties.
    Based on Strands documentation: https://strandsagents.com/latest/documentation/docs/user-guide/concepts/multi-agent/graph/
    """
    results = {
        'status': graph_result.status,
        'execution_order': [node.node_id for node in graph_result.execution_order],
        'completed_count': graph_result.completed_nodes,
        'failed_count': graph_result.failed_nodes,
        'total_execution_time': sum(node.execution_time for node in graph_result.execution_order),
        'total_tokens': graph_result.accumulated_usage['totalTokens'],
        'node_results': {}
    }
    
    # Extract individual node results
    for node_id, node_result in graph_result.results.items():
        results['node_results'][node_id] = node_result.result.message['content'][0]['text']
    
    return results 