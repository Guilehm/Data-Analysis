from die import Die


die = Die()
results = []

# lunches and save results
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# analyse the results
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
