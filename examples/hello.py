
from markpy import int32, float32

def main() -> int32:
    i = int32(0)
    i += 1
    return i


if __name__ == '__main__':
    r = main()
    print(r)
