import json

def create_dict_list(data):
    return [{idx + 1: val} for idx, val in enumerate(data)]


def create_dict_list_with_key(data):
    return [{"question_meta_id": idx + 1, "question_meta_text": val} for idx, val in enumerate(data)]


def sort_alphabetically(data):
    sorted_data = sorted(data)
    return sorted_data


def populate_question_ids(questions, start_id=1):
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
        score = item['score']
        question_meta_text = question_item['text']
        writing_answer = item['answerText']
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
            "writing_answer": writing_answer
        }

        questions_data.append(formatted_question)


# SORT ALPHABETICALLY
skill_data = sort_alphabetically(skill_data)
exam_data = sort_alphabetically(exam_data)
exam_level_data = sort_alphabetically(exam_level_data)
meta_data_data = sort_alphabetically(meta_data_data)
ques_format_data = sort_alphabetically(ques_format_data)

# CREATE DICT
skill_list = create_dict_list(skill_data)
exam_list = create_dict_list(exam_data)
meta_data_list = create_dict_list(meta_data_data)
ques_format_list = [{8: '[13~16] 다음을 듣고 내용과 일치하는 것을 고르십시오.'},
                    {9: '[13∼15] 다음을 순서대로 맞게 배열한 것을 고르십시오.'},
                    {10: '[16~18] 다음을 읽고 ( )에 들어갈 내용으로 가장 알맞은 것을 고르십시오.'},
                    {11: '[17~20] 다음을 듣고 남자의 중심 생각을 고르십시오.'},
                    {12: '[19~24] 다음을 읽고 물음에 답하십시오.'},
                    {1: '[1~2] ( )에 들어갈 가장 알맞은 것을 고르십시오.'},
                    {2: '[1~3] 다음을 듣고 알맞은 그림을 고르십시오.'},
                    {13: '[21~36] 다음을 듣고 물음에 답하십시오.'},
                    {14: '[25~27] 다음 신문 기사의 제목을 가장 잘 설명한 것을 고르십시오.'},
                    {15: '[28~31] 다음을 읽고 ( )에 들어갈 내용으로 가장 알맞은 것을 고르십시오.'},
                    {16: '[32~34] 다음을 읽고 내용이 같은 것을 고르십시오.'},
                    {17: '[35~38] 다음 글의 주제로 가장 알맞은 것을 고르십시오.'},
                    {18: '[37~50] 다음은 (교양 프로그램/강연/다큐멘터리)입니다. 잘 듣고 물음에 답하십시오.'},
                    {19: '[39~41] 다음 글에서 <보기>의 문장이 들어가기에 가장 알맞은 곳을 고르십시오.'},
                    {3: '[3~4] 다음 밑줄 친 부분과 의미가 비슷한 것을 고르십시오.'},
                    {20: '[42~47] 다음을 읽고 물음에 답하십시오.'},
                    {21: '[48~50] 다음을 읽고 물음에 답하십시오.'},
                    {4: '[4~8] 다음 대화를 잘 듣고 이어질 수 있는 말을 고르십시오.'},
                    {22: '[51~52] 다음을 읽고 ᄀ과 ᄂ에 들어갈 말을 각각 한 문장으로 쓰시오.'},
                    {23: '[53] 다음을 참고하여 (~에 대한 ) 글을 200~300자로 쓰시오. 단, 글의 제목을 쓰지 마시오.'},
                    {24: '[54] 다음을 주제로 하여 자신의 생각을 600~700자로 글을 쓰시오. 단, 문제를 그대로 옮겨 쓰지 마시오.'},
                    {5: '[5∼8] 다음은 무엇에 대한 글인지 고르십시오.'},
                    {6: '[9~12] 다음 글 또는 그래프의 내용과 같은 것을 고르십시오.'},
                    {7: '[9~12] 다음 대화를 잘 듣고 여자가 이어서 할 행동으로 알맞은 것을 고르십시오.'}]

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



file_path = 'question_data.json'

with open(file_path, 'w') as json_file:
    json.dump(questions_data, json_file)

file_path_2 = 'question_meta_data.json'

with open(file_path_2, 'w') as json_file:
    json.dump(formatted_meta_data_list, json_file)

import json


# Path to the new JSON file
new_json_file = '2.json'

# Read the original JSON file
with open(file_path, 'r') as f:
    data = json.load(f)

# Extract only the desired fields
filtered_data = []
for item in data:
    filtered_item = {
        'writing_answer': item['writing_answer'],
        'question_id': item['question_id']
    }
    filtered_data.append(filtered_item)

# Write the filtered data to a new JSON file
with open(new_json_file, 'w') as f:
    json.dump(filtered_data, f)

print("Filtered JSON data has been saved to", new_json_file)

print(lists)
print('aa')
