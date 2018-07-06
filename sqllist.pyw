# python2.7
#formats for oracle lists

import pyperclip
text = str(pyperclip.paste()).strip()

lines = text.split('\n')
for i in range(len(lines)):
    if (i+1) < len(lines):
        lines[i] = str('\'')+str(lines[i]).replace("\r","").replace("\n","") + str('\',')
    elif (i+1) == len(lines):
        lines[i] = str('\'')+str(lines[i]).replace("\r","").replace("\n","")+ '\''
text =  '(' + '\n'.join(lines) + ')'

pyperclip.copy(text)
