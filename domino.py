from random import shuffle
from copy import deepcopy

#LIST_OF_DOMINOES = [(6,6), (6,6), (1,1), (1,1), (4,4), (4,4), (1,3), (1,3), (5,5), (5,5), (3,3), (3,3), (2,2), (2,2), (5,6), (5,6), (4,6), (4,6), (1,6), (1,6), (1,5), (1,5), (3,6), (4,5), (2,6), (3,5), (2,5), (3,4), (1,4), (2,3), (2,4), (1,2)]
lodominoes = [[0, 1, 1, 2], [1, 1, 2, 1], [2, 1, 3, 2], [3, 1, 4, 1], [4, 1, 5, 2], [5, 1, 6, 2], [6, 2, 2, 2], [7, 2, 3, 1], [8, 2, 4, 1], [9, 2, 5, 1], [10, 2, 6, 1], [11, 3, 3, 2], [12, 3, 4, 1], [13, 3, 5, 1], [14, 3, 6, 1], [15, 4, 4, 2], [16, 4, 5, 1], [17, 4, 6, 2], [18, 5, 5, 2], [19, 5, 6, 2], [20, 6, 6, 2]]
flod = [[0, 1, 1], [0, 1, 1], [1, 1, 2], [2, 1, 3], [2, 1, 3], [3, 1, 4], [4, 1, 5], [4, 1, 5], [5, 1, 6], [5, 1, 6], [6, 2, 2], [6, 2, 2], [7, 2, 3], [8, 2, 4], [9, 2, 5], [10, 2, 6], [11, 3, 3], [11, 3, 3], [12, 3, 4], [13, 3, 5], [14, 3, 6], [15, 4, 4], [15, 4, 4], [16, 4, 5], [17, 4, 6], [17, 4, 6], [18, 5, 5], [18, 5, 5], [19, 5, 6], [19, 5, 6], [20, 6, 6], [20, 6, 6]]
lotrios = [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 0, 3], [0, 0, 4], [0, 0, 5], [0, 1, 6], [0, 1, 20], [0, 2, 11], [0, 2, 19], [0, 2, 20], [0, 3, 15], [0, 3, 17], [0, 3, 18], [0, 3, 19], [0, 3, 20], [0, 4, 14], [0, 4, 16], [0, 4, 17], [0, 4, 18], [0, 4, 19], [0, 4, 20], [0, 5, 10], [0, 5, 13], [0, 5, 14], [0, 5, 15], [0, 5, 16], [0, 5, 17], [0, 5, 18], [0, 5, 19], [0, 5, 20], [0, 6, 6], [0, 6, 7], [0, 6, 11], [0, 7, 7], [0, 12, 15], [0, 13, 18], [0, 14, 20], [1, 1, 1], [1, 1, 6], [1, 1, 7], [1, 1, 11], [1, 2, 6], [1, 2, 7], [1, 5, 5], [1, 6, 6], [1, 7, 11], [1, 8, 15], [1, 9, 18], [1, 10, 20], [1, 11, 11], [1, 12, 19], [1, 13, 17], [1, 14, 16], [2, 2, 2], [2, 2, 6], [2, 3, 15], [2, 4, 5], [2, 4, 18], [2, 5, 5], [2, 5, 20], [2, 6, 11], [2, 7, 7], [2, 7, 11], [2, 8, 19], [2, 9, 17], [2, 10, 16], [2, 11, 11], [2, 15, 15], [3, 3, 3], [3, 3, 5], [3, 3, 12], [3, 4, 4], [3, 4, 5], [3, 5, 5], [3, 6, 15], [3, 7, 19], [3, 8, 8], [3, 9, 14], [3, 10, 13], [3, 12, 15], [3, 15, 15], [3, 18, 18], [4, 4, 4], [4, 4, 5], [4, 4, 13], [4, 5, 5], [4, 6, 18], [4, 7, 17], [4, 8, 14], [4, 9, 9], [4, 10, 12], [4, 16, 18], [4, 18, 18], [4, 20, 20], [5, 5, 5], [5, 5, 14], [5, 6, 20], [5, 7, 16], [5, 8, 13], [5, 9, 12], [5, 10, 10], [5, 19, 20], [5, 20, 20], [6, 6, 6], [6, 6, 7], [6, 6, 8], [6, 6, 9], [6, 6, 10], [6, 7, 11], [6, 7, 19], [6, 7, 20], [6, 8, 15], [6, 8, 17], [6, 8, 18], [6, 8, 19], [6, 8, 20], [6, 9, 14], [6, 9, 16], [6, 9, 17], [6, 9, 18], [6, 9, 19], [6, 9, 20], [6, 10, 13], [6, 10, 14], [6, 10, 15], [6, 10, 16], [6, 10, 17], [6, 10, 18], [6, 10, 19], [6, 10, 20], [6, 15, 15], [7, 7, 7], [7, 9, 10], [7, 10, 10], [7, 11, 11], [7, 11, 20], [7, 14, 14], [7, 18, 18], [8, 8, 8], [8, 8, 10], [8, 8, 15], [8, 9, 9], [8, 9, 10], [8, 10, 10], [8, 15, 15], [8, 15, 20], [8, 17, 17], [8, 20, 20], [9, 9, 9], [9, 9, 10], [9, 10, 10], [9, 13, 18], [9, 18, 18], [9, 18, 20], [9, 19, 19], [10, 10, 10], [10, 11, 14], [10, 15, 17], [10, 17, 20], [10, 18, 19], [10, 20, 20], [11, 11, 11], [11, 11, 12], [11, 11, 13], [11, 11, 14], [11, 12, 15], [11, 12, 17], [11, 12, 18], [11, 12, 19], [11, 12, 20], [11, 13, 16], [11, 13, 17], [11, 13, 18], [11, 13, 19], [11, 13, 20], [11, 14, 15], [11, 14, 16], [11, 14, 17], [11, 14, 18], [11, 14, 19], [11, 14, 20], [11, 20, 20], [12, 12, 12], [12, 12, 14], [12, 13, 13], [12, 13, 14], [12, 14, 14], [12, 15, 15], [12, 15, 19], [12, 15, 20], [12, 16, 17], [12, 17, 17], [13, 13, 13], [13, 13, 14], [13, 14, 14], [13, 15, 17], [13, 18, 18], [13, 18, 20], [13, 19, 19], [14, 14, 14], [14, 14, 20], [14, 15, 16], [14, 15, 17], [14, 18, 19], [14, 20, 20], [15, 15, 15], [15, 15, 16], [15, 15, 17], [15, 16, 18], [15, 16, 19], [15, 16, 20], [15, 17, 18], [15, 17, 19], [15, 17, 20], [15, 18, 19], [15, 18, 20], [15, 19, 19], [16, 16, 16], [16, 16, 17], [16, 16, 19], [16, 16, 20], [16, 17, 17], [16, 17, 18], [16, 17, 19], [16, 18, 18], [16, 18, 20], [16, 19, 19], [16, 19, 20], [17, 17, 17], [17, 17, 18], [17, 18, 19], [17, 18, 20], [17, 19, 19], [17, 20, 20], [18, 18, 18], [18, 18, 19], [18, 19, 20], [19, 19, 19], [19, 20, 20], [20, 20, 20]]
lopairs = [[0, 0], [1, 8], [2, 2], [3, 7], [4, 4], [5, 5], [6, 6], [9, 12], [10, 13], [11, 11], [14, 16], [15, 15], [17, 17], [18, 18], [19, 19], [20, 20]]

class dummyClass:
    def __init__(self):
        self.name = "name"

'''Used for generating
def generateLoD():
    lod = []
    f = open("listofdominoes.csv", "r")
    data = f.read().split("\n")
    for dom in data:
        newline = dom.split(",")
        for i in range(len(newline)):
            newline[i] = int(newline[i])
        lod += [newline]
    f.close()
    return lod

def generateFullLoD():
    lod = generateLoD()
    fulllod = []
    for ent in lod:
        fulllod += [ent[:-1]] * ent[-1]
    return fulllod
'''

def isGoodTrio(indone, indtwo, indthree, lod):
    tuplet = [lod[indone][1], lod[indone][2], lod[indtwo][1], lod[indtwo][2], lod[indthree][1], lod[indthree][2]]
    tuplet = sorted(tuplet)
    summy = sum(tuplet)

    for i in range(1,7):
        if tuplet.count(i) == 3:
            if summy - 3*i == 5 or summy - 3*i >=14:
                return True
            for j in range(i+1,7):
                if tuplet.count(j) == 3:
                    return True
        elif tuplet.count(i) == 4:
            if summy == 5*i:
                return True
            return False
        elif tuplet.count(i) >= 5:
            return True
    if tuplet in [[1,2,3,4,5,6], [1,1,2,2,3,3], [4,4,5,5,6,6]]:
        return True
    return False

def isGoodPair(indone, indtwo):
    if indone == indtwo:
        return True
    tbc = sorted([indone, indtwo])
    if tbc in ([1,8], [3,7], [9,12], [10,13], [14,16]):
        return True
    return False

def isGood(listofindices, lotrios, lopairs):
    loi = sorted(listofindices)
    if len(listofindices) == 3:
        if loi in lotrios:
            return True
    elif len(listofindices) == 2:
        if loi in lopairs: 
            return True
    return False

'''Used for generating
def generateTrios():
    fulllod = generateFullLoD()
    lod = generateLoD()
    result = []
    for i in range(32):
        indone = fulllod[i][0]
        for j in range(i,32):
            indtwo = fulllod[j][0]
            for k in range(j,32):
                indthree = fulllod[k][0]
                if [indone, indtwo, indthree] not in result:
                    if isGoodTrio(indone, indtwo, indthree, lod):
                        result += [[indone, indtwo, indthree]]
    return result
'''

def swappableTrip(trip1, trip2):
    '''reads two tripples, returns swappable respective positions in the form of [trip1poss1, trip2poss1, trip1poss2, trip2poss2...] if swappable, otherwise returns []'''
    possible = []
    for i in range(3):
        ind1 = trip1.indices[i]
        for j in range(3):
            ind2 = trip2.indices[j]
            if not ind1 == ind2:
                newtrip1 = deepcopy(trip1)
                newtrip2 = deepcopy(trip2)
                newtrip1.edit(i, ind2)
                newtrip2.edit(j, ind1)
                if newtrip1.isValid() and newtrip2.isValid():
                    possible += [i,j]
    return possible

def swappableDoub(trip, double):
    '''input double should be of the same form as [[8, 2, 4], [9, 2, 5]], trip should be type triplet
    returns swappable respective positions if swappable, otherwise returns []'''
    possible = []
    for i in range(3):
        ind1 = trip.indices[i]
        for j in range(2):
            ind2 = double[j][0]
            if not ind1 == ind2:
                newtrip = deepcopy(trip)
                newdoub = deepcopy(double)
                newtrip.edit(i, double[j][0])
                if newtrip.isValid() and isGoodPair(trip.indices[i], newdoub[1-j][0]):
                    possible += [i,j]
    return possible

def swappableIndices(inds1, inds2, lotrios, lopairs):
    possible = []
    for i in range(len(inds1)):
        swappy1 = inds1[i]
        for j in range(len(inds2)):
            swappy2 = inds2[j]
            if not swappy1 == swappy2:
                newinds1 = deepcopy(inds1)
                newinds2 = deepcopy(inds2)
                newinds1[i] = swappy2
                newinds2[j] = swappy1
                if isGood(newinds1, lotrios, lopairs) and isGood(newinds2, lotrios, lopairs):
                    possible += [i,j]
    return possible

def validFromRaw(rawlist, lotrios, lopairs):
    result = []
    for i in range(10):
        if isGood(rawlist[i*3:i*3+3], lotrios, lopairs):
            result += [i]
    if isGood(rawlist[-2:], lotrios, lopairs):
        result += [10]
    return result

def movableFromRaw(raw, lotrios, lopairs):
    possible = []
    for i in range(10):
        for j in range(i+1,10):
            r = swappableIndices(raw[i*3:i*3+3], raw[j*3:j*3+3], lotrios, lopairs)
            if len(r)>0:
                for k in range(len(r)//2):
                    possible += [[i, r[k*2], j, r[k*2+1]]]
        r = swappableIndices(raw[i*3:i*3+3], raw[-2:], lotrios, lopairs)
        if len(r)>0:
            for k in range(len(r)//2):
                possible += [[i, r[k*2], 10, r[k*2+1]]]
    return possible

def swapRaw(raw, possibility):
    '''swaps raw itself, returns the indices that are done'''
    i = possibility[0]
    j = possibility[2]
    pos1 = i*3+possibility[1]
    pos2 = j*3+possibility[3]
    swappy1 = raw[pos1]
    swappy2 = raw[pos2]
    raw[pos1] = swappy2
    raw[pos2] = swappy1
    return [i,j]

class domino:
    def __init__(self, numone, numtwo, indx):
        self.vals = (numone, numtwo)
        self.ind = indx
        self.position = None
        
    def getVal(self):
        return self.vals

class triplet:
    def __init__(self, lotrios, lodominoes, one, two, three, isIndexOnly):
        if isIndexOnly:
            self.indices = [one, two, three]
            self.details = [lodominoes[one], lodominoes[two], lodominoes[three]]
        else:
            self.details = [one, two, three]
            self.indices = [one[0], two[0], three[0]]

    def isValid(self):
        return sorted((self.indices)) in lotrios

    def getIndices(self):
        return self.indices
    
    def getDetails(self):
        return self.details
    
    def edit(self, loc, newindex):
        self.indices[loc] = newindex
        self.details[loc] = lodominoes[newindex]

class classicalBoard:

    def __init__(self, loDominoes, fLod, loTrios, knownRaw = None):
        if knownRaw == None:
            self.flod = fLod
            self.lodominoes = loDominoes
            self.lotrios = loTrios
            #self.order is not always updated, in particular it is not under manual input
            self.raw = self.generateTripleList()
            self.tripletlist = self.raw[:10]
            self.double = self.raw[10:]
            self.indicesraw = []
            self.movable = []
            self.printableMoves = []
            self.printableSolution = []
            self.updateRaw()
            self.updateTripletList()
        else:
            self.flod = fLod
            self.lodominoes = loDominoes
            self.lotrios = loTrios
            #self.order is not always updated, in particular it is not under manual input
            self.indicesraw = rawvaluestoindices(knownRaw)
            self.movable = []
            self.printableMoves = []
            self.updateTripletList()
            self.updateRaw()
    
    def __repr__(self):
        s = ""
        for i in range(10)[::2]:
            s+= "\n"
            triplyleft = self.tripletlist[i]
            triplyright = self.tripletlist[i+1]
            vals = triplyleft.getDetails() + triplyright.getDetails()
            for j in range(3):
                s += str(vals[j][1]) + "\t"
            s+="\t\t"
            for j in range(3,6):
                s += str(vals[j][1]) + "\t"
            s+="\n"
            for j in range(3):
                s += str(vals[j][2]) + "\t"
            s+="\t\t"
            for j in range(3,6):
                s += str(vals[j][2]) + "\t"
            s+="\n\n"
        s += "\n" + str(self.double[0][1]) + "\t" + str(self.double[1][1]) + "\n" + str(self.double[0][2]) + "\t" + str(self.double[1][2])
        return s

    def succinct(self):
        result = []
        for i in self.tripletlist:
            s += lodominoes[i][0]

    def updateRaw(self):
        '''uses tripletlist and double, updates everything else'''
        self.raw = self.tripletlist + self.double
        ir = []
        for x in self.tripletlist:
            ir += x.getIndices()
        ir += [self.double[0][0], self.double[1][0]]
        self.indicesraw = ir
        self.dummyFontConvert()
        self.assignMovableFromRaw(self.indicesraw, lotrios, lopairs)

    def updateTripletList(self):
        '''uses indicesraw, updates everything else'''
        result = []
        for i in range(10):
            result += [triplet(self.lotrios, self.lodominoes, self.indicesraw[i*3], self.indicesraw[i*3+1], self.indicesraw[i*3+2], True)]
        result += [self.lodominoes[self.indicesraw[30]], self.lodominoes[self.indicesraw[31]]]
        self.raw = result
        self.tripletlist = self.raw[:10]
        self.double = self.raw[10:]
        self.dummyFontConvert()
        self.assignMovableFromRaw(self.indicesraw, lotrios, lopairs)


    def generateTripleList(self, input = None):
        shuffledFlod = deepcopy(self.flod)
        shuffle(shuffledFlod)
        result = []
        for i in range(10):
            result += [triplet(self.lotrios, self.lodominoes, shuffledFlod[i*3], shuffledFlod[i*3+1], shuffledFlod[i*3+2], False)]
        result += [shuffledFlod[30], shuffledFlod[31]]
        return result
    
    def manualUpdate(self, rawtl):
        self.tripletlist = []
        self.double = []
        indices = []
        for i in range(32):
            indices += [self.indexCalculator(int(rawtl[i*2]), int(rawtl[i*2+1]))]
        for i in range(10):
            self.tripletlist += [triplet(self.lotrios, self.lodominoes, indices[i*3], indices[i*3+1], indices[i*3+2], True)]
        self.double += [self.lodominoes[indices[30]]]
        self.double += [self.lodominoes[indices[31]]]
        self.updateRaw()
    
    def indexCalculator(self, valone, valtwo):
        if valtwo < valone:
            print(str(valone), "\t", str(valtwo), "\tincorrect input!")
            return None
        result = 0
        for i in range(valone-1):
            result += 6-i
        result += valtwo - valone
        return result
    
    def movable(self):
        possible = []
        for i in range(10):
            for j in range(i+1,10):
                r = swappableTrip(self.tripletlist[i], self.tripletlist[j])
                if len(r)>0:
                    for k in range(len(r)//2):
                        possible += [[i, r[k*2],j, r[k*2+1]]]
            r = swappableDoub(self.tripletlist[i], self.double)
            if len(r)>0:
                for k in range(len(r)//2):
                    possible += [[i, r[k*2], 10, r[k*2+1]]]
        return possible
    
    def move(self, possibility):
        '''possibility should be of the form [trip i, 2, trip j, 0]]'''
        i = possibility[0]
        j = possibility[2]
        indi = possibility[1]
        indj = possibility[3]
        swappyi = deepcopy(self.indicesraw[i*3 + indi])
        swappyj = deepcopy(self.indicesraw[j*3 + indj])
        self.indicesraw[i*3 + indi] = swappyj
        self.indicesraw[j*3 + indj] = swappyi
        self.updateTripletList()

    def alrValid(self):
        result = []
        for i in range(10):
            if self.tripletlist[i].isValid():
                result += [i]
        if isGoodPair(self.double[0][0], self.double[1][0]):
            result += [11]
        return result

    def dummyFontConvert(self):
        result = ""
        for ent in self.raw[:10]:
            for dom in ent.details:
                for j in dom[1:3]:
                    if j == 1 or j == "1":
                        result += "k"
                    elif j == 2 or j == "2":
                        result += "l"
                    elif j == 3 or j == "3":
                        result += "m"
                    elif j == 4 or j == "4":
                        result += "n"
                    elif j == 5 or j == "5":
                        result += "o"
                    elif j == 6 or j == "6":
                        result += "p"
                    else:
                        result += "A"
        for ent in self.raw[10:]:
            for j in ent[1:3]:
                if j == 1 or j == "1":
                    result += "k"
                elif j == 2 or j == "2":
                    result += "l"
                elif j == 3 or j == "3":
                    result += "m"
                elif j == 4 or j == "4":
                    result += "n"
                elif j == 5 or j == "5":
                    result += "o"
                elif j == 6 or j == "6":
                    result += "p"
                else:
                    result += "A"
        self.dummyFont = result
        #return result
    def setFromRawInput(self, rawInput):
        raw = rawvaluestoindices(rawInput)
        self.updateTripletList(raw)
        print("done")

    def swapRaw(self, i, j):
        temp = self.indicesraw[j]
        self.indicesraw[j] = self.indicesraw[i]
        self.indicesraw[i] = temp
        self.updateTripletList()
        return self.raw
    
    def getActualRaw(self):
        values = ""
        for i in range(32):
            values += str(lodominoes[self.indicesraw[i]][1])
            values += str(lodominoes[self.indicesraw[i]][2])
        print(values)
        return str(values)


    def couponCollector(self, startState, lotrios, lopairs, lodominoes, BOUND):
        prevStateHistories = [[len(validFromRaw(startState, lotrios, lopairs)), [startState]]]
        targetValidCount = len(validFromRaw(startState, lotrios, lopairs))+1
        print("VALID FROM RAW", targetValidCount-1)
        print(prevStateHistories)
        #alreadyValid = validFromRaw(startState)
        level = 0
        validCount = len(validFromRaw(startState, lotrios, lopairs))
        print(validCount)
        if validCount == 11:
            print("DONE DONE DONE", level)
            return " found in " + str(level) + " steps!"
        while level<20:
            level += 1
            #targetValidCount += 1
            newStateHistories = []
            found = False
            for vertex in prevStateHistories:
                for possibility in movableFromRaw(vertex[1][-1], lotrios, lopairs):
                    if not found:
                        changingState = deepcopy(vertex[1][-1])
                        localVertex = deepcopy(vertex)
                        swapRaw(changingState, possibility)
                        if changingState not in localVertex[1]:
                            validCount = len(validFromRaw(changingState, lotrios, lopairs))
                            if validCount == 11:
                                print("DONE DONE DONE", level)
                                print(localVertex[1] + [changingState])
                                self.printableSolution = formatPrintableSol(localVertex[1] + [changingState])
                                return " found in " + str(level) + " steps!"
                            if validCount >= targetValidCount:
                                targetValidCount = validCount + 1
                                print("valid count", 11-validCount, "targetValidCount", 11-targetValidCount)
                                if targetValidCount == 11:
                                    print(changingState)
                                found = True
                    if not found:
                        newStateHistories += [[11-validCount, localVertex[1] + [changingState]]]
                    else:
                        newStateHistories = [[11-validCount, localVertex[1] + [changingState]]]
                        prevStateHistories = deepcopy(newStateHistories)
            if len(newStateHistories) > BOUND:
                prevStateHistories = deepcopy(newStateHistories)
                shuffle(prevStateHistories)
                prevStateHistories = prevStateHistories[:BOUND]
            else:
                prevStateHistories = deepcopy(newStateHistories)
            print("new state length", len(newStateHistories), "valid count", 11-targetValidCount)
            print(level, "is done.")
        return " not found in 20 steps. No hints are available :("
    
    def movableFromRaw(self, raw, lotrios, lopairs):
        possible = []
        for i in range(10):
            for j in range(i+1,10):
                r = swappableIndices(raw[i*3:i*3+3], raw[j*3:j*3+3], lotrios, lopairs)
                if len(r)>0:
                    for k in range(len(r)//2):
                        possible += [[i, r[k*2], j, r[k*2+1]]]
            r = swappableIndices(raw[i*3:i*3+3], raw[-2:], lotrios, lopairs)
            if len(r)>0:
                for k in range(len(r)//2):
                    possible += [[i, r[k*2], 10, r[k*2+1]]]
        return possible

        
    def assignMovableFromRaw(self, raw, lotrios, lopairs):
        l = ""
        for i in range(32):
            l += str(lodominoes[self.indicesraw[i]][1]) + str(lodominoes[self.indicesraw[i]][2])
        possible = []
        for i in range(10):
            for j in range(i+1,10):
                r = swappableIndices(raw[i*3:i*3+3], raw[j*3:j*3+3], lotrios, lopairs)
                if len(r)>0:
                    for k in range(len(r)//2):
                        possible += [str(i) + str(r[k*2]) + str(j) + str(r[k*2+1])]
            r = swappableIndices(raw[i*3:i*3+3], raw[-2:], lotrios, lopairs)
            if len(r)>0:
                for k in range(len(r)//2):
                    possible += [str(i) + str(r[k*2]) + "*" + str(r[k*2+1])]
        print(possible)
        self.movable = possible
        tempResult = []
        for i in range(len(possible)):
            ent = possible[i]
            s = ""
            if ent[0] == "*":
                if ent[1] == "0":
                    s += "PR-1"
                    dom1 = 30
                else:
                    s += "PR-2"
                    dom1 = 31
            else:
                temp = int(ent[0])
                s += "R" + str(temp//2+1) + "C" + str((temp%2)*3 + int(ent[1])+1) + " | "
                dom1 = int(ent[0])*3 + int(ent[1])
            if ent[2] == "*":
                if ent[3] == "0":
                    s += "PR-1"
                    dom2 = 30
                else:
                    s += "PR-2"
                    dom2 = 31
            else:
                temp= int(ent[2])
                s += "R" + str(temp//2+1) + "C" + str((temp%2)*3 + int(ent[3])+1)
                dom2 = int(ent[2])*3 + int(ent[3])

            newl = l[0:dom1*2] + l[dom2*2:dom2*2+2] + l[dom1*2+2:dom2*2] + l[dom1*2:dom1*2+2] + l[dom2*2+2:64]
            tempResult += [[s, newl]]
        print(tempResult)
        self.printableMoves = tempResult



    def isGoodPair(self,indone, indtwo):
        if indone == indtwo:
            return True
        tbc = sorted([indone, indtwo])
        if tbc in ([1,8], [3,7], [9,12], [10,13], [14,16]):
            return True
        return False

def formatPrintableSol(aListOfIndices):
    result = []
    for i in range(1, len(aListOfIndices)):
        swapped = helperCompareOneChange(aListOfIndices[i], aListOfIndices[i-1])
        dom1 = lodominoes[aListOfIndices[i-1][swapped[0]]]
        dom2 = lodominoes[aListOfIndices[i-1][swapped[1]]]
        result += [[helperConvertToReadableCoordinate(swapped[0]) + " ("+ str(dom1[1]) + ", " + str(dom1[2]) + ")   " +   helperConvertToReadableCoordinate(swapped[1]) +   " (" + str(dom2[1]) + ", " + str(dom2[2]) + ")", swapped[0], swapped[1]]]
    print(result)
    return result

def helperCompareOneChange(l1, l2):
    result = []
    if (len(l1)!=len(l2)):
        print(" ---------------- WE THINK YOU MESSED UP AGAIN ---------------- ")
        print(" ------------- HOW DOES IT FEEL TO ALWAYS BE WRONG ------------- ")
    else:
        for i in range(len(l1)):
            if (l1[i] != l2[i]):
                result += [i]
    if len(result)!= 2:
        print(" ---------------- WE THINK YOU MESSED UP AGAIN ---------------- ")
        print(" ------------- HOW DOES IT FEEL TO ALWAYS BE WRONG ------------- ")
    print(result)
    return result

def helperConvertToReadableCoordinate(num):
    if num < 30:
        return "R"+ str((num // 6 + 1)) + "C" + str(num % 6 + 1)
    else:
        if num == 30:
            return "PR-1"
        else:
            return "PR-2"

'''
def findSolution(cb, previndexstates, alreadyValid):
    recursively, start with self.findSolution([],[])
    curheight = len(previndexstates)
    if curheight == 0:
        previndexstates += [deepcopy(cb.indicesraw)]
    if curheight < 3:
        print(previndexstates)
    if curheight > 10:
        print(cb, curheight, "\nbig height")
        return False
    if len(alreadyValid) > 5:
        print(curheight, len(alreadyValid), "\nVALID IS BIG")
    if len(alreadyValid) == 11:
        print(previndexstates)
        for indstate in previndexstates:
            cb.indicesraw = indstate
            cb.updateTripletList()
            print(cb)
        return previndexstates
    cb.updateTripletList()
    possible = cb.movable()
    possible = prioritize(possible, alreadyValid)
    print(possible)

    for possibility in possible:
        cbcopy = deepcopy(cb)ç
        cb.move(possibility)
        if helperexistsalready(cb.indicesraw, previndexstates):
            print("here")
            break
        alrValid = cb.alrValid()
        previndexstates += [deepcopy(cb.indicesraw)]
        x = findSolution(cb, previndexstates, alrValid)
        if x:
            return x'''

def findSol(cb, previndexstates, alreadyValid,i):
    curheight = len(previndexstates)
    if curheight == 0:
        previndexstates += [deepcopy(cb.indicesraw)]
    possible = cb.movable()
    possible = prioritize(possible, alreadyValid)
    if curheight == 0:
        print(possible)
    for possibility in possible:
        cbcopy = deepcopy(cb)
        cbcopy.move(possibility)
        if not helperexistsalready(cbcopy.indicesraw, previndexstates):
            previs = deepcopy(previndexstates)+[deepcopy(cbcopy.indicesraw)]
            curheight = len(previs)
            valid = cbcopy.alrValid()
            
            if curheight > 4:
                return
            if len(valid) == 11:
                for indstate in previs:
                    cbtemp = deepcopy(cbcopy)
                    cbtemp.indicesraw = indstate
                    cbtemp.updateTripletList()
                    print(cbtemp)
                print("DONE DONE DONE DONE DONE")
                print(previs)
                print(len(previs))
                return previs
            findSol(cbcopy, previs, valid, i+1)
    print(i)

def indicesRecur(raw, prevStates, alreadyValid, lotrios, lopairs, lodominoes, i):
    curheight = len(prevStates)
    if curheight == 0:
        prevStates += [deepcopy(raw)]
        alreadyValid = validFromRaw(raw, lotrios, lopairs)
    possible = movableFromRaw(raw, lotrios, lopairs)
    possible = prioritize(possible, alreadyValid)
    for possibility in possible:
        rawcopy = deepcopy(raw)
        swapped = swapRaw(rawcopy, possibility)
        if not helperexistsalready(rawcopy, prevStates):
            prevst = deepcopy(prevStates)+[rawcopy]
            curheight = len(prevst)
            validcopy = deepcopy(alreadyValid)
            for sweep in swapped:
                if sweep not in validcopy:
                    validcopy += [sweep]
            if curheight > 15:
                return False
            if len(validcopy) > 9:
                '''for indstate in prevst:
                    cbtemp = classicalBoard(lodominoes, flod, lotrios)
                    cbtemp.indicesraw = indstate
                    cbtemp.updateTripletList()
                    print(cbtemp)'''
                print("DONE DONE DONE DONE DONE", validcopy, len(validcopy), curheight)
                #print(prevst)
                #print(len(prevst))
                #return prevst
            #print(rawcopy, prevst, validcopy, i)
            if len(validcopy) == 11:
                print(curheight)
                '''for indstate in prevst:
                    cbtemp = classicalBoard(lodominoes, flod, lotrios)
                    cbtemp.indicesraw = indstate
                    cbtemp.updateTripletList()
                    print(cbtemp)'''
                return True
            x = indicesRecur(rawcopy, prevst, validcopy, lotrios, lopairs, lodominoes, i+1)
            if x:
                return x
    print(i, alreadyValid)
    
def bfs(startState, lotrios, lopairs, lodominoes, maxheight, kLevelsAtATime, topNEachKLevels):
    prevStateHistories = [[len(validFromRaw(startState, lotrios, lopairs)), [startState]]]
    print(prevStateHistories)
    #alreadyValid = validFromRaw(startState)
    for jump in range(1, maxheight//kLevelsAtATime):
        for level in range(kLevelsAtATime):
            print(len(prevStateHistories))
            newStateHistories = []
            for vertex in prevStateHistories:
                for possibility in movableFromRaw(vertex[1][-1], lotrios, lopairs):
                    changingState = deepcopy(vertex[1][-1])
                    localVertex = deepcopy(vertex)
                    swapRaw(changingState, possibility)
                    if changingState not in localVertex[1]:
                        '''here it is possible to save and print what actually swapped i suppose'''
                        validCount = len(validFromRaw(changingState, lotrios, lopairs))
                        if validCount == 11:
                            print("DONE DONE DONE", jump*kLevelsAtATime+level)
                            print(localVertex[1] + [changingState])
                            return jump*kLevelsAtATime+level
                        newStateHistories += [[11-validCount, localVertex[1] + [changingState]]]
            prevStateHistories = deepcopy(newStateHistories)
        newStateHistories = [min(newStateHistories)]
        prevStateHistories = deepcopy(newStateHistories)
        print(newStateHistories)
        print(jump, "is done.")

def couponCollector(startState, lotrios, lopairs, lodominoes, BOUND):
    prevStateHistories = [[len(validFromRaw(startState, lotrios, lopairs)), [startState]]]
    targetValidCount = len(validFromRaw(startState, lotrios, lopairs))+1
    print(prevStateHistories)
    #alreadyValid = validFromRaw(startState)
    level = 0
    while level<20:
        level += 1
        #targetValidCount += 1
        newStateHistories = []
        found = False
        for vertex in prevStateHistories:
            for possibility in movableFromRaw(vertex[1][-1], lotrios, lopairs):
                if not found:
                    changingState = deepcopy(vertex[1][-1])
                    localVertex = deepcopy(vertex)
                    swapRaw(changingState, possibility)
                    if changingState not in localVertex[1]:
                        validCount = len(validFromRaw(changingState, lotrios, lopairs))
                        if validCount == 11:
                            print("DONE DONE DONE", level)
                            print(localVertex[1] + [changingState])
                            return level
                        if validCount >= targetValidCount:
                            targetValidCount = validCount + 1
                            print("valid count", 11-validCount, "targetValidCount", 11-targetValidCount)
                            if targetValidCount == 11:
                                print(changingState)
                            found = True
                if not found:
                    newStateHistories += [[11-validCount, localVertex[1] + [changingState]]]
                else:
                    newStateHistories = [[11-validCount, localVertex[1] + [changingState]]]
                    prevStateHistories = deepcopy(newStateHistories)
        if len(newStateHistories) > BOUND:
            prevStateHistories = deepcopy(newStateHistories)
            shuffle(prevStateHistories)
            prevStateHistories = prevStateHistories[:BOUND]
        else:
            prevStateHistories = deepcopy(newStateHistories)
        print("new state length", len(newStateHistories), "valid count", 11-targetValidCount)
        print(level, "is done.")
    return 20

def helperexistsalready(indraw, previndexstates):
    for indstate in previndexstates:
        if sortIndices(indraw) == sortIndices(indstate):
            return True
    return False

def prioritize(possible, alreadyValid):
    '''helper for finding solution
    update this to use more parameters by adding them to
    - def findSolution(...),
    - possible = prioritize(...),
    - def prioritize(...)'''
    result = []
    for i in range(len(possible)):
        x = possible[i][0]
        y = possible[i][2]
        result += [[int(x in alreadyValid) + int(y in alreadyValid), possible[i]]]
    result = sorted(result)
    return [x[1] for x in result]

def sortIndices(indices):
    '''doesn't change saved indices'''
    tlist = []
    for i in range(10):
        tlist += [sorted(indices[i*3:i*3+3])]
    tlist = sorted(tlist)
    tlist += [sorted(indices[-2:])]
    return tlist

def rawvaluestoindices(rawvals):
    indices = []
    for i in range(32):
        indices += [indexCalculator(int(rawvals[i*2]), int(rawvals[i*2+1]))]
    return indices


def indexCalculator(valone, valtwo):
    if valtwo < valone:
        print(str(valone), "\t", str(valtwo), "\tincorrect input!")
        return None
    result = 0
    for i in range(valone-1):
        result += 6-i
    result += valtwo - valone
    return result


'''
cb.manualUpdate([4,4,4,6,3,5,2,2,2,3,5,6,1,5,1,6,1,4,5,6,4,6,4,4,3,3,3,6,4,5,6,6,2,2,1,6,6,6,1,3,1,1,2,6,2,4,2,5,5,5,3,4,3,3,1,3,1,5,5,5,1,2,1,1])


'''
cb = classicalBoard(lodominoes, flod, lotrios)

'''
#raw = "4446352223561516145646443336456622166613112624255534331315551211" 
#[4,4,4,6,3,5,2,2,2,3,5,6,1,5,1,6,1,4,5,6,4,6,4,4,3,3,3,6,4,5,6,6,2,2,1,6,6,6,1,3,1,1,2,6,2,4,2,5,5,5,3,4,3,3,1,3,1,5,5,5,1,2,1,1]
#raw = rawvaluestoindices(raw)

raw = [0,0,1,2,2,3,4,4,5,5,6,6,7,8,9,10,11,11,12,13,14,15,15,16,17,17,18,18,19,19,20,20]
shuffle(raw)
#indicesRecur(raw, [], [], lotrios, lopairs, lodominoes, 0)
'''


'''
results = []

for i in range(10):
    raw = [0,0,1,2,2,3,4,4,5,5,6,6,7,8,9,10,11,11,12,13,14,15,15,16,17,17,18,18,19,19,20,20]
    shuffle(raw)
    l2 = couponCollector(raw,  lotrios, lopairs, lodominoes, 100)
    #l3 = couponCollector(raw,  lotrios, lopairs, lodominoes, 500)
    #results += [bfs(raw,lotrios,lopairs,lodominoes,30,5,3)]
    results += [l2]
print(results)

'''

'''
cb.couponCollector(raw,  lotrios, lopairs, lodominoes, 200)
'''