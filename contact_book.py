class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        """Add a new contact"""
        self.contacts[name] = phone
        print(f"✅ Contact '{name}' added successfully.")

    def delete_contact(self, name):
        """Delete an existing contact"""
        if name in self.contacts:
            del self.contacts[name]
            print(f"🗑️ Contact '{name}' deleted.")
        else:
            print("⚠️ Contact not found.")

    def search_contact(self, name):
        """Search for a contact"""
        if name in self.contacts:
            print(f"📞 {name}: {self.contacts[name]}")
        else:
            print("⚠️ Contact not found.")

    def display_contacts(self):
        """Display all contacts"""
        if not self.contacts:
            print("📭 Contact book is empty.")
        else:
            print("\n---- 📖 Contact Book ----")
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")


# ---------- Example Usage ----------
if __name__ == "__main__":
    book = ContactBook()
    book.add_contact("Ramesh", "9876543210")
    book.add_contact("Suresh", "9123456780")
    book.display_contacts()
    book.search_contact("Ramesh")
    book.delete_contact("Suresh")
    book.display_contacts()
