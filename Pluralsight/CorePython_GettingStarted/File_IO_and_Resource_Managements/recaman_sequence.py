from re import A
import sys
from itertools import count, islice

def sequence():
    """Generate Recaman`s sequence."""
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n 
        if c < 0 or c in seen:
            c = a + n
        a = c

def write_sequence(filename, num):
    """Write Recaman`s sequence to a text file"""
    f = open(filename, mode='wt', encoding='utf-8')
    f.writelines(f"{r}\n" for r in islice(sequence(), num + 1))
    f.close()

if __name__ == '__main__':
    write_sequence(filename=sys.argv[1], num=int(sys.argv[2]))


# excution:  python recaman_sequence.py recaman.dat 1000 (for the first 1000 numbers)