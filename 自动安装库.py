import os
libs ={"numpu","matplotlib","pillow","sklearn","requests",\
       "beautifulsoup4","wheel","networkx","sympy","pyinstaller",\
       "django","flask","werobot","pyqt5","pandas","pyopengl","docopt",\
       "pygame"}
try:
    for lib in libs:
        os.system("pip install"+lib)
    print("Successful")
except:
    print("Failed Somehow")
