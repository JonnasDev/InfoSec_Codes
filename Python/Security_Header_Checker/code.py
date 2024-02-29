import requests

def security_header_check(url):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            print("Conexão bem-sucedida com o site.")

            # Verifique os cabeçalhos de segurança
            security_headers = {
                "X-Content-Type-Options": "nosniff",
                "X-Frame-Options": "DENY",
                "Content-Security-Policy": "default-src 'self'",
                "Strict-Transport-Security": "max-age=31536000; includeSubDomains; preload",
                "Referrer-Policy": "no-referrer-when-downgrade",
            }

            for header, expected_value in security_headers.items():
                actual_value = response.headers.get(header)
                if actual_value is None:
                    print(f"{header} não encontrado no cabeçalho de resposta.")
                else:
                    print(f"{header} está definido como {actual_value}")

        else:
            print(f"Falha ao conectar-se ao site. Código de status: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a solicitação: {e}")

if __name__ == "__main__":
    website_url = input("Digite o URL do site que você deseja verificar: ")
    security_header_check(website_url)
