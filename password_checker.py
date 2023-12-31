import sys
import time

def check_password(password_name, wordlist_name):
    try:
        start_time = time.time()

        with open(wordlist_name, 'r', encoding='latin-1') as wordlist_file:
            for line in wordlist_file:
                if password_name == line.strip():
                    print(f"Password '{password_name}' found in '{wordlist_name}'.")
                    break
            else:
                print(f"Password '{password_name}' not found in '{wordlist_name}'.")

        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"Time taken: {elapsed_time:.4f} seconds")
    
    except FileNotFoundError:
        print(f"Error: Wordlist '{wordlist_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: password_checker.py [password] [wordlist_file]")
    else:
        password_name, wordlist_file = sys.argv[1], sys.argv[2]
        check_password(password_name, wordlist_file)
