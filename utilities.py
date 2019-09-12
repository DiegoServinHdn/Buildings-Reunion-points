from Helpers.regex import *
from Helpers.BFS_Algorithm import *


PRINT_PATH_MESSAGE = '{} --> {}[{}] '
REGEX_DICTIONARY = {'building': r'[A-Z]+',
                    'route': r'[-]',
                    'wall': r'[#]',
                    'reunion_point': r'[\d]'
                    }


def find_cords_of_element(Map, element):
    cords_list = []
    for i in range(len(Map)):
        for j in range(len(Map[i])):
            match = search_elements(REGEX_DICTIONARY[element], Map[i][j])
            is_a_element_of_the_search = len(match) > 0
            if is_a_element_of_the_search:
                element_cords = (i, j)
                cords_list.append(element_cords)
            else:
                pass
    return cords_list


def search_closest_reunion_points(MAP, buildings_cords, reunion_points_cords, walls_cords):
    buildings_closest_reunion_points_info = {}
    for building in buildings_cords:
        closest_reunion_point_info_per_building = breadth_first_search(MAP, building, reunion_points_cords, walls_cords)
        building_name = MAP[building[I]][building[J]]
        buildings_closest_reunion_points_info[building_name] = closest_reunion_point_info_per_building
    return buildings_closest_reunion_points_info


def show_closest_reunion_points_path(Map, buildings_info):
    paths = search_paths(buildings_info)
    buildings_names = list(buildings_info.keys())
    for name in buildings_names:
        for path_index in range(len(paths[name])):
            path_reunion_point_cords = buildings_info[name]['closest_to_search_cords'][path_index]
            reunion_point_name = Map[path_reunion_point_cords[I]][path_reunion_point_cords[J]]
            print(PRINT_PATH_MESSAGE.format(name, reunion_point_name, path_reunion_point_cords[DEPTH]))
            print_paths_on_map(Map, paths[name][path_index])


def search_paths(buildings_info):
    paths = {}
    buildings_names = list(buildings_info.keys())
    for name in buildings_names:
        paths_per_building = []
        for closest_cord in buildings_info[name]['closest_to_search_cords']:
            paths_per_building.append(find_path(closest_cord, buildings_info[name]['queue_list']))

        paths[name] = paths_per_building
    return paths


def find_path(start_cord, cord_list):
    cord = start_cord
    path = []
    for steps in range(start_cord[DEPTH]):
        if (cord[I] - 1, cord[J], cord[DEPTH] - 1) in cord_list and (cord[DEPTH] - 1) > 0:
            path.append((cord[I] - 1, cord[J]))
            cord = cord[I] - 1, cord[J], cord[DEPTH] - 1

        elif (cord[I] + 1, cord[J], cord[DEPTH] - 1) in cord_list and (cord[DEPTH] - 1) > 0:
            path.append((cord[I] + 1, cord[J]))
            cord = cord[I] + 1, cord[J], cord[DEPTH] - 1

        elif (cord[I], cord[J] + 1, cord[DEPTH] - 1) in cord_list and (cord[DEPTH] - 1) > 0:
            path.append((cord[I], cord[J] + 1))
            cord = cord[I], cord[J] + 1, cord[DEPTH] - 1

        elif (cord[I], cord[J] - 1, cord[DEPTH] - 1) in cord_list and (cord[DEPTH] - 1) > 0:
            path.append((cord[I], cord[J] - 1))
            cord = cord[I], cord[J] - 1, cord[DEPTH] - 1
    return path


def print_paths_on_map(Map, path):
    map_whit_path = []
    for i in range(len(Map)):
        map_whit_path_i = []
        for j in range(len(Map[i])):
            if (i, j) in path:
                map_whit_path_i.append('0')
            else:
                map_whit_path_i.append(Map[i][j])
        map_whit_path.append(map_whit_path_i)
    print_map(map_whit_path)


def print_map(Map):
    for i in Map:
        print(i)
    print('\n')