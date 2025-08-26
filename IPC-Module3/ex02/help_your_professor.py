# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    help_your_professor.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsilva-x <lsilva-x@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/26 12:33:13 by lsilva-x          #+#    #+#              #
#    Updated: 2025/08/26 17:33:44 by lsilva-x         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def average(students_set: dict[str, int]) -> float:
	"""[Function]: calculate the average grade of a student's dictionary with name and grade"""
	average_grade = 0.0
	if not students_set:
			return average_grade
	if not isinstance(students_set, dict):
			return average_grade
	for _name, grade in students_set.items():
		if grade is None or int(grade) < 0:
			return 0
		average_grade += grade
	average_grade = average_grade / len(students_set)
	return average_grade