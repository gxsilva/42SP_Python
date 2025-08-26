# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    calculator.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/26 14:08:37 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/26 18:05:08 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import Any

def add(x : int, y : int) -> int:
	"""adds two values ​​x and y and returns them"""
	return (x + y)

def subtract(x : int, y : int) -> int:
	"""subtract two values ​​x and y and returns them"""
	return (x - y)

def multiply(x : int, y : int) -> int:
	"""multiply two values ​​x and y and returns them"""
	return (x * y)

def power(base: int, exponent: int) -> Any:
	"""takes the power between x ** y and returns its result"""
	return (base ** exponent)

def divide(x : int, y : int) -> float:
	"""Divide two values ​​x and y and returns them"""
	if y == 0:
		raise ValueError("Cannot divide by zero")
	return (x / y)