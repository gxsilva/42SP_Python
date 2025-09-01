from pathlib import Path
from loader import file_path_check, FileExtensionError, FilePermissionError, file_permission_check
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from loader import Accounts, Base
import pytest

@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_insert_account(session):
     nova_conta = Accounts(numero=1, titular="teste", saldo=100.0, limite=200, data_abertura="2025-01-01")
     session.add(nova_conta)
     session.commit()
     conta_banco = session.query(Accounts).filter_by(numero=1).first()
     assert conta_banco is not None
     assert conta_banco.titular == "teste"
     assert conta_banco.saldo == 100.0
     assert conta_banco.limite == 200
     assert conta_banco.data_abertura == "2025-01-01"

@pytest.fixture
def real_db_session():
    engine = create_engine('sqlite:///rushdatabase.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_nao_ha_numeros_duplicados(real_db_session):
    from sqlalchemy import func

    duplicadas = (
        real_db_session.query(Accounts.numero, func.count(Accounts.numero))
        .group_by(Accounts.numero)
        .having(func.count(Accounts.numero) > 1)
        .all()
    )

    assert not duplicadas

@pytest.mark.parametrize(("valid_file", "expected"), [ ("teste.csv", ".csv"), ("dados.jsonl", ".jsonl") ] )
def test_file_path_check_valid(valid_file: str, expected: str):
    assert file_path_check(valid_file) == expected

@pytest.mark.parametrize("invalid_file", ["teste.txt", "dados.json", "arquivo.xlsx"])
def test_file_path_check_invalid(invalid_file):
    with pytest.raises(FileExtensionError):
        file_path_check(invalid_file)

@pytest.mark.parametrize("file_non_existent", [Path('Home/RUSH02/DADOS.csv')])

def test_fileNotFoundError(file_non_existent):
    with pytest.raises(FilePermissionError):
        file_permission_check(file_non_existent)

@pytest.mark.parametrize("file_non_permitted", [Path("Home/RUSH02/rush/forbidden.csv")])
def test_Permission_Error(file_non_permitted):
    with pytest.raises(FilePermissionError):
        file_permission_check(file_non_permitted)