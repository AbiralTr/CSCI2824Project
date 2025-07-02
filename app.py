import tkinter as tk
import time

class TowerOfHanoiGUI:
    def __init__(self, root, num_disks, speed_delay):
        self.root = root

        # User Num Disks + User Set Speed
        self.num_disks = num_disks
        self.speed_delay = speed_delay
        
        # Setting Canvas Size Variables
        self.canvas_width = 600
        self.canvas_height = 400

        # Setting Rods and Disk Variables
        self.rod_x = [150, 300, 450]
        self.rod_height = 300
        self.disk_height = 20
        self.disk_min_width = 30
        self.disk_max_width = 120
        self.colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink", "cyan", "gray"]

        # Canvas Creation
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        # Creating Rods + Disks
        self.rods = [[], [], []]
        self.initialize_disks()
        self.draw_rods()
        self.draw_disks()

        # Start Movement (After 1 decond)
        self.root.after(1000, lambda: self.move_disks(self.num_disks, 0, 2, 1))

    def initialize_disks(self):
        for i in range(1, self.num_disks + 1):
            width = self.disk_max_width - (self.disk_max_width - self.disk_min_width) * (i - 1) // max(1, self.num_disks - 1)
            color = self.colors[(i - 1) % len(self.colors)]
            self.rods[0].append((i, width, color))

    # Function to draw rods
    def draw_rods(self):
        for x in self.rod_x:
            self.canvas.create_line(x, self.canvas_height, x, self.canvas_height - self.rod_height, width=6)

    # Function to draw and update disks
    def draw_disks(self):
        # At the start of every update, delete disks so we can redraw the new image
        self.canvas.delete("disk")
        # For every rod, draw the disks allocated to that rod
        for rod_index, rod in enumerate(self.rods):
            x_center = self.rod_x[rod_index]
            for level, (disk_id, width, color) in enumerate(rod):
                y = self.canvas_height - (level + 1) * self.disk_height
                self.canvas.create_rectangle(
                    x_center - width // 2,
                    y,
                    x_center + width // 2,
                    y + self.disk_height,
                    fill=color,
                    tags="disk"
                )
        self.root.update()

    # Main Recursive Function
    def move_disks(self, n, source, target, auxiliary):
        if n == 1: # Base Case
            self.move_single_disk(source, target)
        else:
            # Move everything except for the bottom disk
            self.move_disks(n - 1, source, auxiliary, target)
            self.move_single_disk(source, target)
            self.move_disks(n - 1, auxiliary, target, source)

    # Atomic Disk Movement
    def move_single_disk(self, from_rod, to_rod):
        if not self.rods[from_rod]:
            return
        disk = self.rods[from_rod].pop()
        self.rods[to_rod].append(disk)
        self.draw_disks()
        time.sleep(self.speed_delay)  # Spacing for Visualization

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tower of Hanoi")
    x = tk.IntVar()
    def get_input():
        global speed
        x.set(entry.get())
        speed = speed_entry.get()

    # Create an Entry widget
    entry_label = tk.Label(root, text="Enter number of disks:")
    entry_label.pack()
    entry = tk.Entry(root)
    entry.pack(pady=5)

    # Create Speed Entry widget
    speed_label = tk.Label(root, text="Enter speed in seconds:")
    speed_label.pack()
    speed_entry = tk.Entry(root)
    speed_entry.pack(pady=5)

    # Create a button to trigger reading the input
    submit_button = tk.Button(root, text="Submit", command=get_input)
    submit_button.pack()
    
    # Getting Disk Count + Speed from input + Casting float val
    root.wait_variable(x)
    num_disks = x.get()
    speed = float(speed)

    # Clean up GUI
    entry.destroy()
    submit_button.destroy()
    speed_entry.destroy()
    entry_label.destroy()
    speed_label.destroy()

    app = TowerOfHanoiGUI(root, num_disks=num_disks, speed_delay=speed)
    root.mainloop()