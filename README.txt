~~~~~~~~~~~~~~~~API CHATPDF FOR ORDER PDFS~~~~~~~~~~~~~~~~~~~~~~~~

This project use chatPDF API for get formatted information (on CSV file) about pdfs located in a folder.

Objetive: Get CSV File with information that allow to classify and process a lot of pdfs located in a folder.

ENV: use export API_KEY="your_api_key" for config api key environment var on linux.

CSV File format result:
title,summary,keywords,Main Objetive,Experimental Methods,Key Findings,Conclusions,Relevance  \n
----,---------,-------,-------------,--------------------,-----------,------------,-------- \n   (each line is for each pdf file)
----,---------,-------,-------------,--------------------,-----------,------------,-------- \n
----,---------,-------,-------------,--------------------,-----------,------------,-------- \n
----,---------,-------,-------------,--------------------,-----------,------------,-------- \n

Notes: For practical purposes the commas(,) generated in the API response were replaced by underscores(_)

SO: Linux (pending modify GetPaths subprocess for be able on windows and others SO)

Instructions for Modify Parameters:
1) Const.py file keep the parameters.
2) For replace questions request modify the questions String const.
3) In case that you modify the titles, modify the headerQuestions String const.
4) For rename the resulting file you can modify the fileCSV String const.
5) For change the folder relative path modify the folderPath String const.