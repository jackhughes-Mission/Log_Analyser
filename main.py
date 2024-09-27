import os
import re

def get_most_requested_files(logfilepath):
    file_pattern = r'GET\s(.*?)\sHTTP.*"\s(\d{3})'
    file_dictionary = {}

    with open(logfilepath, 'r') as file:
        for logline in file:
            found_files = re.findall(file_pattern, logline)

            for file_path, response_code in found_files:
                key = (file_path, response_code)
                if key in file_dictionary:
                    file_dictionary[key] += 1
                else:
                    file_dictionary[key] = 1

    for (file, response_code), count in file_dictionary.items():
        if count > 100:
            print(f"{file} - accessed {count} times with response code {response_code}.")


def get_all_ip_addresses(logfilepath):
    ip_pattern = r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
    ip_dictionary = {}

    with open(logfilepath, 'r') as file:
        for logfilepath in file:
            found_ips = re.findall(ip_pattern, logfilepath)

            for ip in found_ips:
                if ip in ip_dictionary:
                    ip_dictionary[ip] += 1
                else:
                    ip_dictionary[ip] = 1

    sorted_ips = sorted(ip_dictionary.items(), key=lambda item: item[1], reverse=True)

    for ip, count in sorted_ips:
        print(f"{ip} - appears {count} times.")

def get_response_codes(logfilepath):
    response_code_pattern = r'(?<=\s)(\d{3})(?=\s)'
    response_code_dictionary = {}

    with open(logfilepath, 'r') as file:
        for logfilepath in file:
            found_response_codes = re.findall(response_code_pattern, logfilepath)

            for response_code in found_response_codes:
                if response_code in response_code_dictionary:
                    response_code_dictionary[response_code] += 1
                else:
                    response_code_dictionary[response_code] = 1

    for response_code, count in response_code_dictionary.items():
        print(f"{response_code} - appears {count} times.")

def get_tools_used(logfilepath):
    tools_pattern = r'(?<=\()\w+'
    tools_dictionary = {}

    with open(logfilepath, 'r') as file:
        for logfilepath in file:
            found_tools = re.findall(tools_pattern, logfilepath)

            for tool in found_tools:
                if tool in tools_dictionary:
                    tools_dictionary[tool] += 1
                else:
                    tools_dictionary[tool] = 1

    for tool, count in tools_dictionary.items():
        print(f"{tool} - used {count} times.")


def choose_options(logfilepath):
    while True:
        print("\nChoose an option:"
              "\n1. See IP addresses found"
              "\n2. See requested assets"
              "\n3. See response codes"
              "\n4. See tools used"
              "\n5. Choose another log file")

        option = input("Enter: ")

        if option == '1':
            get_all_ip_addresses(logfilepath)
        elif option == '2':
            get_most_requested_files(logfilepath)
        elif option == '3':
            get_response_codes(logfilepath)
        elif option == '4':
            get_tools_used(logfilepath)
        elif option == '5':
            get_log_file()
        else:
            print("Invalid option")


def read_log_file(logfilepath):
    try:
        with open(logfilepath, 'r') as file:
            choose_options(logfilepath)
    except FileNotFoundError:
        print("File not found")
        return
    except PermissionError:
        print("Permission denied")
        return
    except Exception as e:
        print("An error occurred: " + str(e))
    return


def get_log_file():
    logfiledirectory = 'LogFiles'
    for file in os.listdir(logfiledirectory):
        print(" - "+ file)

    logfilename = input("Enter: ")
    logfilepath = os.path.join(logfiledirectory, logfilename)

    print("You choose " + logfilepath)

    read_log_file(logfilepath)

if __name__ == "__main__":
    get_log_file()