rFile = open("R.tsv")
sFile = open("S.tsv")
output = open("RintersectionS.tsv", "a")
sIndex = 0
s_all_lines = sFile.readlines()
sKey, sValue = "", ""
read = True
for i, line in enumerate(rFile):
    splitLine = line.strip().split("	")
    key, value = splitLine[0], splitLine[1]
    while sIndex < 300:
        if read:
            sKey, sValue = s_all_lines[sIndex].strip().split("	")
            print(sKey, sValue)

        if key < sKey:
            read = False
            break

        sIndex += 1
        read = True

        if key == sKey and value == sValue:
            output.write(f"{key}    {value}\n")
            break
        elif key == sKey:
            break

output.close()