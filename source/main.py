from utils import parse_args
from services import search

def main():
    args = parse_args()

    match args.command:
        case "search":
            search.execute(args.prompt)
        case _:
            print(f"Unknown command {args.command}")

if __name__ == "__main__":
    main()
