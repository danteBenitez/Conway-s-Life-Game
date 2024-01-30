import tkinter as tk
from tkinter import Canvas, Event, ttk, messagebox
from game import ConwayLifeGame

CELL_WIDTH = 30
CELL_HEIGHT = 30
CELL_ACTIVE_COLOR = "#ffff00"
CELL_UNACTIVE_COLOR = "#f0f0f0"

class ConwayRender:
    def __init__(self, conway_game: ConwayLifeGame):
        self.game = conway_game
        self.root = tk.Tk()
        self.frame = ttk.Frame(self.root, width=100, height=100)
        self.frame.grid()
        self.canvas = tk.Canvas(self.frame, background="#f0f0f0")
        self.canvas.grid(row=1, column=1, rowspan=100)
        self.update_fn_id = None

        button = ttk.Button(self.frame, text="Iniciar simulación")
        button.grid(row=10, column=10)
        button.bind("<Button-1>", func=lambda e: self.init_simulation())

        button = ttk.Button(self.frame, text="Cancelar simulación")
        button.grid(row=11, column=10)
        button.bind("<Button-1>", func=lambda e: self.cancel_simulation())
         

    def cancel_simulation(self):
        if self.update_fn_id == None:
            start = messagebox.askyesno(title="No se puede cancelar la simulación porque aún no empezó", \
                                message="¿Quiere iniciar la simulación?")
            if start:
                self.init_simulation()
            return
        self.root.after_cancel(self.update_fn_id)
        self.update_fn_id = None

    def handle_click(self, event):
        col = event.x // CELL_WIDTH
        row = event.y // CELL_HEIGHT
        alive = self.game.get_cell_or_default(row, col)
        self.game.insert_cell(row, col, not alive)
        self.update()

    def update(self):
        self.canvas.bind(sequence="<Button-1>", func=lambda e: self.handle_click(e))
        self.canvas.delete("all")

        for (row_n, row) in enumerate(self.game.cells):
            for (col_n, alive) in enumerate(row):
                x0 = col_n * CELL_WIDTH
                y0 = row_n * CELL_HEIGHT
                x1 = x0 + CELL_WIDTH
                y1 = y0 + CELL_HEIGHT
                if alive:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill=CELL_ACTIVE_COLOR)
                else:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill=CELL_UNACTIVE_COLOR)

    def start(self):
        self.update()
        self.root.mainloop()

    def next_state(self):
        self.game.next_state()
        self.update()
        self.update_fn_id = self.root.after(100, lambda e: self.next_state(), None)

    def init_simulation(self):
        self.root.update()
        self.update_fn_id = self.root.after(100, lambda e: self.next_state(), None)


game = ConwayLifeGame.empty(10, 10)
renderer = ConwayRender(game)
renderer.start()









