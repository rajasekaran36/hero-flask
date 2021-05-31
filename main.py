import datetime
import operator
import io
from os import execlpe, linesep
from student import Student
import csv
from student import Student

def get_all_present(all_students):
    present = []
    for row in all_students:
        if('âœ”' in row):
            present.append(row)
    return present
'''
def get_sheet():
    sheet = []
    with open('data.csv') as input:
        reader = csv.reader(input,delimiter=",")
        for row in reader:
            row_data = []
            for cell in row:
                row_data.append(cell.replace('"','',cell.count('"')).strip())
            sheet.append(row_data)
        return sheet
'''

def get_sheet(data_dump):
    sheet = []
    reader = csv.reader(data_dump,delimiter=",")
    for row in reader:
        row_data = []
        for cell in row:
            row_data.append(cell.replace('"','',cell.count('"')).strip())
        sheet.append(row_data)
    return sheet
        

def get_students(sheet):
    return sheet[4:len(sheet)-4]


def print_list(alist):
    for ele in alist:
        print(ele)

def get_needs(records,list_need_index):
    needs = []
    for record in records:
        need = []
        for index in list_need_index:
            need.append(record[index])
        needs.append(need)
    return needs


def get_duration(start,end):
    a_str = start
    a = datetime.datetime.strptime(a_str, '%H:%M')
    b_str = end
    b = datetime.datetime.strptime(b_str, '%H:%M')
    duration = b-a
    duration_in_minitues = int(duration.total_seconds()/60)
    return duration_in_minitues

def compute_valid_data(ess):
    for row in ess:
        row.append(get_duration(row[1],row[2]))

def get_dict_ess(ess_dict):
    return ess_dict


def rec_to_dict(rec):
    adict = {}
    adict['gmeet_name'] = rec[0]
    adict['joined'] = rec[1]
    adict['exited'] = rec[2]
    adict['duration'] = rec[3]
    return adict


def process(data_dump):
    #print(data_dump)
    f = io.open("dump.csv","w",encoding="utf-8")
    f.write(data_dump)
    f.close()
    print("--------------------------Dump")
    f = open('dump.csv','r')
    data_dump = f.readlines()
    f.close()
    #data_dump = data_dump.splitlines()
    print_list(data_dump)
    sheet = get_sheet(data_dump)
    #print_list(sheet)
    
    all_students = get_students(sheet)
    present_students = get_all_present(all_students)
    ess = get_needs(present_students,[0,4,5])
    compute_valid_data(ess)
    ess_dict = []
    for rec in ess:
        ess_dict.append(rec_to_dict(rec))
    
    ess_dict.sort(key=operator.itemgetter('gmeet_name'))
    
    #print_list(ess_dict)
    return ess_dict


#file = open('data.csv','r');
#data_dump = file.read().splitlines()


