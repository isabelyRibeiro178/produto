def main():
    produtos = []

    while True:
        print("\n=== SISTEMA DE PRODUTOS ===")
        print("(1) Adicionar produtos")
        print("(2) Listar produtos (Inativo)")
        print("(3) Remover produtos (Inativo)")
        print("(4) Sair (Inativo)")

        opcao = input("Escolha uma opção: ").strip()

        # 1 - ADICIONAR (A única ativa)
        if opcao == "1":
            nome = input("Digite o nome do produto: ").strip()
            if not nome:
                print("Erro: nome não pode ser vazio.")
                continue
            
            if nome in produtos:
                print(f"'{nome}' já existe na lista.")
            else:
                produtos.append(nome)
                print(f"Produto '{nome}' adicionado com sucesso!")

        # TODAS AS OUTRAS OPÇÕES SÃO TRATADAS COMO INVÁLIDAS
        else:
            print("Opção inválida! No momento, apenas a opção 1 está disponível.")

if __name__ == "__main__":
    main()
