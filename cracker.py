import itertools
import threading

password = input("Enter the password to crack: ")
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
matches = []

def brute(StartingPoint, End):
    for length in range(StartingPoint, End + 1):
        for guess in itertools.product(characters, repeat=length):
            attempt = "".join(guess)
            print(attempt)
            if attempt == password:
                matches.append(attempt)
                return


midpoint = len(password) // 2 
midpoint = midpoint + 1
print(midpoint)

t1 = threading.Thread(target=brute, args=(1, midpoint))
t1.start()
t1.join()

t2 = threading.Thread(target=brute, args=(midpoint + 1, len(password)))
t2.start()
t2.join()





if matches:
    print(f"Password cracked: {matches[0]}")
else:
    print("Password not found")