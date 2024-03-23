import google.generativeai as genai
GEMINI_SK = ''

genai.configure(api_key=GEMINI_SK)

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("What is the meaning of life?")
print(response)
