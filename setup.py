import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\maury\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\maury\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

executables = [cx_Freeze.Executable("LanguageTranslator.py", base=base, icon="lang.ico")]


cx_Freeze.setup(
    name = "Language Translator",
    options = {"build_exe": {"packages":["tkinter","os","googletrans"], "include_files":["lang.ico",'tcl86t.dll','tk86t.dll']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )