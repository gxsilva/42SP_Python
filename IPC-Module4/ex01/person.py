# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    person.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/27 09:13:31 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/27 16:06:06 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Person:
	"""A class uses da to instantiate an object with name, age and a method to increase the age by 1"""
	def __init__(self, name: str, age: int) -> None:
		self.name = name
		self.age = age
	
	def birthday(self) -> None:
		self.age = self.age + 1
