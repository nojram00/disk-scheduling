import sstf2
import fcfs
import scan

req = [123, 180, 59, 55, 145, 20, 147, 85, 87]
init_pos = 70

fcfsthm = fcfs.fcfs_disk_scheduling(req, init_pos)
print("THM for FCFS: ", fcfsthm)

sstfthm = sstf2.sstf_disk_algorithm(req, init_pos)
print("THM for SSTF: ", sstfthm)

max_value = 199
direction = "up"
scanthm = scan.scan_disk_scheduling(req, init_pos, direction, max_value)
print("THM for scan: ", scanthm)

