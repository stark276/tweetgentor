from random import randint

quotes = ("It's just a flesh wound.",
  "He's not the Messiah. He's a very naughty boy!",
  "THIS IS AN EX-PARROT!!")

rand_index = randint(0, len(quotes) - 1)
print(quotes[rand_index])


