if __name__=="__main__":
    from file_manager import delete_user, getpass, read_password_file, rot13
    username = input("Enter username: ")
    lst = read_password_file("passwd.txt")
    lst = [x.strip().split(":")[0] for x in lst]
    if username in lst:
        password = getpass.getpass("Enter password: ")

        pos = lst.index(username)
        lst = read_password_file("passwd.txt")
        lst = [x.strip().split(":")[-1] for x in lst]
        if rot13(password) == lst[pos]:
            delete_user(username)
        else:
            print("Incorrect password! Cannot delete the user name.")
    else:
        print("User not found")
     