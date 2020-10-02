import re
import pandas as pd

#Defining all the regular expressions
rx_dict = {
    #r ahead of string makes it raw string
    'school': re.compile(r'School = (?P<school>.*)\n'),
    'grade': re.compile(r'Grade = (?P<grade>\d+)\n'),
    'name_score': re.compile(r'(?P<name_score>Name|Score)'),
}

#line parser
def _parse_line(line):
    """
    Do regex search against all defined regexes
    return key and match result of first matching regex

    """

    for key, rx in rx_dict.items():
        match = rx.search(line)
        if match:
            return key, match
    #if there are no matches
    return None, None

#file parser
def parse_file(filepath):
    """
    Parameters:
        filepath : str
            Filepath to be parsed

    Returns
        data : pd.Dataframe
            Parsed data
    """

    data = []  # create an empty list to collect the data
    # open the file and read through it line by line

    with open(filepath, 'r') as file_object:
        line = file_object.readline()
        while line:

            #check for match with regex at each line
            key, match = _parse_line(line)

            if key == 'school':
                school = match.group('school')

            if key == 'grade':
                grade = match.group('grade')
                grade = int(grade)

            if key == 'name_score':
                value_type = match.group('name_score')
                line = file_object.readline()

                while line.strip():
                    number, value = line.strip().split(',')
                    value = value.strip()

                    row = {
                        'School' : school,
                        'Grade' : grade,
                        'Student number' : number,
                        value_type: value
                    }

                    data.append(row)
                    line = file_object.readline()

            line = file_object.readline()
        # data is a dict of values
        print(data)
        # create a pandas DataFrame from the list of dicts
        data = pd.DataFrame(data)
        # set the School, Grade, and Student number as the index
        data.set_index(['School', 'Grade', 'Student number'], inplace=True)
        # consolidate df to remove nans
        data = data.groupby(level=data.index.names).first()
        # upgrade Score from float to integer
        data = data.apply(pd.to_numeric, errors='ignore')
    return data

if __name__ == '__main__':
    filepath = 'sample.txt'
    data = parse_file(filepath)
    print(data)
