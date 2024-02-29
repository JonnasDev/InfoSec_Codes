import requests

def security_header_check(url):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            headers = response.headers
            required_headers = [
                "X-Content-Type-Options",
                "X-Frame-Options",
                "Content-Security-Policy",
                "Strict-Transport-Security",
                "Referrer-Policy",
            ]

            missing_headers = [header for header in required_headers if header not in headers]

            if not missing_headers:
                print("O site possui todos os cabeçalhos de segurança necessários.")
            else:
                print(f"O site está faltando os seguintes cabeçalhos de segurança: {', '.join(missing_headers)}")
        else:
            print(f"Falha ao conectar-se ao site. Código de status: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a solicitação: {e}")

if __name__ == "__main__":
    website_url = input("Digite o URL do site que você deseja verificar: ")
    security_header_check(website_url)
