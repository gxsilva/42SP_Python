# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    coordinates.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/31 23:04:32 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/31 23:21:34 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class Coordinates:
	def __init__(self, lat: float, long: float) -> None:
		self.lat = lat
		self.long = long
	
	def __str__(self) -> str:
		return f"Coordinates(lat={self.lat}, long={self.long})"
	
	def __eq__(self, other) -> bool:
		if isinstance(other, Coordinates):
			return self.lat == other.lat and self.long == other.long
		return False
