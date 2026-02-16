import ollama

while True:
    question = input("Ask something (or type 'exit' to quit): ")

    if question.lower() in ['exit', 'quit', 'bye']:
        print("Goodbye!")
        break

    response = ollama.generate(model='mistral', prompt=question)

    print("Answer:", response['response'])
