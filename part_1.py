# https://adventofcode.com/2019/day/22
# 10007 cards in the deck numbered 0 through 10006
# factory order, with 0 on the top, then 1, then 2, and so on, all the way through to 10006 on the bottom

# get all lines from puzzle_input
f = open("puzzle_input.txt", "r")
lines = f.readlines()


# generate new deck [k, ..., 2, 1, 0]
def generate_deck(total):
    deck = []
    for x in range(total-1, -1, -1):
        deck.append(x)

    return deck

# new stack [0, 1, 2, ..., k]
def new_stack(stack_):
    new_stack = []

    for x in range(len(stack_)):
        new_stack.append(stack_.pop())

    return new_stack

# cut n cards [n+1, n+2, ..., k, n - (n-1), n - (n-2), ..., n]
def cut_stack(stack_, n):
    new_stack = stack_[n:]

    for elem in stack_[:n]:
        new_stack.append(elem)

    return new_stack

# inc move cards n positions
def inc_stack(input_stack, n):
    new_stack = [None] * len(input_stack)
    counter = 0

    for elem in input_stack:
        if(new_stack[counter] == None):
            new_stack[counter] = elem
        counter = (counter + n) % len(input_stack)

    return new_stack


# handle each line
# get instuction and value => operate
# return stack
def shuffle(input_stack):
    res_stack = input_stack
    for line in lines:
        if("deal with increment" in line):
            words = line.split()
            value = int(words[-1])

            res_stack = inc_stack(res_stack, value)
        if("cut" in line):
            words = line.split()
            value = int(words[-1])

            res_stack = cut_stack(res_stack, value)
        if("deal into new stack" in line):
            res_stack = new_stack(res_stack)

    return res_stack


print("Part One")
print("Step: 1")
deck = generate_deck(10)
stack = new_stack(deck)
print(stack)

print("Step: 2")
nStack = cut_stack(stack, -4)
print(nStack)

print("Step: 3")
deck = generate_deck(10)
incStack = inc_stack(stack,3)
print(incStack)

print("Finally")
deck = generate_deck(10007)
stack = new_stack(deck)

resStack = shuffle(stack)
# print(resStack) # finaler Stack
print("Result: ", resStack.index(2019)) # Result

