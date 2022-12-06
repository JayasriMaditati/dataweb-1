from mapreduce import MapReduce

class WordCount(MapReduce):

    def mapper(self, _, line):
        line = line.lower()
        line = "".join([c for c in line if c.isalpha() or c==" "])
        for word in line.split():
            yield(word, 1)

    def reducer(self, key, values):
        yield key, sum(values)

input = open("alice.txt").readlines()

output = WordCount.run(input)
wordlist = [str(n + 100000) + ":" + key for (key, n) in output]
for item in sorted(wordlist)[::-1][0:10]:
    print(item)

