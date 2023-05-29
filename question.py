class Question():
    def __init__(self, question_text, question_diff, question_amswer):
        self.question_text = question_text
        self.question_diff = question_diff
        self.question_amswer = question_amswer

        self.is_asked = False
        self.user_amswer = None
        self.points = int(self.question_diff) * 10

    def get_points(self):
        return self.points

    def is_correct(self):
        return self.user_amswer == self.question_amswer

    def build_question(self):
        return f" Вопрос :{self.question_text} сложность {self.question_diff}"

    def build_possitive_feedback(self):
        return f"Ответ верный Получено {self.points} баллов "

    def build_negative_feedback(self):
        return f" Ответ не верный, правильный ответ {self.question_amswer}"

    def __repr__(self):
        return f"{self.question_text} - {self.question_amswer}({self.question_diff})"