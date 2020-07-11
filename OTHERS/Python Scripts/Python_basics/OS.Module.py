import os


os.chdir(r'C:\Users\hardip thummar\Documents\Python Scripts\File_renaming_sample')
print(os.getcwd())


for f in os.listdir():
    f_name, ext = os.path.splitext(f)
    title, course_name, f_num = f_name.split('-')
    title = title.strip()
    course_name = course_name.strip()
    f_num = f_num.strip()[1:].zfill(2)
    rename_file = '{}-{}-{}{}'.format(f_num, title, course_name, ext)
    print(rename_file)