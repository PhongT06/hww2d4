#1
import re

text = "Contact emails are: john.doe@example.com and jane.doe@example.com."
# emails = re.findall(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+.[A-Z]{2,}", text)
# print(emails)

emails = [email for email in re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", text)]
print(emails)




#2
import re


text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
# emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
# print(emails)

emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com)[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", text)
print(emails)





