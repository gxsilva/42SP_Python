# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    convert.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/26 12:44:08 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/26 14:07:05 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main() -> int:
	"""Received a value as a string and tried to cast it to a float with error handling"""
	cast_float = 0.0
	if len(sys.argv) >= 2:
		try:
			cast_float = float(sys.argv[1])
		except ValueError:
			print("conversion impossible")
			return 1
		print (cast_float)
	return 0

if __name__ == '__main__':
	sys.exit(main())