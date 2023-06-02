import sys
import array
from heapq import *

if len(sys.argv) < 2:
    raise Exception(
        "You need to provide all arguments (python3 TopK.py [value of K]")

k = int(sys.argv[1])

seq1File, seq2File, rndFile = open("seq1.txt"), open("seq2.txt"), open("rnd.txt")
seq1_all_lines, seq2_all_lines = seq1File.readlines(), seq2File.readlines()
seq1Idx, seq2Idx = 0, 0
R = array.array("d", [])
objMap = {}
seq1 = True
minHeap = []
seq1Last, seq2Last = 0, 0
T = 0
NumOfAccess = 0


def extractInfo(string):
    infoArr = string.strip().split(" ")
    return int(infoArr[0]), float(infoArr[1])


def hasLargerElement():
    TopKList = list(item[1] for item in minHeap)
    for key in objMap.keys():
        if key in TopKList:
            continue
        if 0 in objMap[key]:
            upperBound = sum(objMap[key]) + (seq1Last if objMap[key].index(0) == 0 else seq2Last)
            if upperBound > minHeap[0][0]:
                return True
    return False


for i, line in enumerate(rndFile):
    id, score = extractInfo(line)
    R.insert(id, score)

while seq1Idx < len(seq1_all_lines) or seq2Idx < len(seq2_all_lines):
    NumOfAccess += 1

    if seq1:
        id, score = extractInfo(seq1_all_lines[seq1Idx])
        seq1Idx += 1
        seq1Last = score
    else:
        id, score = extractInfo(seq2_all_lines[seq2Idx])
        seq2Idx += 1
        seq2Last = score

    if id not in objMap:
        objMap[id] = [score + R[id], 0] if seq1 else [0, score + R[id]]
    else:
        objMap[id][0 if seq1 else 1] = score + sum(objMap[id])

    if len(objMap) == k:
        for key, value in objMap.items():
            minHeap.append((sum(value) if 0 in value else max(value), key))
        heapify(minHeap)
    elif len(minHeap) > 0:
        objVal = max(objMap[id])
        if objVal > minHeap[0][0]:
            HeapList = list(item[1] for item in minHeap)
            if id not in HeapList:
                heapreplace(minHeap, (objVal, id))
            else:
                if objVal > minHeap[HeapList.index(id)][0]:
                    minHeap.pop(HeapList.index(id))
                    heapify(minHeap) # after deletion, the heap structure changes.
                    heappush(minHeap, (objVal, id))

        T = seq1Last + seq2Last + 5.0
        if T <= minHeap[0][0]:
            if not hasLargerElement():
                break

    seq1 = not seq1

print(f"Number of sequential accesses= {NumOfAccess}")
print("Top k objects:")
for x in nlargest(k, minHeap):
    print(f"{x[1]}: {round(max(objMap[x[1]]), 2)}")