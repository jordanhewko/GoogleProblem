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
    left = 0
    right = len(lst) - 1
    comp = 0
    while lst[right] > sum:
        comp += 1
        right -= 1

    while left != right:

        if lst[left] + lst[right] == sum:
            return True
        elif lst[left] + lst[right] > sum:
            comp += 1
            left -= 1
        else:
            comp += 1
            right += 1

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

    flag = findSum(lst, 120)
    if flag == True:
        print("Matching pair found")
    else:
        print("No pair found")

if __name__ == "__main__":
    main()