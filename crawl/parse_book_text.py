import os
import re 

base_path = "datas"
text_files = [f for f in os.listdir(base_path) if f.split('.')[-1]=="txt"]
target_file = text_files[0]

text_path = os.path.join(base_path, text_files[0])
with open(text_path, "rt") as f:
    text = f.read()

head_body = text.split("\n\n\n")[0]
#print(head_body[:500])
body_with_ex = re.split(r"-{10,}", head_body)[-1]
#print(body_with_ex)

#sections = [b for b in body_with_ex.split('\n\n') if len(b.split("\n")) > 2]
#print(sections)

plackets = r"\[[^\[]*\]"
zen_plackets = r"［[^［]*］"
body = re.sub(plackets, "", body_with_ex)
body = re.sub(zen_plackets, "", body_with_ex)
print(len(body))

os.makedirs(os.path.join(base_path, "processed"))
with open(os.path.join(base_path,"processed", target_file), "wt") as f:
    f.write(body)