# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_password_validator.py                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/26 16:30:53 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/26 18:03:40 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pytest
import password_validator as passval

@pytest.mark.parametrize("input, result",
[
	("6mu(H6j.)\2N\\", True),
	("87Pd]kJKy=|6-", True),
	("<:RJ^3vqWkU", True),
	("j|D$Mx*SI29ct81v", True),
	("u1i@B%Pc(N.b", True),
	("6EgaTMI->,#", True),
	("y{(7#lIk(^d%M.t", True),
	("+o@q5p6/X", True),
	("9SDzJ/rb<Ub5/", True),
	("dZU5<sT4aY", True),
	("ABCDEFGH1@", False),
	("abcd1234", False),
	("abcdefg@", False),
	("ABCDEF12", False),
	("Ab1 ", False),
	("12345678", False),
	("Abcdefgh", False),
	("Abc!@#$%", False)
])

def test_is_valid_password(input: str, result: bool) -> None:
	"""test the password validation chain"""
	assert passval.is_valid_password(input) == result
