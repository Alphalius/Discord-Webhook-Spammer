import base64

def encode_to_base64(text):
  # Encode the input text to base64
  encoded_text = base64.b64encode(text.encode("utf-8"))
  
  # Return the encoded text
  return encoded_text

# Get user input
text = input("Enter the text you want to encode to base64: ")

# Encode the text and print the result
encoded_text = encode_to_base64(text)
print(f"Encoded text: {encoded_text}")
