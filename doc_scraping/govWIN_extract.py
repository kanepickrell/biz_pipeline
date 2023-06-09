# import os
# import PyPDF2
# import regex as re

# folder_path = 'artifacts'
# search_items_file = 'search_items.txt'

# # Read search items from the file
# search_items = []
# with open(search_items_file, 'r') as file:
#     for line in file:
#         search_items.append(line.strip())

# # Iterate over all files in the folder
# for file_name in os.listdir(folder_path):
#     if file_name.endswith('.pdf'):  # Only consider PDF files
#         file_path = os.path.join(folder_path, file_name)
#         # Open the PDF file in read-binary mode
#         with open(file_path, 'rb') as pdf_file:
#             pdf_reader = PyPDF2.PdfReader(pdf_file)

#             # Process the PDF file
#             # Extract and handle the data from each PDF file

#             data_points = {}

#             for page_number in range(len(pdf_reader.pages)):
#                 page = pdf_reader.pages[page_number]
#                 text = page.extract_text()

#                 for search_item in search_items:
#                     match = re.search(search_item + r':\s*(.*)', text)
#                     if match:
#                         data_points[search_item] = match.group(1)

#             print("File:", file_name)
#             for field, value in data_points.items():
#                 print(field + ":", value)
#             print()

#         pdf_file.close()




import os
import PyPDF2
import regex as re

folder_path = 'artifacts'
search_items_file = 'search_items.txt'

# Read search items from the file
search_items = []
with open(search_items_file, 'r') as file:
    for line in file:
        search_items.append(line.strip())

# Iterate over all files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.pdf'):  # Only consider PDF files
        file_path = os.path.join(folder_path, file_name)
        # Open the PDF file in read-binary mode
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Process the PDF file
            # Extract and handle the data from each PDF file

            print("File:", file_name)
            for page_number in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_number]
                text = page.extract_text()

                for search_item in search_items:
                    pattern = r'(^.*?' + re.escape(search_item) + r'.*$)'
                    matches = re.findall(pattern, text, flags=re.MULTILINE)
                    if matches:
                        
                        for match in matches:
                            print(match.strip())
                        print()

        pdf_file.close()
