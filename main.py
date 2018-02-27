import sys
import analyser


if len(sys.argv)==1:

    print("Running in Graphical Interface")

    #import tkMenu
    #M = tkMenu.GUIFactory().create()
    import QtGUI
    M = QtGUI.AppMainWindow()
elif len(sys.argv)==2:
    import textMenu
    An = analyser.Analiser(sys.argv[1])
    M = textMenu.TextMenu(An)
elif len(sys.argv)==3:
    import textMenu
    An = analyser.Analiser(sys.argv[1])
    log = sys.argv[2]
    M = textMenu.TextMenu(An,log)
elif len(sys.argv)==4:
    import textMenu
    An = analyser.Analiser(sys.argv[1])
    log = sys.argv[2]
    AttLog = sys.argv[3]
    M = textMenu.TextMenu(An, log, AttLog)

M.run()


