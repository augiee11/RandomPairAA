import random
group_a = ["Gly","Ala","Val","Pro","Leu","lle", "Met"]
group_b = ["Lys","Arg"]
group_c = ["Asp", "Glu"]
group_d = ["Ser", "Thr", "Asn", "Gln", "Cys"]
group_e = ["Trp", "Phe", "Tyr", "His"]

group_pool = [group_a, group_b, group_c, group_d, group_e]
pairings = []
number_of_pairings = 100
while len(pairings) < number_of_pairings:
    groups_indx = random.sample(range(0,5),2)
    size_1 = len(group_pool[groups_indx[0]]) - 1
    size_2 = len(group_pool[groups_indx[1]]) - 1
    amino1_indx = random.randint(0,size_1)
    amino2_indx = random.randint(0,size_2)
    
    amino_1 = group_pool[groups_indx[0]][amino1_indx]
    amino_2 = group_pool[groups_indx[1]][amino2_indx]
    new_pair = amino_1 + "," + amino_2
    if new_pair not in pairings:
        pairings.append(new_pair)

print(pairings)
