# 🔓 Hash Cracker – MD5 Password Cracking Tool

A lightweight Python tool that cracks **MD5 password hashes** using both a custom wordlist and **user-generated keywords**. Great for learning about password hashing, brute-force concepts, and ethical hacking.

---

## ⚙️ Features

- Cracks **MD5 hashes**
- Takes **user keywords** and generates variations automatically
- Uses a **custom wordlist**
- Combines user input + wordlist to create a stronger attack set
- Simple and customizable

---

## 📦 Requirements:

- Python 3.x

No external packages are needed — just standard Python.

---
## 🚀 How to Use:

### 1. Clone the repository

git clone https://github.com/kiriosx1/hash-cracker.git
cd hash-cracker
## 2. Add your wordlist (or use the provided one)
Place your wordlist.txt in the same folder.

You can use this one or create your own with more entries.

## 3. Run the script:
python hash_cracker.py

## 4. Input Prompts:
🔐 Enter the MD5 hash you want to crack

📝 Enter the path to your wordlist (e.g., wordlist.txt)

💬 Enter keywords (separated by commas): names, years, etc.

# Example:

Enter the MD5 hash to crack: 5f4dcc3b5aa765d61d8327deb882cf99
Enter the path to your wordlist: wordlist.txt
Enter keywords (separated by commas): kyros, admin, 1234
Output:
✅ Password found: password

---
# 🧠 Example Use Cases:
Educational pentesting demos

CTFs (Capture the Flag challenges)

Testing password strength

Brute-force practice (MD5 only)

---
# 🛠 Sample Output:

[+] Trying 350 password combinations...

[✔] Password found: kyros123

---

# 📄 Legal Disclaimer
⚠️ This tool is intended for educational and ethical testing purposes only.
Do not use it against systems or data you do not own or have permission to test.
The author is not responsible for any misuse or damage caused by this script.

---

# 📌 More Features Coming Soon! (maybe)
✅ SHA1 / SHA256 cracking

✅ Export results to file

✅ GUI version using Tkinter

✅ Support for salted hashes

✅ Performance stats & logging


# ✉️ Contact
📧 Business Email: kyros.businesss@gmail.com

Feel free to share ideas or ask for help!
---

