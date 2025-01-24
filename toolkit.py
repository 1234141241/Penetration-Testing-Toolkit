import argparse
from modules.port_scanner import port_scanner
from modules.brute_force_ssh import brute_force_ssh
from modules.vulnerability_scanner import vulnerability_scanner


def main():
    parser = argparse.ArgumentParser(description="Penetration Testing Toolkit")
    parser.add_argument('target', type=str, help="Target IP address")
    parser.add_argument('module', type=str, help="Module to run: port_scanner, brute_force_ssh, vulnerability_scanner")
    parser.add_argument('--username', type=str, help="Username for brute force SSH")
    parser.add_argument('--password_file', type=str, help="Password file for brute force SSH")
    parser.add_argument('--start_port', type=int, help="Start port for port scanner")
    parser.add_argument('--end_port', type=int, help="End port for port scanner")

    args = parser.parse_args()

    if args.module == "port_scanner":
        if args.start_port and args.end_port:
            open_ports = port_scanner(args.target, args.start_port, args.end_port)
            print(f"Open Ports: {open_ports}")
        else:
            print("Please provide both --start_port and --end_port for port_scanner.")

    elif args.module == "brute_force_ssh":
        if args.username and args.password_file:
            with open(args.password_file, 'r') as file:
                password_list = file.readlines()
            password_list = [password.strip() for password in password_list]
            brute_force_ssh(args.target, args.username, password_list)
        else:
            print("Please provide both --username and --password_file for brute_force_ssh.")

    elif args.module == "vulnerability_scanner":
        vulnerable_ports = vulnerability_scanner(args.target)
        print(f"Vulnerable Ports: {vulnerable_ports}")

    else:
        print("Invalid module. Choose from: port_scanner, brute_force_ssh, vulnerability_scanner")


if __name__ == '__main__':
    main()
