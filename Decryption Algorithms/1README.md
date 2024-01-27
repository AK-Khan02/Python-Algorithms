# Decryption Algorithms

## About
This folder is dedicated to a diverse set of decryption algorithms, implemented in Python, ranging from classical ciphers to modern cryptographic techniques. Decryption is the process of converting encrypted data back into its original form. This collection provides a hands-on approach to understanding how various encryption methods can be reversed or decrypted.

## Algorithms Included

### AES (Advanced Encryption Standard)
- **File**: `AES (Advanced Encryption Cipher).py`
- **Description**: The AES decryption algorithm reverses the process of AES encryption to retrieve the original plaintext from the ciphertext. AES is widely used in secure communications, file encryption, and other security-sensitive applications due to its robustness and efficiency.

### Atbash Cipher
- **File**: `Atbash Cipher.py`
- **Description**: The Atbash Cipher is a simple substitution cipher that maps each alphabet letter to its reverse, so the first letter becomes the last letter, and vice versa. Its decryption process simply applies the same substitution in reverse.

### Caesar Cipher
- **File**: `Ceasar Cipher.py`
- **Description**: The Caesar Cipher is one of the oldest known encryption techniques. It decrypts by shifting each letter in the ciphertext a certain number of places down the alphabet. The decryption key is the inverse of the encryption key.

### ECC Decryption (Elliptic Curve Cryptography)
- **File**: `ECC Decryption (Elliptic Curve Cryptography).py`
- **Description**: ECC Decryption uses the properties of elliptic curves to decrypt data encrypted with ECC encryption. It offers a high level of security with smaller key sizes compared to other encryption methods, making it efficient for use in constrained environments.

### RSA Decryption
- **File**: `RSA Decryption.py`
- **Description**: RSA is a public-key cryptographic algorithm that decrypts data by using a pair of keys, a public key for encryption and a private key for decryption. RSA Decryption involves mathematical operations based on the properties of prime numbers.

### Simple Substitution Cipher
- **File**: `Simple Subsitution Cipher.py`
- **Description**: This cipher replaces each element of the plaintext with a corresponding element of the ciphertext alphabet according to a fixed system. The decryption process involves reversing the substitution using the known cipher alphabet.

### Vigenère Cipher
- **File**: `Vigenerer Cipher.py`
- **Description**: The Vigenère Cipher is a method of encrypting alphabetic text through a simple form of polyalphabetic substitution. Decryption requires knowledge of the keyword used to encrypt the text, applying the inverse of the encryption process.
