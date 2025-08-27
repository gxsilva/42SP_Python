# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    account.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/27 19:42:05 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/27 20:03:23 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string

class InsufficientBalance(Exception):
	pass

class Account:
	def __init__(self, id: int, cpf: str) -> None:
		self.account_id = id
		self.cpf = cpf
		self.__balance = 0
		self.__operations = list[str]

	def deposit(self, amount: int, description: string) -> None:
		if not description:
			return None
		if amount <= 0:
			print ("Valor deve ser > 0")
			raise ValueError
		self.__operations.append(description)
		self.__balance += amount

	def withdraw(self, amount: int, description: string) -> None:
		if not description:
			return None
		if amount <= 0:
			print ("Valor deve ser > 0")
			raise ValueError
		if self.__balance - amount < 0:
			print ("Insufficient balance to withdraw")
			raise InsufficientBalance
		self.__operations.append(description)
		self.__balance -= amount
		
		
	def statement(self):
		print (self.__operations)

	def __str__(self):
	
	def __repr__(self):

