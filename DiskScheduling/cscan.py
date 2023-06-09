def get_direction(sp, ps):
    if sp > ps:
        return "left"
    else:
        return "right"
def cscan(start, requests, direction, disk_size):
    r.clear()
    ss.clear()
    new_st.clear()
    # Setting the initial position
    current_position = start

    # Sorting the requests
    sorted_requests = sorted(requests)

    # Adding the endpoints to the sorted requests
    sorted_requests.append(disk_size)
    sorted_requests.append(0)

    # Checking the direction
    if direction == "left":
        sorted_requests.reverse()

    total_head_movement = 0
    previous_request = start

    # Scanning the requests
    for request in sorted_requests:
        # Calculating the head movement
        head_movement = abs(request - previous_request)
        total_head_movement += head_movement


        # Moving to the next request
        r.append(request)
        previous_request = request

    return total_head_movement

r = []
ss = []
new_st = []
def st_order(sp, ps, size):
    r.append(sp)
    ss = sorted(r)
    ss.append(ps)
    print(ss)
    i = ss.index(sp)
    m = ss.index(size)
    z = ss.index(0)


    if get_direction(sp, ps) == "left":

        up = ss[i:m]
        print("up", up)
        down = ss[m:]
        print("down", down)

        down.append(0)
        dd = sorted(down)
        up_up = sorted(up)
        for u in up_up:
            dd.append(u)

        final_ss = []
        for d in dd:
            if d not in final_ss:
                final_ss.append(d)
        return final_ss

    if get_direction(sp, ps) == "right":

        up = ss[i:m]
        print("up", up)
        down = ss[m:]
        print("down", down)

        down_down = sorted(down, reverse=True)
        down_down.append(0)
        for d in down_down:
            up.append(d)

        final_ss = []
        for u in up:
            if u not in final_ss:
                final_ss.append(u)
        return final_ss




# 11, 20, 34, 41, 60, 79, 92, 114, 176, 10