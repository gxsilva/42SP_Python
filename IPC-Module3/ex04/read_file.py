# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    read_file.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/26 13:24:26 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/26 16:39:30 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main() -> int:
	"""open and read a file with possible error handling"""
	if len(sys.argv) >= 2:
		file_path = sys.argv[1]
		try:
			with open(file_path, 'r', encoding="utf-8") as fd:
				print("{}".format(fd.read()), end='')
		except FileNotFoundError:
			print("Erro: Arquivo não encontrado.")
			return 1
		except IsADirectoryError:
			print("Erro: O argumento enviado é um diretório.")
			return 1
		except Exception as e:
			print("Erro inesperado: {}".format(type(e).__name__))
			return 1
		return 0
	else:
		print("The program expects input of a path to a file.")
		return 1

if __name__ == '__main__':
	sys.exit(main())