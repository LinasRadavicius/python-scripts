from passlib.hash import sha512_crypt
import sys

# Colour definitions
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

# Step 1: Accept inputs for hashfile and wordlist
def get_inputs():
    if len(sys.argv) != 3:
        print(f"{RED}Usage:{RESET} python3 linax.py <hashfile> <wordlist>")
        sys.exit(1)
    hash_file = sys.argv[1]
    wordlist_file = sys.argv[2]
    return hash_file, wordlist_file

# Step 2: Load the hash from the hash file
def load_hash(hash_file):
    with open(hash_file, 'r') as file:
        hash_value = file.readline().strip()  # Assumed the hash is on the first line
    return hash_value

# Step 3: Check each password in the wordlist against the hash
def crack_password(hash_value, wordlist_file):
    with open(wordlist_file, 'r') as file:
        for line in file:
            password = line.strip()
            # Step 4: check for a match
            if sha512_crypt.verify(password, hash_value):
                print(f"{GREEN}[+]{RESET} Password found: {GREEN}{password}{RESET}")
                return  # Exit once a match is found
        print("{RED}[-]{RESET} Password not found in the wordlist.")

# Step 5: Bring it all together in the main function
def main():
    hash_file, wordlist_file = get_inputs()
    hash_value = load_hash(hash_file)
    crack_password(hash_value, wordlist_file)

if __name__ == "__main__":
    main()