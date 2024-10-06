import subprocess
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_command(command):
    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info(f"Command {' '.join(command)} executed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Command {' '.join(command)} failed with error: {e.stderr.decode().strip()}")
        exit(1)

def build_image(tag):
    logging.info("Building Docker image...")
    run_command(["docker", "build", "-t", tag, "."])

def run_container(tag):
    logging.info("Running Docker container...")
    # Using the --rm flag to remove the container after it exits
    # Using the -d flag to run the container in detached mode
    run_command(["docker", "run", "--rm", "-d", tag])

def check_network():
    logging.info("Checking network connectivity...")
    try:
        subprocess.run(["ping", "-c", "4", "8.8.8.8"], check=True)  # Ping Google's DNS server
        logging.info("Network connectivity check passed.")
    except subprocess.CalledProcessError:
        logging.error("Network connectivity check failed. Please ensure you have a stable internet connection.")
        exit(1)

def set_resource_limits():
    logging.info("Setting resource limits...")
    # Set memory limit to 500MB and CPU limit to 0.5 of a CPU (assuming the host has at least 1 CPU)
    run_command(["docker", "run", "--memory", "500m", "--cpu", "0.5", "myapp"])

def optimize_image():
    logging.info("Optimizing Docker image...")
    # Use multi-stage builds in the Dockerfile to reduce image size
    # This is a placeholder and assumes the Dockerfile is already optimized for multi-stage builds
    # The actual optimization should be done in the Dockerfile itself

def main():
    # Get the current Git commit hash to use as a tag
    commit_hash = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).strip().decode()
    custom_tag = "custom_name"  # Replace with your custom tag
    tag = f"{custom_tag}:{commit_hash}"

    check_network()
    build_image(tag)
    optimize_image()
    set_resource_limits()
    run_container(tag)

if __name__ == "__main__":
    main()
    