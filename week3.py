from pathlib import Path                                     #we can use os path lib both for making this program I have used path lib that have same pattern of usage like os library#

def contact_manager():
    print(" 1 for adding contact \n 2 for searching contact\n 3 for updating contact") # using choice to provide option to the user #
    choice = int(input("Enter choice: "))
    if choice == 1:
        add_contact()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        show_contacts()

def add_contact():
    number = input("Enter contact number: ")
    name = input("Enter contact name: ")
    target_dir = Path(r"C:\Users\DELL\Desktop\contact_INFO") # here we have mentioned the path where the new text file with contact detail will be saved at the folder location#
    target_dir.mkdir(parents=True, exist_ok=True)            # mkdir helps to make directory if not made by the programmer#
    count = 1                                                #this adds 1 after creating first text file with contact details inside the contact_INFO folder#
    while (target_dir/f"Information{count}.txt").exists():
        count += 1
    name_file = f"Information{count}.txt"
    in_path = target_dir / name_file
    formatted_tx = f"name: {name}\n number: {number}"
    in_path.write_text(formatted_tx)                         #Writes text in to the text file#
    print(f"Details saved as {name_file}")

def search_contact():
    target_dir = Path(r"C:\Users\DELL\Desktop\contact_INFO")  # Targets the folder contact_INFO and searches each text file for the text entered in search_txt#
    search_text = input("Enter contact name: ")

    for file_path in target_dir.glob("Information*.txt"): #.glob is used for match or search all files with extension or the string given to it #
        content = file_path.read_text()                   # read the text if the search_txt is found #
        if search_text in content:
            print(content)                                #prints the text that it has read#

def show_contacts():
    target_dir = Path(r"C:\Users\DELL\Desktop\contact_INFO")
    for contact_file in target_dir.glob("Information*.txt"):
        print(contact_file.read_text(encoding="utf-8"))  #Reads all character string and special character using utf and prints #

contact_manager()                                        #finally called this function to asked user to provide there input#