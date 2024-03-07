import os

api_key = os.environ.get('API_KEY')
folderPath = "./pdfs/"
headerQuestions="title,summary,keywords,Main Objetive,Experimental Methods,Key Findings,Conclusions,Relevance"+"\n"
fileCSV="archivo.csv"
questions = """
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