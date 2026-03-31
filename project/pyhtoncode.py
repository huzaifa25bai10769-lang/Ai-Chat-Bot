# Simple rule-based chatbot

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Chatbot: Hi there!")
    
    elif user_input == "how are you":
        print("Chatbot: I'm just a bot, but I'm doing great!")
    
    elif user_input == "your name":
        print("Chatbot: I'm a simple chatbot.")
    
    elif user_input == "bye":
        print("Chatbot: Goodbye!")
        break
    
    else:
        print("Chatbot: Sorry, I don't understand that.")