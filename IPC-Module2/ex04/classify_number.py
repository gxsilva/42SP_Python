# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    classify_number.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/25 13:50:33 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/25 15:39:17 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def is_positive(x : int) -> bool:
	"""[Function]: Verify if X is a positive (true) or zero/negative value(false)"""
	return (x > 0)

def main() -> int:
	"""[Function]: performs the program's routine tasks"""
	if len(sys.argv) == 2:
		print(is_positive(int(sys.argv[1])))
	return (0)
		
if __name__ == '__main__':
	sys.exit(main())