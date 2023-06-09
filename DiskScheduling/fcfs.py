import plotGraph


def fcfs_disk_scheduling(st, sp):
    r.clear()
    cop = []
    total_head_movements = 0


    print("Seek time: ", st)
    current_pos= sp
    for s in st:
        distance = abs(s-current_pos)
        total_head_movements += distance
        current_pos = s

    return total_head_movements

r = []
def fcfs_order(st, sp):
    r.append(sp)
    for s in st:
        r.append(s)
    return r


# req = [123, 180, 59, 55, 145, 20, 147, 85, 87]
# init_pos = 70
#
# thm = fcfs_disk_scheduling(req, init_pos)
# print("THM for FCFS/FIFO: ", thm)


