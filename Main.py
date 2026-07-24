import os
import ollama

def analyze_setup_image(image_path, prompt):
    """
    Passes a local image and prompt to an offline vision model.
    """
    if not os.path.exists(image_path):
        print(f"Error: Image '{image_path}' not found.")
        return

    print(f"Analyzing '{image_path}' using local vision model...")
    
    # Calls local Ollama vision model (e.g., llama3.2-vision)
    response = ollama.chat(
        model='llama3.2-vision',
        messages=[{
            'role': 'user',
            'content': prompt,
            'images': [image_path]
        }]
    )
    
    return response['message']['content']

if __name__ == "__main__":
    print("--- Local AI Vision & Lab Assistant ---")
    # Example usage:
    # result = analyze_setup_image("sample_setup.jpg", "Explain the setup in this photo.")
    # print(result)
  
