import random

def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  lastNum = 13
  rnd = random.randint(0, lastNum)

  print(quotes[rnd])

if __name__== "__main__":
  primary()
