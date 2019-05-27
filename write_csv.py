lunch = {
  '양자강': '02-557-4211',
  '김밥카페': '02-553-3101',
  '순남시래기': '02-506-0557'
}
# 1. f-string
with open('lunch.csv', 'w', encoding='utf-8') as f:
  for item in lunch.items(): # [('양자강','02-...), ...]
    f.write(f'{item[0]},{item[1]}\n')

# 2. join()
with open('lunch.csv', 'w', encoding='utf-8') as f:
  for item in lunch.items(): # [('양자강','02-...), ...]
    f.write(','.join(item)+'\n')
    # ','.join(('양자강','02-...), ('역삼동', '02-...'))
    # => 양자강,02-557-4211,역삼동,...

# 3.csv
import csv
with open('lunch.csv', 'w', encoding='utf-8') as f:
  csv_writer = csv.writer(f)
  for item in lunch.items():
    csv_writer.writerow(item)
