import requests

def check_sql_injection_vulnerability(url):
    try:
        # Inclua um caractere especial (por exemplo, aspas simples) no parâmetro da URL
        payload = "?"
        response = requests.get(url + payload)

        if "error" in response.text.lower() or "exception" in response.text.lower():
            print("Possível vulnerabilidade de SQL injection detectada.")
        else:
            print("O site parece estar seguro contra SQL injection.")

    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro ao acessar o site: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    url = input("Digite a URL do site para verificar a vulnerabilidade de SQL injection: ")
    check_sql_injection_vulnerability(url)