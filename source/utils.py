import sys
import webbrowser
from urllib.parse import quote

class Args:
    def __init__(self, command: str, prompt: str):
        self.command = command
        self.prompt = prompt

def parse_args() -> Args:
    args = sys.argv[1:]

    if not args:
        return Args("", "")

    command = args[0]
    prompt = " ".join(args[1:]) if len(args) > 1 else ""

    return Args(command, prompt)

def build_url(base_url: str, prompt: str) -> str:
    return f"{base_url}{quote(prompt)}"

def open_in_browser(url: str) -> None:
    webbrowser.open(url)
