def main():
    size = 119315717514047
    n = 101741582076661
    pos = 2020
    m = 1
    b = 0

    with open("puzzle_input.txt", 'rt') as f:
        for line in f:
            if("deal with increment" in line):
                value = int(line.split()[-1])

                m = m * value % size
                b = b * value % size


            if("cut" in line):
                value = int(line.split()[-1])

                b = (b - value) % size

            if("deal into new stack" in line):
                m = -m % size
                b = (size-1-b) % size

    b_ = (b * pow(1-m, size-2, size)) % size
    result =((pos - b_) * pow(m, n*(size-2), size) + b_) % size
    print(result)

if __name__ == "__main__":
    main()





