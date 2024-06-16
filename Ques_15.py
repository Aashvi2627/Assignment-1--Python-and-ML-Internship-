import csv
filename = 'C:\Users\sande\Downloads\CallVoiceQuality_Data_2018_May.csv.xlsx'
with open(filename, mode='r') as file:
    csv_reader = csv.reader(file)