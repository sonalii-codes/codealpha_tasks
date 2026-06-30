# A simple Chatbot 
#task 2

def chatbot():
# Welcome message 
    print("Chatbot: Hello!")
    while True:
# take input from user
        user = input("You: ").lower().strip()
        if user == "hello":
            print("Chatbot: Hii!")
        elif user == "how are you":
            print("Chatbot: I'am fine,Thanks!")
        elif user == "bye":    
            print("Chatbot: Goodbye! Have a nice day")
            break
# If input doesn't match with predefined response
        else:
            
            print("Chatbot: Sorry! I can't understand")
#Call the function to start the chatbot
chatbot()                   

