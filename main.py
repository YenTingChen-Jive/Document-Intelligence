import os
static_directory = 'static/'
if not os.path.exists(static_directory):
    os.makedirs(static_directory)

import speech_recognition as sr
from gtts import gTTS
import fitz  # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def list_microphones():
    mic_list = sr.Microphone.list_microphone_names()
    for i, mic in enumerate(mic_list):
        print(f"Microphone {i + 1}: {mic}")

list_microphones()

# Step 1: Speech Recognition
def record_speech():
    # Replace 'your_microphone_name' with the actual name of your microphone
    microphone_name = 0
    
    recognizer = sr.Recognizer()

    print("Before recording...")

    # Specify the source using the microphone name
    with sr.Microphone(device_index=microphone_name) as source:
        print("Say something:")
        audio = recognizer.listen(source)

    print("After recording...")

    try:
        Text = recognizer.recognize_google(audio, language="zh-TW")     
              ##將剛說的話轉成  zh-TW 繁體中文 的 字串
        print("You said:", Text)
        return Text
    except recognizer.UnknowValueError:
        Text = "無法翻譯"
        return Text
    except sr.RequestError as e:
        Text = "無法翻譯{0}".format(e)
        return Text


def extract_tables_from_pdf(pdf_path, num_columns):
    tables = [[]]

    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text = page.get_text()

    # Split the text into lines
        lines = text.split('\n')

    in_table = False
    table_start = None
    table_end = None
    next_start = None
    table_count = 0
    
    for i, line in enumerate(lines):
        if line.startswith("ai_tables_#") and in_table == False:
            in_tables = True
            table_start = i + 1
            for j in range(i + 1, len(lines)):
                if lines[j].startswith("ai_tables_#"):
                    next_start = j
                    break
            for n in range(i + 2, i + )
            tables[table_count].append()
            table_count += 1


    print(text)
    return 



"""
def extract_tables_from_pdf(pdf_path, num_columns):
    tables = []

    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text = page.get_text()

        # Split the text into lines
        lines = text.split('\n')

        # Identify the start and end of each table
        in_table = False
        table_start = None
        table_end = None

        for i, line in enumerate(lines):
            if line.startswith("ai_tables_#") and in_table == False:
                # If the line starts with "ai_tables_#", it's the title of a table
                in_table = True
                table_start = i + 1
            elif line.startswith("ai_tables_#") and in_table == True:
                in_table = False
                table_end = i - 1
                break

        # print(table_start, table_end)
        if table_start is not None and table_end is not None:
            # Extract the table content between table_start and table_end
            table_lines = lines[table_start:table_end + 1]

            # Group lines into rows based on the dynamically determined number of columns
            table_rows = [table_lines[i:i + num_columns] for i in range(0, len(table_lines), num_columns)]

            # Concatenate rows to form the table text
            table_text = '\n'.join(['\t'.join(row) for row in table_rows]).strip()
            tables.append(table_text)

    pdf_document.close()  # Close the PDF document to release resources
    print(tables)
    return tables
"""
# Step 2: Database Processing


# Step 3: Looking for the table desired
def find_closest_table(question, tables):
    # Use TF-IDF Vectorizer to convert the question and table text into vectors
    vectorizer = TfidfVectorizer()
    question_vector = vectorizer.fit_transform([question])
    table_vectors = [vectorizer.transform([table[1]]) for table in tables]

    # Calculate cosine similarity between the question and each table
    similarities = [cosine_similarity(question_vector, table_vector).item() for table_vector in table_vectors]

    # Find the index of the table with the highest similarity
    closest_table_index = np.argmax(similarities)

    # Return the title and text of the closest table
    return tables[closest_table_index]

# Step 4: Print Out the Table
def format_and_output_tables(matching_tables):
    for table in matching_tables:
        print("Table:")
        print(table)
        print("\n---\n")

# Step 5: Text-to-Speech
def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")

# Step 6: Speak Out
def speak_out():
    os.system("start output.mp3")  # This command might be platform-dependent


# Main
def main():
    pdf_path = "database.pdf"
    question = record_speech()

    if question:
        tables = extract_tables_from_pdf(pdf_path, 4)
        matching_tables = find_closest_table(question, tables)

        if matching_tables:
            print("Closest Table Title:", matching_tables[0])
            print("Closest Table Text:", matching_tables[1])
            format_and_output_tables(matching_tables)
            # Convert information to speech
            text_to_speech("I found some relevant information in the database.")
            # Speak out the information
            speak_out()

if __name__ == "__main__":
    main()
