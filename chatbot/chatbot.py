{
  "greetings": [
    "hello",
    "hi",
    "hey",
    "good morning",
    "good afternoon"
  ],
  "faqs": [
    {
      "question": "What are your hours of operation?",
      "answer": "We operate Monday through Friday from 9:00 AM to 6:00 PM IST."
    },
    {
      "question": "How do I submit my internship project?",
      "answer": "You can submit your public GitHub repository link through your Student Workspace."
    },
    {
      "question": "When will I receive my certificate?",
      "answer": "Certificates are reviewed and issued within 3-5 business days after your code review."
    }
  ]
}


import json
import re
import random


# Function 1: Load FAQ dataset
def load_faq_data():

    try:
        with open("sample_faq.json", "r") as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        print("Error: sample_faq.json file not found.")
        return None

    except json.JSONDecodeError:
        print("Error: Invalid JSON file.")
        return None


# Function 2: Normalize user input
def normalize_input(user_input):

    user_input = user_input.lower().strip()

    user_input = re.sub(r"\s+", " ", user_input)

    return user_input


# Function 3: Check greetings
def check_greeting(user_input, data):

    greetings = data.get("greetings", [])

    for greeting in greetings:

        pattern = r"\b" + re.escape(greeting.lower()) + r"\b"

        if re.search(pattern, user_input):

            return random.choice([
                "Hello! Welcome to our assistant.",
                "Hi! How can I help you today?",
                "Greetings! What would you like to know?"
            ])

    return None


# Function 4: Identify user intentions
def identify_intents(user_input):

    intent_patterns = {

        "hours": [
            r"\bhours?\b",
            r"\bworking hours\b",
            r"\bbusiness hours\b",
            r"\bopening time\b",
            r"\bclosing time\b",
            r"\bwhen are you open\b",
            r"\bwhen do you operate\b"
        ],

        "submission": [
            r"\bsubmit\b",
            r"\bsubmission\b",
            r"\binternship project\b",
            r"\bgithub\b",
            r"\brepository\b",
            r"\bupload my project\b"
        ],

        "certificate": [
            r"\bcertificate\b",
            r"\bcertificates\b",
            r"\bcertification\b",
            r"\bwhen will i receive\b"
        ]

    }

    detected_intents = []

    for intent, patterns in intent_patterns.items():

        for pattern in patterns:

            if re.search(pattern, user_input):

                detected_intents.append(intent)

                break

    return detected_intents


# Function 5: Get answers from JSON dataset
def get_faq_answer(intent, data):

    faqs = data.get("faqs", [])

    faq_mapping = {
        "hours": 0,
        "submission": 1,
        "certificate": 2
    }

    index = faq_mapping.get(intent)

    if index is not None and index < len(faqs):

        return faqs[index]["answer"]

    return None


# Function 6: Generate chatbot response
def generate_response(user_input, data):

    user_input = normalize_input(user_input)

    # Check greeting
    greeting_response = check_greeting(user_input, data)

    # Detect multiple intents
    intents = identify_intents(user_input)

    responses = []

    if greeting_response:

        responses.append(greeting_response)

    # Get answers for all detected intents
    for intent in intents:

        answer = get_faq_answer(intent, data)

        if answer:
            responses.append(answer)

    # Fallback response
    if not responses:

        return (
            "Sorry, I couldn't understand your question. "
            "Please ask about business hours, project submission, "
            "or certificates."
        )

    return "\n".join(responses)


# Function 7: Main chatbot
def chatbot():

    data = load_faq_data()

    if data is None:
        return

    print("\n====================================")
    print("    INTERACTIVE CHATBOT ASSISTANT")
    print("====================================")

    print("\nBot: Hello! Welcome to our support assistant.")

    print("Bot: You can ask me about:")

    print("- Business hours")
    print("- Internship project submission")
    print("- Certificate details")

    print("\nType 'bye', 'exit', or 'quit' to end the chat.")

    # Conversation loop
    while True:

        user_input = input("\nYou: ").strip()

        # Check empty input
        if not user_input:

            print("Bot: Please enter a question.")
            continue

        # Check exit commands
        if user_input.lower() in ["bye", "exit", "quit"]:

            print("\nBot: Thank you for chatting with us!")
            print("Bot: Have a great day. Goodbye!")

            break

        # Generate response
        response = generate_response(user_input, data)

        print("\nBot:", response)


# Execute chatbot
if __name__ == "__main__":

    chatbot()
