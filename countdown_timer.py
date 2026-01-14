import tkinter as tk

running = False
paused = False
remaining_time = 0

def start_timer():
    global running, paused, remaining_time
    if not running:
        try:
            remaining_time = int(time_entry.get())
            running = True
            paused = False
            update_timer()
        except ValueError:
            timer_label.config(text="Invalid Input")

def pause_timer():
    global paused
    if running:
        paused = True

def resume_timer():
    global paused
    if running and paused:
        paused = False
        update_timer()

def stop_timer():
    global running, paused
    running = False
    paused = False
    timer_label.config(text="00:00")

def update_timer():
    global remaining_time, running, paused

    if running and not paused:
        if remaining_time >= 0:
            mins, secs = divmod(remaining_time, 60)
            timer_label.config(text=f"{mins:02d}:{secs:02d}")
            remaining_time -= 1
            root.after(1000, update_timer)
        else:
            timer_label.config(text="⏰ Time's Up!")
            running = False

# Tkinter window
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("350x290")
root.resizable(True, True)

# UI
tk.Label(root, text="Enter Time (seconds)", font=("Times New Roman", 12)).pack(pady=5)

time_entry = tk.Entry(root, font=("Times New Roman", 14), justify="center")
time_entry.pack(pady=5)

timer_label = tk.Label(root, text="00:00", font=("Times New Roman", 28))
timer_label.pack(pady=15)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Start", width=15,command=start_timer).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Pause ⏸", width=15,command=pause_timer).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Resume ▶", width=15,command=resume_timer).grid(row=1, column=0, padx=5)
tk.Button(btn_frame, text="Stop ⏹", width=15,command=stop_timer).grid(row=1, column=1, pady=10)

root.mainloop()
