import tabulate
import numpy
import sys


class IO_operations():
  # Getting starting args
  def get_args(self):
    return int(input("Input n: ")), input("Do you want input yourself (y/n) ?")

  # Output data
  def out_data(self, n, slists, tlists):
    print("Программный метод:")
    self.__print_table(self.__create_table(slists), n)
    print()

    print("Табличный метод:")
    self.__print_table(self.__create_table(tlists), n)

  # Creating table
  def __create_table(self, sequences: list) -> str:
    cols = [list(range(1, len(sequences[0]) + 1))]

    for seq in sequences:
      cols.append(seq.copy())

    cols[0] += ['Ожидаемый', 'Полученный']

    for i in range(1, len(cols)):
      cols[i] += list(self.__frequency_criterion(cols[i], i))

    table = tabulate.tabulate(
      {
        "No": cols[0],
        "1 разр.": cols[1],
        "2 разр.": cols[2],
        "3 разр.": cols[3],
      },
      headers="keys",
      tablefmt="presto",
      numalign="right",
      floatfmt=".4f")

    return table

  # Outputing table with formting with special symbols
  def __print_table(self, table, n):
    rows = table.split('\n')
    print('\n'.join(rows[:5 + 2]))
    if n > 10:
      print(("{:^%ds}" % len(rows[0])).format('\u2022' * 3))
    print('\n'.join(rows[-5 - 2:-2]))
    print(rows[1])
    print('\n'.join(rows[-2:]))

  # Getting frequency 
  def __frequency_criterion(self, sequence, num_len):
    mean = numpy.mean(sequence)
    stdd = numpy.sqrt(numpy.var(sequence))

    cnt = 0
    for item in sequence:
      if (mean - stdd) < item < (mean + stdd):
        cnt += 1

    sequence_max_delta = 10
    if num_len > 1:
      sequence_max_delta = 9 * 10**(num_len - 1)

    return (2 * stdd / sequence_max_delta), (cnt / len(sequence))