#!/usr/bin/env python3
import sys

def unicode_to_hex(text):
    return '%'.join(f"{ord(char):x}" for char in text)

def utf8_to_hex(text):
    return '%' + '%'.join(f"{byte:02x}" for byte in text.encode('utf-8'))

def main():
    if len(sys.argv) < 2:
        print("Usage: python utf8_to_hex.py <text>")
        sys.exit(1)
    
    input_text = ' '.join(sys.argv[1:])
    hex_output = utf8_to_hex(input_text)
    
    print(hex_output)

if __name__ == "__main__":
    main()

