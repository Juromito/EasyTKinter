import easytkinter as etk

etk.window(400, 300, "My window")

etk.rlabel("Hello!")
etk.rbutton("Exit", command=lambda: etk.root.destroy())

etk.run()
