import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import ttk

class DiskSchedulerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Disk Scheduling Algorithms")
        master.geometry("600x400")

        # Input frame
        self.input_frame = tk.Frame(master)
        self.input_frame.pack(pady=10)

        self.start_label = tk.Label(self.input_frame, text="Initial Head Position:")
        self.start_label.grid(row=0, column=0, padx=5)

        self.start_entry = tk.Entry(self.input_frame)
        self.start_entry.grid(row=0, column=1, padx=5)

        self.requests_label = tk.Label(self.input_frame, text="Request Queue (comma-separated):")
        self.requests_label.grid(row=1, column=0, padx=5)

        self.requests_entry = tk.Entry(self.input_frame)
        self.requests_entry.grid(row=1, column=1, padx=5)

        self.submit_button = tk.Button(self.input_frame, text="Submit", command=self.run_scheduling_algorithms)
        self.submit_button.grid(row=2, column=0, columnspan=2, pady=5)

        # Graph frame
        self.graph_frame = tk.Frame(master)
        self.graph_frame.pack(pady=10)

        self.graph_canvas = plt.figure(figsize=(5, 3), dpi=100)
        # self.graph_canvas.draw()
        self.graph_canvas_canvas = self.graph_canvas.canvas
        self.graph_canvas_canvas.pack()

    def run_scheduling_algorithms(self):
        initial_head = int(self.start_entry.get())
        requests = list(map(int, self.requests_entry.get().split(',')))

        # Disk Scheduling Algorithms
        fcfs = FCFS(initial_head, requests)
        sstf = SSTF(initial_head, requests)
        scan = SCAN(initial_head, requests)
        cscan = C_SCAN(initial_head, requests)
        look = LOOK(initial_head, requests)
        clook = C_LOOK(initial_head, requests)

        algorithms = [fcfs, sstf, scan, cscan, look, clook]
        labels = ['FCFS', 'SSTF', 'SCAN', 'C-SCAN', 'LOOK', 'C-LOOK']

        # Calculate seek time for each algorithm
        seek_times = []
        for algorithm in algorithms:
            algorithm.calculate_seek_time()
            seek_times.append(algorithm.seek_time)

        # Display line graphs
        self.display_graphs(labels, algorithms)

    def display_graphs(self, labels, algorithms):
        self.graph_canvas.clear()

        for label, algorithm in zip(labels, algorithms):
            plt.plot(algorithm.processes, label=label)

        plt.xlabel('Process Order')
        plt.ylabel('Process')
        plt.title('Disk Scheduling Algorithms')
        plt.legend()

        self.graph_canvas_canvas.draw()

# Disk Scheduling Algorithms

class FCFS:
    def __init__(self, initial_head, requests):
        self.initial_head = initial_head
        self.requests = requests
        self.seek_time = None
        self.processes = []

    def calculate_seek_time(self):
        seek_time = 0
        curr_head = self.initial_head

        for request in self.requests:
            seek_time += abs(request - curr_head)
            curr_head = request
            self.processes.append(request)

        self.seek_time = seek_time

class SSTF:
    def __init__(self, initial_head, requests):
        self.initial_head = initial_head
        self.requests = requests
        self.seek_time = None
        self.processes = []

    def calculate_seek_time(self):
        seek_time = 0
        curr_head = self.initial_head
        remaining_requests = self.requests.copy()

        while remaining_requests:
            next_request = min(remaining_requests, key=lambda x: abs(x - curr_head))
            seek_time += abs(next_request - curr_head)
            curr_head = next_request
            remaining_requests.remove(next_request)
            self.processes.append(next_request)

        self.seek_time = seek_time

class SCAN:
    def __init__(self, initial_head, requests):
        self.initial_head = initial_head
        self.requests = requests
        self.seek_time = None
        self.processes = []

    def calculate_seek_time(self):
        seek_time = 0
        curr_head = self.initial_head
        upper_requests = [request for request in self.requests if request >= curr_head]
        lower_requests = [request for request in self.requests if request < curr_head]

        upper_requests.sort()
        lower_requests.sort(reverse=True)

        seek_time += abs(curr_head - upper_requests[0])
        seek_time += abs(upper_requests[-1] - lower_requests[0])

        for i in range(len(upper_requests) - 1):
            seek_time += abs(upper_requests[i] - upper_requests[i + 1])

        for i in range(len(lower_requests) - 1):
            seek_time += abs(lower_requests[i] - lower_requests[i + 1])

        self.seek_time = seek_time
        self.processes = upper_requests + lower_requests

class C_SCAN:
    def __init__(self, initial_head, requests):
        self.initial_head = initial_head
        self.requests = requests
        self.seek_time = None
        self.processes = []

    def calculate_seek_time(self):
        seek_time = 0
        curr_head = self.initial_head
        upper_requests = [request for request in self.requests if request >= curr_head]
        lower_requests = [request for request in self.requests if request < curr_head]

        upper_requests.sort()
        lower_requests.sort()

        seek_time += abs(curr_head - upper_requests[0])
        seek_time += abs(upper_requests[-1] - lower_requests[0])
        seek_time += abs(lower_requests[-1] - upper_requests[0])

        for i in range(len(upper_requests) - 1):
            seek_time += abs(upper_requests[i] - upper_requests[i + 1])

        for i in range(len(lower_requests) - 1):
            seek_time += abs(lower_requests[i] - lower_requests[i + 1])

        self.seek_time = seek_time
        self.processes = upper_requests + lower_requests

class LOOK:
    def __init__(self, initial_head, requests):
        self.initial_head = initial_head
        self.requests = requests
        self.seek_time = None
        self.processes = []

    def calculate_seek_time(self):
        seek_time = 0
        curr_head = self.initial_head
        upper_requests = [request for request in self.requests if request >= curr_head]
        lower_requests = [request for request in self.requests if request < curr_head]

        upper_requests.sort()
        lower_requests.sort(reverse=True)

        seek_time += abs(curr_head - upper_requests[0])
        seek_time += abs(upper_requests[-1] - lower_requests[0])

        for i in range(len(upper_requests) - 1):
            seek_time += abs(upper_requests[i] - upper_requests[i + 1])

        for i in range(len(lower_requests) - 1):
            seek_time += abs(lower_requests[i] - lower_requests[i + 1])

        self.seek_time = seek_time
        self.processes = upper_requests + lower_requests

class C_LOOK:
    def __init__(self, initial_head, requests):
        self.initial_head = initial_head
        self.requests = requests
        self.seek_time = None
        self.processes = []

    def calculate_seek_time(self):
        seek_time = 0
        curr_head = self.initial_head
        upper_requests = [request for request in self.requests if request >= curr_head]
        lower_requests = [request for request in self.requests if request < curr_head]

        upper_requests.sort()
        lower_requests.sort()

        seek_time += abs(curr_head - upper_requests[0])
        seek_time += abs(upper_requests[-1] - lower_requests[0])
        seek_time += abs(lower_requests[-1] - upper_requests[0])

        for i in range(len(upper_requests) - 1):
            seek_time += abs(upper_requests[i] - upper_requests[i + 1])

        for i in range(len(lower_requests) - 1):
            seek_time += abs(lower_requests[i] - lower_requests[i + 1])

        self.seek_time = seek_time
        self.processes = upper_requests + lower_requests

root = tk.Tk()
scheduler_gui = DiskSchedulerGUI(root)
root.mainloop()
