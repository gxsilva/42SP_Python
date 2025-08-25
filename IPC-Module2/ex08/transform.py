# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    transform.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/25 17:44:48 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/25 18:14:54 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def is_even(x: int) -> bool:
    """[Function]: Checks if a number is odd"""
    return x % 2 == 0


def square_opt(x: int) -> int:
    """[Function]: Square a number"""
    return x**2


def square_even_numbers(intArray: list[int]) -> list[int]:
    """[Function]: captures the even values ​​and raises it to the exponent 2"""
    even_list = list(filter(is_even, intArray))
    square_list = list(map(square_opt, even_list))
    return square_list


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
