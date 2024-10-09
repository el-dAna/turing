import os
import subprocess
import getpass

def add_user():
    """
    Adds a new user to the system.
    
    This function prompts for a username and password, then uses 
    the 'useradd' command to create the user account in the system.
    """
    # Ask for the input username
    username = input("Enter Username: ")
    
    # Asking for user's password securely
    password = getpass.getpass("Enter Password: ")
    
    # Create the user using subprocess
    try:
        # The '-p' option requires a hashed password, so we hash it using openssl
        hashed_password = subprocess.check_output(
            ["openssl", "passwd", "-1", password]
        ).strip().decode('utf-8')
        
        # Execute useradd command
        subprocess.run(['useradd', '-m', '-p', hashed_password, username], check=True)
        
        print(f"User '{username}' successfully created.")
        
    except subprocess.CalledProcessError as e:
        print(f"Failed to add user: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == '__main__':
    add_user()