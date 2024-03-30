import json


file = open('data-topik.json', 'r')
data = json.load(file)

question_titles = data['props']['pageProps']['initialState']['exam']['quesStrs']
questions = data['props']['pageProps']['initialState']['exam']['quesRun']

questions_data = []
exam_data = set()
skill_data = set()
ques_format_data = set()
exam_level_data = set()
meta_data_data = set()

index = 0  # Initialize index outside the loop
for question_item in questions:
    for item in question_item['QuesDs']:
        index += 1  # Increment index for each question processed
        choices = [item[f'answer{i}'] for i in range(1, 5)]
        question_text = item['question']
        answer = item['answerNumber']
        exam = item['TestType']['testTypeName']
        exam_data.add(exam)
        skill = question_item['QuesStr']['QuesFg']['fgName']
        skill_data.add(skill)
        ques_format = question_item['QuesStr']['StrName']
        ques_format_data.add(ques_format)
        exam_level = question_item['QuesStr']['QuesFg']['ExamId']
        exam_level_data.add(exam_level)
        question_meta_text = question_item['text']
        if question_meta_text is not None and question_meta_text not in meta_data_data:
            meta_data_data.add(question_meta_text)
        else:
            pass

        formatted_question = {
            "question_id": index,  # Use the incremented index as question_id
            "question_text": question_text,
            "option_1": choices[0],
            "option_2": choices[1],
            "option_3": choices[2],
            "option_4": choices[3],
            "correct_option": answer,
            "exam": exam,
            "skill": skill,
            "format": ques_format,
            "level": exam_level,
            "question_meta_data": question_meta_text,
        }

        questions_data.append(formatted_question)


exam_data = list(exam_data)
skill_data = list(skill_data)
ques_format_data = list(ques_format_data)
exam_level_data = list(exam_level_data)
meta_data_data = list(meta_data_data)


def create_dict_list(data):
    return [{idx + 1: val} for idx, val in enumerate(data)]


def  create_dict_list_with_key(data):
    return [{"question_meta_id": idx + 1, "question_meta_text": val} for idx, val in enumerate(data)]


skill_list = create_dict_list(skill_data)
ques_format_list = create_dict_list(ques_format_data)
exam_list = create_dict_list(exam_data)
exam_level_list = create_dict_list(exam_level_data)
meta_data_list = create_dict_list(meta_data_data)

formatted_meta_data_list = create_dict_list_with_key(meta_data_data)

lists = [skill_list, exam_list, ques_format_list, exam_level_list, meta_data_list]

for i, d in enumerate(questions_data):
    for key, value in d.items():
        for list_item in lists:
            for item in list_item:
                if value in item.values():
                    questions_data[i][key] = list(item.keys())[0]
                    break
            else:
                continue
            break

file_path = 'question_data.json'

with open(file_path, 'w') as json_file:
    json.dump(questions_data, json_file)


file_path_2 = 'question_meta_data.json'

with open(file_path_2, 'w') as json_file:
    json.dump(formatted_meta_data_list, json_file)

print(len(questions_data))

print('aa')
