import re
def formatCSVanswer(text):
    modified_text = text.replace(",", "_")
    modified_text = re.sub(r'(?<!^)(\d+)\?', r',', modified_text)
    return modified_text[2:]