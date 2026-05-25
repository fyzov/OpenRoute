from utils import build_url, open_in_browser
from services import service

@service("habr")
def execute(prompt: str) -> None:
    base_url = "https://habr.com/ru/search/?q="
    url = build_url(base_url, prompt)
    open_in_browser(url)
