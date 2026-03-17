def lexerAritmetico(archivo):
    with open (archivo) as f:
        for line in f: 
            line = line.strip()

            if line == "":
                continue
