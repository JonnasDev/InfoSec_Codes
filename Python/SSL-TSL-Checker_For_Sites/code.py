import ssl
import socket

def check_ssl_tls(hostname):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                print(f"-------------------------------------------------------")
                print(f"|Certificado de >{hostname}<:\n")
                print(f"Válido de: {cert['notBefore']}")
                print(f"Válido até: {cert['notAfter']}")
                print(f"Emissor: {cert['issuer']}")
                print(f"Assunto: {cert['subject']}")
                print(f"Versão do SSL/TLS: {ssock.version()}")
                print(f"\nResumo:\n{ssock.cipher()}")
                print(f"-------------------------------------------------------")

    except (socket.gaierror, ConnectionRefusedError):
        print(f"Não foi possível conectar a {hostname}")
    except ssl.SSLError as e:
        print(f"Erro SSL: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    hostname = input("Digite o nome do host (exemplo: www.exemplo.com): ")
    check_ssl_tls(hostname)