import uuid # módulo que permite criar ID's únicos
import json

FILE_NAME = "inventario.json"

# Carregar inventário do arquivo JSON
def carregar_inventario():
  try:
    with open(FILE_NAME, "r") as file:
      return json.load(file)
  except FileNotFoundError:
    return []
  except json.JSONDecodeError:
    print("Erro ao ler o arquivo JSON. Criando inventário vazio.")
    return []

# Salvar inventário no arquivo JSON
def salvar_inventario():
  with open(FILE_NAME, "w") as file:
    json.dump(inventario, file, indent=4)
  print("Inventário salvo com sucesso!")

# Iniciar inventário ao carregar o programa
inventario = carregar_inventario()

# Função para gerar id único
def gerar_id_unico():
  return str(uuid.uuid4())[:8] #id com apenas 8 caracteres

# Adicionar produto
def adicionar_produto():
  nome_produto = input("Insira o nome do produto: ")
  categoria = input("Insira a categoria do produto: ")
  quantidade_estoque = int(input("Insira a quantidade do produto em estoque: "))
  preco = float(input("Insira o preço unitário: "))
  produto = {
      "id": gerar_id_unico(),
      "nome_produto": nome_produto,
      "categoria": categoria,
      "quantidade": quantidade_estoque,
      "preco": preco
  }
  inventario.append(produto)
  salvar_inventario()
  print("Produto adicionado com sucesso!")

# Listar produto
def listar_produto():
  if not inventario:
    print("Invetário vazio.")
    return
  print("\nID       | Nome           | Categoria      | Quantidade | Preço")
  print("-" * 80)

  for produto in inventario:
    print(f"{produto['id']}  |   {produto['nome_produto'][:15]:<15}  |  {produto['categoria'][:15]:<15}  |  {produto['quantidade']:<10}  |  R$ {produto['preco']:.2f}")


# Atualizar produto
def atualizar_produto():
  produto_id = input("Insira o ID do produto a ser atualizado: ")
  for produto in inventario:
    if produto["id"] == produto_id:
      print("\n Produto encontrado: ")
      print(f"Nome do Produto: {produto['nome_produto']}, Categoria: {produto['categoria']}, Quantidade: {produto['quantidade']}, Preço: R${produto['preco']:.2f}")
      print("Escolha o campo a ser atualizado (digite o número correspondente):\n")
      print("1. Nome")
      print("2. Categoria")
      print("3. Quantidade")
      print("4. Preço")
      print("5. Cancelar")

      escolha = input("Digite a opção desejada: ")
      if escolha == "1":
        novo_nome_produto = input("Digite o novo nome do produto: ").strip()
        if novo_nome_produto:
          produto['nome_produto'] = novo_nome_produto
          salvar_inventario()
          print("Nome atualizado com sucesso!")
          
        else:
          print("A informação não pode ficar vazia!")

      elif escolha == "2":
          nova_categoria = input("Digite a nova categoria: ").strip()
          if nova_categoria:
            produto['categoria'] = nova_categoria
            salvar_inventario()
            print("Categoria atualizada com sucesso!")
            
          else:
            print("A informação não pode ficar vazia!")

      elif escolha == "3":
        try:
          nova_quantidade = int(input("Digite a nova quantidade: "))
          if nova_quantidade >= 0:
            produto['quantidade'] = nova_quantidade
            salvar_inventario()
            print("Quantidade atualizada com sucesso!")
            
          else:
            print("A quantidade não pode ser negativa")
        except ValueError:
          print("Valor inválido. Digite um número inteiro.") #lidando com possíveis erros

      elif escolha == "4":
        try:
          novo_preco = float(input("Digite o novo preço: "))
          if novo_preco >=0:
            produto['preco'] = novo_preco
            salvar_inventario()
            print("Preço atualizado com sucesso!")
            
          else:
            print("O preço não pode ser negativo.")
        except ValueError:
          print("Valor inválido. Digite com número decimal válido.")

      elif escolha == "5":
        print("Atualização cancelada.")

      else:
        print("Escolha inválida. Nenhuma alteração foi feita.")

      return

  print("Produto não encontrado.")


# Excluir produto
def excluir_produto():
  produto_id = input("Digite o ID do produto que deseja excluir: ")
  for produto in inventario:
    if produto['id'] == produto_id:
      print("\nProduto encontrado: ")
      print(f"Nome do Produto: {produto['nome_produto']}, Categoria: {produto['categoria']}, Quantidade: {produto['quantidade']}, Preço: R${produto['preco']:.2f}")
      confirma = input("Tem certeza que deseja excluir esse produto? (s/n) ").strip()
      if confirma.lower() == "s":
        inventario.remove(produto)
        salvar_inventario()
        print("Produto excluído com sucesso!")
      else:
        print("Ação cancelada.")

      return

  print("Produto não encontrado.")

# Buscar produto
def procurar_produto():
  busca_termo = input("Insira o ID ou o nome do produto: ").strip().lower()

  # Busca pelo ID
  resultado = [produto for produto in inventario if produto['id'] == busca_termo]

  # Busca pelo nome
  if not resultado:
    resultado = [produto for produto in inventario if busca_termo in produto['nome_produto'].lower()]

  if resultado:
    print("\nResultado da busca: ")
    print("\nID       | Nome           | Categoria      | Quantidade | Preço")
    print("-" * 80)
    for produto in resultado:
      print(f"{produto['id']}  |   {produto['nome_produto'][:15]:<15}  |  {produto['categoria'][:15]:<15}  |  {produto['quantidade']:<10}  |  R$ {produto['preco']:.2f}")

  else:
    print("Nenhum produto encontrado.")

# Função principal
def main():
  while True:
    print("\n=== Gerenciamento de Produtos - Loja AgilStore ===")
    print("1. Adicionar Produto")
    print("2. Listar Produtos")
    print("3. Atualizar Produto")
    print("4. Excluir Produto")
    print("5. Buscar Produto")
    print("6. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
      adicionar_produto()
    elif escolha == "2":
      listar_produto()
    elif escolha == "3":
      atualizar_produto()
    elif escolha == "4":
      excluir_produto()
    elif escolha == "5":
      procurar_produto()
    elif escolha == "6":
      print("Saindo do programa. Até mais!")
      break
    else:
      print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
  main()
