## Regex_Code
import re

def show_contact_info(text):
    phones = re.findall("09[0-9]{9}", text)
    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z]+", text)
    
    return phones, emails


def delete_contact_info(text):
    text = re.sub("09[0-9]{9}", "***", text)
    text = re.sub(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z]+", "***", text)
    
    return text

text = """
        My phone number is 09131111111 and my email is son@email.com
        Also my father's phone number is 09902222222 and his email is father@email.ir
       """

phones, emails = show_contact_info(text)
print(f"Phones: {phones}")
print(f"Emails: {emails}")

changed_text = delete_contact_info(text)
print(changed_text)
