# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    bank.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/28 13:01:58 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/29 21:07:32 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from account import Account, InvalidDescription, InsufficientBalance
from typing import Optional

class RequestBankNotFound(Exception):
	"""Exception class for cases where a request is not found"""
	def __init__(self, message:str = "Requisão de busca por CPF/ID foi inválida") -> None:
		super().__init__(message)

class DuplicateBankId(Exception):
	"""Exception class for when we have duplicate id's"""
	def __init__(self, message:str = "O Id da conta atual já pertence a uma conta nesse banco") -> None:
		super().__init__(message)

class Bank():
	"""Bank class responsible for managing accounts and transfers"""
	def __init__(self) -> None:
		"""Default constructor class"""
		self.__accounts: list[Account] = []
	
	def add_account(self, account: Account) -> None:
		"""Method responsible for adding a bank account"""
		if not account:
			raise ValueError("Banco Inválido")
		
		if self._id_duplicate_verify(account.account_id):
			raise(DuplicateBankId())
		self.__accounts.append(account)
	
	def get_account_by_cpf(self, cpf: str) -> Account:
		"""method responsible for search an account based on cpf"""
		if not cpf:
			raise ValueError("CPF Inválido")
		account_req = next((account for account in self.__accounts if account.cpf == cpf), None)
		if not account_req:
			raise RequestBankNotFound()
		return account_req
	
	def get_account_by_id(self, account_id: int) -> Account:
		"""method responsible for search an account based on id"""
		account_req = next((account for account in self.__accounts if account.account_id == account_id), None)
		if not account_req:
			raise RequestBankNotFound()
		return account_req
	
	def transfer(self, source_account: int, destination_account: int, value: int, description: str) -> None:
		"""method responsible for transfer cents from a source account to a dest account"""
		if value <= 0:
			raise ValueError("Valor de transferência inválida")
		if not description:
			raise InvalidDescription("Descrição de transferência inválida")
		if source_account == destination_account:
			raise ValueError("Valores de identificador de conta duplicados")
		try:
			src_acc = self.get_account_by_id(source_account)
			dst_acc = self.get_account_by_id(destination_account)
			src_acc.withdraw(value, description)
			dst_acc.deposit(value, description)
		except (RequestBankNotFound, InsufficientBalance) as e:
			raise e

	def _id_duplicate_verify (self, id: int) -> bool:
		"""Auxiliary function used to check for duplicate IDs"""
		has_dup_id = next((True for account in self.accounts if account.account_id == id), False)
		return has_dup_id
	
	@property
	def accounts(self) -> list[Account]:
		"""Getter to take Accounts__accounts list"""
		return self.__accounts
	
	def __contains__(self, account: object) -> bool:
		"""Dunder function responsible for overloading the in operator"""
		if isinstance(account, Account):
				return(any(acc == account for acc in self.__accounts))
		if isinstance(account, int):
				return(any(acc.account_id == account for acc in self.__accounts))
		if isinstance(account, str):
				return(any(acc.cpf == account for acc in self.__accounts))
		return False
	
	def __len__(self) -> int:
		"""Dunder function responsible for return the amount of account in bank"""
		return (len(self.__accounts))
	
	def __getitem__(self, index: int) -> Optional[Account]:
		"""Dunder function responsible for overloading de pst[index] syntax"""
		if index >= len(self.__accounts):
			raise IndexError
		return self.__accounts[index]