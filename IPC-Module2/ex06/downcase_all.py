# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    downcase_all.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/25 14:56:03 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/25 17:09:22 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def downcase_it(strinChain: str) -> str:
	"""[Function]: convert all uppercase letters in a string to lowercase"""
	return (strinChain.lower())

def main() -> int:
	"""[Function]: performs the program's routine tasks"""
	if len(sys.argv) >= 2:
			for x in range(1, len(sys.argv)):
				print(downcase_it(sys.argv[x]))
			return (0)
	else:
		print (None) #Invlaid input
		return (1) 

if __name__ == '__main__':
	sys.exit(main())