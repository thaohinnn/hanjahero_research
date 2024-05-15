import json

def create_dict_list(data):
    return [{idx + 1: val} for idx, val in enumerate(data)]


def create_dict_list_with_key(data):
    return [{"question_meta_id": idx + 337, "question_meta_text": val} for idx, val in enumerate(data)]


def sort_alphabetically(data):
    sorted_data = sorted(data)
    return sorted_data


def populate_question_ids(questions, start_id=833):
    """
    Populates the 'question_id' field for a list of question objects.

    Args:
    - questions (list): List of question objects.
    - start_id (int): Starting ID for populating question IDs. Default is 1.

    Returns:
    - list: List of question objects with populated 'question_id' field.
    """
    for i, question in enumerate(questions, start=start_id):
        question['question_id'] = i
    return questions

file = open('topik1.json', 'r')
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
        score = item['score']
        question_meta_text = question_item['text']
        if question_meta_text is not None and question_meta_text not in meta_data_data:
            meta_data_data.add(question_meta_text)
        else:
            pass

        formatted_question = {
            "question_text": question_text,
            "option_1": choices[0],
            "option_2": choices[1],
            "option_3": choices[2],
            "option_4": choices[3],
            "correct_option": answer,
            "score": score,
            "exam": exam,
            "skill": skill,
            "format": ques_format,
            "level": exam_level,
            "question_meta_data": question_meta_text,
        }

        questions_data.append(formatted_question)


# SORT ALPHABETICALLY
skill_data = sort_alphabetically(skill_data)
exam_data = sort_alphabetically(exam_data)
exam_level_data = sort_alphabetically(exam_level_data)
meta_data_data = sort_alphabetically(meta_data_data)
ques_format_data = sort_alphabetically(ques_format_data)

# CREATE DICT
skill_list = [{1: '듣기'}, {2: '쓰기'}, {3: '읽기'}]
exam_list = create_dict_list(exam_data)
meta_data_list = create_dict_list(meta_data_data)
ques_format_list = [{25: '[5~6] 다음을 듣고 <보기>와 같이 이어지는 말을 고르십시오.'},
                    {26: '[7~10] 여기는 어디입니까? <보기>와 같이 알맞은 것을 고르십시오.'},
                    {27: '[11~14] 다음은 무엇에 대해 말하고 있습니까? <보기>와 같이 알맞은 것을 고르십시오.'},
                    {28: '[15~16] 다음 대화를 듣고 알맞은 그림을 고르십시오.'},
                    {29: '[17~21] 다음을 듣고 <보기>와 같이 대화 내용과 같은 것을 고르십시오.'},
                    {30: '[1~4] 다음을 듣고 <보기>와 같이 물음에 맞는 대답을 고르십시오.'},
                    {31: '[22~24] 다음을 듣고 여자의 중심 생각을 고르십시오.'},
                    {32: '[25~30] 다음을 듣고 물음에 답하십시오.'},
                    {33: '[31~33] 무엇에 대한 이야기입니까? <보기>와 같이 알맞은 것을 고르십시오.'},
                    {34: '[34~39] <보기>와 같이 ( )에 들어갈 가장 알맞은 것을 고르십시오.'},
                    {35: '[40~42] 다음을 읽고 맞지 않는 것을 고르십시오.'},
                    {36: '[43~45] 다음의 내용과 같은 것을 고르십시오.'},
                    {37: '[46~48] 다음을 읽고 중심 생각을 고르십시오.'},
                    {38: '[49~56] 다음을 읽고 물음에 답하십시오.'},
                    {39: '[57~58] 다음을 순서대로 맞게 나열한 것을 고르십시오.'},
                    {40: '[59~70] 다음을 읽고 물음에 답하십시오.'},
                    ]

formatted_meta_data_list = create_dict_list_with_key(meta_data_data)

lists = [skill_list, exam_list, ques_format_list, meta_data_list]

for i, d in enumerate(questions_data):
    for key, value in d.items():
        matched_keys = []  # Store keys where a match is found
        for list_item in lists:
            for item in list_item:
                if value in item.values():
                    matched_keys.append(int(list(item.keys())[0]))  # Store the key as an int
        if matched_keys:
            questions_data[i][key] = matched_keys[0]  # Update with list of matched keys

questions_data = sorted(questions_data, key=lambda x: x['format'])

questions_data = populate_question_ids(questions_data)


file_path = 'question_data_topik1.json'

with open(file_path, 'w') as json_file:
    json.dump(questions_data, json_file)

file_path_2 = 'question_meta_data_topik1.json'

with open(file_path_2, 'w') as json_file:
    json.dump(formatted_meta_data_list, json_file)


print('aa')
