
new_requests = []
def sstf_disk_algorithm(requests, initial_position):
    set_new_request(initial_position)
    new_requests.clear()
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


        set_new_request(next_req)
        total_head_movement += min_distance
        current_pos = next_req
        req_copy.remove(next_req)

    return total_head_movement

def set_new_request(request):
    new_requests.append(request)

def get_new_request():
    return new_requests

#129 + 179