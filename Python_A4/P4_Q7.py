import re

text = """
Student: Rahul Patil
Email: rahul.patil@gmail.com
Mobile: 9876543210
Roll No: CS2026-015
Admission Date: 12/06/2026
Hashtags: #Python #StudentLife

Student: Priya Sharma
Email: priya.sharma@example.com
Mobile: 8765432109
Roll No: CS2026-021
Admission Date: 15/06/2026
Hashtags: #Python #College
"""

email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
mobile_pattern = r"\b[6-9]\d{9}\b"
date_pattern = r"\b\d{2}/\d{2}/\d{4}\b"
roll_pattern = r"\b[A-Z]{2}\d{4}-\d{3}\b"
hashtag_pattern = r"#[A-Za-z0-9_]+"

emails = re.findall(email_pattern, text)
mobiles = re.findall(mobile_pattern, text)
dates = re.findall(date_pattern, text)
roll_numbers = re.findall(roll_pattern, text)
hashtags = re.findall(hashtag_pattern, text)

print("Student Email Addresses:")
for item in emails:
    print(item)

print("\nMobile Numbers:")
for item in mobiles:
    print(item)

print("\nDates:")
for item in dates:
    print(item)

print("\nStudent Roll Numbers:")
for item in roll_numbers:
    print(item)

print("\nHashtags:")
for item in hashtags:
    print(item)
