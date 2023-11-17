import subprocess
import psutil

def block_internet_access(program_pid):
    # Disable firewalld
    subprocess.run("sudo systemctl stop firewalld", shell=True)

    # Block outgoing connections
    rule_outgoing = f"sudo iptables -A OUTPUT -p tcp --match owner --uid-owner {program_pid} -j DROP"
    subprocess.run(rule_outgoing, shell=True)

def unblock_internet_access(program_pid):
    # Remove the outgoing rule
    rule_outgoing = f"sudo iptables -D OUTPUT -p tcp --match owner --uid-owner {program_pid} -j DROP"
    subprocess.run(rule_outgoing, shell=True)

    # Enable firewalld back
    subprocess.run("sudo systemctl start firewalld", shell=True)

def get_user_input():
    program_name = input("Enter the program name: ")
    return program_name

def main():
    # Example: Get the program name from the user
    program_name = get_user_input()

    # Example: Check if the program is running and get its PID
    program_pid = None
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == program_name:
            program_pid = process.info['pid']
            break

    if program_pid is not None:
        print(f"The PID of {program_name} is: {program_pid}")

        # Example: Block internet access for the specified program
        block_internet_access(program_pid)

        # Wait for user input before exiting
        input("Press Enter to exit...")

        # Remove the firewall rule after your program completes
        unblock_internet_access(program_pid)

        print("Script completed. restoring settings")
    else:
        print(f"{program_name} is not running.")

if __name__ == "__main__":
    main()
