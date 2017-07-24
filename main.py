import sys
import analyser


if len(sys.argv)==1:

    print("Running in Graphical Interface")
    option = input("Type 1 for Tkinter or 2 for kivy")
    if int(option)==1:
        import tkMenu
        M = tkMenu.GUIFactory().create()
    elif int(option)==2:
        import kivyMenu
        M = kivyMenu.SimpleGuiMenuApp()
    else:
        print("Invalid Option")
        quit(-1)
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


