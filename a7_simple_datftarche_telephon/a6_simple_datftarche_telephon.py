from unittest import result

import json
class ContactManager:
    def __init__(self):
        self.contact_list = []

    def add(self, name, number):
        new_contact = {
            "name": name,
            "number": number
        }
        self.contact_list.append(new_contact)

    def search(self, name):
        # کد برای جستجوی یک مخاطب
        result=[]
        for item in self.contact_list:
            if name.lower() in item["name"].lower():
                result.append(item)
        print(f"***Your search result is: {result}")

    def backup(self):
        # کد برای پشتیبان‌گیری از لیست مخاطبین
        with open("./contacts.json", "w") as f:
            f.write(json.dumps(self.contact_list))

    def print(self):
        # کد برای چاپ لیست مخاطبین
        print(f"*your contact list is: {self.contact_list}")

myContact = ContactManager()
myContact.add("John" , 4545)
myContact.print()
myContact.add("Mitra" , 1515)
myContact.add("Mina", 2222)
myContact.print()
myContact.search("Mi")
myContact.backup()
