# 🔐 Authentication System – Secure CLI Authentication System

**Authentication System** is a Python-based, CLI-driven multi-user authentication system that offers secure one user login, encrypted credential storage, onboarding, and email-based password recovery. Built with modularity and security in mind, it demonstrates practical usage of encryption, environment-based configuration, and user workflows.

---

## 🚀 Features

- 🔒 One User login with encrypted credential storage
- 🧪 Secure password hashing and verification
- 📧 Password recovery via email (OTP support)
- 🧑‍💻 User onboarding with encrypted storage
- 🔐 Environment-based secret and config handling

---

## 📁 Project Structure

Authentication System/
│
├── main.py # CLI launcher
├── .env # Environment variables (SMTP, keys)
│
├── app/
│ └── main.py # Post-auth application logic
│
├── auth/
│ ├── login.py # Login workflow
│ ├── forgot_pass.py # Password recovery
│ ├── SecureLayer.py # Encryption/decryption logic
│ ├── SendEmail.py # Email handler
│ ├── config.py # Configuration manager
│ ├── app.enc # Encrypted user credentials
│ └── onboarding/
│ └── setup.py # New user onboarding


---

## 🔧 Setup Instructions

1. pip install -r requirements.txt

2. Configure your .env file:
    EMAIL=youremail@example.com
    PASSWORD=your_email_password
    

3. Run the App
    python main.py

## 🛠 Requirements
1. Python 3.10+

2. cryptography

3. python-dotenv

## 📬 Contact
    Author: Sai Vignesh
    Instagram: @itz_mr.voidwalker

## ⚠ Disclaimer
    This project is intended for educational purposes only. Do not use in production without code audits and security reviews.




