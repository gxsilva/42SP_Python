# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_person.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/27 09:13:44 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/27 16:07:33 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from person import Person

def test_person_initialization() -> None:
	"""Test the class Person instance and their attributes"""
	p = Person("Alice", 30)
	assert p.name == "Alice"
	assert p.age == 30

def test_person_birthday_method() -> None:
	"""Test the class Person method birthday"""
	p = Person("Marcus", 15)
	assert p.name == "Marcus"
	assert p.age == 15
	p.birthday()
	assert p.age == 16
	p.birthday()
	p.birthday()
	assert p.age == 18
