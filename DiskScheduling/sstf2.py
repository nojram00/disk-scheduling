
new_requests = []
def sstf_disk_algorithm(requests, initial_position):
    req_copy = requests.copy()
    current_pos = initial_position
    total_head_movement = 0

    while req_copy:
        min_distance = float('inf')
        next_req = None

        for request in req_copy:
            distance = abs(request-current_pos)
            if distance < min_distance:
                min_distance = distance
                next_req = request

        new_requests.append(next_req)
        total_head_movement += min_distance
        current_pos = next_req
        req_copy.remove(next_req)

    return total_head_movement

def return_new_requests():
    return new_requests

#129 + 179