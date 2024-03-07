from GetPaths import getPaths
from Consts import api_key,questions,headerQuestions,fileCSV
from Upload import uploadFile
from Questions import ask
from formatCSVAnswer import formatCSVanswer

if api_key is None:
   print("No se encontró la API key en las variables de entorno.")
   exit()

# Make a file.csv and give the first row
with open(fileCSV, "w") as file:
    file.write(headerQuestions)

paths=getPaths()
for file_path in paths:
   print(file_path)
   source_id = uploadFile(api_key, file_path)
   answer = ask(api_key, source_id, questions)
   formated_text=formatCSVanswer(answer)
   #Insert new row in csv file with response API formated text
   with open(fileCSV, "a") as file:
      file.write(formated_text+"\n")







