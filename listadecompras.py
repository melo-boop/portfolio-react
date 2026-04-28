compras = []

while True:
    print("selecione uma opção abaixo: \n" \
          "1 - adicionar um item a lista \n" \
          "2 - remorer um item da lista\n" \
          "3 - limpar a lista \n" \
          "4 - mostrar a lista \n" \
          "5 - sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1: 
       produto = str(input("digite o item a ser adicionado a lista de compras:"))
       compras.append(produto)
       print("produto adicionado a lista!!")
    elif opcao == 2:
      produto = str(input("digite o item que deseja remover:"))
      compras.remove(produto)
      print("produto removido!!")
    elif opcao == 3:
      compras.clear()
      print("lista limpa!!")
    elif opcao == 4:
      print(compras)
    elif opcao == 5:
      print("obrigado por usar o programa :D")
      break
    else:
      print("digite uma opção valida")        
