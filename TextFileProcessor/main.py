import ollama
import os

# assign the model llama3.2 to model variable
model = "llama3.2"

# path to input text file
input_file ="/Users/lohithgk/AI Projects/GenAI/TextFileProcesor/Cars.txt"

# check if the input file exists
if not os.path.exists(input_file):
    print(f"Input file {input_file} does not exist.")
    exit(1)

# open the input file in read mode and close it after reading.
with open(input_file, 'r') as file:
    # read the content of the file into a variable named 'text'
    text = file.read()

# create a detailed prompt for the model to process the text
# The prompt instructs the model to extract car names, their prices, and features in a structured format.
prompt = f"""
You are a helpful assistant. Your task is to process the following text 
and the text is as follows: {text}
Please list Car make, Model, Year and their price, and values are separated by commas.
and the final result should be in bulleted format Categorized by Car make.
"""

# call the ollama model with the prompt and model   
response = ollama.generate(model=model, prompt=prompt)

# print the response, accessing the 'response' key from the response dictionary using the get method
# If 'response' key does not exist, it will print "No response generated"   
print(response.get('response', "No response generated"))