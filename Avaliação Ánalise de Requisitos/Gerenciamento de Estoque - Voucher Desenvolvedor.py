produtos = []
#PRODUTOS CADASTRADOS
produtos.append(["Televisão", "Televisão de tubo", "1001", 10])
produtos.append(["Notebook", "Laptop da Xuxa", "1002", 30])
produtos.append(["Headset", "Fone com mic estourado", "1003", 50])

#FUNCIONÁRIOS CADASTRADOS
nome_funcionario1 = "JORGE"
cod_funcionario1 = 123456

nome_funcionario2 = "MARIA"
cod_funcionario2 = 654321

while True:
    #MENU
    print("===================================================")
    print("MENU\n")
    print("1. Exibir estoque")
    print("2. Editar quantidade no estoque")    
    print("3. Cadastrar novo produto")
    print("4. Sair do sistema.\n")
    print("===================================================")
    escolha_menu = input("\nEscolha uma opção: ")  
    while escolha_menu not in ["1", "2", "3", "4"]:
        print("Você deve escolher uma das opções disponíveis.")
        print("\nMENU")
        print("1. Exibir estoque")
        print("2. Editar quantidade no estoque")
        print("3. Cadastrar novo produto")
        print("4. Sair do sistema.")
        escolha_menu = input("\nEscolha uma opção: ")
#LISTA DOS PRODUTOS (ESTOQUE ATUAL)
    if escolha_menu == '1':
        print("\nEstoque atual:")
        for i in produtos:
            print("\nCódigo:", i[2])
            print("Nome:", i[0])
            print("Descrição:", i[1])
            print("Quantidade:", i[3])
            if i[3] <= 10:
        #AVISO DE QUANTIDADE
                print("AVISO: Produto próximo de atingir a quantidade mínima do estoque. A quantidade atual é:", i[3]) 
            elif i[3] > 100:
                print("AVISO: Produto próximo de atingir a quantidade máxima do estoque. A quantidade atual é:", i[3]) 
#VALIDAR FUNCIONÁRIO E EDITAR QUANTIDADE DO PRODUTO NO ESTOQUE 
    elif escolha_menu == '2':
        nome_func = str(input("Digite seu nome:"))
        while nome_func != nome_funcionario1 and nome_func != nome_funcionario2 :
            print("Nome inválido")
            nome_func = str(input("Digite seu nome:"))
        cod_func = int(input("Digite o código de acesso:"))
        while cod_func != cod_funcionario1 and cod_func != cod_funcionario2 :
            print("Código de acesso inválido.")
            cod_func = int(input("Digite o código de acesso:"))
        cod_produto = str(input("Digite o código do produto que deseja editar: "))
        for i in produtos:
            if cod_produto == i[2] : 
                operacao = input("Escolha uma das opções: 1 - Entrada de produto | 2 - Saída de produto\n")
                if operacao == '1':
                    entrada = int(input("Digite a quantidade de produtos que estão entrando no estoque: "))
                    if entrada + i[3] > 100 :
                        print("A capacidade máxima para cada produto é de 100 unidades. Disponível em estoque:", i[3])
                    else:
                        i[3] += entrada
                        print("Entrada de produtos registrada com sucesso.")
                elif operacao == '2':
                    saida = int(input("Digite a quantidade de produtos que estão saindo do estoque: "))
                    if saida > i[3]:
                        print("Quantidade insuficiente. Disponível em estoque:", i[3])
                        saida = int(input("Digite novamente a quantidade de produtos que estão saindo do estoque: "))
                    i[3] -= saida
                    print("Saída de produtos registrada com sucesso.")
#CADASTRAR PRODUTO
    elif escolha_menu == '3':
        nome_produto = input("Digite o nome do novo produto: ")
        descricao_produto = input("Digite a descrição do novo produto: ")
        cod_produto = input("Digite o código do novo produto: ")
        for i in produtos:
            if nome_produto == i[0]:
                print("Já existe um produto com esse nome. Por favor, escolha outro nome.")
                nome_produto = input("Digite o nome do novo produto novamente: ")   
            elif cod_produto == i[2]:
                print("Já existe um produto com esse código. Por favor, escolha outro código.")
                cod_produto = input("Digite o código do novo produto novamente: ")     
            else:  
                quant_produto = int(input("Digite a quantidade do novo produto que entrará no estoque: "))
                if quant_produto > 100:
                  print("A capacidade máxima para cada produto é de 100 unidades.")
                  quant_produto = int(input("Digite a quantidade do novo produto que entrará no estoque: "))
            produtos.append([nome_produto, descricao_produto, cod_produto, quant_produto])
            print("Novo produto cadastrado com sucesso.")
    elif escolha_menu == '4':
        print("Até logo.")
        quit
        