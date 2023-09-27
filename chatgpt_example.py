import openai

openai.api_key = 'Zi1YPAX8zfVUxvvYRCGFx6o1A-Nmz4Ad_-_DpF-NKPddxPKJCftXOF10tjYhpe4mxaSf4Se99LUKJG1xn73lwGA'
openai.api_base = 'https://api.openai.iniad.org/api/v1'

question = input('Question')
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "user", "content": question},
    ]
)

print(response['choices'][0]['message']['content'])