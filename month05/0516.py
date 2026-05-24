import argparse

"""
parser = argparse.ArgumentParser()
parser.add_argument("echo", help = "echo the string you use here")
parser.add_argument("square", help="the result of multiplying a number by ifself",type=int)
args = parser.parse_args()
print(args.echo)
print(args.square**2)
"""

parser = argparse.ArgumentParser()
parser.add_argument("--verbose",help="increase out verbosity",action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turn on")