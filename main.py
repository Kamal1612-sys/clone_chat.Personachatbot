import openai

openai.api_base = "https://openrouter.ai/api/v1"

# Put your OpenRouter API key here
openai.api_key = "your-api-key-here"

print("🤖 Chatbot loaded! Type 'exit' to quit.")
print("You:")

user_profile = """
This is your custom profile.
You can add details about yourself here, like your interests, background, and personality.
For example:
- Your name or nickname
- Where you are from
- Your hobbies and likes
- Any traits you want the chatbot to embody
"""

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Bye! Take care 😎✌️")
        break

    try:
        response = openai.ChatCompletion.create(
            messages=[
                {"role": "system", "content": f"You are a chatbot. Here's your profile:\n{user_profile}"},
                {"role": "user", "content": user_input}
            ]
        )

        chatbot_reply = response["choices"][0]["message"]["content"]
        print("Chatbot:", chatbot_reply)

    except Exception as e:
        print("❌ Error:", e)
