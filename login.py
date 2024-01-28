if __name__ == "__main__":
    from file_manager import login, getpass
    username = input("Enter username: ")
    password = input("Enter password: ")
    login(username.lower(), password)