def get_direction(sp, ps):
    if sp > ps:
        return "up"
    else:
        return "down"
_s = []
def scan_disk(sp, requests, direction, disk_size):
    _s.clear()
    total_movement = 0
    wews = [0, sp, disk_size]
    serving_order = []
    for w in wews:
        requests.append(w)
    # Sort requests based on their positions
    sorted_requests = sorted(requests)
    print("1 ", sorted_requests[:sp])
    current_position = sp
    # Determine the initial direction
    if direction == "up":
        direction_multiplier = 1
    elif direction == "down":
        direction_multiplier = -1
    else:
        raise ValueError("Invalid direction. Please specify 'up' or 'down'.")

    # print(sorted_requests)
    # Find the index where the current position would fit
    insert_index = 0
    for i in range(len(sorted_requests)):
        if direction_multiplier * sorted_requests[i] >= direction_multiplier * current_position:
            insert_index = i
            break

    # Handle requests in the current direction
    for i in range(insert_index, len(sorted_requests)):
        movement = abs(current_position - sorted_requests[i])
        total_movement += movement
        current_position = sorted_requests[i]
        serving_order.append(sorted_requests[i])

    # Handle requests in the opposite direction
    for i in range(insert_index - 1, -1, -1):
        movement = abs(current_position - sorted_requests[i])
        total_movement += movement
        current_position = sorted_requests[i]
        serving_order.append(sorted_requests[i])


    print("1 ", serving_order[:sp])
    print("2 ", sorted(serving_order[sp:]))

    set_serving_order(serving_order[:sp] + sorted(serving_order[sp:], reverse=True))
    return total_movement


def set_serving_order(serving_order):
    for s in serving_order:
        _s.append(s)

def get_serving_order():
    return _s



# Example usage
# current_pos = 50
# reqs = [98, 183, 37, 122, 14, 124, 65, 67]
# dir = "up"
# disk_size = 200
#
# total_movement, serving_order = scan_disk(current_pos, reqs, dir, disk_size)
#
# print("Total head movement:", total_movement)
# print("Serving order:", serving_order)
