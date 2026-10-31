import base64
import binascii

while True:
    encoded_text = input("Enter a Base64 string: ").strip()

    if not encoded_text:
        print("No input provided. Exiting.")
        break

    try:
        decoded_bytes = base64.b64decode(encoded_text, validate=True)
        decoded_text = decoded_bytes.decode("utf-8")
    except (ValueError, binascii.Error, UnicodeDecodeError):
        print("Invalid Base64 input. Please enter a valid Base64 string.")
        continue

    print("Decoded message:", decoded_text)
    break
