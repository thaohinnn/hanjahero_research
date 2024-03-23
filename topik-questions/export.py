import json

file = open('data-topik.json', 'r')
data = json.load(file)

questionTitles = data['props']['pageProps']['initialState']['exam']['quesStrs']
questions = data['props']['pageProps']['initialState']['exam']['quesRun']
print('aa')