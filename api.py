
# creating a distance map
dist = {"1":
            {'1': -1,'2': 4,'3': -1,'4': 3,},
        "2":
            {'1': 4,'2': -1,'3': 3,'4': 2.5,},
        "3":
            {'1': -1,'2': 3,'3': -1,'4': 2,},
        "4":
            {'1': 3,'2': 2.5,'3': 2,'4': -1,}
    }

def getOrderWeight(a):
    if a==1:
        wtCity1=0
        return c1
    if a==2:
        wtCity2=0
        return c2
    if a==3:
        wtCity3=0
        return c3
    if a == 4:
        return -1

def getPendinOrderWeight(a):
    if a==1:
        return wtCity1
    if a==2:
        return wtCity2
    if a==3:
        return wtCity3

# returns the distance between two cities
def getDistance(city1, city2):
    return dist[str(city1)][str(city2)]

# calculates the cost per unit of commutation
def calcPerUnitCost(weight):
    if weight >= 0 or weight <=5 :
        cost = 10
    if weight > 5:
        cost = 10
        weight = weight - 5
        while(weight > 0):
            cost = cost + 8
            weight = weight - 5
    return cost

def calcTravelCost(weight, distance):
    perUnitCost = calcPerUnitCost(weight)
    return perUnitCost*distance

def calcCity1Weight(aa,bb,cc):
    return aa*3 + bb*2 + cc*8

def calcCity2Weight(aa,bb,cc):
    return aa*12 + bb*25 + cc*15

def calcCity3Weight(aa,bb,cc):
    return aa*0.5 + bb*1 + cc*2

def decideShortestPath():
    costs = []
    if c1 != 0 and c2 != 0 and c3 != 0 :
        costs.append(calcPathCost([2,4,1,4,3,4]))
        costs.append(calcPathCost([2,3,4,1,4]))
        costs.append(calcPathCost([1,4,2,3,4]))
        costs.append(calcPathCost([1,2,3,4]))
        costs.append(calcPathCost([3,2,1,4]))
        costs.append(calcPathCost([3,4,2,1,4]))
        costs.append(calcPathCost([3,4,1,4,2,4]))
        costs.append(calcPathCost([3,4,1,2,4]))
        costs.append(calcPathCost([2,4,3,4,1,4]))
    if c3 == 0 and c1 != 0 and c2 != 0:
        costs.append(calcPathCost([1,2,4]))
        costs.append(calcPathCost([2,1,4]))
        costs.append(calcPathCost([1,4,2,4]))
        costs.append(calcPathCost([2,4,1,4]))
    if c2 == 0 and c1 != 0 and c3 != 0:
        costs.append(calcPathCost([1,4,3,4]))
        costs.append(calcPathCost([3,4,1,4]))
    if c1 == 0 and c2 != 0 and c3 != 0:
        costs.append(calcPathCost([2,3,4]))
        costs.append(calcPathCost([3,2,4]))
        costs.append(calcPathCost([2,4,3,4]))
        costs.append(calcPathCost([3,4,2,4]))
    if c2 == 0 and c1 == 0 and c3 != 0 :
        costs.append(calcPathCost([3,4]))
    if c3 == 0 and c1 == 0 and c2 != 0 :
        costs.append(calcPathCost([2,4]))
    if c2 == 0 and c3 == 0 and c1 != 0 :
        costs.append(calcPathCost([1,4]))
    if c1 == 0 and c2 == 0 and c3 == 0:
        costs.append(0)
    return min(costs)

def calcPathCost(list):
    n = len(list)
    totalCost = 0
    curWeight = 0
    for i in range(0,n-1,1):
        # start with city i
        weight = getOrderWeight(list[i])
        if weight != -1:
            curWeight = curWeight + weight
        else:
            curWeight = 0
        curDist = getDistance(list[i],list[i+1])
        cost = calcTravelCost(curWeight, curDist)
        totalCost = cost + totalCost
        # load truck with that city weight
        # calculate cost to reach destination and add it to totalCost
        # if dest = 4, curWeight should be reset to 0
    if n == 2:
        curDist = getDistance(list[i], list[i+1])
    return totalCost


from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument('-A', dest='stocka', type=int, default=0)
parser.add_argument('-B', dest='stockb', type=int, default=0)
parser.add_argument('-C', dest='stockc', type=int, default=0)
parser.add_argument('-D', dest='stockd', type=int, default=0)
parser.add_argument('-E', dest='stocke', type=int, default=0)
parser.add_argument('-F', dest='stockf', type=int, default=0)
parser.add_argument('-G', dest='stockg', type=int, default=0)
parser.add_argument('-H', dest='stockh', type=int, default=0)
parser.add_argument('-I', dest='stocki', type=int, default=0)
args = parser.parse_args()
a=args.stocka
b=args.stockb
c=args.stockc
d=args.stockd
e=args.stocke
f=args.stockf
g=args.stockg
h=args.stockh
i=args.stocki

c1 = calcCity1Weight(a,b,c)
c2 = calcCity2Weight(d,e,f)
c3 = calcCity3Weight(g,h,i)

print(decideShortestPath())
