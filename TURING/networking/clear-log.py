import subprocess

def run_powershell_script(script_path):
    command = [
        "powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-File", script_path
    ]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        print("Output:", result.stdout)
        print("Errors:", result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    powershell_script_path = r"C:\Users\BenjaminAtadana\YandexDisk\MY_FILES\Visual_Studio_Codes\TURING\CI-CD\clear-powershell-script.ps1"  # Update with your script path
    run_powershell_script(powershell_script_path)