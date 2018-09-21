from cx_Freeze import setup, Executable

base = None    

executables = [Executable("main.py", base=base)]

packages = ["idna", "sys", "mysql", "json", "os"]
packages += ["pandas", "pytz", "dateutil", "six", "numpy"]

options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "pyxslxtosql",
    options = options,
    version = "1.0",
    description = 'made by jp',
    executables = executables
)


#set TCL_LIBRARY=C:\Users\JP\AppData\Local\Programs\Python\Python36\tcl\tcl8.6
#set TK_LIBRARY=C:\Users\JP\AppData\Local\Programs\Python\Python36\tcl\tk8.6