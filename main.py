from contact import Contact
import check_input
#   Name: Louis Pavlovsky & Justin Pongos
#   Date: 02/19/2024

#   Desc: Rolodex, a program to manage a contact list. A display of contacts and options are prompted to the user. These options being to view the whole contact list, add, update, search for contact, and save the contact list. The user will be promted to enter information regarding a contact when choosing a option in the menu ranging from 1-5. one being to display the contact list and five being to save and quit.

def read_file():
  """Read the file addresses.txt and set it in a list of type Contact

  Returns:
      [Contacts]: list of object Contact
  """
  with open("addresses.txt", "r") as file:
    list = file.readlines()
    contacts = []
    for line in list:
      contact = line.split(",")
      # if there are no '\n' we put one for formating purpose
      if contact[5][-1] != '\n':
        contact[5] += '\n'
      contacts.append(
          Contact(contact[0], contact[1], contact[2], contact[3], contact[4],
                  contact[5]))
    contacts.sort()
    return contacts


def write_file(contacts):
  """ Get a list of contacts and write it inside the file addresses

  Args:
      contacts ([Contacts]): List of contacts that will be written inside the txt
  """
  with open("addresses.txt", "w") as file:
    for contact in contacts:
      file.write(repr(contact))


def get_menu_choice():
  """ Display the menu to interact with the list of contacts and take inpu user to determine his choice 
  """
  print("1. Display Contacts\n\
2. Add Contact\n\
3. Search Contacts\n\
4. Modify Contact\n\
5. Save and Quit")
  choice = 0
  choice = check_input.get_int_range("> ", 1, 5)
  return choice


def modify_contact(con):
  """ Get the contact to modify and the new information to update it with

  Args:
      con (Contact): Represent a contact that will be modified
  """
  modifying = True

  while modifying:
    print(
        "Modify Menu:\n1. First name\n2. Last name\n3. Phone\n4. Address\n5. City\n6. Zip\n7. Save"
    )

    choice = check_input.get_int_range("> ", 1, 7)
    if choice == 1:
      con.first_name = input("Enter first name:")
    elif choice == 2:
      con.last_name = input("Enter last name:")
    elif choice == 3:
      con.phone = input("Enter phone #:")
    elif choice == 4:
      con.address = input("Enter address:")
    elif choice == 5:
      con.city = input("Enter city:")
    elif choice == 6:
      con.zip = input("Enter zip:") + '\n'
    elif choice == 7:
      break
    else:
      print("Invalid choice")


def main():
  is_program_running = True
  contacts_list = read_file()

  while is_program_running:
    print("Rolodex Menu:")
    choice = get_menu_choice()

    # Display contacts
    if choice == 1:
      len_contacts_list = len(contacts_list)
      print(f"Number of contacts: {len_contacts_list}")
      for i in range(len_contacts_list):
        print(f"{i + 1}. {contacts_list[i]}")
        i += 1
    # Add contacts
    elif choice == 2:
      print("Enter new contact:")
      new_contact_fn = input("First name: ")
      new_contact_ln = input("Last name: ")
      new_contact_phone = input("Phone #: ")
      new_contact_addr = input("Address: ")
      new_contact_city = input("City: ")
      new_contact_zip = input("Zip: ") + '\n'
      print("")  ##For output formatting
      contacts_list.append(Contact(new_contact_fn, new_contact_ln, new_contact_phone\
                                   , new_contact_addr, new_contact_city, new_contact_zip))
      contacts_list.sort()
    # Search Contacts
    elif choice == 3:
      tmp_list = contacts_list
      print("Search:\n\
1. Search by last name\n\
2. Search by zip")
      # Ask input to search by last name or zip
      search_choice = input("> ")
      if search_choice == "1":
        res = input("Enter last name: ")
        for i in range(len(contacts_list)):
          if res in contacts_list[i].last_name:
            print(contacts_list[i])
      elif search_choice == "2":
        res = input("Enter zip code: ")
        for i in range(len(contacts_list)):
          if res in contacts_list[i].zip:
            print(contacts_list[i])
    # Modify Contact
    elif choice == 4:
      first_name = input("Enter first name: ")
      last_name = input("Enter last name: ")
      #  Searches for Contact matching first and last name given by the user
      for i in range(len(contacts_list)):
        if first_name in \
        contacts_list[i].first_name and last_name in contacts_list[i].last_name:
          print(f"\n{contacts_list[i]}")
          #  Updates contact info
          modify_contact(contacts_list[i])
          contacts_list.sort()
    # Save and Quit
    elif choice == 5:
      write_file(contacts_list)
      print("Saving File. . .\nEnding Program")
      is_program_running = False

main()
