import secrets
from shlex import join
import string
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def generate_key(length=32):
    filtered_punctuation = ''.join(i for i in string.punctuation if i not in ['\\', '/', '{', '}', '[', ']', '(', ')', '"', "'", '`'])
    characters = string.ascii_lowercase + string.digits + string.ascii_uppercase + filtered_punctuation
    key = ''.join(secrets.choice(characters) for _ in range(length))
    return key.encode('utf-8')

def pad_data(data):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    return padded_data

def unpad_data(padded_data):
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    return data

def encrypt_data(key, data):
    backend = default_backend()
    iv = secrets.token_bytes(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    encryptor = cipher.encryptor()
    padded_data = pad_data(data)
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return iv + encrypted_data

def decrypt_data(key, encrypted_data): 
    backend = default_backend()
    iv = encrypted_data[:16]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data[16:]) + decryptor.finalize()
    unpadded_data = unpad_data(decrypted_data)
    return unpadded_data

############withoud using padding
# def encrypt_data(key, data):
#     backend = default_backend()
#     iv = secrets.token_bytes(16)
#     cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
#     encryptor = cipher.encryptor()
#     encrypted_data = encryptor.update(data) + encryptor.finalize()
#     return iv + encrypted_data

# def decrypt_data(key, encrypted_data): 
#     backend = default_backend()
#     iv = encrypted_data[:16]
#     cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
#     decryptor = cipher.decryptor()
#     decrypted_data = decryptor.update(encrypted_data[16:]) + decryptor.finalize()
#     return decrypted_data