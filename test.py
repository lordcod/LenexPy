from lenexpy import fromfile, tofile
path = r"C:\Users\2008d\Downloads\20260125_Брасс.lxf"

tofile(fromfile(path), "output.xml")
