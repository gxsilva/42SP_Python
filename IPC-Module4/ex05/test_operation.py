# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_operation.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/27 18:13:00 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/28 12:57:05 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from operation import Operation, OperationType
import pytest

def test_opeartion_initialization_credit() -> None:
	"""test operation class initialization behavior"""
	o1 = Operation(45, "Buy food")
	assert o1.cents == 45
	assert o1.description == "Buy food"
	assert o1.operation_type == OperationType.CREDIT

def test_opeartion_initialization_debit() -> None:
	"""test operation class initialization with invalid values"""
	o1 = Operation(-15, "Pay bill")
	assert o1.cents == -15
	assert o1.description == "Pay bill"
	assert o1.operation_type == OperationType.DEBIT

def test_operation_format_cents() -> None:
	"""test operation class initialization with invalid values"""
	o1 = Operation(26000, "Buy a gameboy advanced")
	excepted = "[+] R$ 260,00"
	result = str(o1) #to consume __str__ methods
	assert excepted ==result

def teste_operation_invalid_vcents() -> None:
	"""test dunder method __str__ from operation class"""
	with pytest.raises(ValueError):
		Operation(0, "Nothing")
	