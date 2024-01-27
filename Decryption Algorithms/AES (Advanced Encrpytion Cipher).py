from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import base64

def decrypt_aes(ciphertext, key, iv):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
    decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()
    return decrypted.decode('utf-8')

# Examples - Note: For simplicity, these are just placeholders. In practice, use secure key/iv and base64 encoded ciphertexts.
key = b"your16bytesecrety"  # 16 bytes key for AES-128
iv = b"your16bytesivsect"  # 16 bytes initialization vector
examples = [base64.b64encode(b"Example encrypted text 1"), base64.b64encode(b"Example encrypted text 2")]

for example in examples:
    ciphertext = base64.b64decode(example)
    print(f"Decrypted: {decrypt_aes(ciphertext, key, iv)}")
