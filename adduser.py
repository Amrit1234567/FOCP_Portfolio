if __name__ == "__main__":
    from file_manager import add_user
    username = input("Enter new username: ")
    real_name = input("Enter real name: ")
    password = input("Enter password: ")
    add_user(username.lower(), real_name, password)