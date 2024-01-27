def decrypt_vigenere_cipher(text, keyword):
    decrypted = ""
    keyword_repeated = ''.join(keyword[i % len(keyword)] for i in range(len(text)))
    for char, key_char in zip(text, keyword_repeated):
        shift = ord(key_char.lower()) - ord('a')
        decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A')) if char.isupper() else chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
    return decrypted

# Examples
examples = [
    ("Jevpq, Wyvnd!", "KEY"),
    ("Bjj rwkcs dwpyp fwz", "SECRET"),
    ("Hcdm Qcrc!", "HELLO"),
    ("Pmttw, hdwztl!", "WORLD"),
    ("F xjwhwj bnymjw Gjxy", "PYTHON")
]

for text, keyword in examples:
    print(f"Encrypted: {text}, Keyword: {keyword} => Decrypted: {decrypt_vigenere_cipher(text, keyword)}")
