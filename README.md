
# 🔐 Secure Data Encryption System

Welcome to the **Secure Data Encryption System** – a secure and simple Streamlit-based web app for encrypting and decrypting your personal data using your own passkeys.

---

## 🚀 Features

- 📝 **Signup/Login** authentication system
- 🔐 **AES encryption** for securely storing sensitive data
- 🔑 **Passkey-based decryption** (your data is locked behind your own password)
- 🔄 **Multiple attempts protection** (auto-logout on 3 failed attempts)
- 📁 **Data saved locally** in JSON file (can be integrated with a database)
- 🎨 Clean, modern, and user-friendly UI built with **Streamlit**

---

## 🛠️ Tech Stack

- **Frontend/UI:** [Streamlit](https://streamlit.io/)
- **Backend:** Python
- **Encryption:** Fernet (from `cryptography.fernet`)
- **Password Hashing:** SHA-256
- **Storage:** JSON File (can be upgraded to DB later)

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/moizahmedshaikh/secure-data-encryption-app.git
cd secure-data-encryption-app
```

### 2. Create Virtual Environment (Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## 🔐 How It Works

1. **Signup/Login:** Secure login system using SHA-256 password hashing.
2. **Store Data:**
   - Input sensitive data and create a custom passkey.
   - The data is encrypted using AES (Fernet) and saved to a JSON file.
3. **Retrieve Data:**
   - View all stored encrypted entries.
   - Enter the correct passkey to decrypt them.
   - 3 incorrect passkey attempts = forced logout.

---

## 📁 Project Structure

```
secure-data-encryption-app/
│
├── app.py                  # Main Streamlit app
├── utils.py                # Helper functions for encryption, hashing, and data I/O
├── data.json               # Encrypted user data storage
├── users.json              # User login credentials
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🧠 Future Improvements

- 🌐 Add database (MongoDB / Firebase / SQLite) support
- 📲 Add mobile responsiveness
- 🔐 OTP or 2FA login system
- 🧪 Unit Testing and error logging

---

## 🤝 Contribution

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License

This project is licensed under the MIT License.

---

## 🧑‍💻 Author

**Moiz Ahmed**  
📍 Karachi, Pakistan  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/moiz-ahmed-6516b728a/)

---

## 🌟 Show Your Support

If you found this project helpful, give it a ⭐ on GitHub and share it!
