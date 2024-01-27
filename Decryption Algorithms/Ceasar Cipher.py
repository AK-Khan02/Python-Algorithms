def decrypt_caesar_cipher(text, shift):
    decrypted = ""
    for char in text:
        if char.isalpha():
            start = 'A' if char.isupper() else 'a'
            decrypted += chr((ord(char) - ord(start) - shift) % 26 + ord(start))
        else:
            decrypted += char
    return decrypted

# Examples
examples = [
    ("Bqqmf", 1),
    ("Crrng", 2),
    ("Ettqi", 4),
    ("Hwwtl", 7),
    ("Kyywo", 10)
]

for example, shift in examples:
    print(f"Encrypted: {example}, Shift: {shift} => Decrypted: {decrypt_caesar_cipher(example, shift)}")
