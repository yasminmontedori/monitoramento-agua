
from colorama import init, Fore, Style

# Inicializa a biblioteca Colorama
init(autoreset=True)

# Lista com os níveis e as mensagens do reservatório
niveis_agua = [
    {"nivel": 1, "situacao": "Muito baixo - Nível crítico"},
    {"nivel": 2, "situacao": "Baixo - Atenção ao nível da água"},
    {"nivel": 3, "situacao": "Médio - Nível normal"},
    {"nivel": 4, "situacao": "Alto - Reservatório quase cheio"},
    {"nivel": 5, "situacao": "Muito alto - Alerta de nível máximo"}
]

# Função que define a cor conforme o nível da água
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Exibe as mensagens coloridas no terminal
print("=== MONITORAMENTO DO RESERVATÓRIO DE ÁGUA ===\n")

for item in niveis_agua:
    cor = definir_cor(item["nivel"])
    mensagem = f'Nível {item["nivel"]}: {item["situacao"]}'
    print(cor + mensagem + Style.RESET_ALL)

