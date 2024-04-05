import sys
sys.path.append(".")
from first import add,subtract
from second import multiply

def main():
    print(add(5, 3))       
    print(subtract(5, 3))  
    print(multiply(5, 3)) 

if __name__ == "__main__":
    main()
