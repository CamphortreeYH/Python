f = file('scores.txt')
lines = f.readlines()
f.close()

results = []

for line in lines:
    data = line.split()
    sum = 0
    for score in data[1:]:
        sum += int(score)
    result = '%s: %d\n' % (data[0], sum)
    results.append(result)

output = file('results.txt', 'w')
output.writelines(results)
output.close()
