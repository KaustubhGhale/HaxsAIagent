from groq import Groq

client = Groq(
    api_key="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",
)

running = True
while running:
    x=int(input("Enter 1 to talk with ai \nEnter 2 to quit\n"))
    if x == 1:
        prompt= input("What do you want to know: ")
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"{prompt}",
                }
            ],
            model="llama3-8b-8192",
        )
        print(chat_completion.choices[0].message.content)
    elif x == 2:
        running = False
        print("Thank you for using")
    else:
        print("Invalid input")
