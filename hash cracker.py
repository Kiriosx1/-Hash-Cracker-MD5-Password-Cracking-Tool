import hashlib
from itertools import product

def generate_variations(keywords):
    common_suffixes = ['123', '1234', '2024', '2025', '!', '@', '#', '1!', '01', '0']
    variations = set()

    for word in keywords:
        word = word.lower()
        variations.add(word)
        for suffix in common_suffixes:
            variations.add(word + suffix)
            variations.add(word.capitalize() + suffix)
            variations.add(word.upper() + suffix)
        variations.add(word.capitalize())
        variations.add(word.upper())
    return list(variations)

def load_wordlist(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("[!] Wordlist file not found.")
        return []

def crack_hash(target_hash, password_list):
    for password in password_list:
        hashed = hashlib.md5(password.encode()).hexdigest()
        if hashed == target_hash:
            print(f"[✔] Password found: {password}")
            return
    print("[✘] Password not found in the combined list.")

if __name__ == "__main__":
    target_hash = input("Enter the MD5 hash to crack: ").strip()
    wordlist_path = input("Enter the path to your wordlist: ").strip()
    user_input = input("Enter keywords (separated by commas): ").strip()

    keywords = [word.strip() for word in user_input.split(",") if word.strip()]
    generated_variants = generate_variations(keywords)
    wordlist = load_wordlist(wordlist_path)

    combined_list = list(set(generated_variants + wordlist))  # Remove duplicates
    print(f"\n[+] Trying {len(combined_list)} password combinations...\n")
    crack_hash(target_hash, combined_list)