import os
import json
import getpass
from cryptography.fernet import Fernet
from hashlib import sha256

DATA_FOLDER = os.path.expanduser("~/.secure_passman")
KEY_FILE = os.path.join(DATA_FOLDER, "key.key")
DB_FILE = os.path.join(DATA_FOLDER, "passwords.json")
MASTER_HASH_FILE = os.path.join(DATA_FOLDER, "master.hash")

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def init_storage():
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)

    if not os.path.exists(MASTER_HASH_FILE):
        print("🔐 Set up your master password (only once)")
        pw = getpass.getpass("Enter new master password: ")
        with open(MASTER_HASH_FILE, "w") as f:
            f.write(hash_password(pw))

def load_key():
    with open(KEY_FILE, "rb") as f:
        return Fernet(f.read())

def load_db():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "rb") as f:
        data = f.read()
    return json.loads(fernet.decrypt(data))

def save_db(db):
    encrypted = fernet.encrypt(json.dumps(db).encode())
    with open(DB_FILE, "wb") as f:
        f.write(encrypted)

def authenticate():
    attempt = getpass.getpass("Enter master password: ")
    with open(MASTER_HASH_FILE, "r") as f:
        stored_hash = f.read()
    return hash_password(attempt) == stored_hash

def add_password():
    site = input("Site: ")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    db = load_db()
    db[site] = {"username": username, "password": password}
    save_db(db)
    print("✅ Password saved.")

def view_passwords():
    db = load_db()
    if not db:
        print("❌ No passwords stored.")
        return
    for site, creds in db.items():
        print(f"\n🔐 {site}")
        print(f"   Username: {creds['username']}")
        print(f"   Password: {creds['password']}")

def delete_password():
    db = load_db()
    site = input("Enter site name to delete: ")
    if site in db:
        del db[site]
        save_db(db)
        print("🗑️ Deleted.")
    else:
        print("❌ Not found.")

def menu():
    while True:
        print("\n====== Secure Password Manager ======")
        print("1. Add new password")
        print("2. View all passwords")
        print("3. Delete a password")
        print("4. Exit")
        choice = input("Choose: ")

        if choice == '1':
            add_password()
        elif choice == '2':
            view_passwords()
        elif choice == '3':
            delete_password()
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    init_storage()
    fernet = load_key()
    if authenticate():
        menu()
    else:
        print("🚫 Wrong master password.")

