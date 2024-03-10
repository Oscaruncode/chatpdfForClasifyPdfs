import re
def formatCSVanswer(text):
    print(text)
    modified_text = text.replace(",", "_")
    modified_text = re.sub(r'(?<!^)(\d+)\?', r',', modified_text)
    print(modified_text)
    return modified_text[2:]