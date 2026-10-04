import re

text = """
For any queries, contact abc@gmail.com or student123@example.com.
You can also email support.team@college.edu.
"""

pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

emails = re.findall(pattern, text)

print("Email addresses:")
for email in emails:
    print(email)
