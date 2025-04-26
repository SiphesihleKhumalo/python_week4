input_file ="Sample.txt"
output_file = "Output.txt"

with open(input_file, 'r') as file:
    content = file.read()
    # print(content)
    
modified_content = content.upper()
with open(output_file, 'w') as file:
    file.write(modified_content)
    print(modified_content)