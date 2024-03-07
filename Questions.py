import requests
import os

api_key = os.environ.get('API_KEY')
source_id = "src_a1HAxSPLVIEmVH4XyE6Nd"
question = """
estriction: For each answer you cannot give more than 20 words.

I want that you answer follow questions about the pdf in order:

1)title:title
Question: What is the title of this article.

2)Title: Summary
Question: Can you provide a brief summary of the article in 20 words or less?

3)Title: Keywords
Question: What are five keywords that describe the main topics or themes of the article?

4)Title: Main Objective
Question: What is the main objective or goal of the study described in the article?

5)Title: Experimental Methods
Question: Which experimental methods were employed in the research described in the article?

6)Title: Key Findings
Question: What were the main findings or results obtained from the study?

7)Title: Conclusions
Question: What conclusions can be drawn from the research presented in the article?

8)Title: Relevance
Question: What is the relevance or significance of this study within the field of chemistry?

format of your answer (replace the number for the corresponding answer, but not keep the number, and keep the ? symbol): 1?2?3?4?5?6?7?8
"""


if api_key is None:
    print("No se encontró la API key en las variables de entorno.")
    exit()

headers = {
    'x-api-key': api_key,
    "Content-Type": "application/json",
}

data = {
    'sourceId': source_id,
    'messages': [
        {
            'role': "user",
            'content': question,
        }
    ]
}

response = requests.post(
    'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)

if response.status_code == 200:
    print('Result:', response.json()['content'])
else:
    print('Status:', response.status_code)
    print('Error:', response.text)




def obtener_respuesta_pregunta(api_key, source_id, pregunta):
    headers = {
        'x-api-key': api_key,
        "Content-Type": "application/json",
    }

    data = {
        'sourceId': source_id,
        'messages': [
            {
                'role': "user",
                'content': pregunta,
            }
        ]
    }

    response = requests.post('https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['content']
    else:
        print('Status:', response.status_code)
        print('Error:', response.text)
