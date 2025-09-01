# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_coordinates.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/31 23:15:31 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/31 23:27:03 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from coordinates import Coordinates

def test_coordinates_initialize() -> None:
	coor = Coordinates(40.7128, -74.0060)
	assert coor.lat == 40.7128
	assert coor.long == -74.0060

def test_coordinates_print() -> None:
	coor = Coordinates(40.7128, -74.0060)
	assert str(coor) == "Coordinates(lat=40.7128, long=-74.006)"

def test_coordinates_eq() -> None:
	coord1 = Coordinates(40.7128, -74.0060)
	coord2 = Coordinates(34.0522, -118.2437)
	coord3 = Coordinates(40.7128, -74.0060)

	assert (coord1 == coord2) == False
	assert (coord1 == coord3) == True