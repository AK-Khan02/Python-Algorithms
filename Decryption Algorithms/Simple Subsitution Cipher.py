def decrypt_simple_substitution(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_map = {k: v for k, v in zip(key, alphabet)}
    decrypted = ""
    for char in text:
        if char.lower() in key_map:
            decrypted += key_map[char.lower()].upper() if char.isupper() else key_map[char.lower()]
        else:
            decrypted += char
    return decrypted

# Key and Examples
key = "phqgiumeaylnofdxjkrcvstzwb"
examples = ["Kf qlfkd tfqe!", "Qb qbttqz!", "Rfc dmpq gzpq", "Ufmfc ypc ly.", "Jgicqy Dgcej"]

for example in examples:
    print(f"Encrypted: {example} => Decrypted: {decrypt_simple_substitution(example, key)}")
