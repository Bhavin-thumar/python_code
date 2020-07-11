import os
print(os.getcwd())

os.chdir(r'C:\Users\hardip thummar\Documents\Python Scripts\File_renaming_sample')

print(os.getcwd())
for file in os.listdir():
    file_name, ext = os.path.splitext(file)
    title, course_name, num = file_name.split('-')
    new_name = f'{num[1:].zfill(2)}-{title}-{course_name}'
    print(new_name)