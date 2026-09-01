def fizzbuzz (number):
  result = ''
  if number % 3 == 0:
    result += 'Fizz'
  if number % 7 == 0:
    result += 'Buzz'
  if result == '':
    result += str(number)
  return result
limit = int(input('Enter limit:'))
for i in range(1, limit + 1):
  print(fizzbuzz(i))