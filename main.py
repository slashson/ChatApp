from chat import send_message_to_model

print('hi')

def main():
    print("🤖 DeepSeek Chat | Type 'exit' to quit\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        try:
            reply = send_message_to_model(user_input)
            print("Bot:", reply)
        except Exception as e:
            print("❌ Error:", e)

if __name__ == "__main__":
    main()