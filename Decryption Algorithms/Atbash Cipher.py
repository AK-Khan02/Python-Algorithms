def decrypt_atbash_cipher(text):
    decrypted = ""
    for char in text:
        if char.isalpha():
            decrypted += chr(25 - (ord(char.upper()) - ord('A')) + ord('A')) if char.isupper() else chr(25 - (ord(char) - ord('a')) + ord('a'))
        else:
            decrypted += char
    return decrypted

# Examples
examples = ["Zggzxp", "Tlooh", "Gsvjf", "Ufm", "Hvxfirmt"]

for example in examples:
    print(f"Encrypted: {example} => Decrypted: {decrypt_atbash_cipher(example)}")
