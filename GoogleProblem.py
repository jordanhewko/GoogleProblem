import random
import sys

def get_and_sort(n):

    lst = [0] * n
    
    for i in range(0, n):
    
        rando = random.randint(0,100)
        lst[i] = rando 
    
    lst.sort()
    return lst

def findSum(lst, sum):

    print("Sum: " + str(sum))
    i = 0
    j = len(lst) - 1
    comp = 0
    while lst[j] > sum:
        comp += 1
        j-=1
    
    print("max found, comps: " + str(comp))
    while i != j:

        #print("Total: " + str(lst[i] + lst[j]))
        if lst[i] +lst[j] == sum:
            print("Total comparrisons: " + str(comp))
            return True
        elif lst[i] + lst[j] >sum:
            comp += 1
            j-=1
        else:
            comp += 1
            i+=1

    return False

def handle_opt(argv):

	if len(argv) != 2:
		print("usage: GoogleProblem.py number")
		sys.exit(1)

	else:
		try:
			out_value = int(argv[1])
			return int(argv[1])

		except ValueError:
			print("Type Error: sequence_length must be an integer")
			sys.exit(1)
def main():

    n = handle_opt(sys.argv)

    lst = get_and_sort(n)
    #print(lst)
    flag = findSum(lst, 120)
    if flag == True:
        print("ayyy")
    else:
        print("10 ply bud")

if __name__ == "__main__":
    main()