# Gerenciamento de Inventário - AgilStore
Este é um sistema simples de gerenciamento de inventário, que permite adicionar, listar, atualizar, excluir e buscar produtos. A aplicação utiliza Python e armazena os dados em um arquivo JSON local.

## Funcionalidades
- Adicionar um novo produto ao inventário.
- Listar todos os produtos cadastrados.
- Atualizar informações de um produto (nome, categoria, quantidade e preço).
- Excluir um produto do inventário.
- Buscar produtos por ID ou nome.
- Persistência dos dados em um arquivo JSON.

## Tecnologias Utilizadas
- Python 3.9: Linguagem de programação principal.
- JSON: Formato de armazenamento de dados.
- UUID: Geração de identificadores únicos para os produtos.

## Pré-requisitos
Para executar o sistema localmente, você precisa ter o seguinte instalado:
Python 3.9

## Como executar a aplicação
1. Clone este repositório (ou copie o código).
2. Abra o terminal (ou prompt de comando) e navegue até o diretório onde o arquivo está salvo.
3. Execute o comando abaixo para iniciar a aplicação:

```bash
python gerenciamento_inventario.py
```

4. O menu principal será exibido no terminal, com as opções abaixo. Escolha a opção desejada digitando o número correspondente e siga as instruções exibidas no terminal.

=== Gerenciamento de Produtos - Loja AgilStore ===
1. Adicionar Produto
2. Listar Produtos
3. Atualizar Produto
4. Excluir Produto
5. Buscar Produto
6. Sair


## Estrutura do Código
- `carregar_inventario()`: Carrega os dados do inventário a partir do arquivo JSON.
- `salvar_inventario()`: Salva as alterações feitas no inventário no arquivo JSON.
- `adicionar_produto()`: Adiciona um novo produto ao inventário.
- `listar_produto()`: Exibe todos os produtos cadastrados no inventário.
- `atualizar_produto()`: Permite a atualização de informações de um produto existente.
- `excluir_produto()`: Remove um produto do inventário.
- `procurar_produto()`: Realiza buscas de produtos por ID ou nome.
- `main()`: Função principal que exibe o menu e gerencia a interação com o usuário.

## Observações
- Os dados são armazenados no arquivo inventario.json, que será criado automaticamente no diretório raiz ao executar a aplicação pela primeira vez.
- Cada produto cadastrado recebe um ID único gerado automaticamente.

## Melhorias Futuras
- Criar uma interface gráfica para facilitar a interação do usuário.
