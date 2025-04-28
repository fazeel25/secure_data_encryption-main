from cryptography.fernet import Fernet
import hashlib
import json
import os


if not os.path.exists("secret.key"):
    with open("secret.key", "wb") as key_file:
        key_file.write(Fernet.generate_key())

with open("secret.key", "rb") as file:
    KEY = file.read()


cipher = Fernet(KEY)

# Hash Password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Load Users
def load_users():
    with open("users.json", "r") as file:
        return json.load(file)

# Save Users
def save_users(users):
    with open("users.json", "w") as file:
        return json.dump(users, file, indent=4)
    
# Load Data
def load_data():
    if not os.path.exists("data.json"):
        return {}
    with open("data.json", "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

    
# Save Data
def save_data(data):
    with open("data.json", "w") as file:
        return json.dump(data, file, indent=4)
    
# Encrypt Data
def encrypt(text):
    return cipher.encrypt(text.encode()).decode()

# Decrypt Data
def decrypt(encrypted):
    return cipher.decrypt(encrypted.encode()).decode()

