import re

text = """
Welcome to our college website: https://www.example.com.
For details, email admin@college.edu or call 9876543210.
The examination is on 15/10/2026 and the fee is 2500.
Follow us on social media using #CollegeLife and #Python.
"""

# Email addresses
email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

# Phone numbers
phone_pattern = r"\b[6-9]\d{9}\b"

# URLs
url_pattern = r"https?://[A-Za-z0-9.-]+(?:/[A-Za-z0-9_./?=&%-]*)?"

# Dates
date_pattern = r"\b\d{2}/\d{2}/\d{4}\b"

# Numbers
number_pattern = r"\b\d+\b"

# Hashtags
hashtag_pattern = r"#[A-Za-z0-9_]+"

emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)
urls = re.findall(url_pattern, text)
dates = re.findall(date_pattern, text)
numbers = re.findall(number_pattern, text)
hashtags = re.findall(hashtag_pattern, text)

print("Email addresses:")
for item in emails:
    print(item)

print("\nPhone numbers:")
for item in phones:
    print(item)

print("\nURLs:")
for item in urls:
    print(item)

print("\nDates:")
for item in dates:
    print(item)

print("\nNumbers:")
for item in numbers:
    print(item)

print("\nHashtags:")
for item in hashtags:
    print(item)
