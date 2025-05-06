#!/usr/bin/env python3

# Dictionary mapping characters to their Morse code equivalents
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': ' ', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', '!': '-.-.--', '@': '.--.-.'
}

def text_to_morse(text):
    """
    Convert input text to Morse code.
    
    Args:
        text (str): The input text to convert
        
    Returns:
        str: The Morse code representation of the input text
    """
    # Convert text to uppercase for consistent mapping
    text = text.upper()
    
    # Convert each character to Morse code
    morse_code = ' '.join(MORSE_CODE_DICT.get(char, '') for char in text)
    
    return morse_code

def main():
    print("Welcome to the Morse Code Converter!")
    print("Enter 'quit' to exit the program.")
    
    while True:
        # Get input from user
        user_input = input("\nEnter text to convert to Morse code: ")
        
        # Check if user wants to quit
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Convert and display the result
        morse_result = text_to_morse(user_input)
        print(f"Morse code: {morse_result}")

if __name__ == "__main__":
    main() 