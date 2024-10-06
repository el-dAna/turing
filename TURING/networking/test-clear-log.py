import subprocess
import os
import sys
import logging
import configparser
import getpass

# Configure logging
logging.basicConfig(
    filename="automation_log.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


# Function to read and validate configuration
def read_config(config_file="config.ini"):
    """
    Reads configuration from the given config file and validates its integrity.
    :param config_file: The path to the configuration file.
    :return: A dictionary of configurations.
    """
    config = configparser.ConfigParser()
    config.read(config_file)
    return {
        section: dict(config.items(section))
        for section in config.sections()
    }


# Function to check if the current user is authorized
def is_user_authorized():
    """
    Checks if the current user is in the list of allowed users from the config.
    :return: True if authorized, False otherwise.
    """
    config = read_config()
    allowed_users = config["Security"][
        "allowed_users"
    ].split(",")
    current_user = getpass.getuser()

    if current_user.strip() not in [
        user.strip() for user in allowed_users
    ]:
        logging.error(
            f"User '{current_user}' is not authorized to execute this script."
        )
        return False

    return True


# Function to run a PowerShell script
def run_powershell_script(script_path):
    """
    Executes a PowerShell script with execution policy set to Bypass.
    :param script_path: The path to the PowerShell script file.
    :return: None
    """
    command = [
        "powershell",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        script_path,
    ]

    try:
        # Run the PowerShell script
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
        )

        # Log the output and errors
        logging.info(f"Output: {result.stdout}")
        if result.stderr:
            logging.error(
                f"Errors: {result.stderr}"
            )
    except subprocess.CalledProcessError as cpe:
        logging.error(
            f"Command '{
                cpe.cmd}' returned non-zero exit status {
                cpe.returncode}. Output: {
                cpe.output}, Error: {
                    cpe.stderr}")
        raise
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise


# Main function to schedule the script execution
def main():
    """
    Main function to schedule and run the PowerShell script.
    :return: None
    """

    # Check if the user is authorized
    if not is_user_authorized():
        print(
            "User is not authorized to execute this script."
        )
    else:
        print("User granted access")
        config = read_config()
        script_path = config["Paths"][
            "script_path"
        ]

        assert os.path.isdir(
            os.path.dirname(script_path)
        ), f"Directory does not exist: {os.path.dirname(script_path)}"

        # Inform the user about the script execution
        print(
            f"Running PowerShell script: {script_path}"
        )

        # Run the script
        run_powershell_script(script_path)

        # Inform the user about the completion of the script
        print(
            "PowerShell script execution completed."
        )


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.critical(
            f"Failed to execute the main function: {e}"
        )
        sys.exit(1)
    else:
        sys.exit(0)
