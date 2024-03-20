import sys
import markdown

action = sys.argv[1]
imput_file = sys.argv[2]
output_file = sys.argv[3]

with open(imput_file, 'r') as file:
    data = file.read()

html = markdown.markdown(data)

with open(output_file, 'w') as file:
    file.write(html)
