import os
import PyPDF2
import re
import doc_scraping.regex_vars as regex_vars

folder_path = 'artifacts'

# Iterate over all files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.pdf'):  # Only consider PDF files
        file_path = os.path.join(folder_path, file_name)
        # Open the PDF file in read-binary mode
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            

            # Process the PDF file
            # extract and handle the data from each PDF file

            data_points = []
            for page_number in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_number]  # Use pages[page_number] instead of getPage(page_number)
                text = page.extract_text()

                prop_match = re.search(regex_vars.proposal_regex, text)
                if prop_match:
                    proposal = prop_match.group(1)
                    data_points.append(("Value:", proposal))

                desc_match = re.search(regex_vars.description_regex, text)
                if desc_match:
                    description = desc_match.group(1)
                    data_points.append(("Description", description))

                date_match = re.search(regex_vars.date_regex, text)
                if date_match:
                    date = date_match.group(1)
                    data_points.append(("Date", date))

                time_match = re.search(regex_vars.due_time_regex, text)
                if time_match:
                    dt = time_match.group(1)
                    data_points.append(("Due Date", dt))

                rec_date_match = re.search(regex_vars.recording_date_regex, text)
                if rec_date_match:
                    rd = rec_date_match.group(1)
                    data_points.append(("Recording Date", rd))

                rec_time_match = re.search(regex_vars.recording_time_regex, text)
                if rec_time_match:
                    rt = rec_time_match.group(1)
                    data_points.append(("Recording Time", rt))

        pdf_file.close()

        for field, value in data_points:
            print(field + ":", value)

        print("\nTotal data points:", len(data_points))
