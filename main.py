import os

# Function to load your system prompt instructions
def load_system_prompt(file_path="system_prompt.text"):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.read()
    return "You are an AI research assistant helping with project setups."

# Main assistant pipeline
def run_assistant():
    print("--- Local AI Lab & Research Assistant ---")
    system_prompt = load_system_prompt()
    print("System Prompt Loaded Successfully.\n")
    
    while True:
        user_query = input("Ask a setup or research question (or type 'exit'): ")
        if user_query.lower() == 'exit':
            print("Exiting Assistant.")
            break
            
        print(f"\n[AI Assistant]: Processing query with local context...")
        # Note: In a local setup, this connects to Ollama via the ollama API library.
        print(f"Responding to: '{user_query}' under System Prompt guidelines.\n")

if __name__ == "__main__":
    run_assistant()
