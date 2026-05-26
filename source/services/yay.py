from utils import build_url, open_in_browser
from services import service


@service("yay")
def execute(prompt: str) -> None:
    base_url = "https://aur.archlinux.org/packages?O=0&SeB=nd&K="
    url = build_url(base_url, prompt)
    open_in_browser(url)
