
from utility.name import Name
from utility.phone import Phone
from utility.record import Record
from utility.email import Email
from utility.birthday import Birthday
from utility.address import Address
from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter
from pathlib import Path
# Erorr handler
 

def add_name(addressbook): ## obiektem lub strukturą danych, która reprezentuje książkę adresową. Przekazując ją jako argument do funkcji, można manipulować danymi książki adresowej wewnątrz funkcji, a zmiany dokonane w tej funkcji będą miały wpływ na oryginalny obiekt książki adresowej poza funkcją
    while True:
        name = input("Type name or <<< if you want to cancel: ").strip().title()
        if name in addressbook.keys():
            print(f"Contact {name} already exists. Choose another name.")
            continue
        elif name == "<<<":
            return None
        return Name(name)

def add_phone():
    phone = input("Type phone or <<< if you want to cancel: ")
    if phone == "<<<":
        return None
    return Phone(phone)

def add_email():
    
    email = input("Type email or <<< if you want to cancel: ")
    if email == "<<<":
        return None
    return Email(email)

def add_birthday():
    birthday = input("Input the date of birth as day month year (e.g. 15-10-1985 or 15 10 1985) or <<< if you want to cancel: ")
    if birthday == "<<<":
        return None
    return Birthday(birthday)    

def add_address():
    street = input("street: ")
    city = input("city: ")
    zip_code = input("zip code: ")
    country = input("country: ")
    return Address(street, city, zip_code, country)


 # dict for create_record commands
CREATE_RECORD_COMMANDS = {
    "phones": add_phone,
    "emails": add_email,
    "birthday": add_birthday,
    "address": add_address,
}


def create_record(name): 
    phones = []
    emails = []
    birthday = None
    address = None
    while True:
        add_phone_choice = input(("Type Y (yes) if you want to add phone number: ").strip().lower())
        if add_phone_choice == "y" or add_phone_choice == "yes":
            phone = add_phone()
            if phone is not None:
                phones.append(phone)
                add_phone_choice = (input("Type Y (yes) if you want to add another phone number: ").strip().lower())
                if add_phone_choice == "y" or add_phone_choice == "yes":
                    continue
            break
        break

    while True:
        add_email_choice = input("Type Y (yes) if you want to add email: ").strip().lower()
        if add_email_choice == "y" or add_email_choice == "yes":
            email = add_email()
            if email is not None:
                emails.append(email)
                add_email_choice = (input("Type Y (yes) if you want to add another email: ").strip().upper())
                if add_email_choice == "y" or add_email_choice == "yes":
                    continue
            break
        break

    add_bday_choice = input("Type Y (yes) if you want to add birthday: ").strip().lower()
    if add_bday_choice == "y" or add_bday_choice == "yes":
        birthday= add_birthday()
    
    add_address_choice = input("Type Y (yes) if you want to add address: ").strip().lower()
    if add_address_choice == "y" or add_address_choice == "yes":
        address = add_address()
    
    return Record(name, phones, emails, birthday, address)

def add_record(addressbook, *args):
    if len(args) == 0:
        name = add_name(addressbook)      
    else:
        name = " ".join(args).strip().title()
        if name in addressbook.keys():
            print(f"Contact {name} already exists. Choose another name.")
            name = add_name(addressbook) 
        else:
            name = Name(name)
    if name is not None:
        record = create_record(name)
        addressbook.add_record(record)
        return f"A record: {record} added to your address book."
    return "Operation cancelled"


# Edit existing name
def edit_name(addressbook, record):
    print(f"Type new name for contact {record.name}")
    new_name = add_name(addressbook)
    if new_name:
        addressbook.add_record(Record(new_name, record.phones, record.emails, record.birthday, record.address))
        old_record = addressbook.pop(record.name.value)
        return f"Name changed from {old_record.name} to {new_name}"
    return "Operation canceled."

def edit_phone(addressbook, record):
    print(f"Type new name for contact {record.name}")
    new_name = add_name(addressbook)
    if new_name:
        addressbook.add_record(Record(new_name, record.phones, record.emails, record.birthday, record.address))
        old_record = addressbook.pop(record.name.value)
        return f"Name changed from {old_record.name} to {new_name}"
    return "Operation canceled."




# dict for menu edit handler
EDIT_COMMANDS = {
    "name": edit_name, 
    # "phone": edit_phone, 
    # "email": edit_email,
    # "address": edit_address,
    # "birthday": edit_birthday,
    }


def edit_record(addresbook, record):
    commands_completer = FuzzyWordCompleter(ADDRESSBOOK_MENU_COMMANDS.keys())
    pass

def export_to_csv(addressbook, filename):
    while True:
        if not filename:
            filename = input("Type the filename to export to (e.g., sample.csv) or <<< to cancel: ").strip()
        elif filename == "<<<" or filename == "":
            return "Export cancelled."
        
        program_dir = Path(__file__).parent.parent
        full_path = program_dir.joinpath("data/" + filename)
    
        addressbook.export_to_csv(full_path)
        return f"Data exported successfully to {full_path}."
    return "Export cancelled."









def save_addressbook(addressbook, filename):
    addressbook.save_addressbook(filename)
    return "Addressbook saved"

def load_addressbook_addressbook(addresbook, filename):
    addressbook = addressbook.load_addressbook(filename)
    return f" Addressbook loaded form file(filename)"



# dict for addressbook menu
ADDRESSBOOK_MENU_COMMANDS = {
        "add": add_record,
        #"edit": edit_record,
        # "show": show,
        # "delete": del_record,
        "export": export_to_csv,
        # "import": import_from_csv,
        # "birthday": show_upcoming_birthday,
        # "search": search,
        # "save": save_addressbook,
        # "up": "up",
        # "exit": exit_program,
        "help": help,
    }

# dict for addressbook menu
ADDRESSBOOK_COMMANDS = {
    # "exit": cli_pyassist_exit,
    "add": add_record, #lambda *args: add_record(ADDRESSBOOK, *args),
     #"edit": edit_record, #lambda *args: edit_record(ADDRESSBOOK, *args),
    # "show": show, #lambda *args: show(ADDRESSBOOK, *args),
    # "delete": del_record, #lambda *args: del_record(ADDRESSBOOK, *args),
    "export": export_to_csv, #lambda *args: export_to_csv(ADDRESSBOOK, *args),
    # "import": import_from_csv, #lambda *args: import_from_csv(ADDRESSBOOK, *args),
    # "birthday": show_upcoming_birthday, #lambda *args: show_upcoming_birthday(ADDRESSBOOK, *args),
    # "search": search, #lambda *args: search(ADDRESSBOOK, *args),
    # "up": pyassist_main_menu,
    # "help": addressbook_menu,
}

def execute_commands(commands_dict: dict, cmd: str, argument):

    """Function to execute user commands

    Args:
        menu_commands (dict): dict for menu-specific commands
        cmd (str): user command
        data_to_use: dict (for addressbook) or list (for notes) or None (for rest) to use in calling functions
        arguments (tuple): arguments from user input

    Returns:
        func: function with data_ti_use and arguments
    """

    if cmd not in commands_dict:
        return f"Command {cmd} is not recognized"
    cmd_func = commands_dict[cmd]
    return cmd_func(argument)


# Function that parses user input commands
def parse_command(user_input: str) -> (str, str):
    
    """
    "Process user input and return relevant information.

    Args:
        user_input (str): user input command
    
    Returns:
        str: command
        tuple: arguments
    """

    tokens = user_input.split()
    command = tokens[0].lower()
    argument = "".join(tokens[1:])
    return command, argument



# Function for receiving user commands in a command-line interface
def user_command_input(ADDRESSBOOK_MENU_COMMANDS,menu_name=""):
    commands_completer = FuzzyWordCompleter(ADDRESSBOOK_MENU_COMMANDS.keys())
    user_input = prompt(f"{menu_name} >>> ", completer = commands_completer).strip()
    if user_input:
        return parse_command(user_input)
    return "", ""


def cli_addressbook_menu():     ## obsługa interfejsu wiersza poleceń (CLI) 
    while True:
        cmd, argument = user_command_input()
        if cmd == "up":
            return "back to previous (main) menu"
        print(execute_commands(ADDRESSBOOK_MENU_COMMANDS, cmd, argument))



# def main():
#     # Inicjalizacja obiektu AddressBook
#     ADDRESSBOOK = AddressBook()

#     # Wczytaj dane z pliku, jeśli istnieje
#     ADDRESSBOOK_DATA_PATH = "ścieżka/do/twojej/książki/adresowej.dat"
#     ADDRESSBOOK.load_addressbook(ADDRESSBOOK_DATA_PATH)

#     # # Przekaż ADDRESSBOOK jako argument do funkcji addressbook_interaction
#     addressbook_interaction(ADDRESSBOOK)

    # # Zapisz książkę adresową po zakończeniu działania programu


















####################### Skrypt testowy
# def main():
#     address_book = {}

#     while True:
#         name = add_name(address_book)
#         if name is None:
#             break

#         record = Record(name)
#         create_record(record)

#         address_book[name.value] = record

#     # Wyświetl zawartość książki adresowej
#     print("\nAddress Book:")
#     for contact_name, contact_record in address_book.items():
#         print(f"{contact_name}: {', '.join(phone.value for phone in contact_record.phones)}")

# if __name__ == "__main__":
#     main()

