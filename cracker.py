import itertools

password = input("Enter the password to crack: ")
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

for guess in itertools.product(characters, repeat=5):
    attempt = "".join(guess)
    print(f"Trying: {attempt}")
    if attempt == password:
        print(f"Password cracked: {attempt}")
        break
