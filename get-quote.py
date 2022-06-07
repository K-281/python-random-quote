import random


def primary():
    f = open("quotes.txt", encoding="utf8")
    quotes = f.readlines()
    f.close()
    last = 115
    rnd = random.randint(0, last)
    print(quotes[rnd] + "\n" + quotes[rnd + 1])


if __name__ == "__main__":
    primary()
