import aiml

def play():
    ker = aiml.Kernel()
    ker.learn("p4aiml.aiml")
    print("Game bot: type rock paper scissors to play. Type quit to exit.")

    while True:
        user_input = input("You: ").strip().upper()
        if user_input == "QUIT":
            print("Good day")
            break
        elif user_input in ["ROCK", "PAPER", "SCISSORS"]:
            response = ker.respond(user_input)
            print("Game Bot:", response)
        else:
            print("I don't understand the command")

play()
