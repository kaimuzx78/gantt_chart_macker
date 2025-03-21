import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
from datetime import datetime

selected_colors = ["skyblue", "lightgreen", "lightcoral", "lightpink", "lightyellow"]

def load_data():
    filepath = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return
    
    try:
        with open(filepath, "r") as file:
            lines = file.readlines()
        
        data = []
        for line in lines[1:]:  # Skip header
            parts = line.strip().split('\t')
            if len(parts) == 5:
                data.append({
                    "Task Name": parts[1],
                    "Duration": int(parts[2]),
                    "Start Date": parts[3],
                    "Finish Date": parts[4]
                })
        
        if not data:
            messagebox.showerror("Error", "No valid data found in the file.")
            return
        
        create_gantt_chart(data)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load file: {str(e)}")

def create_gantt_chart(data):
    df = pd.DataFrame(data)
    df["Start Date"] = pd.to_datetime(df["Start Date"], format="%d-%m-%Y")
    df["Finish Date"] = pd.to_datetime(df["Finish Date"], format="%d-%m-%Y")
    df["Duration"] = (df["Finish Date"] - df["Start Date"]).dt.days
    
    fig, ax = plt.subplots(figsize=(12, 6))
    for i, (task, start, duration) in enumerate(zip(df["Task Name"], df["Start Date"], df["Duration"])):
        ax.barh(task, duration, left=start, color=selected_colors[i % len(selected_colors)], edgecolor="black")
    
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    plt.xlabel("Timeline")
    plt.ylabel("Tasks")
    plt.title("Gantt Chart - Project Timeline")
    plt.grid(axis="x", linestyle="--", alpha=0.6)
    plt.xticks(rotation=45)
    plt.show()

def choose_color(index):
    color = colorchooser.askcolor()[1]
    if color:
        selected_colors[index] = color

def main():
    root = tk.Tk()
    root.title("KAIMU - Gantt Chart")
    root.geometry("400x300")
    
    label = tk.Label(root, text="Load a text file containing project data:")
    label.pack(pady=10)
    
    button = tk.Button(root, text="Load Data", command=load_data)
    button.pack(pady=10)
    
    color_buttons_frame = tk.Frame(root)
    color_buttons_frame.pack(pady=10)
    
    for i in range(len(selected_colors)):
        color_button = tk.Button(color_buttons_frame, text=f"Choose Color {i+1}", command=lambda i=i: choose_color(i))
        color_button.grid(row=0, column=i, padx=5)
    
    root.mainloop()

if __name__ == "__main__":
    main()
