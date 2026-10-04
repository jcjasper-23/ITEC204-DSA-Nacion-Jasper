# ITEC 204 - Data Structures and Algorithms
# Laboratory Activity 1: IT Automation Incident Ticket Manager
# Linear data structure used: Python List (each ticket is stored as a dictionary)

# The list that stores all active incident tickets
tickets = []

# The 10 sample incident tickets from the lab sheet
SAMPLE_TICKETS = [
    ("INC1392939", "BOT-Inventory", "Failed to generate the daily report"),
    ("INC1392940", "BOT-Email", "Failed to send the scheduled notification"),
    ("INC1392941", "BOT-DataSync", "Encountered an error during data transfer"),
    ("INC1392942", "BOT-Invoice", "Failed to process an invoice"),
    ("INC1392943", "BOT-Report", "Failed to generate the weekly report"),
    ("INC1392944", "BOT-FileTransfer", "Failed to upload the required file"),
    ("INC1392945", "BOT-DataEntry", "Encountered an error while entering records"),
    ("INC1392946", "BOT-Backup", "Failed to complete the scheduled backup"),
    ("INC1392947", "BOT-Validation", "Failed to validate the submitted records"),
    ("INC1392948", "BOT-Notification", "Failed to send the system alert"),
]


def find_index(incident_id):
    """Linear search: returns the position of the ticket in the list, or -1 if not found."""
    for i in range(len(tickets)):
        if tickets[i]["id"] == incident_id.upper():
            return i
    return -1


def add_ticket(incident_id, bot, description):
    """Adds a new ticket to the end of the list."""
    incident_id = incident_id.strip().upper()
    if incident_id == "" or bot.strip() == "" or description.strip() == "":
        print("Error: All fields are required.")
        return False
    if find_index(incident_id) != -1:
        print(f"Error: Ticket {incident_id} already exists.")
        return False
    tickets.append({"id": incident_id, "bot": bot.strip(), "desc": description.strip()})
    print(f"Ticket {incident_id} added successfully.")
    return True


def display_tickets():
    """Displays all active tickets in a table."""
    if len(tickets) == 0:
        print("No active incident tickets.")
        return
    print("-" * 80)
    print(f"{'No.':<5}{'Incident ID':<14}{'Bot':<20}{'Short Description'}")
    print("-" * 80)
    for i in range(len(tickets)):
        t = tickets[i]
        print(f"{i + 1:<5}{t['id']:<14}{t['bot']:<20}{t['desc']}")
    print("-" * 80)


def search_ticket(incident_id):
    """Searches for a ticket using its Incident ID."""
    index = find_index(incident_id.strip())
    if index == -1:
        print(f"Ticket {incident_id.strip().upper()} not found.")
    else:
        t = tickets[index]
        print("Ticket found!")
        print(f"  Position    : {index + 1}")
        print(f"  Incident ID : {t['id']}")
        print(f"  Bot         : {t['bot']}")
        print(f"  Description : {t['desc']}")


def remove_ticket(incident_id):
    """Removes a resolved ticket from the list."""
    index = find_index(incident_id.strip())
    if index == -1:
        print(f"Ticket {incident_id.strip().upper()} not found. Nothing removed.")
    else:
        removed = tickets.pop(index)
        print(f"Ticket {removed['id']} ({removed['bot']}) marked as resolved and removed.")


def count_tickets():
    """Displays the total number of active tickets."""
    print(f"Total active incident tickets: {len(tickets)}")


def load_sample_tickets():
    """Adds the 10 sample tickets from the lab sheet."""
    for incident_id, bot, desc in SAMPLE_TICKETS:
        add_ticket(incident_id, bot, desc)


def show_menu():
    print("\n===== IT AUTOMATION INCIDENT TICKET MANAGER =====")
    print("[1] Add a new incident ticket")
    print("[2] Display all active tickets")
    print("[3] Search for a ticket")
    print("[4] Remove a resolved ticket")
    print("[5] Display total number of active tickets")
    print("[6] Load the 10 sample tickets")
    print("[0] Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        print()

        if choice == "1":
            incident_id = input("Enter Incident ID: ")
            bot = input("Enter Bot: ")
            description = input("Enter Short Description: ")
            add_ticket(incident_id, bot, description)
        elif choice == "2":
            display_tickets()
        elif choice == "3":
            search_ticket(input("Enter Incident ID to search: "))
        elif choice == "4":
            remove_ticket(input("Enter Incident ID of the resolved ticket: "))
        elif choice == "5":
            count_tickets()
        elif choice == "6":
            load_sample_tickets()
        elif choice == "0":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 0 to 6.")


if __name__ == "__main__":
    main()