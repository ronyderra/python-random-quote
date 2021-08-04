import random
def main():
    #   print("Keep it logically awesome.")
    # LiorHashava = "Lior can be a bag full of dicks sometimes"
    # print(LiorHashava)

    # get quoted
    f = open("quotes.txt")
    # read the file quotes
    quotes = f.readlines()
    f.close()
    # print(quotes)
    for line in quotes:print(line.strip())
    # print(quotes[0])
    # print(quotes[-1])
    # last = len(quotes)-1
    # rnd = random.randint(0, last)
    # print(quotes[rnd] + quotes[2])

if __name__ == "__main__":
    main()
