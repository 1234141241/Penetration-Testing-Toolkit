# Penetration-Testing-Toolkit

TASK-3

**COMPANY**: CODETECH IT SOLUTIONS

**NAME**: VIJAY SHINDE

**INTERN ID**: CT08GYF

**DOMAIN**: Cyber Security & Ethical Hacking

**BATCH DUARATION**: December 25th, 2024 to January 25th, 2025

**MENTOR NAME**: NEELA SANTOSH KUMAR

**DESCRIPTION OF TASK**:

The Penetration Testing Toolkit is a Python-based, modular toolkit designed to assist security professionals in conducting penetration tests. This toolkit includes multiple modules that automate common tasks in penetration testing, such as Port Scanning and Brute Force Attacks. Each module can be run independently or integrated into a larger testing framework, allowing users to customize their penetration testing approach.

Modules Included:
Port Scanner: Identifies open ports on a target host, providing valuable information about which services are exposed.
Brute-Forcer: Tests login forms or SSH services with a wordlist to attempt to gain unauthorized access by trying multiple combinations of usernames and passwords.
Additional Modules: Future updates will include more modules such as vulnerability scanners, network sniffers, and more, making this toolkit a comprehensive penetration testing suite.

Clone this repository to your local machine:
git clone https://github.com/1234141241/Penetration-Testing-Toolkit

Requirements
Python 3.x
Requests
Paramiko

Usage:

Run the desired module from the command line:

To run port scanner:
python port_scanner.py 192.168.1.1

To run the brute-force module:
python brute_forcer.py --target http://example.com/login --wordlist passwords.txt
