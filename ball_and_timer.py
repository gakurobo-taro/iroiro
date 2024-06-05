import tkinter as tk
from tkinter import ttk
import time
import random

class BallGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.base_font_size = 24
        self.create_widgets()
        self.pack(fill=tk.BOTH, expand=True)
        self.generate_balls()
        self.timer_running = False
        self.master.bind("<space>", self.start_stop_timer)
        self.master.bind("<Return>", self.record_lap_time)
        self.master.bind("<g>", self.regenerate_balls)
        self.master.bind("<c>", self.countdown)

    def create_widgets(self):
        # ボール表示用のキャンバス
        self.ball_canvas = tk.Canvas(self, bg='white', highlightthickness=0)
        self.ball_canvas.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # ボタンフレーム
        button_frame = tk.Frame(self)
        button_frame.grid(row=0, column=1, padx=20, pady=20, sticky="ns")

        # ボタン
        self.start_button = tk.Button(button_frame, text="START", command=self.start_timer, font=("Helvetica", int(self.base_font_size * 0.8)))
        self.start_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.stop_button = tk.Button(button_frame, text="STOP", command=self.stop_timer, font=("Helvetica", int(self.base_font_size * 0.8)))
        self.stop_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.rap_button = tk.Button(button_frame, text="LAP", command=self.record_lap_time, font=("Helvetica", int(self.base_font_size * 0.8)))
        self.rap_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        self.generate_button = tk.Button(button_frame, text="GENERATE", command=self.regenerate_balls, font=("Helvetica", int(self.base_font_size * 0.8)))
        self.generate_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.countdown_button = tk.Button(button_frame, text="COUNTDOWN", command=self.countdown, font=("Helvetica", int(self.base_font_size * 0.8)))
        self.countdown_button.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        # タイマー表示用のフレーム
        timer_frame = tk.Frame(self)
        timer_frame.grid(row=1, column=0, columnspan=2, pady=20, sticky="nsew")

        # タイマー表示用のラベル
        self.timer_label = tk.Label(timer_frame, text="00:00:00.000", font=("Helvetica", int(self.base_font_size * 3)))
        self.timer_label.pack()

        # ラップタイム表示用のフレーム
        rap_frame = tk.Frame(self)
        rap_frame.grid(row=2, column=0, columnspan=2, pady=20, sticky="nsew")

        # ラップタイム表示用のラベルとスクロールバー
        rap_label = tk.Label(rap_frame, text="Lap Times:", font=("Helvetica", int(self.base_font_size * 0.8)))
        rap_label.pack(side=tk.LEFT)
        self.rap_scrollbar = ttk.Scrollbar(rap_frame, orient=tk.VERTICAL)
        self.rap_listbox = tk.Listbox(rap_frame, yscrollcommand=self.rap_scrollbar.set, font=("Helvetica", int(self.base_font_size * 0.8)))
        self.rap_listbox.config(yscrollcommand=self.rap_scrollbar.set)
        self.rap_scrollbar.config(command=self.rap_listbox.yview)
        self.rap_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.rap_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # ウィンドウサイズ変更時のイベント
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.bind("<Configure>", self.on_resize)

    def generate_balls(self):
        self.ball_canvas.delete("all")
        canvas_width = self.ball_canvas.winfo_width()
        canvas_height = self.ball_canvas.winfo_height()
        ball_radius = min(canvas_width, canvas_height) // 8
        self.colors = ["blue"] * 6 + ["red"] * 6
        for row in range(2):
            for col in range(6):
                x1 = col * (canvas_width // 6) + (canvas_width // 6 - (ball_radius * 2)) / 2
                y1 = row * (canvas_height // 2) + (canvas_height // 2 - (ball_radius * 2)) / 2
                x2 = x1 + ball_radius * 2
                y2 = y1 + ball_radius * 2
                color = self.colors[row * 6 + col]
                self.ball_canvas.create_oval(x1, y1, x2, y2, fill=color)

    def regenerate_balls(self, event=None):
        self.ball_canvas.delete("all")
        canvas_width = self.ball_canvas.winfo_width()
        canvas_height = self.ball_canvas.winfo_height()
        ball_radius = min(canvas_width, canvas_height) // 8
        self.colors = ["blue"] * 6 + ["red"] * 6
        random.shuffle(self.colors)
        for row in range(2):
            for col in range(6):
                x1 = col * (canvas_width // 6) + (canvas_width // 6 - (ball_radius * 2)) / 2
                y1 = row * (canvas_height // 2) + (canvas_height // 2 - (ball_radius * 2)) / 2
                x2 = x1 + ball_radius * 2
                y2 = y1 + ball_radius * 2
                color = self.colors[row * 6 + col]
                self.ball_canvas.create_oval(x1, y1, x2, y2, fill=color)

    def resize_balls(self, event=None):
        self.ball_canvas.delete("all")
        canvas_width = self.ball_canvas.winfo_width()
        canvas_height = self.ball_canvas.winfo_height()
        ball_radius = min(canvas_width, canvas_height) // 8
        for row in range(2):
            for col in range(6):
                x1 = col * (canvas_width // 6) + (canvas_width // 6 - (ball_radius * 2)) / 2
                y1 = row * (canvas_height // 2) + (canvas_height // 2 - (ball_radius * 2)) / 2
                x2 = x1 + ball_radius * 2
                y2 = y1 + ball_radius * 2
                color = self.colors[row * 6 + col]
                self.ball_canvas.create_oval(x1, y1, x2, y2, fill=color)


    def start_timer(self, event=None):
        if not self.timer_running:
            self.start_time = time.time()
            self.timer_running = True
            self.update_timer()  # タイマーの更新を開始
            self.rap_listbox.delete(0, tk.END)

    def update_timer(self):
        if self.timer_running:
            elapsed_time = time.time() - self.start_time
            self.timer_label.config(text=self.format_time(elapsed_time))
            self.timer_label.after(10, self.update_timer)

    def format_time(self, elapsed_time):
        hours = int(elapsed_time / 3600)
        minutes = int((elapsed_time % 3600) / 60)
        seconds = int(elapsed_time % 60)
        milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"

    def stop_timer(self, event=None):
        if self.timer_running:
            self.timer_running = False

    def record_lap_time(self, event=None):
        if self.timer_running:
            current_time = self.timer_label['text']
            self.rap_listbox.insert(0, current_time)

    def countdown(self, event=None):
        self.timer_label.config(text=str("READY"))
        self.update_idletasks()
        time.sleep(2)
        for i in range(3, 0, -1):
            self.timer_label.config(text=str(i))
            self.update_idletasks()
            time.sleep(1)
        self.start_timer()

    def on_resize(self, event):
        new_font_size = max(int(self.base_font_size * event.width / 1000), 10)
        self.timer_label.config(font=("Helvetica", int(new_font_size * 3)))
        button_font_size = int(new_font_size * 0.8)
        self.start_button.config(font=("Helvetica", button_font_size))
        self.stop_button.config(font=("Helvetica", button_font_size))
        self.rap_button.config(font=("Helvetica", button_font_size))
        self.generate_button.config(font=("Helvetica", button_font_size))
        self.rap_listbox.config(font=("Helvetica", int(button_font_size * 0.75)))
        self.countdown_button.config(font=("Helvetica", button_font_size))

        # キャンバスのサイズを調整
        self.ball_canvas.config(width=event.width * 0.5, height=event.height * 0.1)
        if not self.timer_running:  # タイマーが動作していない場合にのみボールを再生成
            self.resize_balls()

    def start_stop_timer(self, event=None):
        if self.timer_running:
            self.stop_timer()
        else:
            self.start_timer()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Ball and Stopwatch GUI")
    app = BallGUI(master=root)
    app.mainloop()
