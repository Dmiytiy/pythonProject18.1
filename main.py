import random
from question import Question
from data import questions_data

def main():
    questions = []
    for question_data in questions_data:
        new_question = Question(
            question_data["q"],
            question_data["d"],
            question_data["a"]
        )
        print(new_question)
        questions.append(new_question)
    random.shuffle(questions)
    for question in questions:
        print(question.build_question())
        user_amswer = input()
        question.user_amswer = user_amswer

        if question.is_correct():
            print(question.build_possitive_feedback())
        else:
            print(question.build_negative_feedback())

    counter = 0
    points = 0
    for question in questions:
        if question.is_correct():
            counter += 1
            points += question.get_points()

    print("Вот и всё ")
    print(f" Отвечено {counter} вопросов из {len(questions)}")
    print(f"Набрано баллов {points}")


main()