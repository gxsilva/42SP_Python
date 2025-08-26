# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    functions_everywhere.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/25 15:19:49 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/26 09:27:19 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def shrink(stringChain: str) -> str:
    """[Function]: shrink the string size to 8 characters"""
    return stringChain[0:8]

def enlarge(strincChain: str) -> str:
    """[Function]: function responsible for increasing the size of the string with letters 'Z' up to the size of 8 characters"""
    return (strincChain.ljust(8, 'Z'))

def main() -> int:
    """[Function]: performs the program's routine tasks"""
    if len(sys.argv) >= 2:
        for x in range(1, len(sys.argv)):
            if len(sys.argv[x]) > 8:
                print(shrink(sys.argv[x]))
            elif len(sys.argv[x]) < 8:
                print(enlarge(sys.argv[x]))
            else:
                print(sys.argv[x])
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())

# f"{stringChain:{'Z'}<{(len(stringChain)) + (8 - len(stringChain))}}"
