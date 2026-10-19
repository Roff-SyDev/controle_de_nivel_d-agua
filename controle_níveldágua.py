# Importando libraries.

import time
from colorama import Fore, Style, init

# Garantindo compatibilidade no terminal.
init()

# Organizando a lista dos níveis do reservatório (com cores e situações que os representam).

niveis_reserv = [
    {"Nível":1, "Situação": "Muito baixo", "cor":Fore.RED},
    {"Nível":2, "Situação": "Baixo", "cor":Fore.YELLOW},
    {"Nível":3, "Situação": "Aceitável", "cor":Fore.GREEN},
    {"Nível":4, "Situação": "Alto", "cor":Fore.CYAN},
    {"Nível":5, "Situação": "Muito alto", "cor":Fore.BLUE},
]

def exibir_alerta(nivel_info): # Função que determina a mensagem colorida no terminal a partir do nível situacional. Após isso, restaura o padrão de texto no final.

    found = False

    for item in niveis_reserv:
        if item["Nível"] == nivel_info:
            # Exibe a mensagem com as especificações, restaurando o padrão logo em seguida.
            print(
                f"{item["cor"]}Nível{item["Nível"]}:{item["Situação"]}{Style.RESET_ALL}"
                )
            encontrado = True
            break
# Bloco de código de execução de testes.
if __name__ == "__main__":
  print("=== SISTEMA DE CONTROLE DE NÍVEIS DE ÁGUA ===")

  # Simulando a verificação de todos os níveis do reservatório
  for nivel_atual in range(1, 6):
    exibir_alerta(nivel_atual)
