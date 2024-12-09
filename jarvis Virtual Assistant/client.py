import openai

# Set your API key here (be sure to keep it private and secure!)
openai.api_key = "sk-proj-WxS17ehGk2PnwmzCHcDwT3B1bkFJFMj6bYTk9jG1bqZaFTcj"

# Send a chat completion request to OpenAI API
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud."},
        {"role": "user", "content": "What is coding?"}
    ]
)

# Print the response from OpenAI
print(completion.choices[0].message["content"])
