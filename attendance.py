from pandas import read_csv, read_excel

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
