import os

if os.path.exists("TopK.txt"):
    os.remove("TopK.txt")

seq1File, seq2File, rndFile = open("seq1.txt"), open("seq2.txt"), open("rnd.txt")
seq1_all_lines, seq2_all_lines = seq1File.readlines(), seq2File.readlines()
output = open("TopK.txt", "a")
totalScoreMap = {}
printMap = {}
seq1Idx, seq2Idx = 0, 0
seq1 = True

while seq1Idx < len(seq1_all_lines) or seq2Idx < len(seq2_all_lines):
    if seq1:
        lineSplit = seq1_all_lines[seq1Idx].strip().split(" ")
        id, score = int(lineSplit[0]), float(lineSplit[1])
        seq1Idx += 1
        if id not in totalScoreMap:
            totalScoreMap[id] = score
        else:
            totalScoreMap[id] += score
    else:
        lineSplit = seq2_all_lines[seq2Idx].strip().split(" ")
        id, score = int(lineSplit[0]), float(lineSplit[1])
        seq2Idx += 1
        if id not in totalScoreMap:
            totalScoreMap[id] = score
        else:
            totalScoreMap[id] += score

    seq1 = not seq1

for x in rndFile:
    x = x.strip().split(" ")
    totalScoreMap[int(x[0])] += float(x[1])

for key, value in totalScoreMap.items():
    value = round(value, 2)
    if value not in printMap:
        printMap[value] = [key]
    else:
        printMap[value].append(key)

printMap = dict(sorted(printMap.items(), key=lambda item: item[0], reverse=True))

for key, value in printMap.items():
    for x in value:
        # output.write(f"{x}: {key}\n")
        output.write(f"{key}\n")