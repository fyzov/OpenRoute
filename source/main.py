from utils import parse_args
import services
import importlib
import os

def main():
    services_dir = os.path.dirname(__file__) + "/services"
    for file in os.listdir(services_dir):
        if file.endswith(".py") and file not in ["__init__.py"]:
            module_name = file[:-3]
            importlib.import_module(f"services.{module_name}")

    args = parse_args()

    if not args.command:
        print_help()
        return

    if args.command in services.SERVICES:
        services.SERVICES[args.command](args.prompt)
    else:
        print(f"❌ Command '{args.command}' not found")
        print_help()

def print_help():
    print("\n📚 Available services:")
    for name in services.SERVICES.keys():
        print(f"  • {name}")

if __name__ == "__main__":
    main()
