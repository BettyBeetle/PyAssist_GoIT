from datetime import datetime
from utility.name import Name
from utility.phone import Phone
from utility.email import Email
from utility.address import Address

class Record:
    ''' 
    Record class represents a single address book record consisting of name, phone list, email list, address and birthday.
    '''

    def __init__ (self, name: Name, emails = [], phones = [], birthday = None, address = None):
        self.name = name # wartość przekazana jako name będzie przypisana do atrybutu _name w instancji klasy.
        self.phones = phones
        self.emails = emails
        self.birthday = birthday
        self.address = address


    # Overridden method __repr__
    def __repr__(self) -> str:
        record_view = f"Name: {self.name}\n"
        if self.phones:
            record_view += "Phones:"
            for phone in self.phones:
                record_view += f" {phone}\n"
        if self.emails:
            record_view += "Emails:"
            for email in self.emails:
                record_view += f" {email}\n"
        if self.birthday:
            record_view += f"Birthday:\n    {self.birthday}\n"    #{self.days_to_birthday()}\n"
        if self.address:
            record_view += f"Address:\n    Street: {self.address.street}\n"
            record_view += f"    City: {self.address.city}\n"
            record_view += f"    Zip Code: {self.address.zip_code}\n"
            record_view += f"    Country: {self.address.country}\n"
        record_view += "----------------------------------\n"
        return record_view
   


    # Add phone to phones list
    def add_phone(self, phone: Phone):  ## setter- przyjmuje obiekt phone jako argument i dodaje go do atrybutu _phones. Umożliwia dodawanie telefonów do listy przechowywanej w atrybucie _phones.
        self.phones.append(phone)

    # Remove phone from phone list
    def remove_phone(self, phone: Phone):
        self.phones.remove(phone)
    
    # Change phone - add new one and remove old one
    def change_phone(self, old_phone, new_phone):   # może zrobić jakiegoś dekoratora
        if old_phone in self.phones:                # znajduje indeks old_phone w liście self.phones. Funkcja index() zwraca pierwsze wystąpienie wartości w liście, której indeks chcemy znaleźć. Jeśli old_phone nie istnieje w liście, zostanie zgłoszony błąd ValueError.
            index = self.phones.index(old_phone)
            self.phones[index] = new_phone
            print(f"Phone number {old_phone} changed to {new_phone}")
        else:
            print(f"Phone number {old_phone} not found in the list of phones.")

    # Add email to emails list
    def add_email(self, email: Email):
        self.emails.append(email)

    # Remove email from emails list
    def remove_email(self, email: Email):
        self.emails.remove(email)

    # Change email - add new one and remove old one
    def change_email(self, old_email, new_email):   # może zrobić jakiegoś dekoratora
        if old_email in self.emails:                # znajduje indeks old_phone w liście self.phones. Funkcja index() zwraca pierwsze wystąpienie wartości w liście, której indeks chcemy znaleźć. Jeśli old_phone nie istnieje w liście, zostanie zgłoszony błąd ValueError.
            index = self.emails.index(old_email)
            self.emails[index] = new_email
            print(f"Email address {old_email} changed to {new_email}")
        else:
            print(f"Email address {old_email} not found in the list of emails.")
    
    ############# SPRAWDZIĆ################
    # Add address to address list
    def add_address(self, address: Address):
        self.address = address

    # Remove address from address list    
    def remove_address(self):
        self.address = None

    # Change address - add new one and remove old one
    def change_address(self, new_address: Address):   
        self.address = new_address
        print(f"Address changed to {new_address}")

        
    # Return amount of days to the next birthday
    def days_to_birthday(self):     # UWAGA!!!   sprawdzenie działało gdy nie było value w month i day
        current_date = datetime.now().date()
        this_year_bday = datetime(
            year = current_date.year,
            month = self.birthday.value.month,
            day = self.birthday.value.day,
        ).date()
        difference = this_year_bday - current_date
        if difference.days == 0:
            return f"{self.name}'s birthday is today!"
        if difference.days > 0: # if bday is in the current year
            return f"day(s) to next birthday: {difference.days}"





