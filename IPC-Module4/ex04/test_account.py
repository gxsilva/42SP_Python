# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_account.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/28 10:13:02 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/28 12:09:32 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pytest

from account import Account, InvalidDescription, InsufficientBalance
from utils import format_cents

# ----------------- ACCOUNT-------------------
def test_account_initialization() -> None:
	"""Test account initialization values"""
	class_public_id = 100
	class_public_cpf = '733.290.310-50'

	ac = Account(class_public_id, class_public_cpf)

	assert ac.account_id == class_public_id
	assert ac.cpf == class_public_cpf
	assert ac.balance == 0
	assert ac.operation == {}

def test_account_str() -> None:
	"""Test account dunder __str__ class method"""
	class_public_id = 462
	class_public_cpf = '347.357.360-42'

	ac = Account(class_public_id, class_public_cpf)

	str_account_patter = f"Account: {ac.account_id}\nBalance: {format_cents(ac.balance)}"
	assert str(ac) == str_account_patter

# ----------------- ACCOUNT DEPOSIT -------------------

def test_acoount_deposit() -> None:
	"""Test account deposit method behavior"""
	class_public_id = 155
	class_public_cpf = '655.708.040-72'

	ac = Account(class_public_id, class_public_cpf)

	assert ac.balance == 0

	ac.deposit(613, "Selling")
	assert ac.balance == 613
	
	ac.deposit(210, "Selling 2")
	assert ac.balance == 823

def test_account_invalid_deposit() -> None:
	"""Test account invalid value to deposit method"""
	class_public_id = 35
	class_public_cpf = '861.707.750-68'

	ac = Account(class_public_id, class_public_cpf)

	with pytest.raises(ValueError):
		ac.deposit(-100, "Paying the bill")

def test_account_invalid_description_deposit() -> None:
	"""Test account invalid description to deposit method"""
	class_public_id = 62
	class_public_cpf = '685.477.990-10'

	ac = Account(class_public_id, class_public_cpf)

	with pytest.raises(InvalidDescription):
		ac.deposit(122, "")

# ----------------- ACCOUNT WITHDRAW -------------------

def test_acoount_withdraw() -> None:
	"""Test account withdraw method behavior"""
	class_public_id = 255
	class_public_cpf = '873.437.240-70'

	ac = Account(class_public_id, class_public_cpf)

	ac.deposit(613, "Selling")
	assert ac.balance == 613

	ac.withdraw(200, "Paying the bill")
	assert ac.balance == 413


def test_acoount_withdraw_invalid() -> None:
	"""Test account invalid withdraw method"""
	class_public_id = 47
	class_public_cpf = '390.759.870-99'

	ac = Account(class_public_id, class_public_cpf)

	ac.deposit(55, "Deposit")
	with pytest.raises(ValueError):
		ac.withdraw(-100, "Paying the bill")

def test_acoount_withdraw_invalid_description() -> None:
	"""Test account invalid  description withdraw method"""
	class_public_id = 47
	class_public_cpf = '083.182.700-96'

	ac = Account(class_public_id, class_public_cpf)

	ac.deposit(55, "Deposit")
	with pytest.raises(InvalidDescription):
		ac.withdraw(10, "")


def test_acoount_withdraw_invalid_balance() -> None:
	"""Test account invalid withdraw with insufficient balance"""
	class_public_id = 47
	class_public_cpf = '674.294.110-37'

	ac = Account(class_public_id, class_public_cpf)

	ac.deposit(55, "Deposit")
	with pytest.raises(InsufficientBalance):
		ac.withdraw(57, "Paying the bill")
