import os
import stat

# define the users and their roles
users = {
    'admin': {'name': 'admin', 'role': 'admin'},
    'developer': {'name': 'developer', 'role': 'developer'},
    'tester': {'name': 'tester', 'role': 'tester'},
    'cloud_engineer': {'name': 'cloud_engineer', 'role': 'cloud_engineer'}
}

# define the permissions for each role
permissions = {
    'admin': stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO,  # read, write, and execute for user, group, and others
    'developer': stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR,  # read, write, and execute for user only
    'tester': stat.S_IRUSR | stat.S_IWUSR,  # read and write for user only
    'cloud_engineer': stat.S_IRWXU  # read, write, and execute for user only
}

# set the permissions for each file for each user
for user in users.values():
    for file in os.listdir():
        if user['role'] == 'admin':
            os.chmod(file, permissions[user['role']])
        elif user['role'] == 'developer' and file == 'app.py':
            os.chmod(file, permissions[user['role']])
        elif user['role'] == 'tester' and file == 'test.py':
            os.chmod(file, permissions[user['role']])
        elif user['role'] == 'cloud_engineer':
            os.chmod(file, permissions[user['role']])