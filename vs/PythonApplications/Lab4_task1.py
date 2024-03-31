def CostCalculation(AmountOfGarbage, offset):
    a = offset - 1
    b = offset + 1
    stat = [False] * len(AmountOfGarbage)
    stat[offset] = True
    tot_count = 1
    price_a = 1
    price_b = 1
    total_sum = 0
    while tot_count < len(AmountOfGarbage):
        if a < 0:
            a = len(AmountOfGarbage) - 1
        if b >= len(AmountOfGarbage):
            b = 0
        if not stat[a]:
            stat[a] = True
            total_sum = price_a * AmountOfGarbage[a]
            tot_count += 1
        if not stat[b]:
            stat[b] = True
            total_sum = price_b * AmountOfGarbage[b]
            tot_count += 1
        a -= 1
        b += 1
        price_a += 1
        price_b += 1
    return total_sum

def GetIndex(AmountOfGarbage):
    ind = 0
    tsum = CostCalculation(AmountOfGarbage, 0)
    ctsum = tsum
    cesh_sum = [0] * len(AmountOfGarbage)
    for i in range(len(AmountOfGarbage)):
        cesh_sum[i] = CostCalculation(AmountOfGarbage, i)
    for i in range(1, len(AmountOfGarbage)):
        if cesh_sum[i] < tsum:
            tsum = cesh_sum[i]
            ind = i
    return ind




with open("27-99a.txt", "r") as file:
    lines = file.readlines()

val = [int(line) for line in lines[1:]]
print(GetIndex(val))
print("\n")
with open("27-99b.txt", "r") as file:
    lines = file.readlines()

val = [int(line) for line in lines[1:]]
print(GetIndex(val))
print("\n")

