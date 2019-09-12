# QUEUE UPDATES
VISITED = 2
QUEUED = 1
NO_QUEUED_OR_VISITED = 0
I = 0
J = 1
DEPTH = 2


def breadth_first_search(Map, start_cords, to_search_cords, to_evade_cords):
    depth = 0
    start_cords = add_depth_to_cords(start_cords, depth)
    queue = [start_cords]
    queued_list = []
    visits_and_queue_map = create_visits_and_queue_map(Map)
    search_found = []
    empty_queue = False
    while not empty_queue:
        queue_popped = queue.pop(0)
        if is_the_search(queue_popped, to_search_cords):
            search_found.append(queue_popped)
        else:
            pass
        update_visits_and_queue_map(visits_and_queue_map, queue_popped, VISITED)
        queued_list.append(queue_popped)
        if len(search_found) == 0:
            queue = add_cords_to_queue(Map, visits_and_queue_map, queue_popped, queue, to_evade_cords)
        else:
            remove_deeper_queue(search_found, queue)
            pass

        if len(queue) == 0:
            empty_queue = True
        else:
            pass
        pass

    search_info = {'closest_to_search_cords': [], 'queue_list': queued_list}
    for cords in search_found:
        search_info['closest_to_search_cords'].append(cords)
    return search_info


def create_visits_and_queue_map(Map):
    visits_and_queue_map = []
    for i in range(len(Map)):
        visits_and_queue_map.append([])
        for j in range(len(Map[i])):
            visits_and_queue_map[i].append(NO_QUEUED_OR_VISITED)
    return visits_and_queue_map


def update_visits_and_queue_map(visits_and_queue_map, cords, update):
    visits_and_queue_map[cords[I]][cords[J]] = update


def add_depth_to_cords(cord, depth):
    cord_whit_depth = (cord[0], cord[1], depth)
    return cord_whit_depth


def add_cords_to_queue(Map, visit_and_queue_map, popped, queue, to_evade_cords):
    # for i
    if 0 <= (popped[I] + 1) < len(Map) \
            and visit_and_queue_map[popped[I] + 1][popped[J]] == NO_QUEUED_OR_VISITED \
            and (popped[I] + 1, popped[J]) not in to_evade_cords:
        queue.append((popped[I] + 1, popped[J], popped[DEPTH] + 1))
        visit_and_queue_map[popped[I] + 1][popped[J]] = QUEUED
    else:
        pass
    if 0 <= (popped[I] - 1) < len(Map) \
            and visit_and_queue_map[popped[I] - 1][popped[J]] == NO_QUEUED_OR_VISITED \
            and (popped[I] - 1, popped[J]) not in to_evade_cords:
        queue.append((popped[I] - 1, popped[J], popped[DEPTH] + 1))
        visit_and_queue_map[popped[I] - 1][popped[J]] = QUEUED
    else:
        pass
    if 0 <= (popped[J] + 1) < len(Map[0]) \
            and visit_and_queue_map[popped[I]][popped[J] + 1] == NO_QUEUED_OR_VISITED \
            and (popped[I], popped[J] + 1) not in to_evade_cords:
        queue.append((popped[I], popped[J] + 1, popped[DEPTH] + 1))
        visit_and_queue_map[popped[I]][popped[J] + 1] = QUEUED
    else:
        pass
    if 0 <= (popped[J] - 1) < len(Map[0]) \
            and visit_and_queue_map[popped[I]][popped[J] - 1] == NO_QUEUED_OR_VISITED \
            and (popped[I], popped[J] - 1) not in to_evade_cords:
        queue.append((popped[I], popped[J] - 1, popped[DEPTH] + 1))
        visit_and_queue_map[popped[I]][popped[J] - 1] = QUEUED
    else:
        pass

    return queue


def is_the_search(popped_queue, to_search_cords):
    cords = (popped_queue[I], popped_queue[J])
    if cords in to_search_cords:
        return True
    else:
        return False


def remove_deeper_queue(cords, queue):
    cords_to_remove = []
    first_found_search = cords[0]
    for queued_cord in range(len(queue)):
        if first_found_search[DEPTH] < queue[queued_cord][DEPTH]:
            cords_to_remove.append(queue[queued_cord])
        else:
            pass
    for cords in cords_to_remove:
        queue.remove(cords)

