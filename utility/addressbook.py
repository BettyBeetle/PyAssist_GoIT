from collections import UserDict

import pickle
import csv
from pathlib import Path

from utility.record import Record
from utility.name import Name
from utility.phone import Phone
from utility.email import Email
from utility.birthday import Birthday
from utility.address import Address


class AddressBook(UserDict):
    # def __init__(self, value):
    #     self.value = value
    '''
    The AddressBook class extends the UserDict class.
    The class checks whether the elements added to the dictionary are valid (keys and values based on the Record class).

    Args:
        UserDict (class): parent class

    '''


    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def save_addressbook(self, filename):
        with open(filename, "wb") as fh:
            pickle.dump(self, fh)

    def load_addressbook(self, filename):
        if Path.exists(Path(filename)):         # if Path(filename).exists():  
            with open(filename, "rb") as fh:    
                return pickle.load(fh)          
        return self                             

   

    def search(self):
        pass

    def export_to_csv(self, filename):
        if len(self.data) > 0:
            with open(filename, "w", newline='') as fh:
                field_names = [             ## # Zdefiniowanie nazw pól nagłówka CSV
                    "name",
                    "phones",
                    "emails",
                    "birthday",
                    "street",
                    "city",
                    "zip_code",
                    "country",
                ]
                writer = csv.DictWriter(fh, fieldnames=field_names)     ## Utworzenie obiektu do zapisu danych CSV z użyciem zdefiniowanych pól
                writer.writeheader()                                    ## Zapisanie nagłówka CSV
                for record in self.data.values():
                    record_dict = {"name": record.name.value}
                    phones = []
                    for phone in record.phones:
                        phones.append(phone.value)
                    record_dict["phones"] = " | ".join(phones)

                    emails = []
                    for email in record.emails:
                        email.append(email.value)
                    record_dict["emails"] = " | ".join(emails)

                if record.birthday is not None:
                    record_dict["birthday"] = record.birthday.value.strftime("%d-%m-%Y")    

                if record.address:
                    record_dict["street"] = record.address.street.value
                    record_dict["city"] = record.address.city.value
                    record_dict["zip_code"] = record.address.zip_code.value
                    record_dict["country"] = record.address.country.value
                    writer.writerow(record_dict)


    def import_from_csv(self):
        pass

