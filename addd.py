import sys

def add(a, b):
    return a + b

if __name__ == "__main__":
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print("sum:", add(x, y))
