import tkinter as tk

class Application(tk.Frame):

    def __init__(self, window=None):
        super().__init__(window)
        self.window = window
        self.update_time = ''
        self.running = False
        self.godziny = 0
        self.minuty = 0
        self.sekundy = 0
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.stopwatch_label = tk.Label(self, text='00:00:00', font=('Arial', 80), fg="red", bg="black")
        self.stopwatch_label.pack()
        self.start_button = tk.Button(self, text='start', height=3, width=7, font=('Arial', 20), fg="red", bg="black", command=self.start)
        self.start_button.pack(side=tk.LEFT)
        self.pause_button = tk.Button(self, text='stop', height=3, width=7, font=('Arial', 20), fg="red", bg="black", command=self.pause)
        self.pause_button.pack(side=tk.LEFT)
        self.reset_button = tk.Button(self, text='reset', height=3, width=7, font=('Arial', 20), fg="red", bg="black", command=self.reset)
        self.reset_button.pack(side=tk.LEFT)
        self.quit_button = tk.Button(self, text='wyjdz', height=3, width=7, font=('Arial', 20), fg="red", bg="black", command=self.window.quit)
        self.quit_button.pack(side=tk.LEFT)
        self.name_label = tk.Label(self, text="Stoper by Bartosz Sołtyk", height=4, font=("arial", 18), fg="red", bg="black")
        self.name_label.pack()
        self.window.title('Stoper')

    def start(self):
        if not self.running:
            self.stopwatch_label.after(1000)
            self.update()
            self.running = True

    def pause(self):
        if self.running:
            self.stopwatch_label.after_cancel(self.update_time)
            self.running = False

    def reset(self):
        if self.running:
            self.stopwatch_label.after_cancel(self.update_time)
            self.running = False
        self.godziny, self.minuty, self.sekundy = 0, 0, 0
        self.stopwatch_label.config(text='00:00:00')

    def update(self):
        self.sekundy += 1
        if self.sekundy == 60:
            self.minuty += 1
            self.seconds = 0
        if self.minuty == 60:
            self.godziny += 1
            self.minutes = 0
        hours_string = f'{self.godziny}' if self.godziny > 9 else f'0{self.godziny}'
        minutes_string = f'{self.minuty}' if self.minuty > 9 else f'0{self.minuty}'
        seconds_string = f'{self.sekundy}' if self.sekundy > 9 else f'0{self.sekundy}'
        self.stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
        self.update_time = self.stopwatch_label.after(1000, self.update)

root = tk.Tk()
app = Application(window=root)
app.mainloop()