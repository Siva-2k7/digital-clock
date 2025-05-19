import tkinter as tk
from time import strftime

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Digital Clock")
        self.root.geometry("600x300")
        self.root.configure(bg='#2d2d2d')
        self.root.minsize(500, 200)
        
        # Configure theme colors
        self.colors = {
            'background': '#2d2d2d',
            'time': '#00ff00',
            'date': '#ffffff',
            'button_bg': '#404040',
            'button_fg': 'white'
        }
        
        # Create main container
        self.main_frame = tk.Frame(root, bg=self.colors['background'])
        self.main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Time display
        self.time_label = tk.Label(self.main_frame, 
                                font=('DS-Digital', 80),
                                bg=self.colors['background'],
                                fg=self.colors['time'])
        self.time_label.pack(pady=10)
        
        # Date display
        self.date_label = tk.Label(self.main_frame,
                                font=('Arial', 24),
                                bg=self.colors['background'],
                                fg=self.colors['date'])
        self.date_label.pack(pady=10)
        
        # Control buttons
        self.button_frame = tk.Frame(self.main_frame, bg=self.colors['background'])
        self.button_frame.pack(pady=10)
        
        self.quit_btn = tk.Button(self.button_frame, text="Quit", 
                               font=('Arial', 12),
                               command=root.destroy,
                               bg=self.colors['button_bg'],
                               fg=self.colors['button_fg'],
                               padx=15)
        self.quit_btn.pack(side='left', padx=10)
        
        self.format_btn = tk.Button(self.button_frame, text="12/24H", 
                                 font=('Arial', 12),
                                 command=self.toggle_format,
                                 bg=self.colors['button_bg'],
                                 fg=self.colors['button_fg'],
                                 padx=15)
        self.format_btn.pack(side='left', padx=10)
        
        # Initialize time format
        self.is_24h_format = True
        self.update_time()

    def toggle_format(self):
        """Toggle between 12-hour and 24-hour formats"""
        self.is_24h_format = not self.is_24h_format
        self.update_time()

    def update_time(self):
        """Update time and date displays"""
        if self.is_24h_format:
            time_format = '%H:%M:%S'
        else:
            time_format = '%I:%M:%S %p'
        
        current_time = strftime(time_format)
        current_date = strftime('%A, %B %d, %Y')
        
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        
        # Schedule next update
        self.time_label.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()