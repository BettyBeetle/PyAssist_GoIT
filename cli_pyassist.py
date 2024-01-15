import pyfiglet
import difflib
from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter
from pathlib import Path
from utility.cli_addressbook_inter import cli_addressbook_menu
from utility.cli_addressbook_inter import show_menu, add_record

from utility.addressbook import AddressBook  
import sys
import cowsay

def addressbook_interaction(cli_addressbook_inter):
    return cli_addressbook_inter.cli_addressbook_menu()

program_dir = Path(__file__).parent
ADDRESSBOOK_DATA_PATH = program_dir.joinpath("data/addresbook.dat") 
ADDRESSBOOK = AddressBook().load_addressbook(ADDRESSBOOK_DATA_PATH)



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
        print(execute_commands(MAIN_COMMANDS, cmd, arguments))


def cli_pyassist_exit(*args):
    global ADDRESSBOOK
    program_path = Path(__file__).parent    # paths to files with data
    addressbook_path = program_path.joinpath("data/addressbook.dat")
    ADDRESSBOOK = AddressBook().load_addressbook(addressbook_path)
    ADDRESSBOOK.save_addressbook(addressbook_path)
    cowsay.daemon("Your data has been saved.\nGood bye!") 
    sys.exit()


MAIN_COMMANDS = {
    "exit": cli_pyassist_exit,
    "addressbook": cli_addressbook_menu,
    # "sort": sort_files_command,
    # "notes": notes_command,
}


    
COMMANDS = {
    "addressbook": addressbook_interaction
    # "notes": notes_interaction,
    # "sort": sort_init,
    # "exit": cli_pyassist_exit,
    # "help": help,
}




# receiving a command from a user
def user_command_input(completer, menu_name):
    commands_completer = FuzzyWordCompleter(COMMANDS.keys())
    user_input = prompt(f"main menu >>> ", completer=completer).strip()
    if user_input:
        return parse_command(user_input)
    return "", ""

def execute_commands(COMMANDS: dict, cmd: str, argument):
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
    return cmd(*argument)

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







###  ==================================================================================================
def main():
    print(pyfiglet.figlet_format("PyAssist", font="slant"))
    
    pyassist_main_menu()
   
if __name__ == "__main__":
    main()
## ==================================================================================================