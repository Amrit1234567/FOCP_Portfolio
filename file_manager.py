import getpass

def rot13(text):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()
            
            # Convert the character to its ASCII code
            ascii_code = ord(char)
            
            # Apply ROT-13 transformation
            if is_upper:
                rotated_code = (ascii_code - ord('A') + 13) % 26 + ord('A')
            else:
                rotated_code = (ascii_code - ord('a') + 13) % 26 + ord('a')
            
            # Convert the rotated ASCII code back to a character
            rotated_char = chr(rotated_code)
            
            result += rotated_char
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    
    return result

def login(username, password, filename = "passwd.txt"):
    """
    checks username and password in the file. 
    """
    lst = read_password_file(filename)
    for std_data in lst:
        if std_data.startswith(username + ":"):
            _, _, pswd =  std_data.strip().split(":")
            if pswd == rot13(password):
                print("Access Granted")
                return None
    else:
        print("Access Denied")

def passwd(username, filename = "passwd.txt"):
    """
        
    """
    lst = read_password_file(filename)
    for std_data in lst:
        if std_data.startswith(username + ":"):
            username, realname, password =  std_data.strip().split(":")
            break
    else:
        print("User not found!")
        return None
    psd_check = getpass.getpass("Current Password: ")
    psd_check = rot13(psd_check)
    if psd_check == password:
        new_password = getpass.getpass("New Password: ")
        confirm = getpass.getpass("Confirm: ")
        if new_password ==confirm:
            delete_user(username)
            add_user(username, realname, confirm)
            print("Password Changed!")
        else:
            print("Your password did not confirm. Nothing changed")
    else:
        print("Sorry, password does not match")
        
def add_user( username, real_name, encrypted_password, filename= "passwd.txt"):
    lst = read_password_file(filename)
    lst = [x.split(":")[0] for x in lst]
    encrypted_password = rot13(encrypted_password)
    if username not in lst:
        f = open(filename, "a")
        f.write(f"{username}:{real_name}:{encrypted_password}\n")
        f.close()
        print("User Created")
    else:
        print("Cannot add. Most likely username already exists.")

        
def delete_user(username, filename= "passwd.txt"):
    lst = read_password_file(filename)
    lst = [x.split(":")[0] for x in lst]
    if username in lst:
        pos = lst.index(username)
        lst = read_password_file(filename)
        lst.pop(pos)
        f = open(filename, "w")
        f.writelines(lst)
        f.close()
        print("Successfully deleted")
    else:
        print("Nothing was changed!")
    
def read_password_file(file_name):
    """
        Reads the file and returns list
    """
    f = open(file_name)
    lst = f.readlines()
#     lst = [x.split(":") for x in lst]
    f.close()
    return lst

def write_password_file(file_name, content):
    lst = read_password_file(file_name)
    print(lst)
    
    f = open(file_name, "w")
    lst.append(content+"\n")
    f.writelines(lst)
    f.close()
    return None

