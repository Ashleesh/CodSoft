import random, string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

print("Password Generator")

while True:
    try:
        length = int(input("Password length: "))
        if length > 0:
            break
        print("Enter a positive number.")
    except ValueError:
        print("Invalid input. Enter a number.")

password = generate_password(length)
print(f"\nGenerated password: {password}")
