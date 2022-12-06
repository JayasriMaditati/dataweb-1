import time

def mapper(line):
    for word in line.split():
        # print("computing a value")
        yield(word, 1)

text = """twinkle twinkle you little star
how I wonder what you twinkle about"""

lines = text.split("\n")
print(lines)

all_values = []

for line in lines:
    x = mapper(line)
    values = list(x)
    print(values)
    all_values = all_values + values

print(all_values)
def shuffle(values):
    combined_values = {}
    for value in values:
        key, n = value
        if key in combined_values:
            combined_values[key].append(n)
        else:
            combined_values[key] = [n]
    combined_values = [(key, combined_values[key]) for key in combined_values.keys()]
    return combined_values

def reduce(combined_values):
    reduced_values = []
    for value in combined_values:
        key, ns = value
        reduced_values.append((key, sum(ns)))
    return reduced_values
    
print(reduce(shuffle(all_values)))


# w = next(x)
# while w:
#     print(w)
#     w = next(x)
#     time.sleep(1)

# values = list(x)
# print(values)

