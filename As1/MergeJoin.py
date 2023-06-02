rFile = open("R.tsv")
tFile = open("T.tsv")
output = open("RjoinT.tsv", "a")
tIndex = 0
t_all_lines = tFile.readlines()
tKey, tValue = "", ""
read = True
for i, line in enumerate(rFile):
    splitLine = line.strip().split("	")
    key, value = splitLine[0], splitLine[1]
    while tIndex < 1000:
        if read:
            tKey, tValue = t_all_lines[tIndex].strip().split("	")
            #print(tKey, tValue)

        if tKey < key:
            tIndex += 1
        elif tKey != key:
            read = False
            break
        else:
            output.write(f"{key}    {value}    {tValue}\n")
            tIndex += 1
        read = True

output.close()
