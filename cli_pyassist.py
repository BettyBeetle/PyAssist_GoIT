import pyfiglet
import difflib
from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter
from pathlib import Path
from utility.cli_addressbook_inter import add_record
from utility.addressbook import AddressBook  
import sys
import cowsay

def addressbook_interaction(cli_addressbook_inter):
    return cli_addressbook_inter.cli_addressbook_menu()

program_dir = Path(__file__).parent
ADDRESSBOOK_DATA_PATH = program_dir.joinpath("data/addresbook.dat") 
ADDRESSBOOK = AddressBook().load_addressbook(ADDRESSBOOK_DATA_PATH)








def cli_pyassist_exit(*args):
    program_path = Path(__file__).parent    # paths to files with data
    addressbook_path = program_path.joinpath("data/addressbook.dat")
    ADDRESSBOOK = AddressBook().load_addressbook(addressbook_path)
    ADDRESSBOOK.save_addressbook(addressbook_path)
    cowsay.daemon("Your data has been saved.\nGood bye!") 
    sys.exit()

# Function to display the menu
def show_menu(menu_options):
    max_option_length = max(len(item['option']) for item in menu_options) 
    print("Options:".ljust(max_option_length + 5), "Command:")
    print("-" * (max_option_length + 24))
    for _, item in enumerate(menu_options): ## tutaj index, option
        print(f"{item['option'].ljust(max_option_length + 5)} {item['command']}")
    print("-" * (max_option_length + 24))


# Function to display PyAssist main menu options
def pyassist_main_menu(*args):      ### Pierwsze menu pokazujące co może PyAssist
    menu_options = [
        {"option": "Your's AddressBook", "command": "addressbook"},
        {"option": "Your's notes", "command": "notes"},
        {"option": "Your's file sorter", "command": "sort <folder>"}, 
        {"option": "Close Your's PyAssist", "command": "exit"},
        {"option": "Back to this Options", "command": "help"},
    ]
    show_menu(menu_options)
    completer = FuzzyWordCompleter(MAIN_COMMANDS.keys())
    while True:
        cmd, arguments = user_command_input(completer, "main menu")
        print(execute_commands(MAIN_COMMANDS, cmd, None, arguments))





def addressbook_menu(*args):        ### w starym projekcie def addressbook_commands(*args):
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
        print(execute_commands(ADDRESSBOOK_MENU_COMMANDS, cmd, ADDRESSBOOK, arguments))


MAIN_COMMANDS = {
    "exit": cli_pyassist_exit,
    "addressbook": addressbook_menu,
    # "sort": sort_files_command,
    # "notes": notes_command,
}

# dict for addressbook menu
ADDRESSBOOK_MENU_COMMANDS = {
    "exit": cli_pyassist_exit,
    "add": add_record, #lambda *args: add_record(ADDRESSBOOK, *args),
    # "edit": edit_record, #lambda *args: edit_record(ADDRESSBOOK, *args),
    # "show": show, #lambda *args: show(ADDRESSBOOK, *args),
    # "delete": del_record, #lambda *args: del_record(ADDRESSBOOK, *args),
    # "export": export_to_csv, #lambda *args: export_to_csv(ADDRESSBOOK, *args),
    # "import": import_from_csv, #lambda *args: import_from_csv(ADDRESSBOOK, *args),
    # "birthday": show_upcoming_birthday, #lambda *args: show_upcoming_birthday(ADDRESSBOOK, *args),
    # "search": search, #lambda *args: search(ADDRESSBOOK, *args),
    "up": pyassist_main_menu,
    # "help": addressbook_menu,
}



# def help(*args):
#     for command['help'] in COMMANDS.items():
#         return pyassist_main_menu
    
COMMANDS = {
    "addressbook": addressbook_interaction
    # "notes": notes_interaction,
    # "sort": sort_init,
    # "exit": cli_pyassist_exit,
    # "help": help,
}







def parse_command(user_input: str) -> (str, str):
        """
        Parse user input command

        Args:
            user_input (str): user input command

        Returns:
            str: command
            str: argument
        """
        tokens = user_input.split()
        command = tokens[0].lower()
        arguments = " ".join(tokens[1:])
        return command, tuple(arguments)

# receiving a command from a user
def user_command_input(completer, menu_name):
    commands_completer = FuzzyWordCompleter(COMMANDS.keys())
    user_input = prompt(f"main menu >>> ", completer=completer).strip()
    if user_input:
        return parse_command(user_input)
    return "", ""

def execute_commands(COMMANDS: dict, cmd: str, data_to_use, argument: tuple):
    """Function to execute user commands

    Args:
        cmd (str): user command
        argument (str): argument from user input

    Returns:
        func: function with data_ti_use and arguments
    """
    if cmd not in COMMANDS:
        matches = difflib.get_close_matches(cmd, COMMANDS)
        info = f"\nmaybe you meant: {' or '.join(matches)}" if matches else ""
        return f"Command {cmd} is not recognized" + info
    cmd = COMMANDS[cmd]
    return cmd(data_to_use, *argument)




###  ==================================================================================================
def main():
    print(pyfiglet.figlet_format("PyAssist", font="slant"))
    
    pyassist_main_menu()
   
if __name__ == "__main__":
    main()
## ==================================================================================================