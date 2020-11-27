import os
import re

root = "_posts"

file_list = [os.path.join(root,x) for x in os.listdir(root) if os.path.isfile(os.path.join(root,x))]
for path in file_list:
    print("handle {}".format(path))
    with open(path,'r',encoding='utf-8') as f:
        content = f.readlines()
    for i,line in enumerate(content):
        m = re.match(r"!\[(.*?)\]\((.*?)\)",line)
        if m is not None:
            pic_name = os.path.split(m.group(2))[-1]
            content[i] = "{% asset_img " + pic_name +  " %}\n"
    # print(m)
    # print("".join(content))
    with open(path,'w',encoding='utf-8') as f:
        f.write("".join(content))
    # break
