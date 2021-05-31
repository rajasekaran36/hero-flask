import gspread

def gps():
    gc = gspread.service_account(filename='cre.json')
    wb = gc.open("datapoint")
    ws = wb.get_worksheet(0)
    return ws.get_all_values()