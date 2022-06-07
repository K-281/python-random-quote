import random


def primary():
    f = open("quotes.txt", encoding="utf8")
    quotes = f.readlines()
    f.close()
    last = len(quotes) - 1
    rnd = random.randint(0, last)
    print(quotes[rnd] + "\n" + quotes[rnd + 1])


# make user input a quote and see if it is in the list, if not, add it
def secondary():
    f = open("quotes.txt", encoding="utf8")
    quotes = f.readlines()
    f.close()
    quote = input("Enter a quote: ")
    if quote in quotes or quote == "" or quote == int or quote == float:
        print("Quote already exists")
    else:
        quotes.append(quote + "\n")
        f = open("quotes.txt", "w", encoding="utf8")
        f.writelines(quotes)
        f.close()
        print("Quote added")
# if it is, print it and ask if they want to add it to the list
# if they do, add it to the list
# if they don't, print the quote and ask if they want to see another quote
# if they do, print another quote and ask if they want to see another quote


if __name__ == "__main__":
    primary()
    secondary()
