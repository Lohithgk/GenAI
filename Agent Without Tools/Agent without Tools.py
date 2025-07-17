# Run Large Language Models locally with Ollama #

# Import the agent and the Ollama model
from agno.agent import Agent
# from ollama module import Ollama class
from agno.models.ollama import Ollama

# Create the agent
agent = Agent(
    model=Ollama(
                 name = "Agent 001",
                 id = "llama3.2", 
                 provider = "Ollama", 
                 system_prompt = "You are a helpful assistant, based on the input, answer in markdown format."),
    markdown=True)

# Print the response in the terminal
agent.print_response("what is today's date & time in Banglore?")