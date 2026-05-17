import argparse

from luckydate import move



parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")
move_parser = subparsers.add_parser("move",help= "move는 이사나 개업등의 행동하기 좋은 날을 추천해줍니다.")
move_parser.add_argument("birthday" ,type=int,help="생년월일을 입력해주세요 ex 20260101")

args = parser.parse_args()
if len(str(args.birthday)) != 8:
    print("생년월일을 다시 확인해주세요")
    exit()
if args.command == "move":
    print("생년월일:", args.birthday)
    move.move_getSondate(args.birthday)