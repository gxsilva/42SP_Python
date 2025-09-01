# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loader.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/29 09:10:24 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/29 11:53:33 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from pathlib import Path

import sys

import pandas

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Accounts(Base):
    __tablename__ = 'accounts'
    numero = Column(String, primary_key=True)
    titular = Column(String)
    saldo = Column(Float)
    limite = Column(Float)
    data_abertura = Column(String)

# ====================EXCEPTION ERROR CLASS===========================

class FileExtensionError(Exception):
	def __init__(self, error_msg: str = "Invalid file extension. Only .jsonl and .csv files are supported."):
		super().__init__(error_msg)

class FilePermissionError(Exception):
	def __init__(self, error_msg: str = "Invalid file permission. read permission is necessary."):
		super().__init__(error_msg)

# ====================METHODS===========================


# ---------------FILE VALIDATION-----------------------

def file_path_check(file_path: str,) -> str:
		valid_extension: list[str] = [".jsonl", ".csv"]

		try:
			file_fd = Path(file_path)
		except Exception as e:
			raise e
		extension = file_fd.suffix.lower()
		if not extension in valid_extension:
			raise FileExtensionError
		return extension

def file_permission_check(file_path: str) -> bool:
	try:
		with open(file_path, "r", encoding="utf-8"):
			pass
		return True
	except PermissionError:
		raise FilePermissionError(f"Permissão negada: {file_path}")
	except FileNotFoundError:
		raise FilePermissionError(f"Arquivo não encontrado: {file_path}")
	except OSError as e:
		raise FilePermissionError(f"Erro de OS enquanto acessa o arquivo {file_path}: {e}")

# ---------------FILE VALIDATION-----------------------
def parser_information(file_path: str, file_extension: str) -> list[dict]:
    try:
        if file_extension == ".jsonl":
            df = pandas.read_json(file_path, lines=True)
            df = df.astype({ "numero": str, "titular": str, "saldo": float, "limite": float, "data_abertura": str })
        if file_extension == ".csv":
            df = pandas.read_csv(file_path, dtype={ "numero": str, "titular": str, "saldo": float, "limite": float, "data_abertura": str})
    except Exception as e:
        raise e
    return df.to_dict(orient="records")

def main() -> int:
	if len(sys.argv) < 2:
		print("Invalid number of arguments. Supported file types: .csv, .jsonl", file=sys.stderr)
		return 1
	# ====================FILE VALIDATION===========================
	try:
		extension = file_path_check(sys.argv[1])
		file_permission_check(sys.argv[1])
	except (FileExtensionError, FilePermissionError) as e:
		print("Error: {}".format(type(e).__name__))
		return 1

	# ====================FILE PARSER===========================
	try:
		parsed_list = parser_information(sys.argv[1], extension)
	except Exception as e:
		print("Error: {}".format(type(e).__name__))
		return 1
	
	engine = create_engine('sqlite:///rushdatabase.db')

	Base.metadata.create_all(engine)

	Session = sessionmaker(bind=engine)
	session = Session()

	for item in parsed_list:
		conta = session.query(Accounts).filter_by(numero=item['numero']).first()
		if conta:
			conta.titular = item['titular']
			conta.saldo = item['saldo']
			conta.limite = item['limite']
			conta.data_abertura = item['data_abertura']
		else:
			conta = Accounts(**item)
			session.add(conta)
		session.commit()

if __name__ == '__main__':
	sys.exit(main())