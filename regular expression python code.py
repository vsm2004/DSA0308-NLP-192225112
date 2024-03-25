import re

def main():
    text = "Hello, my email is v.s.manu2004@gmail.com and my phone number is 8341801538."
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    emails = re.findall(email_pattern, text)
    print("Email addresses found:", emails)
    phones = re.findall(phone_pattern, text)
    print("Phone numbers found:", phones)
if __name__ == "__main__":
    main()
