# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_operation.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/27 18:13:00 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/27 19:41:32 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from operation import Operation
import pytest

def test_opeartion_initialization_credit() -> None:
	o1 = Operation(45, "Buy food")
	assert o1.cents == 45
	assert o1.description == "Buy food"
	assert o1.operation == "credit"

def test_opeartion_initialization_debit() -> None:
	o1 = Operation(-15, "Pay bill")
	assert o1.cents == -15
	assert o1.description == "Pay bill"
	assert o1.operation == "debit"

def test_operation_format_cents() -> None:
	o1 = Operation(26000, "Buy a gameboy advanced")
	excepted = "[+] R$ 260,00"
	result = str(o1) #to consume __str__ methods
	assert excepted ==result

def teste_operation_invalid_vcents() -> None:
	with pytest.raises(ValueError):
		Operation(0, "Nothing")
	