#oppgave 1

#assosiative lister

#1.1
d0_a = []
d0_b = [[]]

#1.2
d1_a = [1, 2]
d1_b = [3, 4, 5]

#1.3 elementer i d1_a
from collections import Counter
# d1_a = [1, 2]

Counter(d1_a)

# 1.4
d1_a = {1, 2}

#bokstaver som key
d1_a[a] = 1
d1_a[b] = 2
print(d1_a)

# 1.5
import timeit
timer1 = timeit.Timer('Counter(d1_a)', \
'import random; import string; from collections import Counter; n 1000; d1_a = [random.choice(string.ascii_letters)'
'for x in range(n)]'

# 1.6
#d9_int = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#d9_str = ['null', 'ein', 'to', 'tre', 'fire', 'fem', 'seks', 'sju', 'åtte']

# 1.7
d9_int = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
d9_str = ['null', 'ein', 'to', 'tre', 'fire', 'fem', 'seks', 'sju', 'åtte']

for i in d9_int(10):
    print(d9_int.index(i) + 1, end='')
    print(" ", i)

for y in d9_str(10):
    print(d9_str.index(y) + 1, end=' ')
    print(" ", y)















