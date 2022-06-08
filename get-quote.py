import random


def primary():
    f = open("quotes.txt", encoding="utf8")
    quotes = f.readlines()
    f.close()
    quote = random.choice(quotes)
    print(quote)


def secondary():
    f = open("quotes.txt", encoding="utf8")
    quotes = f.readlines()
    f.close()
    quote = input("Enter a quote to add it or press 'e' to exit or 'r' to get a random quote: ")
    if quote == "e":
        print("Goodbye!")
        exit()
    elif quote == "r":
        quote = random.choice(quotes)
        print(quote)
    else:
        for i in quotes:
            if quote in i:
                print(i)
                break
        else:
            print("Quote not found.")
            quotes.append(quote)
            f = open("quotes.txt", "w", encoding="utf8")
            for i in quotes:
                f.write(i)
            f.close()

while True:
    primary()
    secondary()
# End of file

