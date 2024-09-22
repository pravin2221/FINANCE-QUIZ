import tkinter as tk
from tkinter import messagebox

# List of questions and answers
questions = [
    {
        "question": "What is the 50/30/20 rule in budgeting?",
        "options": ["50% needs, 30% wants, 20% savings", "50% savings, 30% needs, 20% wants", "50% wants, 30% savings, 20% needs", "10% wants, 3% savings, 2% needs"],
        "answer": "50% needs, 30% wants, 20% savings",
        "feedback": "The 50/30/20 rule suggests allocating 50% of your income to needs, 30% to wants, and 20% to savings."
    },
    {
        "question": "What is a good debt-to-income ratio?",
        "options": ["Below 20%", "Below 36%", "Below 50%", "Below 80%"],
        "answer": "Below 36%",
        "feedback": "A good debt-to-income ratio is below 36%. This indicates that your debt is manageable relative to your income."
    },
    {
        "question": "What is the primary purpose of creating a budget?",
        "options": ["To track expenses only", "To determine how much money you can borrow", "To plan income and expenses", "To avoid taxes"],
        "answer": "To plan income and expenses",
        "feedback": "To plan income and expenses.Good keep going."
    },
    {
        "question": "What is an emergency fund?",
        "options": ["Money set aside for vacations", "Savings for non-essential expenses", "Funds reserved for unexpected financial situations", "A loan taken out in case of emergencies"],
        "answer": "Funds reserved for unexpected financial situations",
        "feedback": "Funds reserved for unexpected financial situations. Good keep going."
    },
    {
        "question": "Which of the following is considered a fixed expense??",
        "options": ["Groceries", " Electricity bill", "Rent or mortgage", "Dining out " ],
        "answer": "Rent or mortgage",
        "feedback": "Rent or mortgage. Good keep going."
        
    },
    {
        "question": "What does pay yourself first mean in personal finance?",
        "options": ["Spend money before budgeting", " Set aside savings before spending on other things ", "Pay your bills first", "Pay off debts before saving  " ],
        "answer": "Set aside savings before spending on other things",
        "feedback": "Set aside savings before spending on other things. Good keep going."
        
    },
    {
        "question": "Which of the following is a benefit of tracking your expenses?",
        "options": ["Increasing your spending ", " Understanding where your money goes", "Reducing your income  ", "Avoiding credit card payments " ],
        "answer": "Understanding where your money goes",
        "feedback": "Understanding where your money goes. Good keep going."
    },
    {
        "question": "What is the best definition of a variable expense?",
        "options": ["An expense that remains the same each month  ", " An expense that changes from month to month", "An investment in the stock market", "An emergency fund contribution  " ],
        "answer": "An expense that changes from month to month",
        "feedback": "An expense that changes from month to month. Good keep going."
        
    },
    {
        "question": "What is compound interest?",
        "options": ["Interest on an original amount only ", "Interest on both the original amount and the interest that has been added  ", "A one-time interest payment ", " Interest that decreases over time  " ],
        "answer": "Interest on both the original amount and the interest that has been added",
        "feedback": "Interest on both the original amount and the interest that has been added. Good keep going."
        
    },
    {
        "question": "Which of the following is a good strategy for paying off debt?",
        "options": [" Make only the minimum payment  ", "Pay off high-interest debt first ", "Ignore debt and focus on savings ", "Borrow more to pay off old debt  " ],
        "answer": "Pay off high-interest debt first",
        "feedback": "Pay off high-interest debt first. Good keep going."
    },
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Quiz")
        self.score = 0
        self.question_index = 0
        self.create_widgets()
        self.show_question()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", wraplength=400)
        self.question_label.pack(pady=20)

        self.options = tk.StringVar()
        self.option_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.root, text="", variable=self.options, value=i, wraplength=400)
            rb.pack(anchor="w")
            self.option_buttons.append(rb)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)

    def show_question(self):
        question = questions[self.question_index]
        self.question_label.config(text=question["question"])
        for i, option in enumerate(question["options"]):
            self.option_buttons[i].config(text=option)
        self.options.set(-1)

    def check_answer(self):
        selected_option = int(self.options.get())
        if selected_option == -1:
            messagebox.showwarning("Warning", "Please select an option")
            return

        question = questions[self.question_index]
        if question["options"][selected_option] == question["answer"]:
            self.score += 1
            messagebox.showinfo("Correct!", "Correct!\n" + question["feedback"])
            self.question_index += 1
        else:
            messagebox.showinfo("Incorrect", "Incorrect.\n" + question["feedback"])
            self.question_index += 1
        if self.question_index < len(questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        result_text = f"Your final score is {self.score}/{len(questions)}\n"
        if self.score >= 8:
            result_text += "Great job! You have a good understanding of personal finance."
        elif self.score >= 5:
            result_text += "Good effort! Consider reviewing some personal finance topics."
        else:
            result_text += "Keep learning! Here are some resources to help you improve your personal finance knowledge:\n"
            result_text += "1. 'The Total Money Makeover' by Dave Ramsey\n"
            result_text += "2. 'Your Money or Your Life' by Vicki Robin and Joe Dominguez\n"
            result_text += "3. Websites like Investopedia and NerdWallet"
            result_text += ">8. Great job! You have a good understanding of personal finance."
            result_text += ">5. Good effort! Consider reviewing some personal finance topics."

        messagebox.showinfo("Quiz Result", result_text)
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
