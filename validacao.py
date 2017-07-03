import matplotlib.pyplot as plt
import import_adjacency
import import_eventLog
import replay

def re():
    Graph = import_adjacency.import_full_graph("Afastados20160902.xml")

    eventLog = import_eventLog.import_eventlog("na.csv")

    report = replay.replay_log(eventLog,Graph)

    replay.write_report(report)

def perc_test(xml_path,event_log_path):
    Graph = import_adjacency.import_full_graph(xml_path)

    eventLog = import_eventLog.import_eventlog(event_log_path)

    report = replay.replay_log_perc(eventLog,Graph)

    return report

def validacao():
    list = []
    r100p100 = perc_test("100p100/Afastados20160902.xml","Afastados20160902_Legenda.csv")
    list.append((100,100,r100p100))
    r100p75 = perc_test("100p75/Afastados20160902.xml","Afastados20160902_Legenda.csv")
    list.append((100,75,r100p75))
    r100p50 = perc_test("100p50/Afastados20160902.xml","Afastados20160902_Legenda.csv")
    list.append((100,50,r100p50))
    r100p25 = perc_test("100p25/Afastados20160902.xml","Afastados20160902_Legenda.csv")
    list.append((100,25,r100p25))
    r100p0 = perc_test("100p0/Afastados20160902.xml","Afastados20160902_Legenda.csv")
    list.append((100,0,r100p0))
    r75p100 = perc_test("75p100/Afastados20160902.xml","Afastados20160902_Legenda.csv")
    list.append((75,100,r75p100))
    r75p75 = perc_test("75p75/Afastados20160902.xml","Afastados20160902_Legenda.csv")
    list.append((75,75,r75p75))
    r75p50 = perc_test("75p50/Afastados20160902.xml","Afastados20160902_Legenda.csv")
    list.append((75,50,r75p50))
    r75p25 = perc_test("75p25/Afastados20160902.xml","Afastados20160902_Legenda.csv")
    list.append((75,25,r75p25))
    r75p0 = perc_test("75p0/Afastados20160902.xml","Afastados20160902_Legenda.csv")
    list.append((75,0,r75p0))
    r50p100 = perc_test("50p100/Afastados20160902.xml","Afastados20160902_Legenda.csv")
    list.append((50,100,r50p100))
    r50p75 = perc_test("50p75/Afastados20160902.xml","Afastados20160902_Legenda.csv")
    list.append((50,75,r50p75))
    r50p50 = perc_test("50p50/Afastados20160902.xml","Afastados20160902_Legenda.csv")
    list.append((50,50,r50p50))
    r50p25 = perc_test("50p25/Afastados20160902.xml","Afastados20160902_Legenda.csv")
    list.append((50,25,r50p25))
    r50p0 = perc_test("50p0/Afastados20160902.xml","Afastados20160902_Legenda.csv")
    list.append((50,0,r50p0))
    r25p100 = perc_test("25p100/Afastados20160902.xml","Afastados20160902_Legenda.csv")
    list.append((25,100,r25p100))
    r25p75 = perc_test("25p75/Afastados20160902.xml","Afastados20160902_Legenda.csv")
    list.append((25,75,r25p75))
    r25p50 = perc_test("25p50/Afastados20160902.xml","Afastados20160902_Legenda.csv")
    list.append((25,50,r25p50))
    r25p25 = perc_test("25p25/Afastados20160902.xml","Afastados20160902_Legenda.csv")
    list.append((25,25,r25p25))
    r25p0 = perc_test("25p0/Afastados20160902.xml","Afastados20160902_Legenda.csv")
    list.append((25,0,r25p0))

    csv_report = open("case_analisys.csv",mode="w")

    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')

    for (nodes,paths,(cases,failed_cases,sequences,failed_sequences)) in list:
        event_p = (nodes,paths,failed_cases/cases,failed_sequences/sequences)
        print(event_p)
        line = str(nodes)+";"+str(paths)+";"+str(failed_cases/cases)+";"+str(failed_sequences/sequences)+"\n"
        csv_report.write(line)
        ax.scatter(nodes,paths,failed_cases/cases,c="r")
        ax.scatter(nodes, paths, failed_sequences/sequences, c="b")

    plt.show()

    csv_report.close()