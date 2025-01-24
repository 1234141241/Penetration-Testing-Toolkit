import socket


def port_scanner(target_ip, start_port, end_port):
    open_ports = []
    print(f"Scanning {target_ip} for open ports between {start_port} and {end_port}...")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports
