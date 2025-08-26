# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    namebook.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/26 10:05:31 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/26 17:25:41 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def format_names(dict_names: dict[str, str]) -> list[str]:
	"""[Function]: transform a dictionary of first and last names into a list of capitalized full names"""
	full_name_list: list[str] = []
	if not dict_names:
		return full_name_list
	for first_name, surname in dict_names.items():
		format_string = first_name.capitalize() + " " +surname.capitalize()
		full_name_list.append(format_string)
	return full_name_list
