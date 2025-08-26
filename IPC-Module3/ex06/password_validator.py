# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    password_validator.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/26 16:30:54 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/26 17:54:13 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string

def has_lower_char(strinchain: str) -> bool:
	"""checks if the string contains an lowercase letter"""
	for char in strinchain:
		if char.islower():
			return True
	return False

def has_upper_char(strinchain: str) -> bool:
	"""checks if the string contains an uppercase letter"""
	for char in strinchain:
		if char.isupper():
			return True
	return False

def has_digit_char(strinchain: str) -> bool:
	"""checks if the string contains an digit"""
	for char in strinchain:
		if char.isdigit():
			return True
	return False

def has_special_char(strinchain: str) -> bool:
	"""checks if the string contains any special character"""
	special_char = string.punctuation # --> !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

	for char in strinchain:
		for special in special_char:
			if char == special:
				return True
	return False

def has_white_space_char(strinchain: str) -> bool:
	"""checks if the string contains an white space"""
	for char in strinchain:
		if char == " ":
			return True
	return False

def is_valid_password(strinChain: str) -> bool:
	"""verification chain for password validation"""
	if not strinChain:
		return False
	if len(strinChain) < 8 or len (strinChain) > 18:
		return False
	if not has_lower_char(strinChain):
		return False
	if not has_upper_char(strinChain):
		return False
	if not has_digit_char(strinChain):
		return False
	if not has_special_char(strinChain):
		return False
	if has_white_space_char(strinChain):
		return False
	return True