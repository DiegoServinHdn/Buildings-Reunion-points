"""

    Author: Diego Servin Hamden
    Date: 8/15/2019

"""


from utilities import *


# CONFIG PARAMS
MAP = [['A', '-', '-', '-', '3', '#', '-'],
       ['-', '-', '#', '-', '-', '-', '1'],
       ['-', '#', 'B', '-', '-', '#', '-'],
       ['-', '#', '#', '#', '-', '-', '#'],
       ['2', '-', '-', '#', '#', '-', '#'],
       ['-', '-', '-', '-', '-', '-', 'C']]


# SCRIPT
def main():
    buildings_cords = find_cords_of_element(MAP, 'building')
    reunion_points_cords = find_cords_of_element(MAP, 'reunion_point')
    walls_cords = find_cords_of_element(MAP, 'wall')
    to_evade = (walls_cords + buildings_cords)
    buildings_closest_reunion_points_info = search_closest_reunion_points(MAP, buildings_cords, reunion_points_cords,
                                                                          to_evade)
    show_closest_reunion_points_path(MAP, buildings_closest_reunion_points_info)


# MAIN CALL
main()
