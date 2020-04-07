# https://adventofcode.com/2019/day/22
# 10007 cards in the deck numbered 0 through 10006
# factory order, with 0 on the top, then 1, then 2, and so on, all the way through to 10006 on the bottom

# # get all lines from puzzle_input
# f = open("puzzle_input.txt", "r")
# lines = f.readlines()
# filename = "puzzle_input.txt"


# generate new deck [k, ..., 2, 1, 0]
def generate_deck(total):
    return list(range(total-1,-1,-1))

# new stack [0, 1, 2, ..., k]
def new_stack(stack_):
    return stack_[::-1]

# cut n cards [n+1, n+2, ..., k, n - (n-1), n - (n-2), ..., n]
def cut_stack(stack_, n):
    return stack_[n:] + stack_[:n]

# inc move cards n positions
def inc_stack(input_stack, n):
    new_stack = [None] * len(input_stack)
    counter = 0

    for elem in input_stack:
        if(new_stack[counter] == None):
            new_stack[counter] = elem
        counter = (counter + n) % len(input_stack)

    return new_stack



def main():
    print("Part One")
    print("Step: 1")
    deck = generate_deck(10)
    print(deck)

    print("Step: 2")
    nStack = cut_stack(deck, -4)
    print(nStack)

    print("Step: 3")
    deck = generate_deck(10)
    incStack = inc_stack(deck,3)
    print(incStack)

    print("Finally")
    deck = generate_deck(10007)
    stack = new_stack(deck)


    with open("puzzle_input.txt", 'rt') as f:
        for line in f:
            if("deal with increment" in line):
                words = line.split()
                value = int(words[-1])

                stack = inc_stack(stack, value)
            if("cut" in line):
                words = line.split()
                value = int(words[-1])

                stack = cut_stack(stack, value)
            if("deal into new stack" in line):
                stack = new_stack(stack)

    print("Result: ", stack.index(2019)) # Result

if __name__ == "__main__":
    main()


