import argparse

def get_sum_of_nums(num1,num2,num3):
  return(int(num1)+int(num2)+int(num3))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script that adds 3 numbers from CMD"
    )
    parser.add_argument("--num1", required=True, type=int , help="1 param :day")
    parser.add_argument("--num2", required=True, type=int, help="2 param :number_exec")
    parser.add_argument("--num3", required=True, type=int, help="3 param :number_core")
    args = parser.parse_args()

    num1 = args.num1
    num2 = args.num2
    num3 = args.num3

    print(get_sum_of_nums(num1, num2, num3))

#python3 main_ext_arg_decl.py -h --num1=1 --num2=2 --num3='b'

#python3 main_ext_arg_decl.py -h --num1=1 --num2=2 --num3=4

#python3 main_ext_arg_decl.py --num1=1 --num2=2 --num3=4