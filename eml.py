import re
import os
import email

path = 'C:/Users/dakota/Downloads/'  ## TODO: browse file option

def extract_text(eml):
    m = email.message_from_file(eml)
    if m.is_multipart():
        for part in m.get_content_type():
            if part == 'text/plain':
                obj = part.get_payload(decode=True)
                #parser = BytesParser()
                #print(parser.parsebytes(obj))
                print(obj)  ## TODO: Parse better?




for file in os.walk(path):
    if re.search(r'*.eml', files):
        f = open(file)  ## TODO: browse files option
    extract_text(f)
