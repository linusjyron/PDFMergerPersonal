import PyPDF2
import sys
import os

num_files = int(input("How many files do you want to merge? "))
pdf_files = []
for i in range(num_files):
    file_name = input("Enter the name of file {}: ".format(i+1))
    pdf_files.append(file_name)

pdf_writer = PyPDF2.PdfWriter()

for file_name in pdf_files:
    with open(file_name, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

merged_file_name = input("Enter the name of the merged file: ")
with open(merged_file_name, 'wb') as merged_file:
    pdf_writer.write(merged_file)
    print("Merged file saved successfully!")

if os.path.exists(merged_file_name):
    if sys.platform.startswith('darwin'):
        os.system("open " + merged_file_name)
    elif os.name == 'nt':
        os.startfile(merged_file_name)
    elif os.name == 'posix':
        os.system("xdg-open " + merged_file_name)
else:
    print("Error: Merged file was not created!")