# Logfile -> CSV Formatter
import csv

file_ext = ".txt"

# Extract needed data from logfile to new txt file
def extract_data(log_file, keywordList):
    with open(log_file, 'r') as in_file:
        lines = in_file.readlines()

    with open(log_file, 'w') as out_file:
        for line in lines:
            for word in keywordList:
                if word in line:
                    out_file.write(line)

    with open(log_file, 'r') as in_file:
        for line in in_file:
            print(line)

    return

# Write logfile with extracted data to csv
def data_to_csv(log_file, keywordList):
    csv_file = log_file[:-4] + ".csv"
        
    while True:
        with open(log_file, 'r') as in_file:
            stripped = (line.strip() for line in in_file)
            char = input("Enter char to split logs by: ")
            lines = (line.split(char) for line in stripped if line)
            with open(csv_file, 'w') as out_file:
                writer = csv.writer(out_file)
                writer.writerows(lines)

            with open(csv_file, 'r') as in_file:
                for line in in_file:
                    print(line)
                    
        with open(log_file, 'w') as out_file:
            for line in lines:
                out_file.write(line)
        
        done = input("Are you done with data splitting? (y/n): ")
        if done == "y":
            return
            
    
def main():
    log_file = input("Enter logfile name: ")

    keywords = input("Enter keywords you want extracted (whitespace-separated): ")
    keywordList = keywords.split()

    extract_data(log_file, keywordList)
    data_to_csv(log_file, keywordList)

if __name__=="__main__":
    main()
