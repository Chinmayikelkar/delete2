import re

text = """
Visit https://www.google.com for searching.
Our college website is https://www.fergusson.edu.
You can also visit http://example.com/page for more information.
"""

pattern = r"https?://[A-Za-z0-9.-]+(?:/[A-Za-z0-9_./?=&%-]*)?"

urls = re.findall(pattern, text)

print("URLs found:")
for url in urls:
    print(url)
