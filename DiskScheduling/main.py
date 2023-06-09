import clook
import look
import cscan
import sstf2
import fcfs
import scan
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure as fig
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np

# from look import Direction
from enum import Enum

tk = Tk()
title = tk.title("Disk Scheduling Algorithms")
frame = Frame(tk)
tk.geometry("500x500")
frame.pack()


def plot(req):
    array_y = []
    for r in range(len(req)):
        array_y.insert(r, r)

    xpoints = np.array(array_y)
    ypoints = np.array(req)
    a = f.add_subplot(111)
    a.plot(xpoints, ypoints, marker='o')

    canvas.draw()
    canvas.get_tk_widget().pack()

f = fig(figsize=(5, 5),
            dpi=100)
canvas = FigureCanvasTkAgg(f, master=tk)
toolbar = NavigationToolbar2Tk(canvas, tk)
toolbar.update()
canvas.get_tk_widget().pack()


def clearPlot():
    req.clear()
    init_pos = 0
    max_value = 0
    canvas.get_tk_widget().pack_forget()
    f.axes.clear()
    f.clf()
    text.config(text=" ")

text = Label(frame, text=" ", padx=5, pady=5, font="black")
text.pack()

def fcfs_plot():
    clearPlot()
    req_string = input_req_box.get(1.0, "end-1c")
    ps = ps_text.get(1.0, "end-1c")
    req_split = req_string.split(',')
    print(req_split)
    for r in req_split:
        req.append(int(r))
    print(req)
    init_pos = input_initial_pos.get(1.0, "end-1c")
    fcfsthm = fcfs.fcfs_disk_scheduling(req, int(init_pos)  )
    plot(fcfs.fcfs_order(req, int(init_pos)))
    fcfsText = repr(fcfsthm)
    print(fcfsText)
    text.config(text="Total Head Movement for FCFS: " + fcfsText)

def sstf_plot():
    r = []
    r.clear()
    clearPlot()
    req_string = input_req_box.get(1.0, "end-1c")
    req_split = req_string.split(',')
    for r in req_split:
        req.append(int(r))
    init_pos = input_initial_pos.get(1.0, "end-1c")
    sstfthm = sstf2.sstf_disk_algorithm(req, int(init_pos))
    r = sstf2.get_new_request()
    plot(r)
    #print(r)
    sstfText = repr(sstfthm)
    print(sstfText)
    text.config(text="Total Head Movement for SSTF: " + sstfText)

def scan_plot():
    clearPlot()
    req_string = input_req_box.get(1.0, "end-1c")
    req_char_array = req_string.split(',')
    for r in req_char_array:
        req.append(int(r))
    sp = input_initial_pos.get(1.0, "end-1c")
    ps = ps_text.get(1.0, "end-1c")
    disk_size = input_max_value.get(1.0, "end-1c")
    scanthm = scan.scan_disk(convert_to_integer(sp), req, scan.get_direction(convert_to_integer(sp), convert_to_integer(ps)), convert_to_integer(disk_size))
    plot(scan.get_serving_order())
    scanText = repr(scanthm)
    print(scanText)
    text.config(text="Total Head Movement for Scan: " + scanText)

def cscan_plot():
    clearPlot()
    req_string = input_req_box.get(1.0, "end-1c")
    req_char_array = req_string.split(',')
    for r in req_char_array:
        req.append(convert_to_integer(r))
    sp = input_initial_pos.get(1.0, "end-1c")
    ps = ps_text.get(1.0, "end-1c")
    disk_size = input_max_value.get(1.0, "end-1c")
    cscanthm = cscan.cscan(int(sp), req, cscan.get_direction(int(sp), int(ps)), convert_to_integer(disk_size))
    cscanText = repr(cscanthm)
    print(cscan.st_order(int(sp), int(ps), int(disk_size)))
    plot(cscan.st_order(int(sp), int(ps), int(disk_size)))
    text.config(text = "Total Head Movement for C-Scan: " + cscanText)

def c_look():
    clearPlot()
    req_string = input_req_box.get(1.0, "end-1c")
    req_char_array = req_string.split(',')
    for r in req_char_array:
        req.append(convert_to_integer(r))
    sp = input_initial_pos.get(1.0, "end-1c")
    ps = ps_text.get(1.0, "end-1c")
    disk_size = input_max_value.get(1.0, "end-1c")
    ss, sc = clook.CLOOK(req, convert_to_integer(sp))
    clook_total = sc
    clook_total_text = repr(clook_total)
    print(ss)
    plot(ss)
    text.config(text = "Total Head Movement for C-Look: " + clook_total_text)




def convert_to_integer(string):
    if string.strip():  # Check if the string is not empty or contains only whitespace
        try:
            return int(string)
        except ValueError:
            print("Invalid literal for int():", string)
    else:
        print("Empty string cannot be converted to int.")


def _look():
    clearPlot()
    req_string = input_req_box.get(1.0, "end-1c")
    req_char_array = req_string.split(',')
    for r in req_char_array:
        req.append(int(r))
    init_pos = input_initial_pos.get(1.0, "end-1c")
    max_value = input_max_value.get(1.0, "end-1c")
    vt, total = look.look_disk_scheduling(req, int(init_pos))
    # plot()
    look_text = repr(total)
    plot(vt)
    text.config(text="Total Head Movement for Scan: " + look_text)


req = []
init_pos = 0
max_value = 0
# direction = " "


# a = [123, 180, 59, 55, 145, 20, 147, 85, 87]
# b = 70
# print("hatdog = ",csan.LOOK(a, b, "right"))

# print(clook.CLOOK(a, b, 9))
# print("clook seek time: ", clook.get_seek_time())
# print(clook.get_seek_time())

req_box_label = Label(frame, text="Enter Seek time Here:")
input_req_box = Text(frame, height=2, width=25)
req_box_label.pack(side=LEFT, fill=X)
input_req_box.pack(side=LEFT, fill=X)
initial_pos_label = Label(frame, text="Enter Initial Position Here:")
input_initial_pos = Text(frame, height=2, width=10)
initial_pos_label.pack(side=LEFT, fill=X)
input_initial_pos.pack(side=LEFT, fill=X)
ps_label = Label(frame, text="Enter the Previously served: ")
ps_text = Text(frame, height=2, width=10)
ps_label.pack(side=LEFT, fill=X)
ps_text.pack(side=LEFT, fill=X)
max_value_label = Label(frame, text="Enter Disk Size: ")
input_max_value = Text(frame, height=2, width=10)
max_value_label.pack(side=LEFT, fill=X)
input_max_value.pack(side=LEFT, fill=X)

#buttons:

fcfc_plot_btn = Button(master=tk,
                       command=fcfs_plot,
                       height=2,
                       width=15,
                       text="FCFS",
                       pady=10)
fcfc_plot_btn.pack(side=LEFT, fill=X)


sstf_plot_btn = Button(master=tk,
                       command=sstf_plot,
                       height=2,
                       width=15,
                       text="SSTF",
                       pady=10)
sstf_plot_btn.pack(side=LEFT, fill=X)



scan_plot_btn = Button(master=tk,
                       command=scan_plot,
                       height=2,
                       width=15,
                       text="Scan",
                       pady=10)
scan_plot_btn.pack(side=LEFT, fill=X)

look_plot_btn = Button(master=tk,
                       command=_look,
                       height=2,
                       width=15,
                       text="Look",
                       pady=10)
look_plot_btn.pack(side=LEFT, fill=X)

cscan_plot_button = Button(master=tk,
                           command=cscan_plot,
                           height=2,
                           width=15,
                           text="C-scan",
                           pady=10)

cscan_plot_button.pack(side=LEFT, fill=X)

clook_btn = Button(master=tk,
                   command=c_look,
                   height=2,
                   width=15,
                   text="C-Look",
                   pady=10)
clook_btn.pack(side=LEFT, fill=X)

clearBtn = Button(master=tk,
                  command=clearPlot,
                  height=2,
                  width=10,
                  text="Reset",
                  pady=10)
clearBtn.pack(side=LEFT, fill=X)



newline = Label(frame, text=" ")
newline.pack(side=TOP, fill=X)

clearPlot()



tk.mainloop()
#
#
#
#
#
#
#
# tk.geometry("500x500")
# frame.pack()
#
# import AllDiskSched
# import wewwwwwws