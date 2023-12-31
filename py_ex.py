
import tkinter as tk
from tkinter import messagebox


class Form1(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("صفحه نخست")

        final_text = ''
        self.next_button = tk.Button(self, text="نمایش سوالات", command=self.open_form2)
        self.next_button.pack(padx=10, pady=10)

        self.video_button = tk.Button(self, text="پخش ویدئو", command=self.play_video)
        self.video_button.pack(padx=10, pady=10)

        for line in self.read_text('texts\\1.txt'):
            final_text += (line + '\n')
            
        self.label = tk.Label(self, text=final_text, font=("B Nazanin", 14), wraplength=400, justify="right")
        self.label.pack(padx=10, pady=10, anchor='center')
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


        
    def read_text(self, file_name):
        f = open(file_name, "r", encoding='utf8')
        return f.readlines()

    def play_video(self):
        try:
            vid = cv2.VideoCapture('videos\\2.mp4') 
            while(True): 
                _, frame = vid.read() 
                cv2.imshow('ویدئو آموزشی', frame) 
      
                if cv2.waitKey(1) & 0xFF == ord('q'): 
                    break
  
            vid.release() 
            cv2.destroyAllWindows() 

        except Exception as e:
            print(e)
            pass        

    def open_form2(self):
        questions = [
        {
            "question": "برای استفاده صحیح از بستر های مختلف دیجیتالی کدام مورد لازم است؟",
            "answers": ["اینترنت", "گوشی موبایل", "تلفن همراه", "سواد دیجیتال"],
            "correct_answer": "سواد دیجیتال"
        },
        {
            "question": "امروزه مردم از کدام مورد بسیار زیاد در زندگی روزمره خود استفاده میکنند؟",
            "answers": ["پس انداز کردن", "مسافرت", "شبکه های اجتماعی", "صله رحم"],
            "correct_answer": "شبکه های اجتماعی"
        },
        {
            "question": "نابرابری در دسترسی و استفاده از فن آوری های اطلاعاتی و ارتباطی منجر به کدام مورد میشود؟",
            "answers": ["نهایت شکاف اقتصادی", "افزایش مهارت کار با کامپیوتر", "شکاف دانایی", "گزینه یک و سه"],
            "correct_answer": "گزینه یک و سه"
        },
        {
            "question": "با توجه به متن اولیه , هدف سواد دیجیتال چیست؟",
            "answers": ["تحریم اقتصادی", "افزایش اعتماد به نفس", "گسترش فساد", "توانمند کردن افراد"],
            "correct_answer": "توانمند کردن افراد"
        }
        ,
        {
            "question": "دو ضربدر دو؟",
            "answers": ["2", "4", "1", "0"],
            "correct_answer": "4"
        }]

        self.withdraw()
        form1 = QuizForm(questions)
        form1.mainloop()
        

class Form2(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Form 2")
        
        self.label = tk.Label(self, text="فرم 2")
        self.label.pack(padx=10, pady=10)

        self.prev_button = tk.Button(self, text="فرم 1", command=self.open_form1)
        self.prev_button.pack(padx=10, pady=10)
        
    def open_form1(self):
        self.withdraw()
        form2 = Form2(self)
        form2.mainloop()


class QuizForm(tk.Toplevel):
    def __init__(self, questions):
        super().__init__()
        self.title("آزمون")
        
        self.questions = questions
        self.num_questions = len(questions)
        self.correct_answers = 0
        
        self.current_question = 0
        
        self.question_label = tk.Label(self, text=self.questions[self.current_question]["question"],
                                       font=("B Nazanin", 13), wraplength=400, justify="right")
        self.question_label.pack(padx=10, pady=10)
        
        self.answer_var = tk.StringVar()
        
        self.answer1_radio = tk.Radiobutton(self, text=self.questions[self.current_question]["answers"][0],
                                            variable=self.answer_var, value=self.questions[self.current_question]["answers"][0])
        self.answer1_radio.pack(padx=10, pady=5)
        
        self.answer2_radio = tk.Radiobutton(self, text=self.questions[self.current_question]["answers"][1],
                                            variable=self.answer_var, value=self.questions[self.current_question]["answers"][1])
        self.answer2_radio.pack(padx=10, pady=5)
        
        self.answer3_radio = tk.Radiobutton(self, text=self.questions[self.current_question]["answers"][2],
                                            variable=self.answer_var, value=self.questions[self.current_question]["answers"][2])
        self.answer3_radio.pack(padx=10, pady=5)
        
        self.answer4_radio = tk.Radiobutton(self, text=self.questions[self.current_question]["answers"][3],
                                            variable=self.answer_var, value=self.questions[self.current_question]["answers"][3])
        self.answer4_radio.pack(padx=10, pady=5)
        
        self.next_button = tk.Button(self, text="بعدی", command=self.next_question)
        self.next_button.pack(padx=10, pady=10)
        
    def next_question(self):
        print(self.questions[self.current_question]["correct_answer"])
        print(self.answer_var.get())

        if self.current_question < self.num_questions - 1:
            if self.answer_var.get() == self.questions[self.current_question]["correct_answer"]:
                self.correct_answers += 1
            else:
                messagebox.showinfo('پاسخ اشتباه', f'جواب درست : {self.questions[self.current_question]["correct_answer"]}')

            self.current_question += 1
            self.question_label.config(text=self.questions[self.current_question]["question"])
            self.answer_var.set("")
            
            self.answer1_radio.destroy()
            self.answer2_radio.destroy()
            self.answer3_radio.destroy()
            self.answer4_radio.destroy()

            self.answer1_radio = tk.Radiobutton(self, text=self.questions[self.current_question]["answers"][0],
                                                variable=self.answer_var, value=self.questions[self.current_question]["answers"][0])
            self.answer1_radio.pack(padx=10, pady=5)
        
            self.answer2_radio = tk.Radiobutton(self, text=self.questions[self.current_question]["answers"][1],
                                                variable=self.answer_var, value=self.questions[self.current_question]["answers"][1])
            self.answer2_radio.pack(padx=10, pady=5)
        
            self.answer3_radio = tk.Radiobutton(self, text=self.questions[self.current_question]["answers"][2],
                                                variable=self.answer_var, value=self.questions[self.current_question]["answers"][2])
            self.answer3_radio.pack(padx=10, pady=5)
        
            self.answer4_radio = tk.Radiobutton(self, text=self.questions[self.current_question]["answers"][3],
                                                variable=self.answer_var, value=self.questions[self.current_question]["answers"][3])
            self.answer4_radio.pack(padx=10, pady=5)

        else:
            if self.answer_var.get() == self.questions[self.current_question]["correct_answer"]:
                self.correct_answers += 1

            messagebox.showinfo("نتیجه", "تعداد پاسخ‌های درست: {}\nتعداد پاسخ‌های غلط: {}".format(self.correct_answers, self.num_questions - self.correct_answers))
            self.destroy()

form1 = Form1()
form1.mainloop()
