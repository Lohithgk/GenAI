# Run Large Language Models locally with Ollama #

# Import the agent and the Ollama model
from agno.agent import Agent
from agno.models.ollama import Ollama

# Create the agent
agent = Agent(
    model=Ollama(id = "llama3.2", 
                 provider = "Ollama", 
                 system_prompt = "You are a helpful assistant, based on the input, answer in markdown format."),
    markdown=True)

# Print the response in the terminal
agent.print_response("Tell me about yourself.")