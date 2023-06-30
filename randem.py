import random
import string

def generate_random_email(domain):
    username_length = random.randint(5, 10)  # Random username length between 5 and 10 characters
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    email = f"{username}@{domain}"
    return email

def generate_multiple_emails(domain, count):
    emails = []
    for _ in range(count):
        email = generate_random_email(domain)
        emails.append(email)
    return emails

# Generate 5 random email addresses with the domain 'example.com'
emails = generate_multiple_emails('gmail.com', 10)
print("Random Email Addresses:")
for email in emails:
    print(email)
