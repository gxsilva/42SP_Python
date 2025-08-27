# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operation.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/27 17:58:30 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/27 19:40:12 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils import format_cents

class Operation:
	def __init__(self, cents: int, description: str) -> None:
		if cents == 0:
			raise ValueError
		self.cents = cents
		self.description = description
		self.operation = "credit" if cents > 0 else "debit"
	
	def __str__(self) -> str:
		return format_cents(self.cents)
	
	def __repr__(self) -> str:
		return f"Operation(cents={self.cents}, operation_type='{self.operation}', description={self.description})"
	