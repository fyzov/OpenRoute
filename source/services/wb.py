from utils import build_url, open_in_browser
from services import service


@service("wb")
@service("wildberries")
def execute(prompt: str) -> None:
    base_url = "https://www.wildberries.ru/catalog/0/search.aspx?search="
    url = build_url(base_url, prompt)
    open_in_browser(url)
