# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    transform.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/25 17:44:48 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/26 09:46:04 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def square_even_numbers(intArray: list[int]) -> list[int]:
    """[Function]: captures the even values ​​and raises it to the exponent 2"""
    square_even_list = [x**2 for x in intArray if x % 2 == 0]
    return (square_even_list)


def main() -> int:
    """[Function]: performs the program's routine tasks"""
    if len(sys.argv) >= 2:
        int_list = list(map(int, sys.argv[1].split(" ")))
        print(square_even_numbers(int_list))
    else:
        return 1
    return 0


if __name__ == "__main__":
    main()
