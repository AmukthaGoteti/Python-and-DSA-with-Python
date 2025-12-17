import re
import random

# Define patterns and responses for the chatbot
patterns = {
    r'\bhi\b': ['Hello!'],
    r'\bhello\b': ['Hi there!'],
    r'\bhey\b': ['Hey!'],
    r'how are you': [
        "I'm just a chatbot, but I'm here to help!",
        "I'm here to provide support. How can I assist you today?"
    ],
    r'(.*) sad': [
        "I'm sorry to hear that. It's okay to feel down sometimes. Would you like to talk about it?",
        "I'm here to listen. What's been bothering you?"
    ],
    r'(.*) happy': [
        "That's great to hear!",
        "I'm glad to hear that you're feeling happy. What's making you feel this way?"
    ],
    r'(.*) anxious': [
        "I understand that feeling. Let's work through it together. What's been causing you stress or anxiety?"
    ],
    r'(.*) thank you': [
        "You're welcome!",
        "No problem at all. If you have more questions or need support, feel free to ask."
    ],
    r'(.*) unhappy|depressed|down|bad': [
        "I'm sorry to hear that. It's okay to feel down sometimes.",
        "I'm here to listen. What's been bothering you?"
    ],
    r'(.*) joyful|good': [
        "That's great to hear!",
        "I'm glad to hear that you're feeling positive."
    ],
    r'(.*) stressed|worried': [
        "I understand that feeling. Let's work through it together."
    ],
    r'\bbye\b|\bgoodbye\b': [
        "Goodbye!",
        "Take care!",
        "If you ever need to talk, I'll be here."
    ],
    r'(.*) help': [
        "Of course, I'm here to help. What do you need assistance with?"
    ],
    r'(.*) information': [
        "I can provide information on a wide range of topics. What would you like to know?"
    ],
    r'(.*) age': [
        "I'm just a computer program, so I don't have an age."
    ],
    r'(.*) hobby|hobbies': [
        "Hobbies are a great way to relax. What do you enjoy doing?"
    ],
    r'(.*) love': [
        "Love is a wonderful feeling. What would you like to talk about?"
    ],
    r'(.*) travel': [
        "Travelling is exciting! Where would you like to go?"
    ],
    r'(.*) food': [
        "Food is a great topic! What's your favourite cuisine?"
    ],
    r'(.*) indian food': [
        "Indian food is diverse, flavorful, and rich in spices."
    ],
    r'(.*) music': [
        "Music is a wonderful form of expression. What's your favourite genre?"
    ],
    r'(.*) sports': [
        "Sports are a great way to stay active. Do you play or watch any sports?"
    ],
    r'(.*) career advice|job': [
        "Career planning is important. Tell me more about what you're looking for."
    ],
    r'(.*) interview': [
        "Interviews can be challenging, but preparation makes a big difference."
    ],
    r'(.*) resume': [
        "A strong resume highlights skills, achievements, and experience clearly."
    ],
}

# Create a function to respond to user input
def respond(user_input):
    for pattern, responses in patterns.items():
        if re.search(pattern, user_input.lower()):
            return random.choice(responses)
    return "I'm here to provide support. How can I assist you today?"

# Main function
def main():
    print("Emotional Support Chatbot: Hello! How can I assist you today?")
    print("Type 'goodbye' to end the conversation.\n")

    while True:
        user_input = input("You (Type Goodbye to end conversation): ").strip()

        if user_input.lower() in ['goodbye', 'bye']:
            print("Emotional Support Chatbot: Goodbye! Take care.")
            break

        response = respond(user_input)
        print("Emotional Support Chatbot:", response)

# Entry point
if __name__ == "__main__":
    main()