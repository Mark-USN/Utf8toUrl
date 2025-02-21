#!/usr/bin/env python3
import sys

def unicode_to_hex(text):
    return '%'.join(f"{ord(char):x}" for char in text)

def utf8_to_hex_bytes(text):
    return '%' + '%'.join(f"{byte:02x}" for byte in text.encode('utf-8'))

def utf8_to_hex(text):
    hex_parts = []
    for char in text:
        utf8_bytes = char.encode('utf-8')  # Get UTF-8 encoding
        if len(utf8_bytes) == 1:
            hex_parts.append(f"%{utf8_bytes[0]:02x}")  # Single byte
        else:
            hex_parts.append(f"%{''.join(f'{b:02x}' for b in utf8_bytes)}")  # Multi-byte combined

    return ''.join(hex_parts)

def url_encode(text):
    return ''.join(f"%{byte:02x}" for byte in text.encode('utf-8'))

def main():
    if len(sys.argv) < 2:
        print("Usage: python utf8_to_hex.py <text>")
        sys.exit(1)
        
    input_text = ' '.join(sys.argv[1:])
    hex_output = url_encode(input_text)
    
    print(hex_output)

if __name__ == "__main__":
    main()

