from utils import build_url, open_in_browser

def execute(prompt: str) -> None:
    base_url = "https://www.youtube.com/results?search_query="
    url = build_url(base_url, prompt)
    open_in_browser(url)
