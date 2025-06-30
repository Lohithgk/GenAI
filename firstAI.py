# Import the ollama module to interact with the Ollama API
import ollama
# define a variable 'Country' and assign it the value 'India'
# passing the country name as a string to the prompt of the Ollama API generate function
Country = 'India'
# generate a response using the Ollama API 
# The generate function takes a model and a prompt as arguments
# The model is 'llama3.2' and the prompt is a question about the capital of the specified country.
# The response will be a dictionary containing the generated text.
response: dict = ollama.generate(
    model = 'llama3.2',
    prompt = f'which is the capital of {Country}?')
# Print the response by accessing the 'response' key from the response dictionary using the get method
# If 'response' key does not exist, it will print "No response generated"
print(response.get('response', "No response generated"))