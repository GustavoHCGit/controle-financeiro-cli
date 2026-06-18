# Controle Financeiro CLI

Um aplicativo de linha de comando (CLI) para controle financeiro pessoal, desenvolvido em Python. Ele permite adicionar transações (receitas e despesas), visualizar o histórico de transações e verificar o saldo atual, utilizando SQLite para armazenamento de dados.

## Tecnologias Utilizadas

*   **Python**: Linguagem de programação principal.
*   **SQLite**: Banco de dados leve e embutido para persistência das transações.

## Funcionalidades

O aplicativo oferece as seguintes opções:

1.  **Adicionar Transação**: Registra uma nova receita ou despesa com descrição, valor e tipo.
2.  **Ver Transações**: Exibe todas as transações registradas, ordenadas por data.
3.  **Ver Saldo**: Calcula e mostra o saldo financeiro atual (receitas - despesas).
4.  **Sair**: Encerra o aplicativo.

## Como Executar o Projeto

Siga os passos abaixo para configurar e executar o aplicativo localmente:

1.  **Clone o repositório** (se ainda não o fez):

    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd controle_financeiro_cli
    ```

2.  **Crie e ative um ambiente virtual** (recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: .\venv\Scripts\activate
    ```

3.  **Execute o script**:

    ```bash
    python main.py
    ```

    O aplicativo será iniciado no terminal, apresentando um menu interativo para as operações financeiras.
