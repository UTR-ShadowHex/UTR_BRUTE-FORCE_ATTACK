🚀 Brute-Force Attack Tool

A Multi-Threaded Login Cracker for Termux & Linux.

---

╔═════════════════════════════════════════════════════════╗
║                  BRUTE-FORCE ATTACK TOOL                          ║
║═════════════════════════════════════════════════════════║
║     TOOL OWNER    ║   ARSHAN AHMED ERFAN                          ║
║═════════════════════════════════════════════════════════║
║       GITHUB      ║   UTR-ShadowHex                               ║
╚═════════════════════════════════════════════════════════╝


---

⚠️ Legal Disclaimer

> This tool is strictly for educational, research & authorized penetration testing only.
Unauthorized use on systems you do not own is a criminal offense.
You are responsible for your own actions.




---

⭐ Features

✔ Multi-threaded brute-forcing

✔ Supports multiple wordlists

✔ Auto logs successful credentials

✔ Thread-safe output

✔ Custom speed delay

✔ Works on Termux / Linux / Windows

✔ Beginner-friendly CLI UI


---

🔧 Installation Guide (Termux / Linux)

1️⃣ Update System
```
pkg update && pkg upgrade -y
```
2️⃣ Install Python
```
pkg install python -y
```
3️⃣ Required Python Module
```
pip install requests
```
4️⃣ Clone the Repository
```
git clone https://github.com/UTR-ShadowHex/UTR_BRUTE-FORCE_ATTACK.git
```
5️⃣ Add Wordlists

Use:

rockyou.txt

custom.txt


If missing, create your own.


---

▶️ Run The Tool
```
python tool.py
```

---

📌 Example Usage

👉 Enter login page URL: http://example.com/login.php
👉 Enter username: admin

Output:

[-] Tried: 123456
[-] Tried: admin123
[✅] Password found: secretpass2024


---

🧠 How It Works (Simplified Flow)

Load Wordlists → Queue Passwords → Spawn Threads → Try Login → Check Response → Save Log

---

⚙️ Recommended Packages for Termux

Purpose	Package	Command

Zip extract	unzip	
```
pkg install unzip
```
Git 
```
pkg install git
```
Storage access
```
termux-setup-storage
```
Large wordlist download	wget	
```
pkg install wget
```


---

🐞 Troubleshooting

❌ "Wordlist not found"

Add your wordlist in tool folder:

rockyou.txt (install from github)
or create your own password file

```
nano custom.txt
```


❌ "SSL error"
```
pip install certifi
```
❌ Slow cracking speed

Increase num_threads inside script

Reduce delay value



---

🧑‍💻 Maintainer

ARSHAN AHMED ERFAN
GitHub: https://github.com/UTR-ShadowHex


---

📜 License

Licensed under the MIT License — free to modify & distribute.

