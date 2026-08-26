import main


def test_transactions_and_balance(monkeypatch, tmp_path, capsys):
    monkeypatch.chdir(tmp_path)

    main.create_table()
    main.add_transaction("Salário", 2500.0, "receita")
    main.add_transaction("Aluguer", 800.0, "despesa")

    assert main.get_balance() == 1700.0
    output = capsys.readouterr().out
    assert "Saldo Atual: R$ 1700.00" in output

    main.view_transactions()
    output = capsys.readouterr().out
    assert "Salário" in output
    assert "Aluguer" in output
