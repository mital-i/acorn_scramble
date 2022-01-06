n = int(input())
source = []
target = []

for i in range(n): 
    source.append(int(input()))

for i in range(n): 
    target.append(int(input()))
    
tracker = [0]*n

print(source, target)

cycle_ac = None
def scramble(current_acorn, curr_index, source, target, tracker, ac_in_cyc):
    global cycle_ac
    current_acorn = source[curr_index]
    new_acorn = source[target.index(current_acorn)]
    tracker[new_acorn-1]+=1
    new_index_for_curr = source.index(new_acorn)
    
    source[curr_index] = 0
    source[new_index_for_curr] = current_acorn
    
    print(source, tracker, curr_index, new_acorn)
    
    if tracker[new_acorn-1] > 1:
        cycle_ac = ac_in_cyc
        print("hi", tracker)
        return
    if source[new_index_for_curr] == 0: 
        cycle_ac = ac_in_cyc
        return
    
    print()
    
    scramble(new_acorn, new_index_for_curr, source, target, tracker, ac_in_cyc+1)

if source == target: 
    print(0, -1)
else: 
    scramble(source[0], 0, source, target, tracker, 1)
    print(cycle_ac)
