import re

def add(number: str):
  if number == '':
    return 0

  delimiter = None
  if number[:2] == '//':
    number = number[2:]
    delimiter, number = re.split('\n', number, 1)

  pattern = ',|\n'
  if delimiter is not None:
    pattern = f',|\n|\{delimiter}'

  nums = [ int(_) for _ in re.split(pattern, number) ]

  # checking for negative numbers
  for num in nums:
    if num < 0:
      raise ValueError(f'negatives not allowed. found {num}')
  return sum(nums) 
