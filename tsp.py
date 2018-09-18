import random

distance =[[0,110,125,175],[110,0,150,170],[125,150,0,150],[175, 170,150,0]]

population = [[0,1,2,3],[0,1,3,2],[0,2,1,3],[0,2,3,1],[0,3,2,1],[0,3,1,2]]
total_dist = 0
best_fit = 0
best_chrom = [0,0,0,0]
iteration = 50

def fitness_func(chrom):
    global total_dist, best_fit, best_chrom
    for x in range (3):
        total_dist += distance[chrom[x]][chrom[x+1]]
    total_dist += distance[chrom[3]][chrom[0]]
    fitness = float(1/total_dist)
    if best_fit < fitness:
        best_fit = fitness
        best_chrom = chrom

def crossover(chrom1, chrom2):
    cr1=chrom1[:2]
    cr2=chrom2[:2]
    cr1.append(chrom2[2:])
    cr2.append(chrom1[2:])
    chrom1 = cr1
    chrom2 = cr2

def mutation(c):
    n = random.randint(1,3)
    m = random.randint(1,3)
    if n!=m:
        temp = c[n]
        c[n] = c[m]
        c[m] = temp

while(iteration):
    for x in range (6):
        fitness_func(population[x])
    for x in range (0,6,2):
        crossover(population[x], population[x+1])
    for x in range(6):
        mutation(population[x])
       
    iteration = iteration - 1

print("Best fitness:")
print(best_fit)
print("Best chromosome:")
print(best_chrom)
