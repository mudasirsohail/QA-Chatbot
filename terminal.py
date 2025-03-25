import google.generativeai as geneai
from dotenv import load_dotenv
import os

load_dotenv()

geneai.configure(api_key= os.environ["GEMINI_API_KEY"])

model = geneai.GenerativeModel(model_name="gemini-2.0-flash")

while True:
    user_input = input("Enter your message (or 'quit' to exit): ")
    
    if user_input.lower() == 'quit':
        print("Thanks for chatting, Bye!")
        break
        
    response = model.generate_content(user_input)
    print(response.text)
    print() # Add blank line between responses