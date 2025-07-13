🔐 Secure Password Manager (CLI-Based)

A simple, secure, and offline command-line password manager built in Python.
All credentials are encrypted using AES (Fernet) and protected with a master password.
📦 Features

    🔐 Master password authentication

    🔒 AES-128 encryption using cryptography.fernet

    🧾 Store, view, and delete passwords securely

    💾 Local file-based storage (offline)

    👀 No clipboard, no leaks, no dependencies on cloud

    🔒 SHA-256 used to protect master password

    👤 Data stored only in your ~/.secure_passman folder

🛠️ Installation
✅ Prerequisites

    Python 3.x

    cryptography package

Install the required package:

pip install cryptography

🚀 Getting Started

    Clone the repo:

git clone https://github.com/yourusername/secure-password-manager.git
cd secure-password-manager

Run the script:

    python secure_password_manager.py

    On first run, you'll be asked to set a master password.
    This password will be required for future access.

🧑‍💻 Usage

Once authenticated, choose from the menu:

====== Secure Password Manager ======
1. Add new password
2. View all passwords
3. Delete a password
4. Exit

🔐 Data Storage

All files are stored in:

~/.secure_passman/
├── key.key            # Encryption key (Fernet)
├── master.hash        # SHA-256 hash of master password
└── passwords.json     # Encrypted credentials

    ⚠️ Do not share or upload these files publicly!

🧹 Uninstall / Delete All Data

To delete all data and remove the tool:

rm -rf ~/.secure_passman
rm secure_password_manager.py

📄 License

This project is licensed under the MIT License.
Feel free to use, modify, and share.
✨ Future Enhancements (Optional Ideas)

Add password generator

Add search functionality

Convert to GUI using PyQt or Tkinter

    Encrypt key.key with master password (key wrapping)

🙋 Author

Made with ❤️ by Pavan Sai S.K.
