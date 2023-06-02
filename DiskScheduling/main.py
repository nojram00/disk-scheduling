import sstf2
import fcfs
import scan
from tkinter import *
from matplotlib.figure import Figure as fig
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np

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
    canvas.get_tk_widget().pack_forget()
    f.axes.clear()
    f.clf()
    text.config(text=" ")

text = Label(frame, text=" ", padx=5, pady=5, font="black")
text.pack()

def fcfs_plot():
    clearPlot()
    plot(req)
    fcfsText = repr(fcfsthm)
    text.config(text="Total Head Movement for FCFS: " + fcfsText)

def sstf_plot():
    clearPlot()
    plot(sstf2.return_new_requests())
    sstfText = repr(sstfthm)
    text.config(text="Total Head Movement for SSTF: " + sstfText)

def scan_plot():
    clearPlot()
    plot(scan.get_new_request())
    scanText = repr(scanthm)
    text.config(text="Total Head Movement for Scan: " + scanText)


req = [123, 180, 59, 55, 145, 20, 147, 85, 87]
init_pos = 70
fcfsthm = fcfs.fcfs_disk_scheduling(req, init_pos)

clearPlot()

fcfc_plot_btn = Button(master=tk,
                       command=fcfs_plot,
                       height=2,
                       width=15,
                       text="Plot FCFS Graph")
fcfc_plot_btn.pack()

sstfthm = sstf2.sstf_disk_algorithm(req, init_pos)
sstf_plot_btn = Button(master=tk,
                       command=sstf_plot,
                       height=2,
                       width=15,
                       text="Plot SSTF Graph")
sstf_plot_btn.pack()


max_value = 199
direction = "up"
scanthm = scan.scan_disk_scheduling(req, init_pos, max_value)
scan_plot_btn = Button(master=tk,
                       command=scan_plot,
                       height=2,
                       width=15,
                       text="Plot Scan Graph")
scan_plot_btn.pack()


clearBtn = Button(master=tk,
                  command=clearPlot,
                  height=2,
                  width=10,
                  text="Reset")
clearBtn.pack()

tk.mainloop()





