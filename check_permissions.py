import os
import pwd

def list_users_with_access(file_path):
    """
    List users who can access the specified file based on its permissions.

    Parameters:
    file_path (str): The path to the file for which to check access.

    Returns:
    list: A list of usernames who have access to the file.
    """
    # Get the file's permissions
    file_stat = os.stat(file_path)
    
    # Get the owner's user ID
    owner_uid = file_stat.st_uid
    
    # Get the group ID
    group_id = file_stat.st_gid

    # Get the mode (permissions) of the file
    mode = file_stat.st_mode

    # Initialize a list to hold users with access
    accessible_users = []

    # Check if the owner has read permissions
    if mode & 0o400:  # Owner read permission
        accessible_users.append(pwd.getpwuid(owner_uid).pw_name)

    # Check if the group has read permissions
    if mode & 0o040:  # Group read permission
        for user in pwd.getpwall():
            if user.pw_gid == group_id:
                accessible_users.append(user.pw_name)

    # Check if others have read permissions
    if mode & 0o004:  # Others read permission
        for user in pwd.getpwall():
            accessible_users.append(user.pw_name)

    return list(set(accessible_users))  # Return unique usernames

# Example usage
file_path = 'app.py'  # Specify the path to your file
users_with_access = list_users_with_access(file_path)
print("Users who can access", file_path, ":", users_with_access)