import aiml

kernel = aiml.Kernel()
kernel.learn("rest.aiml")

print("recommendation is running")
print("type quit to exit")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":  # Handles case-insensitive exit
        print("Bot: GoodBye!")
        break
    response = kernel.respond(user_input)
    if response:
        print("bot:", response)
    else:
        print("bot: Sorry, I didn't understand that.")  # Handles unknown inputs
