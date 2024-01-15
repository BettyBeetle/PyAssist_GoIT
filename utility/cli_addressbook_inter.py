
from utility.name import Name
from utility.phone import Phone
from utility.record import Record
from utility.email import Email
from utility.birthday import Birthday
from utility.address import Address
from utility.addressbook import AddressBook
from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter
from pathlib import Path

# Erorr handler
ADDRESSBOOK = AddressBook() 

 # Function to display the menu
def show_menu(menu_options):
    max_option_length = max(len(item['option']) for item in menu_options) 
    print("Options:".ljust(max_option_length + 5), "Command:")
    print("-" * (max_option_length + 24))
    for _, item in enumerate(menu_options): ## tutaj index, option
        print(f"{item['option'].ljust(max_option_length + 5)} {item['command']}")
    print("-" * (max_option_length + 24))

# Function for receiving user commands in a command-line interface
def user_command_input(completer, menu_name=""):
    commands_completer = FuzzyWordCompleter(completer.words)
    user_input = prompt(f"{menu_name} >>> ", completer=commands_completer).strip()
    if user_input:
        return parse_command(user_input)
    return "", ""


def execute_commands(commands_dict: dict, cmd: str, addressbook, *arguments):

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
    cmd_func = commands_dict.get(cmd)
    return cmd_func(addressbook, *arguments)


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




# # Main menu function for the command-line interface
# def main_menu(commands_dict, menu_name=""):
#     while True:
#         cmd, arguments = user_command_input(commands_dict, menu_name)
#         print(execute_commands(commands_dict, cmd, arguments))




def cli_addressbook_menu(*args):        ### w starym projekcie def addressbook_commands(*args):
    menu_options = [
        {"option": "Add Record", "command": "add"}, ## to jest item
        {"option": "Show Specific Record", "command": "show <name>"},
        {"option": "Main Menu", "command": "up"}, 
        {"option": "Program exit", "command": "exit"},
        {"option": "Edit Record", "command": "edit"},
    ]

    show_menu(menu_options)
    completer = FuzzyWordCompleter(list(ADDRESSBOOK_MENU_COMMANDS.keys()))
    while True:
        cmd, arguments = user_command_input(completer, "address book")
        print(execute_commands(ADDRESSBOOK_MENU_COMMANDS, cmd, ADDRESSBOOK, *arguments))




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
            while True:
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
            while True:
                email = add_email()
                if email is not None:
                    emails.append(email)
                    
                    add_email_choice = input("Type Y (yes) if you want to add another email: ").strip().lower()
                    
                    if add_email_choice == "y" or add_email_choice == "yes":
                        continue
                    elif add_email_choice != "y" and add_email_choice != "yes":
                        break
                else:
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
     "phone": edit_phone, 
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























