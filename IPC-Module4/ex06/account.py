# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    account.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/27 19:42:05 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/28 18:31:28 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils import format_cents

class InsufficientBalance(Exception):
	"""Exception class to insufficiet balance"""
	pass

class InvalidDescription(Exception):
	"""Exception class to invalide operation description"""
	pass
	
class Account:
	"""Class responsible for creating an object with value representation in cents and operations"""
	
	def __init__(self, id: int, cpf: str) -> None:
		"""Parameterized account class constructor"""
		self.account_id = id
		self.cpf = cpf
		self.__balance = 0
		self.__operations: list[str] = []

	def deposit(self, amount: int, description: str) -> None:
		"""performs deposit the value of cents in the object instance"""
		if not description:
			raise InvalidDescription("Descrição de deposito inválida")
		if amount <= 0:
			raise ValueError("Valor deve ser > 0")
		self.__balance += amount
		self.__operations.append(f"{format_cents(self.__balance)} {description}")

	def withdraw(self, amount: int, description: str) -> None:
		"""makes the withdrawal from the account based on the amount of the amount passed"""
		if not description:
			raise InvalidDescription("Descrição de saque inválida")
		if amount <= 0:
			raise ValueError("Valor deve ser > 0")
		if self.__balance - amount < 0:
			raise InsufficientBalance("Saldo insuficiente para saque")
		self.__balance -= amount
		self.__operations.append(f"{format_cents(self.__balance)} {description}")
#		self.__operations[description] = self.__balance

	def statement(self) -> None:
		"""makes a complete printout of all deposit and withdrawal operations with descriptions"""
		for opt in self.__operations:
			print (opt)

	@property
	def balance(self) -> int:
		"""return the __balence attribute"""
		return self.__balance
	
	@property
	def operation(self) -> list[str]:
		"""return the __operation list attribute"""
		return self.__operations

	def __str__(self) -> str:
		"""handles the printable text form of the class instance"""
		formatted_string = f"Account: {self.account_id}\nBalance: {format_cents(self.__balance)}"
		return formatted_string
		
	def __repr__(self) -> str:
		"""handles the text form of printing the class instance in debug mode"""
		formatted_string = (f"Account({self.account_id}, '{self.cpf}')")
		return formatted_string


# class InsufficientBalance(Exception):
# 	"""Eexception class in case of insufficient balance"""
# 	pass

# class InvalidDescription(Exception):
# 	"""exception class in case of invalid description"""
# 	pass
