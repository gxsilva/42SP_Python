# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/27 16:08:14 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/27 19:39:55 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def format_cents(value: int) -> str:
	"""Converts an integer (or float | not recommended) value to a formatted money representation"""
	formatted_money = ""
	sign = "[+]" if value > 0 else "[-]"
	value_f = abs(value) / 100
	formatted_money = "{} R$ {:,.2f}".format(sign, value_f).replace(",", "X").replace(".", ",").replace("X", ".")
	return formatted_money

# , -> mile separator
# formatted_money = sign + " R$ {:,.2f}".format(value)
