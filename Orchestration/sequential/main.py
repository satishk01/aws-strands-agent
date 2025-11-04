"""Sequential graph example with data creation and analysis."""

from strands import Agent
from strands_tools import shell 
from strands.multiagent import GraphBuilder
from config import get_model, DATA_CREATION_PROMPT, DATA_ANALYSIS_PROMPT


def create_agents():
    """Create and return the data creation and analysis agents."""
    model = get_model()
    
    data_creation_agent = Agent(
        model=model,
        tools=[shell],
        system_prompt=DATA_CREATION_PROMPT
    )
    
    data_analysis_agent = Agent(
        model=model,
        tools=[shell],
        system_prompt=DATA_ANALYSIS_PROMPT
    )
    
    return data_creation_agent, data_analysis_agent


def build_sequential_graph():
    """Build and return the sequential graph."""
    data_creation_agent, data_analysis_agent = create_agents()
    
    builder = GraphBuilder()
    builder.add_node(data_creation_agent, "data_creation")
    builder.add_node(data_analysis_agent, "data_analysis")
    builder.add_edge("data_creation", "data_analysis")
    builder.set_entry_point("data_creation")
    
    return builder.build()


def run_graph(prompt: str):
    """Execute the sequential graph and return results."""
    graph = build_sequential_graph()
    result = graph(prompt)
    return result


def main():
    """Main execution function."""
    sample_prompt = "Generate a CSV file with mock transaction data for the month of October, then analyze the data and give me a report."
    
    result = run_graph(sample_prompt)
    
    # Display results
    print(f"\nGraph Execution Finished!")
    print(f"Final Status: {result.status}")
    if result.status == "FAILED":
        print("Graph execution failed")
    else:
        print("Graph execution successful!")
        print(f"Execution order: {[node.node_id for node in result.execution_order]}")

if __name__ == "__main__":
    main()