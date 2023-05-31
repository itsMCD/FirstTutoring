import random as r
import stdarray as arr
def generate_board(size, probability):
    out = arr.create2D(size, size, 0)
    
    for row in out:
        for column in range(size):
            if r.uniform(0,1) < probability:
              row[column] = 1
    return out 

def print_matrix(arr):
    print('','▁▁'*len(arr))
    for row in arr:
        print('▕', end="")
        for ch in row:
            if ch == 0:
                print('  ', end="")
            elif ch == 1:
                print('██', end="")
            elif ch == 2:
                print('░░', end="")
        print('▌')
    print('','▀▀'*len(arr)+'▘')
def main():
    arr = generate_board(8, 0.3)
    print_matrix(arr)
    
if __name__ == "__main__":
    main()