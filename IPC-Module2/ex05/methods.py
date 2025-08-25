# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    methods.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/25 14:36:08 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/25 15:39:22 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def string_prop(string_chain: str) -> None:
	"""[Function]: Uses the methods of str objects"""
	print("São maíusculas? ", string_chain.isupper())
	print("È númerico? ", string_chain.isnumeric())
	print("È ascii? ", string_chain.isascii())
	print("È alfanumérico? ", string_chain.isalnum())


def main() -> int:
	"""[Function]: performs the program's routine tasks"""
	if len(sys.argv) == 2:
		string_prop(sys.argv[1])
	return (0)

if __name__ == '__main__':
	sys.exit(main())
