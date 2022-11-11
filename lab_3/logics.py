from my_random import *


# Loginc operator
class Logics():

  def get_lists(n, mode):
    slists = [[], [], []]
    tlists = [[], [], []]

    # Programm input
    if mode == "n":
      sgen = StandardRandom()
      tgen = TableRandom()
      for i in range(n):
        for j in range(3):
          slists[j].append(sgen.get(j + 1))
          tlists[j].append(tgen.get(j + 1))
    # Manual input
    elif mode == "y":
      for i in range(n):
        for j in range(3):
          print("Input ", j + 1, "bitness number:")
          num = float(input())
          slists[j].append(num)
          tlists[j].append(num)

    return slists, tlists
