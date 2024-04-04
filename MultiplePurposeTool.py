import hashlib
from itertools import product
import requests

def welcome():
    print(                                                                "WELCOME TO RAYYAN PROJECT!")


    print("Updates Will Come SOON!!")

def command_cheat_sheet():
    cheat_sheet = {
        'ls': 'List directory contents',
        'cd': 'Change the current directory',
        'pwd': 'Print the working directory',
        'mkdir': 'Create a new directory',
        'rm': 'Remove files or directories',
        'cp': 'Copy files or directories',
        'mv': 'Move/rename files or directories',
        'chmod': 'Change the permissions of files or directories',
        'grep': 'Search text using patterns',
        'find': 'Search for files in a directory hierarchy',
        'cat': 'Concatenate files and print on the standard output',
        'echo': 'Display a line of text',
        'man': 'Display the user manual of any command',
        'sudo': 'Execute a command as the superuser',
        'apt-get': 'Package management command (Debian based)',
        'df': 'Report file system disk space usage',
        'du': 'Estimate file space usage',
        'free': 'Display amount of free and used memory in the system',
        'ps': 'Report a snapshot of the current processes',
        'kill': 'Send a signal to a process',
        'netstat': 'Print network connections, routing tables, interface statistics',
        'ifconfig': 'Configure a network interface',
        'wget': 'Retrieve content from web servers',
        'curl': 'Transfer data from or to a server',
        'ssh': 'OpenSSH SSH client (remote login program)',
        'scp': 'Secure copy (remote file copy program)',
        'tar': 'An archiving utility',
        'gzip': 'Compress or expand files',
        'unzip': 'List, test and extract compressed files in a ZIP archive'
    }
    cmd = input("Enter the command you want to know about: ")
    print(cheat_sheet.get(cmd, "No information available for this command."))

def decrypt_sha512(hash_value, dictionary_file):
    try:
        with open(dictionary_file, 'r') as file:
            for word in file:
                word = word.strip()
                if hashlib.sha512(word.encode()).hexdigest() == hash_value:
                    print(f"Found matching input: {word}")
                    return
        print("No match found.")
    except FileNotFoundError:
        print("Dictionary file not found.")

def find_subdomains(domain):
    subdomains_list = ['www', 'mail', 'ftp', 'localhost']
    for subdomain in subdomains_list:
        url = f"http://{subdomain}.{domain}"
        try:
            requests.get(url)
            print(f"Found subdomain: {url}")
        except requests.ConnectionError:
            pass

def main():
    welcome()
    while True:
        choice = input("\nSelect an option:\n1. Command Cheat Sheet\n2. Decrypt SHA-512 Hash\n3. Find Subdomains\n4. Exit\n> ")
        if choice == '1':
            command_cheat_sheet()
        elif choice == '2':
            hash_value = input("Enter the SHA-512 hash: ")
            dictionary_file = input("Enter the path to your dictionary file: ")
            decrypt_sha512(hash_value, dictionary_file)
        elif choice == '3':
            domain = input("Enter the domain: ")
            find_subdomains(domain)
        elif choice == '4':
            print("Exiting RAYYAN PROJECT.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
