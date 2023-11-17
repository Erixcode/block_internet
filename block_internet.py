import subprocess
import psutil

def block_internet_access(program_name):
    # Disable firewalld
    subprocess.run("sudo systemctl stop firewalld", shell=True)

    # Find all UIDs for the specified program name
    program_uids = [process.info['username'] for process in psutil.process_iter(['pid', 'name', 'username']) if process.info['name'] == program_name]

    # Block outgoing connections for each UID
    for uid in program_uids:
        subprocess.run(f"sudo iptables -A OUTPUT -p tcp --match owner --uid-owner {uid} -j DROP", shell=True)

    # Block incoming connections for each UID
    for uid in program_uids:
        subprocess.run(f"sudo iptables -A INPUT -p tcp --match owner --uid-owner {uid} -j DROP", shell=True)

def unblock_internet_access(program_name):
    # Find all UIDs for the specified program name
    program_uids = [process.info['username'] for process in psutil.process_iter(['pid', 'name', 'username']) if process.info['name'] == program_name]

    # Remove outgoing rules for each UID
    for uid in program_uids:
        subprocess.run(f"sudo iptables -D OUTPUT -p tcp --match owner --uid-owner {uid} -j DROP", shell=True)

    # Remove incoming rules for each UID
    for uid in program_uids:
        subprocess.run(f"sudo iptables -D INPUT -p tcp --match owner --uid-owner {uid} -j DROP", shell=True)

    # Enable firewalld back
    subprocess.run("sudo systemctl start firewalld", shell=True)

def get_user_input():
    program_name = input("Enter the program name: ")
    return program_name

def main():
    # Example: Get the program name from the user
    program_name = get_user_input()

    # Example: Check if the program is running and block internet access
    block_internet_access(program_name)

    # Wait for user input before unblocking and exiting
    input("Press Enter to unblock and exit...")

    # Remove the firewall rules after user input
    unblock_internet_access(program_name)

    print("Script completed.")

if __name__ == "__main__":
    main()
