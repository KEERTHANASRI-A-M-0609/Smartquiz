import tkinter as tk
from tkinter import messagebox, ttk
import random
import time

class QuizApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Enhanced Multi-Subject Quiz Application")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # Quiz data organized by subjects
        self.quiz_data = {
            "Mathematics": [
                {"question": "What is 15 × 8?", "choices": ["120", "125", "115", "130", "110"], "answer": "120", "difficulty": "Easy"},
                {"question": "What is the derivative of x²?", "choices": ["2x", "x", "2", "x²", "0"], "answer": "2x", "difficulty": "Medium"},
                {"question": "What is the integral of 2x?", "choices": ["x²", "2x²", "x² + C", "2x", "x"], "answer": "x² + C", "difficulty": "Hard"},
                {"question": "What is √144?", "choices": ["12", "14", "10", "16", "11"], "answer": "12", "difficulty": "Easy"},
                {"question": "What is log₁₀(100)?", "choices": ["2", "10", "100", "1", "0"], "answer": "2", "difficulty": "Medium"}
            ],
            "Science": [
                {"question": "What is the chemical symbol for Gold?", "choices": ["Go", "Gd", "Au", "Ag", "Al"], "answer": "Au", "difficulty": "Easy"},
                {"question": "What is the speed of light?", "choices": ["3×10⁸ m/s", "3×10⁶ m/s", "3×10⁷ m/s", "3×10⁹ m/s", "3×10⁵ m/s"], "answer": "3×10⁸ m/s", "difficulty": "Medium"},
                {"question": "Which organelle is called the powerhouse of the cell?", "choices": ["Nucleus", "Ribosome", "Mitochondria", "Golgi body", "Lysosome"], "answer": "Mitochondria", "difficulty": "Easy"},
                {"question": "What is Avogadro's number?", "choices": ["6.022×10²³", "6.022×10²²", "6.022×10²⁴", "6.022×10²¹", "6.022×10²⁵"], "answer": "6.022×10²³", "difficulty": "Hard"},
                {"question": "What gas makes up 78% of Earth's atmosphere?", "choices": ["Oxygen", "Carbon dioxide", "Nitrogen", "Argon", "Hydrogen"], "answer": "Nitrogen", "difficulty": "Medium"}
            ],
            "History": [
                {"question": "In which year did World War II end?", "choices": ["1944", "1945", "1946", "1943", "1947"], "answer": "1945", "difficulty": "Easy"},
                {"question": "Who was the first President of the United States?", "choices": ["Thomas Jefferson", "John Adams", "George Washington", "Benjamin Franklin", "Alexander Hamilton"], "answer": "George Washington", "difficulty": "Easy"},
                {"question": "Which empire was ruled by Julius Caesar?", "choices": ["Greek", "Roman", "Byzantine", "Ottoman", "Persian"], "answer": "Roman", "difficulty": "Medium"},
                {"question": "When did the Berlin Wall fall?", "choices": ["1987", "1988", "1989", "1990", "1991"], "answer": "1989", "difficulty": "Medium"},
                {"question": "Who wrote 'The Art of War'?", "choices": ["Confucius", "Sun Tzu", "Lao Tzu", "Mencius", "Mozi"], "answer": "Sun Tzu", "difficulty": "Hard"}
            ],
            "Geography": [
                {"question": "What is the longest river in the world?", "choices": ["Amazon", "Nile", "Mississippi", "Yangtze", "Congo"], "answer": "Nile", "difficulty": "Easy"},
                {"question": "Which country has the most time zones?", "choices": ["Russia", "USA", "China", "Canada", "Australia"], "answer": "Russia", "difficulty": "Medium"},
                {"question": "What is the smallest country in the world?", "choices": ["Monaco", "Vatican City", "San Marino", "Liechtenstein", "Malta"], "answer": "Vatican City", "difficulty": "Easy"},
                {"question": "Which mountain range contains Mount Everest?", "choices": ["Andes", "Alps", "Himalayas", "Rockies", "Urals"], "answer": "Himalayas", "difficulty": "Easy"},
                {"question": "What is the deepest ocean trench?", "choices": ["Puerto Rico Trench", "Java Trench", "Mariana Trench", "Peru-Chile Trench", "Kermadec Trench"], "answer": "Mariana Trench", "difficulty": "Medium"}
            ],
            "Literature": [
                {"question": "Who wrote '1984'?", "choices": ["George Orwell", "Aldous Huxley", "Ray Bradbury", "H.G. Wells", "Jules Verne"], "answer": "George Orwell", "difficulty": "Easy"},
                {"question": "Which Shakespeare play features the character Hamlet?", "choices": ["Macbeth", "Othello", "King Lear", "Hamlet", "Romeo and Juliet"], "answer": "Hamlet", "difficulty": "Easy"},
                {"question": "Who wrote 'Pride and Prejudice'?", "choices": ["Charlotte Brontë", "Emily Brontë", "Jane Austen", "George Eliot", "Virginia Woolf"], "answer": "Jane Austen", "difficulty": "Medium"},
                {"question": "What is the first book in the Harry Potter series?", "choices": ["Chamber of Secrets", "Prisoner of Azkaban", "Philosopher's Stone", "Goblet of Fire", "Order of Phoenix"], "answer": "Philosopher's Stone", "difficulty": "Easy"},
                {"question": "Who wrote 'One Hundred Years of Solitude'?", "choices": ["Gabriel García Márquez", "Mario Vargas Llosa", "Jorge Luis Borges", "Pablo Neruda", "Octavio Paz"], "answer": "Gabriel García Márquez", "difficulty": "Hard"}
            ]
        }
        
        self.current_subject = None
        self.current_questions = []
        self.current_question_index = 0
        self.score = 0
        self.total_questions = 0
        self.start_time = 0
        self.time_limit = 30  # seconds per question
        self.timer_id = None
        
        self.setup_main_menu()
    
    def setup_main_menu(self):
        self.clear_window()
        
        # Title
        title_label = tk.Label(self.root, text="Enhanced Quiz Application", 
                              font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#2c3e50")
        title_label.pack(pady=30)
        
        # Subject selection
        subject_frame = tk.Frame(self.root, bg="#f0f0f0")
        subject_frame.pack(pady=20)
        
        tk.Label(subject_frame, text="Select Subject:", font=("Arial", 16), 
                bg="#f0f0f0", fg="#34495e").pack(pady=10)
        
        for subject in self.quiz_data.keys():
            btn = tk.Button(subject_frame, text=subject, font=("Arial", 12),
                           bg="#3498db", fg="white", width=15, height=2,
                           command=lambda s=subject: self.start_quiz(s))
            btn.pack(pady=5)
        
        # Mixed quiz option
        mixed_btn = tk.Button(subject_frame, text="Mixed Quiz (All Subjects)", 
                             font=("Arial", 12, "bold"), bg="#e74c3c", fg="white", 
                             width=20, height=2, command=self.start_mixed_quiz)
        mixed_btn.pack(pady=15)
    
    def start_quiz(self, subject):
        self.current_subject = subject
        self.current_questions = random.sample(self.quiz_data[subject], 
                                             min(5, len(self.quiz_data[subject])))
        self.setup_quiz()
    
    def start_mixed_quiz(self):
        self.current_subject = "Mixed"
        all_questions = []
        for subject_questions in self.quiz_data.values():
            all_questions.extend(subject_questions)
        self.current_questions = random.sample(all_questions, 10)
        self.setup_quiz()
    
    def setup_quiz(self):
        self.current_question_index = 0
        self.score = 0
        self.total_questions = len(self.current_questions)
        self.clear_window()
        
        # Quiz header
        header_frame = tk.Frame(self.root, bg="#34495e", height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        self.subject_label = tk.Label(header_frame, text=f"Subject: {self.current_subject}", 
                                     font=("Arial", 14, "bold"), bg="#34495e", fg="white")
        self.subject_label.pack(side=tk.LEFT, padx=20, pady=25)
        
        self.progress_label = tk.Label(header_frame, text="", font=("Arial", 12), 
                                      bg="#34495e", fg="white")
        self.progress_label.pack(side=tk.RIGHT, padx=20, pady=25)
        
        # Timer
        self.timer_label = tk.Label(self.root, text="", font=("Arial", 14, "bold"), 
                                   bg="#e74c3c", fg="white", height=2)
        self.timer_label.pack(fill=tk.X)
        
        # Question area
        question_frame = tk.Frame(self.root, bg="#ecf0f1", padx=40, pady=30)
        question_frame.pack(fill=tk.BOTH, expand=True)
        
        self.question_label = tk.Label(question_frame, text="", font=("Arial", 16), 
                                      bg="#ecf0f1", fg="#2c3e50", wraplength=700, justify=tk.CENTER)
        self.question_label.pack(pady=30)
        
        self.difficulty_label = tk.Label(question_frame, text="", font=("Arial", 10, "italic"), 
                                        bg="#ecf0f1", fg="#7f8c8d")
        self.difficulty_label.pack()
        
        # Answer buttons
        self.buttons = []
        for i in range(5):
            btn = tk.Button(question_frame, text="", font=("Arial", 12), 
                           bg="#95a5a6", fg="white", height=2, width=50,
                           command=lambda idx=i: self.check_answer(idx))
            btn.pack(pady=8, padx=20, fill=tk.X)
            self.buttons.append(btn)
        
        self.display_question()
    
    def display_question(self):
        if self.current_question_index < len(self.current_questions):
            question_data = self.current_questions[self.current_question_index]
            
            # Update progress
            self.progress_label.config(text=f"Question {self.current_question_index + 1}/{self.total_questions}")
            
            # Display question
            self.question_label.config(text=question_data["question"])
            self.difficulty_label.config(text=f"Difficulty: {question_data['difficulty']}")
            
            # Display choices
            for i, choice in enumerate(question_data["choices"]):
                self.buttons[i].config(text=choice, state=tk.NORMAL, bg="#3498db")
            
            # Start timer
            self.start_timer()
        else:
            self.show_results()
    
    def start_timer(self):
        self.start_time = time.time()
        self.update_timer()
    
    def update_timer(self):
        elapsed = int(time.time() - self.start_time)
        remaining = max(0, self.time_limit - elapsed)
        
        self.timer_label.config(text=f"Time Remaining: {remaining} seconds")
        
        if remaining > 0:
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.time_up()
    
    def time_up(self):
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)
        messagebox.showwarning("Time's Up!", "Time's up for this question!")
        self.root.after(2000, self.next_question)
    
    def check_answer(self, selected_index):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        
        question_data = self.current_questions[self.current_question_index]
        selected_answer = question_data["choices"][selected_index]
        correct_answer = question_data["answer"]
        
        # Disable all buttons
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)
        
        # Highlight correct and selected answers
        for i, btn in enumerate(self.buttons):
            if question_data["choices"][i] == correct_answer:
                btn.config(bg="#27ae60")  # Green for correct
            elif i == selected_index and selected_answer != correct_answer:
                btn.config(bg="#e74c3c")  # Red for wrong selection
        
        if selected_answer == correct_answer:
            self.score += 1
        
        self.root.after(2000, self.next_question)
    
    def next_question(self):
        self.current_question_index += 1
        self.display_question()
    
    def show_results(self):
        self.clear_window()
        
        # Results frame
        results_frame = tk.Frame(self.root, bg="#2c3e50", padx=50, pady=50)
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        tk.Label(results_frame, text="Quiz Completed!", font=("Arial", 24, "bold"), 
                bg="#2c3e50", fg="white").pack(pady=20)
        
        # Score
        percentage = (self.score / self.total_questions) * 100
        tk.Label(results_frame, text=f"Your Score: {self.score}/{self.total_questions} ({percentage:.1f}%)", 
                font=("Arial", 18), bg="#2c3e50", fg="white").pack(pady=10)
        
        # Performance message
        if percentage >= 80:
            message = "Excellent! Outstanding performance!"
            color = "#27ae60"
        elif percentage >= 60:
            message = "Good job! Well done!"
            color = "#f39c12"
        else:
            message = "Keep practicing! You can do better!"
            color = "#e74c3c"
        
        tk.Label(results_frame, text=message, font=("Arial", 14), 
                bg="#2c3e50", fg=color).pack(pady=10)
        
        # Subject info
        tk.Label(results_frame, text=f"Subject: {self.current_subject}", 
                font=("Arial", 12), bg="#2c3e50", fg="#bdc3c7").pack(pady=5)
        
        # Buttons
        button_frame = tk.Frame(results_frame, bg="#2c3e50")
        button_frame.pack(pady=30)
        
        tk.Button(button_frame, text="Play Again", font=("Arial", 12), 
                 bg="#3498db", fg="white", width=15, height=2,
                 command=self.setup_main_menu).pack(side=tk.LEFT, padx=10)
        
        tk.Button(button_frame, text="Exit", font=("Arial", 12), 
                 bg="#e74c3c", fg="white", width=15, height=2,
                 command=self.root.quit).pack(side=tk.LEFT, padx=10)
    
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = QuizApp()
    app.run()