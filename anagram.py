"""Count possible steps to make words anagrams.
Return a list of options for zipped lists:
-1 in case words have different length and cannot be anagrams
0 if they already are anagrams (ex: 'ace' is an anagram of 'eca')
n number of steps to make them anagrams"""

def anagrams(a, b):
    compare_list = zip(a,b)
    result = list()
    for i in compare_list:
        if len(i[0]) != len(i[1]):
            result.append(-1)
        else:
            counter = 0
            seen = ''
            for j in i[0]:
                if j in seen:
                    continue
                if j not in i[1]:
                    counter += 1
                    print(counter)
                if j in i[1] and i[0].count(j) != i[1].count(j):
                    counter += abs(i[0].count(j) - i[1].count(j))
                    print(counter)
                    print(j)
                    seen += j
            result.append(counter)
    return result

if __name__ == __main__:
  anagrams(['fffghggjf', 'i'], ['aaffghuyi', 'hh'])
