les = int(input())
minutes =  les * 45 + ((les - 1) // 2 * 15 + (les  // 2 * 5))
print(f'{minutes // 60 + 9} {minutes % 60}')