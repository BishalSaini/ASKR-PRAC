import aiml
import os

def run():
    kernel = aiml.Kernel() 
    kernel.learn("p3aiml.aiml")
    
    print("E-commerence chatbot is ready to run")
    
    while True:
        user_input = input("YOU:")
        if user_input.lower() == "exit": 
            print("ChatBot: Thank you for visiting! Come back soon.")
            break
        response = kernel.respond(user_input)
        print("ChatBot:", response)

run()
