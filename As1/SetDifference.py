rFile = open("R.tsv")
sFile = open("S.tsv")
output = open("RdifferenceS.tsv", "a")
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
            output.write(f"{key}    {value}\n")
            read = False
            break

        sIndex += 1
        read = True

        if key == sKey and value == sValue:
            break
        elif key == sKey:
            output.write(f"{key}    {value}\n")
            break

    if sIndex >= 300:
        output.write(f"{key}    {value}\n")


output.close()