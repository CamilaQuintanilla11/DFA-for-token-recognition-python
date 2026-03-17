def lexerAritmetico(archivo):
    try: 
        with open (archivo) as f:
            for line in f: 
                line = line.strip()

                if line == "":
                    continue

                myDfa(line)

    except FileNotFoundError:
        print("no se leyó el archivo correctamente")

