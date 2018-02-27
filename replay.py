import csv
import datetime
import os.path
import time
import sys

def replay_case(case,Graph):

    transformedEventsSeq = []
    auxitem = case[1][0]
    for n in range(1, len(case[1])):
        item = case[1][n]
        # print(item[1])
        t1 = datetime.datetime.strptime(item[1], "%Y-%m-%d %H:%M:%S.000")  # remoção dos milisegundos
        # print(t1)
        t2 = datetime.datetime.strptime(auxitem[1], "%Y-%m-%d %H:%M:%S.000")
        delta = t1 - t2
        # print(delta)
        vectorofEvent = (auxitem[0], item[0], delta)
        transformedEventsSeq.append(vectorofEvent)
        auxitem = item

    # print(transformedEventsSeq)

    Approval = True
    Annotations = []

    for (eventOrigem, eventDestino, tempo) in transformedEventsSeq:
        if Graph.has_edge(eventOrigem, eventDestino):
            meanTime = datetime.timedelta(milliseconds=Graph.get_edge_data(eventOrigem, eventDestino)['meanTime'])

            try: #Se houver os atributos max e min ele irá assumir
                limite_inferior = datetime.timedelta(milliseconds=Graph.get_edge_data(eventOrigem, eventDestino)['minTime'])
                limite_sup = datetime.timedelta(milliseconds=Graph.get_edge_data(eventOrigem, eventDestino)['maxTime'])
            except: #Se não houver os atributos usará os limites como 70% acima e abaixo
                limite_sup = 1.7 * meanTime  # Substituir por Tempo Maximo
                limite_inferior = 0.3 * meanTime  # Substituir por Tempo Minimo

            if tempo > limite_sup or tempo < limite_inferior:
                Approval = False
                an = "-- Reprovado por tempo Inadequado -- " + "Tempo entre eventos " + eventOrigem + " e " + eventDestino + " :" + str(
                    tempo) + ". Tempo esperado em Média:" + str(meanTime)
                Annotations.append(an)
        else:
            Approval = False
            an = "-- Reprovado por sequencia Inadequada" + " -- Evento: " + eventOrigem + " procedido de " + eventDestino
            Annotations.append(an)

    CaseResolution = (case[0], Approval, Annotations)

    return CaseResolution

def replay_log(eventLog,Graph):
    results = []
    for (case,eventSeq) in eventLog.items():
        dummyCase = (case,eventSeq)
        results.append(replay_case(dummyCase,Graph))
    return results

def write_report(report):
    report.sort()

    text = ""
    nPositivos = 0
    nFalsos = 0
    positivos = ""
    falsos = ""
    for (case, caseDecision, Annotations) in report:
        print("Caso: ", case, " Aprovado: ", caseDecision)
        text += "Caso: " + case + " Aprovado: " + str(caseDecision) + "\n"
        if caseDecision:
            print("-")
            nPositivos += 1
            positivos = positivos + case + "; "
        else:
            nFalsos += 1
            falsos = falsos + case + "; "
            for annotation in Annotations:
                print("\t", annotation)
                text += "\t" + annotation + "\n"
        print("\n")
        text += "\n"

    resumo = "Numero de Positivos: " + str(nPositivos) + "\n" + "Casos: " + positivos + "\n\nNumero de Falsos: " + str(
        nFalsos) + "\nCasos: " + falsos + "\n\n\n" + text

    report = open("report " + time.asctime() + ".txt", mode='w')
    report.write(resumo)
    report.close()

def replay_case_perc(case,Graph):
    transformedEventsSeq = []
    auxitem = case[1][0]
    for n in range(1, len(case[1])):
        item = case[1][n]
        # print(item[1])
        t1 = datetime.datetime.strptime(item[1], "%Y-%m-%d %H:%M:%S.000")  # remoção dos milisegundos
        # print(t1)
        t2 = datetime.datetime.strptime(auxitem[1], "%Y-%m-%d %H:%M:%S.000")
        delta = t1 - t2
        # print(delta)
        vectorofEvent = (auxitem[0], item[0], delta)
        transformedEventsSeq.append(vectorofEvent)
        auxitem = item

    # print(transformedEventsSeq)

    Approval = True
    Annotations = []
    n_seq = 0
    n_seq_fail = 0
    for (eventOrigem, eventDestino, tempo) in transformedEventsSeq:
        n_seq+=1
        if Graph.has_edge(eventOrigem, eventDestino):
            meanTime = datetime.timedelta(milliseconds=Graph.get_edge_data(eventOrigem, eventDestino)['meanTime'])

            try:  # Se houver os atributos max e min ele irá assumir
                limite_inferior = datetime.timedelta(
                    milliseconds=Graph.get_edge_data(eventOrigem, eventDestino)['minTime'])
                limite_sup = datetime.timedelta(milliseconds=Graph.get_edge_data(eventOrigem, eventDestino)['maxTime'])
            except:  # Se não houver os atributos usará os limites como 70% acima e abaixo
                #print("Debug Line 1 replay.py function replay_case_perc")
                limite_sup = 1.7 * meanTime  # Substituir por Tempo Maximo
                limite_inferior = 0.3 * meanTime  # Substituir por Tempo Minimo

            if tempo > limite_sup or tempo < limite_inferior:
                #Approval = False
                an = "-- Reprovado por tempo Inadequado -- " + "Tempo entre eventos " + eventOrigem + " e " + eventDestino + " :" + str(
                    tempo) + ". Tempo esperado em Média:" + str(meanTime)
                Annotations.append(an)
        else:
            n_seq_fail+=1
            Approval = False


    CaseResolutionPerc = (Approval, n_seq, n_seq_fail)

    return CaseResolutionPerc

def replay_log_perc(eventLog,Graph):
    cases_t=0
    fail_cases=0
    n_seq_t=0
    n_seq_fail_t=0
    for (case,eventSeq) in eventLog.items():
        dummyCase = (case,eventSeq)
        (Approval, n_seq, n_seq_fail) = replay_case_perc(dummyCase,Graph)
        cases_t+=1
        if(Approval==False):
            fail_cases+=1
        n_seq_t+=n_seq
        n_seq_fail_t+=n_seq_fail
    return (cases_t,fail_cases,n_seq_t,n_seq_fail_t)

def export_replay_results(report,file=None):
    name = "report_log " + time.asctime() + ".txt"
    if file is None:
        file = open(name, mode='w')
    file.write("case;aproval;anotation\n")

    for (case,aproval,anotations) in report:
        line = str(case)+";"
        if aproval:
            line+="Conform;"
        else:
            line+="Not Conform;"
        line+="("
        for an in anotations:
            line+=an+" "
        line+=")\n"
        file.write(line)
    file.close()
    return name

def rebuild_event_log(log, replay_result):
    dictq = dict()
    for (case,aproval,anotation) in replay_result:
        if aproval:
            dictq[case]="Conform"
        else:
            dictq[case]="Not Conform"

    name = os.path.basename(log)[0]
    old_log = open(log)
    name = "new_log_of_"+name+".csv"
    new_log= open(name,mode="w")
    read = csv.reader(old_log,delimiter=";")
    lines = []

    for line in read:
        lines.append(line)

    new_log.write(str(lines[0][0])+";"+str(lines[0][1])+";"+str(lines[0][2])+";Conformity\n")
    for line in lines[1:]:
        case = line[0]
        new_log.write(str(line[0])+";"+str(line[1])+";"+str(line[2])+";"+dictq[case]+"\n")

    old_log.close()
    new_log.close()
    return name

def Rebuild_class_log(log, replay_result,delimit=";",case_atribute=0,legend=True):
    dictq = dict()
    for (case, aproval, anotation) in replay_result:
        if aproval:
            dictq[case] = "Conforme"
        else:
            dictq[case] = "Não Conforme"
    file = open(log,encoding="utf-8")
    read = csv.reader(file,delimiter=delimit)
    rows = []

    file.close()

    name = os.path.basename(log)
    name = "new_log_of_"+name+".csv"
    new_log = open(name)

    n_rows = []

    for item in read:
        rows.append(item)

    if legend:
        l = rows[0]
        l.append("Conformidade")
        n_rows.append(l)
        rows.pop(0)

    for row in rows:
        l = row
        l.append(dict[row[case_atribute]])
        n_rows.append(l)

    write_f = csv.writer(new_log,delimiter=delimit)

    for item in n_rows:
        write_f.writerow(item)

    new_log.close()

    return name

def Rebuild_Atributes_Log(log, replay_result,save_path=None,delimit=";",case_atribute=0,legend=True):
    dictq = dict()

    def txdictq(i):
        try:
            return dictq[i]
        except:
            return i

    for (case, aproval, anotation) in replay_result:
        if aproval:
            dictq[case] = "Conforme"
        else:
            dictq[case] = "Não Conforme"
    file = open(log)
    read = csv.reader(file,delimiter=delimit,dialect=csv.excel,)

    if save_path is None:
        name = os.path.basename(log).split(sep=".")[0]
        name = "new_log_of_"+name+" "+time.asctime()+".csv"
        new_log = open(name, mode="x")
    else:
        new_log = save_path
        name = new_log.name
    write_f = csv.writer(new_log, delimiter=delimit, dialect=csv.excel, lineterminator='\n')

    for item in read:
        row = item
        if legend:
            row.append("Conformidade")
            legend = False
        else:
            #print(row[case_atribute] in dictq, txdictq(row[case_atribute]))
            if row[case_atribute] in dictq:
                row.append(dictq[row[case_atribute]])
            else:
                row.append("Not Found")
        write_f.writerow(row)

    file.close()
    new_log.close()

    return name



