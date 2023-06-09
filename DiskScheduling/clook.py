
# size = 8
# disk_size = 200

_seek_time = []

def CLOOK(arr, head):
    _seek_time.clear()
    seek_count = 0
    distance = 0
    cur_track = 0

    left = []
    right = []

    seek_sequence = []
    for i in range(len(arr)):
        if (arr[i] < head):
            left.append(arr[i])
        if (arr[i] > head):
            right.append(arr[i])

    left.sort()
    right.sort()


    for i in right:
        cur_track = i

        seek_sequence.append(cur_track)

        distance = abs(cur_track - head)

        seek_count += distance

        head = cur_track

    left.append(head)
    # seek_count += abs(head - left[0])
    print(seek_count)
    # head = left[0]

    for i in range(len(left)):
        cur_track = left[i]

        seek_sequence.append(cur_track)

        distance = abs(cur_track - head)

        seek_count += distance

        head = cur_track

    # print("Total number of seek operations =",
    #       seek_count)
    # print("Seek Sequence is")

    for i in range(len(seek_sequence)):
        print(seek_sequence[i])
        # set_seek_time(seek_sequence[i])
    return seek_sequence, seek_count


# arr = [176, 79, 34, 60,
#        92, 11, 41, 114]
# head = 50
#
# print("Initial position of head:", head)

# a = CLOOK(arr, head, size)
# print(a)


# def cscan(disk_,size, initial_position, disks_position):
#     head = initial_position
#
#     #sort increasing
#     for pos in disks_position:
#         if(pos >= head):
