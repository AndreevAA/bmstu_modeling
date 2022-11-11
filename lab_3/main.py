from io_operations import *
from logics import *


def main():
  # Initializing cicling counting
  while True:
    # Getting starting args
    number, mode = IO_operations().get_args()

    # Getting lists
    slists, tlists = Logics.get_lists(number, mode)

    # Output data
    IO_operations().out_data(number, slists, tlists)

if __name__ == "__main__":
  main()
