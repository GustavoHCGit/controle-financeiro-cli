import sqlite3

def get_db_connection():
    conn = sqlite3.connect("finance.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            type TEXT NOT NULL,
            date TEXT DEFAULT CURRENT_DATE
        )
    """)
    conn.commit()
    conn.close()

def add_transaction(description, amount, type):
    conn = get_db_connection()
    conn.execute("INSERT INTO transactions (description, amount, type) VALUES (?, ?, ?)",
                   (description, amount, type))
    conn.commit()
    conn.close()
    print("Transação adicionada com sucesso!")

def view_transactions():
    conn = get_db_connection()
    transactions = conn.execute("SELECT * FROM transactions ORDER BY date DESC").fetchall()
    conn.close()
    if not transactions:
        print("Nenhuma transação encontrada.")
        return
    print("\n--- Transações ---")
    for t in transactions:
        print(f"ID: {t["id"]}, Descrição: {t["description"]}, Valor: {t["amount"]:.2f}, Tipo: {t["type"]}, Data: {t["date"]}")
    print("------------------")

def get_balance():
    conn = get_db_connection()
    income = conn.execute("SELECT SUM(amount) FROM transactions WHERE type = 'receita'").fetchone()[0] or 0
    expense = conn.execute("SELECT SUM(amount) FROM transactions WHERE type = 'despesa'").fetchone()[0] or 0
    conn.close()
    balance = income - expense
    print(f"\nSaldo Atual: R$ {balance:.2f}")
    return balance

def main():
    create_table()
    while True:
        print("\nMenu:")
        print("1. Adicionar Transação")
        print("2. Ver Transações")
        print("3. Ver Saldo")
        print("4. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            description = input("Descrição: ")
            amount = float(input("Valor: "))
            type = input("Tipo (receita/despesa): ").lower()
            if type not in ['receita', 'despesa']:
                print("Tipo inválido. Use 'receita' ou 'despesa'.")
                continue
            add_transaction(description, amount, type)
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            get_balance()
        elif choice == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
