from utils import build_url, open_in_browser
from services import service

@service("wiki")
def execute(prompt: str) -> None:
    base_url = "https://en.wikipedia.org/w/index.php?search="
    url = build_url(base_url, prompt)
    open_in_browser(url)
