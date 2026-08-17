# os: para mexer nas pastas e arquivos do computador
# Documentação: https://docs.python.org/3/library/os.html
import os

# sys: para indicar ao Python onde ele deve procurar os arquivos
# Documentação: https://docs.python.org/3/library/sys.html
import sys

# importlib: para carregar e rodar outros scripts enquanto o programa está rodando
# Documentação: https://docs.python.org/3/library/importlib.html
import importlib


def main():
    # Pega o caminho da pasta onde este arquivo main.py está salvo
    caminho_diretorio_atual = os.path.dirname(os.path.abspath(__file__))

    # Monta o caminho completo até a pasta onde ficam os scripts dos gráficos
    caminho_pasta_graficos = os.path.join(caminho_diretorio_atual, "Graph_AI_Analizy")

    # Avisa ao Python que a pasta atual faz parte dos caminhos de busca para importações
    if caminho_diretorio_atual not in sys.path:
        sys.path.insert(0, caminho_diretorio_atual)

    # Busca dentro da pasta e guarda apenas os arquivos que terminam com '.py'
    lista_arquivos_python = [
        nome_arquivo
        for nome_arquivo in os.listdir(caminho_pasta_graficos)
        if nome_arquivo.endswith(".py")
    ]

    # Mostra o título do menu e percorre a lista numerando cada script encontrado
    print("\n--- SELECIONE O SCRIPT ---")
    for indice_opcao, nome_arquivo in enumerate(lista_arquivos_python):
        # Remove o '.py' do final para exibir apenas o nome limpo na tela
        nome_script_sem_extensao = nome_arquivo.replace(".py", "")
        print(f"[{indice_opcao}] {nome_script_sem_extensao}")

    # Pede para o usuário digitar o número e converte o texto digitado em um número inteiro
    opcao_escolhida = int(input("\nDigite o número: "))

    # Verifica se o número digitado está dentro do intervalo válido (de 0 até a quantidade de scripts)
    if 0 <= opcao_escolhida < len(lista_arquivos_python):
        # Pega o arquivo correspondente à escolha e tira o '.py' para saber o nome exato do módulo
        nome_do_modulo = lista_arquivos_python[opcao_escolhida].replace(".py", "")
        print(f"\nRodando: {nome_do_modulo}...\n")

        # Carrega e executa dinamicamente o script escolhido de dentro da pasta Graph_AI_Analizy
        importlib.import_module(f"Graph_AI_Analizy.{nome_do_modulo}")
    else:
        # Se o usuário digitou um número que não existe na lista, avisa que é inválido
        print("Opção inválida!")


# Garante que a função main() só seja executada quando rodamos este arquivo diretamente
if __name__ == "__main__":
    main()
