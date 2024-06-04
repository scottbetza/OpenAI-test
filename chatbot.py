# importing openai library for AI chatbot 
import openai

# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 

# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI()

# Function to generate a response from the chatbot
def generate_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

# Main loop for the chatbot
while True:
    user_input = input("User: ")
    if user_input.lower() in ["bye", "goodbye", "exit"]:
        print("Chatbot: Goodbye!")
        break
    
    prompt = user_input
    response = generate_response(prompt)
    print(f"Chatbot: {response}")