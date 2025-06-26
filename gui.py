import tkinter as tk

class TowerOfHanoiGUI:
    def __init__(self, root, num_disks):
        self.root = root
        self.num_disks = num_disks
        self.canvas_width = 600
        self.canvas_height = 400
        self.rod_x = [150, 300, 450]
        self.rod_height = 300
        self.disk_height = 20
        self.disk_min_width = 30
        self.disk_max_width = 120
        self.colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink", "cyan", "gray"]

        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        self.rods = [[], [], []]
        self.initialize_disks()
        self.draw_rods()
        self.draw_disks()

    def initialize_disks(self):
        for i in range(self.num_disks, 0, -1):
            width = self.disk_max_width - (self.disk_max_width - self.disk_min_width) * (i - 1) // (self.num_disks - 1)
            color = self.colors[(i - 1) % len(self.colors)]
            self.rods[0].append((i, width, color))


    def draw_rods(self):
        for x in self.rod_x:
            self.canvas.create_line(x, self.canvas_height, x, self.canvas_height - self.rod_height, width=6)

    def draw_disks(self):
        self.canvas.delete("disk")
        for rod_index, rod in enumerate(self.rods):
            x_center = self.rod_x[rod_index]
            for level, (disk_id, width, color) in enumerate(reversed(rod)):
                y = self.canvas_height - (level + 1) * self.disk_height
                self.canvas.create_rectangle(
                    x_center - width // 2,
                    y,
                    x_center + width // 2,
                    y + self.disk_height,
                    fill=color,
                    tags="disk"
                )

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tower of Hanoi")
    app = TowerOfHanoiGUI(root, num_disks=6)
    root.mainloop()
