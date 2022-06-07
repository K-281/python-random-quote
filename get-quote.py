import random


def primary():
    f = open("quotes.txt", encoding="utf8")
    quotes = f.readlines()
    f.close()
    last = len(quotes) - 1
    rnd = random.randint(0, last)
    print(quotes[rnd] + "\n" + quotes[rnd + 1])


def secondary():
    f = open("quotes.txt", encoding="utf8")
    quotes = f.readlines()
    f.close()
    quote = input("Enter a quote: ")
    if quote in quotes or quote == "" or quote == int or quote == float:  # if quote is in quotes.txt
        print("Quote already exists")
    else:
        quotes.append(quote + "\n")  # add quote to quotes.txt
        f = open("quotes.txt", "w", encoding="utf8")
        f.writelines(quotes)
        f.close()
        print("Quote added")


if __name__ == "__main__":
    primary()
    secondary()
