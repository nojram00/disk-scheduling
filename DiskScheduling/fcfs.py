import plotGraph

def fcfs_disk_scheduling(requests, initial_pos):
    total_head_movements = 0

    current_pos = initial_pos
    for request in requests:
        distance = abs(request-current_pos)
        total_head_movements += distance
        current_pos = request
    return total_head_movements


# req = [123, 180, 59, 55, 145, 20, 147, 85, 87]
# init_pos = 70
#
# thm = fcfs_disk_scheduling(req, init_pos)
# print("THM for FCFS/FIFO: ", thm)


