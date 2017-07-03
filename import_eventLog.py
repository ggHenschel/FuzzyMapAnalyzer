import csv



def import_eventlog(path):
    file = open(path)
    read = csv.reader(file,delimiter=";")
    rows = []

    for row in read:
        rows.append(row)

    eventos_por_caso = {"0":[(0,0)]}

    for row in rows[1:]:
        case = str(row[0])
        evento = row[1]
        timestampe = row[2]
        if case in eventos_por_caso:
            nx = eventos_por_caso[case]
            nx.append((evento,timestampe))
        else:
            eventos_por_caso[case]= [(evento,timestampe)]

    eventos_por_caso.pop("0")
    return  eventos_por_caso