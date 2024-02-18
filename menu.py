from random import shuffle
import html
import json
import math
from question_model import Question

def split_questions_into_sets(questions_bank, num_questions_per_set):
    num_sets = math.ceil(len(questions_bank) / num_questions_per_set)
    question_sets = []

    for i in range(num_sets):
        start_index = i * num_questions_per_set
        end_index = min(start_index + num_questions_per_set, len(questions_bank))
        question_set = questions_bank[start_index:end_index]
        shuffle(question_set)
        question_sets.append(question_set)

    return question_sets

def load_questions_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        question_data = json.load(f)

    question_bank = []
    for question in question_data:
        if 'ĐÁP ÁN ĐÚNG' in question:
            choices = [html.unescape(str(question[key])) for key in ['A', 'B', 'C', 'D']]
            correct_answer = html.unescape(str(question["ĐÁP ÁN ĐÚNG"]))
            question_text = html.unescape(question["CÂU HỎI"])
            correct_index = ['A', 'B', 'C', 'D'].index(correct_answer)
            shuffled_choices = choices[:]
            # shuffle(shuffled_choices)
            correct_answer = choices[correct_index]
            new_question = Question(question_text, correct_answer, shuffled_choices)
            question_bank.append(new_question)
        else:
            print(f"Lỗi: Không tìm thấy đáp án đúng cho câu hỏi: '{question_text}'")
    
    return question_bank

