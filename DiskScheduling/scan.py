def scan_disk_scheduling(requests, init_pos, direction, max_cylinder):
    requests_copy = requests.copy()
    toadd = [init_pos, max_cylinder]
    for a in toadd:
        requests_copy.append(a)

    sorted_requests = sorted(requests_copy)
    initial_index = sorted_requests.index(init_pos)
    print(initial_index)

    total_head_movement = 0
    if direction == "up":
        up_requests = sorted_requests[initial_index:]
        down_requests = sorted_requests[:initial_index]
        up_requests_movement = 0
        down_requests_movement = 0

        for u in up_requests:
            distance = abs(u-init_pos)
            up_requests_movement += distance
            #print(distance)
            init_pos = u

        sorted_down = sorted(down_requests, reverse=True)
        for d in sorted_down:
            distance = abs(max_cylinder-d)
            down_requests_movement += distance
            max_cylinder = d

    total_head_movement = up_requests_movement + down_requests_movement
    return total_head_movement


#[123, 180, 59, 55, 145, 20, 147, 85, 87, 70, 199]
#[20, 55, 59, 70, 85, 87, 123, 145, 147, 180, 199]
#[70, 85, 87, 123, 145, 147, 180, 199]
#[20, 55, 59]
# 20
# 55
# 59