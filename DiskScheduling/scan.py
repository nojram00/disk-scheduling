

def scan_disk_scheduling(requests, init_pos, max_cylinder):
    new_requests = []

    toadd = [init_pos, max_cylinder]
    for req in requests:
        new_requests.append(req)
    for a in toadd:
        new_requests.append(a)
    requests_copy = new_requests.copy()

    sorted_requests = sorted(requests_copy)

    initial_index = sorted_requests.index(init_pos)


    up = []
    up = sorted(sorted_requests[:initial_index], reverse=True)
    down = []
    down = sorted_requests[initial_index:]

    if init_pos > max_cylinder:
        direction = "up"
    elif init_pos < max_cylinder:
        direction = "down"

    total_head_movement = 0
    up_requests_movement = 0
    down_requests_movement = 0

    if direction == "up":

        for u in up:
            distance = abs(u-init_pos)
            up_requests_movement += distance
            init_pos = u

        for d in down:
            distance = abs(max_cylinder-d)
            down_requests_movement += distance
            max_cylinder = d

        set_new_request(up + down)

    if direction == "down":

        for d in down:
            distance = abs(d-init_pos)
            down_requests_movement += distance
            init_pos = d

        for u in up:
            distance = abs(max_cylinder-u)
            up_requests_movement += distance
            max_cylinder = u

        set_new_request(down + up)

    total_head_movement = up_requests_movement + down_requests_movement
    return total_head_movement

new_req = []
def set_new_request(requests):
    for r in requests:
        new_req.append(r)

def get_new_request():
    return new_req

#[123, 180, 59, 55, 145, 20, 147, 85, 87, 70, 199]
#[20, 55, 59, 70, 85, 87, 123, 145, 147, 180, 199]
#[70, 85, 87, 123, 145, 147, 180, 199]
#[20, 55, 59]
# 20
# 55
# 59
# [70, 85, 87, 123, 145, 147, 180, 199, 59, 55, 20]
# [59, 55, 20, 70, 85, 87, 123, 145, 147, 180, 199]