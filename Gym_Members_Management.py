import time
import os
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

gym_users = []

# Gym_Members_Class
class Gym_Members:
  def __init__ (self, first_name, last_name, member_ID, status = "inactive"):
    self.first_name = first_name
    self.last_name = last_name
    self.member_ID = member_ID
    self.status = status
    gym_users.append(f"-------------------------\nFirst Name: {self.first_name}\nLast Name: {self.last_name}\nMember ID: {self.member_ID}\nStatus: {self.status}\n-------------------------")


# Create_New_Member
def create_user():
  first_name = input("Enter your first name: ")
  while first_name == "":
    print("You didn't enter your first name.")
    first_name = input("Enter your first name: ")
  last_name = input("Enter your last name: ")
  while last_name == "":
    print("You didn't enter your last name.")
    first_name = input("Enter your last name: ")
  member_ID = input("Enter your member ID: ")
  while member_ID == "":
    print("You didn't enter your Member_ID name.")
    first_name = input("Enter your Member_ID name: ")
  status = input("Enter your status or press enter to continue without write: ")
  while status != "active" and status != "inactive" and status != "":
    print("Sorry, Invalid Status")
    status = input("Enter your status: ")
  if status == "":
    status = "inactive"
  else:
    status = status
  return Gym_Members(first_name, last_name, member_ID, status)


# Interface
def introduction():
  print("\nWelcome to the Gym Membership System!\n\n")
  # User_Choice
  print("Choose an Action: \n\n1. Add new member\n2. Display all members\n3. Search for a member\n4. Exit\n")
  user_choice = input("Enter your choice: ")
  # User_Choice_Validation
  while user_choice != "1" and user_choice != "2" and user_choice != "3" and user_choice != "4":
    print("Sorry, Invalid Input. Please try again.")
    user_choice = input("Enter your choice: ")
  # Add_New_Member
  if user_choice == "1":
    clear_screen()
    create_user()
    print("Member added successfully!")
    time.sleep(3)
    clear_screen()
    time.sleep(0.5)
    introduction()
  # Display_All_Members
  elif user_choice == "2":
    if gym_users:
      clear_screen()
      print("Displaying all members......")
      print("".join(gym_users))
      time.sleep(3)
      clear_screen()
      time.sleep(0.5)
      introduction()
    else:
      print("Sorry, there are no members in the system.")
      time.sleep(2)
      clear_screen()
      time.sleep(0.5)
      introduction()
  # Search_For_Member
  elif user_choice == "3":
    clear_screen()
    print("Search by:\n\n1. Membership ID\n2. First_name\n3. Membership Status\n")
    search_choice = input("Enter your choice: ") 
    while search_choice != "1" and search_choice != "2" and search_choice != "3":
      print("Sorry, Invalid Input. Please try again.")
      search_choice = input("Enter your choice: ")
    # Search_By_Membership_ID
    if search_choice == "1":
      search_ID = input("Enter the member ID: ")
      for user in gym_users:
        if search_ID in user:
          clear_screen()
          print(user)
          time.sleep(3)
          clear_screen()
          time.sleep(0.5)
          introduction()
        else:
          print("Member not found.")
          clear_screen()
          introduction()
    # Search_By_First_Name
    elif search_choice == "2":
      search_first_name = input("Enter the First Name: ")
      for user in gym_users:
        if search_first_name in user:
          clear_screen()
          print(user)
          time.sleep(3)
          clear_screen()
          time.sleep(0.5)
          introduction()
        else:
          print("Member not found.")
          clear_screen()
          time.sleep(0.5)
          introduction()
    # Search_By_Membership_Status
    else:
      search_member_status = input("Enter the Member Status: ")
      for user in gym_users:
        if search_member_status in user:
          clear_screen()
          print(user)
          time.sleep(3)
          clear_screen()
          time.sleep(0.5)
          introduction()
        else:
          print("Member not found.")
          clear_screen()
          time.sleep(0.5)
          introduction()
  # Exit
  else:
    print("Thank you for using the Gym Membership System!")
    print("Exiting...........")
    time.sleep(2)

# Code
introduction()

    
    