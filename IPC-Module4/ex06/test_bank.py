# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_bank.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/28 15:12:35 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/28 18:30:41 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pytest

from bank import Bank, DuplicateBankId, RequestBankNotFound
from account import InsufficientBalance
from account import Account

#=================CLASS==================
def test_bank_initialization() -> None:
	"""test bank initialization"""
	b = Bank()
	assert b.accounts == []

def test_bank_add_account() -> None:
	"""test add a account in bank"""
	acc1 = Account(1, "946.612.610-54")
	b = Bank()
	b.add_account(acc1)
	assert b.accounts[0] == acc1

#=================METHODS==================

#add_account
def test_bank_add_multi_account() -> None:
	"""test add multiple accounts in bank"""
	acc1 = Account(1, "946.612.610-54")
	acc2 = Account(2, "939.594.310-66")
	acc3 = Account(3, "620.855.850-60")
	acc4 = Account(4, "311.384.660-93")
	acc5 = Account(5, "739.754.600-59")
	b = Bank()
	
	b.add_account(acc1)
	assert b.accounts[0] == acc1

	b.add_account(acc2)
	assert b.accounts[1] == acc2

	b.add_account(acc3)
	assert b.accounts[2] == acc3

	b.add_account(acc4)
	assert b.accounts[3] == acc4

	b.add_account(acc5)
	assert b.accounts[4] == acc5

def test_bank_duplicate_acc_id() -> None:
	"""test add a duplicate account in bank"""
	acc1 = Account(1, "946.612.610-54")
	acc2 = Account(1, "939.594.310-66")

	b = Bank()
	with pytest.raises(DuplicateBankId, match="O Id da conta atual já pertence a uma conta nesse banco"):
		b.add_account(acc1)
		b.add_account(acc2)

#get_acount_cpf
def test_get_account_cpf() -> None:
	"""test search for an account based on cpf"""
	acc1 = Account(1, "946.612.610-54")
	b = Bank()

	b.add_account(acc1)
	request = b.get_account_by_cpf("946.612.610-54")
	assert request == acc1

def test_get_account_cpf_empty() -> None:
	"""test search for an empty account based on cpf"""
	acc1 = Account(1, "946.612.610-54")
	b = Bank()

	b.add_account(acc1)
	with pytest.raises(ValueError, match="CPF Inválido"):
		b.get_account_by_cpf("")

def test_get_account_cpf_failed() -> None:
	"""test search for an account based on cpf and handle the failed"""
	acc1 = Account(1, "946.612.610-54")
	b = Bank()

	b.add_account(acc1)
	with pytest.raises(RequestBankNotFound, match="Requisão de busca por CPF/ID foi inválida"):
		b.get_account_by_cpf("311.384.660-93")

#add_account_id
def test_get_account_id() -> None:
	"""test search for an account based on id"""
	acc1 = Account(1, "946.612.610-54")
	b = Bank()

	b.add_account(acc1)
	with pytest.raises(RequestBankNotFound, match="Requisão de busca por CPF/ID foi inválida"):
		b.get_account_by_id(2)

#transfer

def test_account_transfer() -> None:
	"""test transfer method"""
	acc1_id = 1
	acc2_id = 2

	acc1 = Account(acc1_id, "946.612.610-54")
	acc2 = Account(acc2_id, "311.384.660-93")
	
	acc1.deposit(526300, "Deposit AMT")
	acc2.deposit(65445, "Inherit")

	b = Bank()

	b.add_account(acc1)
	b.add_account(acc2)

	b.transfer(acc1_id, acc2_id, 3000, "Transference")
	assert acc1.balance == 523300
	assert acc2.balance == 68445


def test_transfer_entire_balance() -> None:
	"""test transfer entire bale"""
	acc1_id = 1
	acc2_id = 2

	acc1 = Account(acc1_id, "946.612.610-54")
	acc2 = Account(acc2_id, "311.384.660-93")

	acc1.deposit(10000, "Initial")
	acc2.deposit(1, "Empty")

	b = Bank()
	b.add_account(acc1)
	b.add_account(acc2)

	b.transfer(acc1_id, acc2_id, 10000, "All money")
	assert acc1.balance == 0
	assert acc2.balance == 10001

def test_transfer_duplicat_dst() -> None:
	"""test transfer with duplicate destination account"""
	acc1_id = 1
	acc1 = Account(acc1_id, "946.612.610-54")

	acc1.deposit(65461, "Initial")

	b = Bank()
	b.add_account(acc1)

	with pytest.raises(ValueError, match="Valores de identificador de conta duplicados"):
		b.transfer(acc1_id, acc1_id, 10000, "All money")

def test_transfer_zero_amount() -> None:
	"""test transfer with zero value from an account to another"""
	acc1_id = 1
	acc2_id = 2

	acc1 = Account(acc1_id, "946.612.610-54")
	acc2 = Account(acc2_id, "311.384.660-93")

	acc1.deposit(10000, "Initial")
	acc2.deposit(1, "Empty")

	b = Bank()
	b.add_account(acc1)
	b.add_account(acc2)

	with pytest.raises(ValueError):
		b.transfer(acc1_id, acc2_id, 0, "Valor de transferência inválida")


def test_transfer_negative_amount() -> None:
	"""test transfer negative valuer"""
	acc1_id = 1
	acc2_id = 2

	acc1 = Account(acc1_id, "946.612.610-54")
	acc2 = Account(acc2_id, "311.384.660-93")

	acc1.deposit(10000, "Initial")
	acc2.deposit(1, "Empty")

	b = Bank()
	b.add_account(acc1)
	b.add_account(acc2)

	with pytest.raises(ValueError):
		b.transfer(acc1_id, acc2_id, -250, "Valor de transferência inválida")


def test_transfer_insufficient_funds() -> None:
	"""test transfer with insufficient balance"""
	acc1_id = 1
	acc2_id = 2

	acc1 = Account(acc1_id, "946.612.610-54")
	acc2 = Account(acc2_id, "311.384.660-93")

	acc1.deposit(500, "Initial")
	acc2.deposit(270, "Initial")

	b = Bank()
	b.add_account(acc1)
	b.add_account(acc2)

	with pytest.raises(InsufficientBalance):
		b.transfer(acc1_id, acc2_id, 600, "Valor de transferência inválida")

def test_transfer_from_nonexistent_account() -> None:
	"""test transfer from a non existtent account"""
	acc1_id = 1
	acc2_id = 2

	acc1 = Account(acc1_id, "946.612.610-54")
	acc2 = Account(acc2_id, "311.384.660-93")

	acc1.deposit(500, "Initial")
	acc2.deposit(270, "Initial")

	b = Bank()
	b.add_account(acc1)
	b.add_account(acc2)

	with pytest.raises(RequestBankNotFound, match="Requisão de busca por CPF/ID foi inválida"):
		b.transfer(acc1_id, 3, 600, "ID inválido ou usuário não encontrado")


def test_bank_contains() -> None:
	"""test bank dunder methods __contains__"""
	acc1_id = 1
	acc2_id = 2

	acc1 = Account(acc1_id, "946.612.610-54")
	acc2 = Account(acc2_id, "311.384.660-93")

	acc1.deposit(500, "Initial")
	acc2.deposit(270, "Initial")

	b = Bank()
	b.add_account(acc1)
	b.add_account(acc2)
	assert acc1 in b
	assert 2 in b
	assert "946.612.610-54" in b

def test_bank_len() -> None:
	"""test bank dunder methods __len__"""
	acc1_id = 1
	acc2_id = 2
	acc3_id = 3

	acc1 = Account(acc1_id, "946.612.610-54")
	acc2 = Account(acc2_id, "311.384.660-93")
	acc3 = Account(acc3_id, "020.200.200-41")

	acc1.deposit(500, "Initial")
	acc2.deposit(270, "Initial")

	b = Bank()
	b.add_account(acc1)
	assert len(b) == 1
	b.add_account(acc2)
	assert len(b) == 2
	b.add_account(acc3)
	assert len(b) == 3

def test_bank_getitem() -> None:
	"""test bank dunder methods __getitem__"""
	acc1_id = 1
	acc2_id = 2

	acc1 = Account(acc1_id, "946.612.610-54")
	acc2 = Account(acc2_id, "311.384.660-93")

	acc1.deposit(500, "Initial")
	acc2.deposit(270, "Initial")

	b = Bank()
	b.add_account(acc1)
	b.add_account(acc2)
	assert b[0] == acc1
	assert b[1] == acc2
	with pytest.raises(IndexError):
		assert b[4]