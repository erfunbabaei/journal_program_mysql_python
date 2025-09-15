from database import create_table, add_entry, get_entries

menu: str = """please select one of the following options:
1) Add new entry for today
2) View all entries
3) Exit.

Your selection: """

welcome: str = "welcome to the programming diary!"

def prompt_new_entry():
    entry_content: str = input("What have you learned today?: ")
    entry_date: str = input("Enter the date: ")
    add_entry(entry_content, entry_date)

def view_entries(entries):
    for entry in entries:
        print(f"{entry['publication_date']}\n{entry['content']}\n\n")

print(welcome)

create_table()

while (userInput := input(menu)) != "3":
    if userInput == "1":
        prompt_new_entry()

    elif userInput == "2":
        view_entries(get_entries())

    else:
        print("invalid option, please try again!")
