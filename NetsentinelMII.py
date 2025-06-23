from ping3 import ping
import socket
import ssl
import datetime 

def port_scan(target, start_port, end_port):
    print(f"\n Scanning ports {start_port}-{end_port} on {target} ... \n")
    found_open = False # Track if any ports are found open


    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((target, port))
                if result == 0:
                    found_open = True
                    try:
                        banner_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        banner_sock.settimeout(1)
                        banner_sock.connect((target, port))
                        banner = banner_sock.recv(1024).decode(errors="ignore").strip()
                        banner_sock.close()

                        if banner:
                            print(f"[+] Port {port} is OPEN | Banner: {banner}")
                        else:
                            print(f"[+] Port {port} is OPEN | No banner returned")
                    except Exception:
                        print(f"[+] Port {port} is OPEN | Banner grab failed")
        except Exception as e:
            print(f"[!] Error scannign port {port}: {e}")

       

    if not found_open:
        print(f"\n No open ports found in the range {start_port}-{end_port}.")                        
                                             
# Main routine

target = input("Enter a domain or IP address to ping and scan: ")

try:
    response = ping(target, timeout=3)
    if response:
        print(f"{target} responded in {round(response * 1000, 2)} ms")

        start = int(input("Enter start port (e.g., 1): "))
        end =int (input("Enter end port (e.g., 1024):"))
        port_scan(target, start, end)
    else:
        print(f"No response from {target}")
except Exception as e:
    print(f"Ping error: {e}")

# Optional TLS cert scan on port 443
if 443 >= start and 443 <= end:
    run_tls = input("Run TLS certificate scan on port 443? (y/n): ").lower()
    if run_tls == 'y':
        tls_certificate_scan(target)
    
    try:
        with socket.create_connection((domain, port), timeout=3) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                print(f"\n TLS certificate Info for {target}:{port}\n")

                subject = dict(x[0] for x in cert['subject'])
                issued_to = subject.get('commonName', 'N/A')
                issuer = dict(x[0] for x in cert['issuer']).get('commonName', 'N/A')

                valid_from = cert['notBefore']
                valid_to = cert['notAfter']
                expires = datetime.datetime.strptime(valid_to, "%b %d %H:%M:%S %Y %Z")
                days_left = (expires - datetime.datetime.utcnow()).days
                print(f"Issued to     : {issued_to}")
                print(f"Issuer        : {issuer}")
                print(f"Valid From    : {valid_from}")
                print(f"Valid Until   : {valid_to}")
                print(f"Days left     : {days_left} dasy(s)")

                if days_left < 0:
                    print("Certficate has EXPIRED!")
                elif days_left < 15:
                    print("Certificate is expiring soon.")
                else:
                    print("Certificate is valid.")
    except Exception as e:                   
        print(f"\n[!] TLS Scan Error for {domain}:{port} - {e}")
                
            

                        
