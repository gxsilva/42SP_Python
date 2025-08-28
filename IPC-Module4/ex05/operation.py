# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operation.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/27 17:58:30 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/28 12:54:32 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from enum import Enum

from utils import format_cents

class OperationType(Enum):
	CREDIT = "credit"
	DEBIT = "debit"

class Operation:
	"""creates an object that handles deposits and withdrawals and debits and credits in an account quoted in cents"""
	
	def __init__(self, cents: int, description: str) -> None:
		"""Parameterized operation class construcotr"""
		if cents == 0:
			raise ValueError
		self.cents = cents
		self.description = description
		if cents > 0:
			self.operation_type = OperationType.CREDIT
		else:
			self.operation_type = OperationType.DEBIT
	
	def __str__(self) -> str:
		"""handles the printable text form of the class instance"""
		return format_cents(self.cents)
	
	def __repr__(self) -> str:
		"""handles the text form of printing the class instance in debug mode"""
		return f"Operation(cents={self.cents}, operation_type='{self.operation_type}', description={self.description})"
	