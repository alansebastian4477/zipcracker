import zipfile
import itertools
import argparse

# Function to attempt to crack the zip file
def crack_zip(zip_file, password):
    try:
        with zipfile.ZipFile(zip_file) as zf:
            zf.extractall(pwd=password.encode())
            print(f"Password found: {password}")
            return True
    except:
        return False

# Dictionary Attack
def dictionary_attack(zip_file, dictionary_file):
    with open(dictionary_file, 'r') as file:
        for line in file:
            password = line.strip()
            if crack_zip(zip_file, password):
                break

# Brute Force Attack
def brute_force_attack(zip_file, max_length):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for length in range(1, max_length + 1):
        for pwd_tuple in itertools.product(chars, repeat=length):
            password = ''.join(pwd_tuple)
            if crack_zip(zip_file, password):
                return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zip Cracker")
    parser.add_argument("zipfile", help=""C:\Users\alans\Downloads\demo.zip"")
    parser.add_argument("--dict", help="Path to dictionary file", default=None)
    parser.add_argument("--bruteforce", help="Max length for brute force", type=int, default=None)
    args = parser.parse_args()

    if args.dict:
        dictionary_attack(args.zipfile, args.dict)
    elif args.bruteforce:
        brute_force_attack(args.zipfile, args.bruteforce)
    else:
        print("Specify either a dictionary or brute force method.")
