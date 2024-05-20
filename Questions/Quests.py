import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Questões - TheReadyProject")
        self.questions = [
            "Desenvolvimento Android: Qual é o link para acessar os cursos oficiais do Android?",
            "Desenvolvimento PC: Qual é o site oficial da Microsoft para aprender sobre desenvolvimento de aplicativos para PC?",
            "Desenvolvimento iOS: Onde você pode encontrar a documentação oficial da Apple para desenvolvimento de aplicativos iOS?",
            "Desenvolvimento Front-End: Quais são os três frameworks JavaScript populares mencionados no site?",
            "Desenvolvimento de Bots: Qual é a diferença entre chatbots e frameworks de bot?",
            "Desenvolvimento de TV: Além do Android TV, qual outra plataforma de desenvolvimento para TV é mencionada nos recursos?",
            "Desenvolvimento Back-End: Quais são duas ferramentas populares de integração contínua mencionadas para automatizar testes e implantações no desenvolvimento back-end?",
            "Circuitos Eletrônicos: Explique a diferença entre transistores bipolares e de efeito de campo (FET)."
        ]
        self.alternatives = [
            ["a) www.androiddev.com", "b) www.android.com/courses", "c) www.developer.android.com/courses", "d) www.androiddevelopers.google/courses"],
            ["a) www.microsoftdev.com", "b) www.pcdevelopment.microsoft.com", "c) www.developer.microsoft.com/pc", "d) www.windows.dev"],
            ["a) www.developer.apple.com/ios/docs", "b) www.iosdocs.apple.com", "c) www.apple.com/developer/ios/documentation", "d) www.developer.apple.com/documentation/ios"],
            ["a) Angular, Ruby on Rails, Ember.js", "b) React, Vue.js, Angular", "c) Django, Express.js, Backbone.js", "d) Spring Boot, Flask, Knockout.js"],
            ["a) Chatbots são ferramentas para desenvolver bots, enquanto frameworks de bot são bots pré-construídos.", "b) Chatbots são sistemas autônomos, enquanto frameworks de bot são ferramentas para desenvolver chatbots.", "c) Não há diferença, ambos se referem à mesma coisa.", "d) Chatbots são usados em plataformas de redes sociais, enquanto frameworks de bot são usados em sites."],
            ["a) iOS TV", "b) Roku", "c) Windows TV", "d) Linux TV"],
            ["a) Jenkins e CircleCI", "b) Docker e Kubernetes", "c) GitHub Actions e Travis CI", "d) Ansible e Chef"],
            ["a) Os transistores bipolares usam campos magnéticos para controlar o fluxo de elétrons, enquanto os FETs usam campos elétricos.", "b) Transistores bipolares têm duas camadas de semicondutores, enquanto os FETs têm três camadas.", "c) Transistores bipolares são controlados pela corrente, enquanto os FETs são controlados pela tensão.", "d) Não há diferença, ambos os tipos de transistores funcionam da mesma maneira."]
        ]
        self.answers = ["c", "d", "d", "b", "b", "b", "a", "c"]
        self.user_answers = []
        self.current_question = 0
        self.score = 0

        self.label_question = tk.Label(master, text=self.questions[self.current_question], wraplength=400, justify="left")
        self.label_question.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.radio_btns = []
        for i in range(4):
            radio_btn = tk.Radiobutton(master, text=self.alternatives[self.current_question][i], variable=self.radio_var, value=self.alternatives[self.current_question][i].split(")")[0].strip())
            radio_btn.pack(anchor="w")
            self.radio_btns.append(radio_btn)

        self.button_next = tk.Button(master, text="Próxima", command=self.next_question)
        self.button_next.pack(pady=5)

    def next_question(self):
        user_answer = self.radio_var.get()
        if user_answer is None:
            messagebox.showwarning("Aviso", "Por favor, selecione uma alternativa.")
            return

        self.user_answers.append(user_answer)
        if user_answer == self.answers[self.current_question]:
            self.score += 1

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.label_question.config(text=self.questions[self.current_question])
            self.radio_var.set(None)
            for i in range(4):
                self.radio_btns[i].config(text=self.alternatives[self.current_question][i])
        else:
            self.show_result()

    def show_result(self):
        result_window = tk.Toplevel(self.master)
        result_window.title("Resultado")

        result_label = tk.Label(result_window, text=f"Você acertou {self.score} de {len(self.questions)} perguntas.")
        result_label.pack(pady=10)

        answers_label = tk.Label(result_window, text="Respostas do usuário:")
        answers_label.pack()

        for i, answer in enumerate(self.user_answers):
            answer_label = tk.Label(result_window, text=f"Pergunta {i+1}: {answer}")
            answer_label.pack(anchor="w")

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
