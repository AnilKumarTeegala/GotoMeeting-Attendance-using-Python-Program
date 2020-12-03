from pandas import read_csv, read_excel

def split_name(df, sep):
    return [[name[0].split(sep)[0].strip().strip('()'), name[1]] for name in df.values]

def csv(file_path):
    df = read_csv(file_path)
    # Converting all the roll numbers to capital 
    df['Roll Number'] = df['Roll Number'].str.upper()
    return df

def excel(filepath):
    df = read_excel(filepath, skiprows = 6)[['Name','Time in Session (minutes)']]
    
    # Converting all the roll numbers to capital 
    df['Name'] = df['Name'].str.upper()
    
    # Grouping all the rejoined students if any and calculating total time in the session
    df = df.groupby('Name').sum().reset_index()
    return df