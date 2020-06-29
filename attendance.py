from pandas import read_csv, read_excel
import pandas as pd

def split_name(df, sep):
    return [name.split(sep)[0] for name in df]

def filterdf(df, time):
    return df[df['Time in Session (minutes)'] >= time]

def csv(file_path):
    return read_csv(file_path)

def excel(filepath):
        return read_excel(filepath, skiprows = 6)[['Name','Email Address','Time in Session (minutes)']]
    
def remove_trainers(df):
        return [name for name in df if not name.isalpha()]
    
def rollNumber_upper(col):
    return [number.upper() for number in col]

master = csv(input("Enter the original student registered csv path: "))

print(master.head())

goToMeetingAttendanceFile = input("Enter the day Goto Meeting Sheet Path: ")

day4 = excel(goToMeetingAttendanceFile)
print(day4.head())

day4.groupby('Name').sum().reset_index(inplace = True)

req_time = filterdf(day4, 45)

# Spliting the Roll numbers based on -, ' ', _, (
result = split_name(req_time['Name'], '-')
result = split_name(result, ' ')
result = split_name(result, '_')
result = split_name(result, '(')
FinalRollNUmbers = remove_trainers(result)

# Converting all roll numbers to Upper case
FinalRollNUmbers = rollNumber_upper(FinalRollNUmbers)

FinalStudentAttendees = pd.DataFrame(FinalRollNUmbers, columns=['Roll Number'])
FinalStudentAttendees[str(pd.datetime.today().date())] = ['P' for i in range(len(FinalRollNUmbers))]
FinalStudentAttendees.head()

FinalStudentAttendees = pd.merge(master, FinalStudentAttendees, how = 'left', on = 'Roll Number')

FinalStudentAttendees[str(pd.datetime.today().date())].value_counts()

Unknown = pd.merge(master, FinalStudentAttendees, how = 'right', on = 'Roll Number').tail(10)
print("Unknown Roll Numbers", Unknown)

FinalStudentAttendees.fillna('A', inplace=True)

FinalStudentAttendees.to_excel(str(pd.datetime.today().date())+'.xlsx')

print("Sucessfully Output file Generated File name is: ", str(pd.datetime.today().date())+'.xlsx')