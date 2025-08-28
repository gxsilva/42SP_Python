# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_utils.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/27 16:08:15 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/28 18:31:00 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils import format_cents

def test_format_cents_positive_int() -> None:
	"""Teste format_cents function with positive integer values"""
	input = 7200
	excepted = "[+] R$ 72,00"
	result = format_cents(input)
	assert result == excepted

def test_format_cents_negative_int() -> None:
	"""Teste format_cents function with negative integer values"""
	input = -9800
	excepted = "[-] R$ 98,00"
	result = format_cents(input)
	assert result == excepted

def test_format_cents_negative_float() -> None:
	"""Teste format_cents function with negative float values"""
	input = -63500
	excepted = "[-] R$ 635,00"
	result = format_cents(input)
	assert result == excepted

def test_format_cents_large_positive_int() -> None:
	"""Teste format_cents function with large positive integer values"""
	input = 2034623500
	excepted = "[+] R$ 20.346.235,00"
	result = format_cents(input)
	assert result == excepted

def test_format_cents_large_negative_int() -> None:
	"""Teste format_cents function with large negative integer values"""
	input = -6843521500
	excepted = "[-] R$ 68.435.215,00"
	result = format_cents(input)
	assert result == excepted

def test_format_cents_underscore() -> None:
	"""Teste format_cents function with large negative integer values"""
	input = 11_222_00
	excepted = "[+] R$ 11.222,00"
	result = format_cents(input)
	assert result == excepted


# def test_format_cents_large_positive_float() -> None:
# 	"""Teste format_cents function with large postive float values"""
# 	input = 203462.35
# 	excepted = "[+] R$ 203.462,35"
# 	result = format_cents(input)
# 	assert result == excepted

# def test_format_cents_large_negative_float() -> None:
# 	"""Teste format_cents function with large negative float values"""
# 	input = -68435.25
# 	excepted = "[-] R$ 68.435,25"
# 	result = format_cents(input)
# 	assert result == excepted

# def test_format_cents_positive_float() -> None:
# 	"""Teste format_cents function with positive float values"""
# 	input = 416.48
# 	excepted = "[+] R$ 416,48"
# 	result = format_cents(input)
# 	assert result == excepted