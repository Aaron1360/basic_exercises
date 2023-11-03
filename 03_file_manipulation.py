"""3. **File Manipulation**: Write a program to read a text file, count the occurrences of each word, and create a summary report.
"""
# Function to read a text file and count word occurrences
def count_word_occurrences(file_path):
    word_count = {}
    with open(file_path,"r") as file:
        for line in file:
            words = line.split()
            for word in words:
                # Remove punctuation and convert to lowercase
                word = word.strip('.,!?"+*:;()[]')
                if not word.isdigit():
                    word = word.lower()
                    if word not in word_count:
                        word_count[word] = 1
                    else:
                        word_count[word] += 1
    return word_count

# Function to create a summary report
def create_summary_report(word_count, report_file):
    with open(report_file,"w") as report:
        for word,count in word_count.items():
            report.write(f"{word}: {count}\n")
        
# File paths
input_file = '/home/remote/Documents/python_dev/basic_exercises_GPT/text.txt'  # Replace with your input file
output_file = 'summary_report.txt'  # Replace with your desired output file

# Count word occurrences and create a summary report
word_count = count_word_occurrences(input_file)
create_summary_report(word_count, output_file)
