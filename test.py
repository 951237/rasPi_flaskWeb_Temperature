FILE_PATH = 'webapp/result_temp.txt'

with open(FILE_PATH, 'r') as f:
    body = f.read().split(',')

print(body)
