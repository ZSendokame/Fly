from typing import Any, Self

from lxml.html import fromstring
from lxml.cssselect import CSSSelector


class HTML:
    def __init__(self, html: str) -> None:
        self.html = fromstring(html.strip()) if isinstance(html, str) else html

    def __repr__(self) -> str:
        return f'<Tag {self.html.tag} [{hex(id(self))}]>'

    def __getitem__(self, attr: str) -> Any:
        return self.html.attrib.get(attr)

    def text(self) -> str:
        return self.html.text_content().strip()

    def css(self, selector: str, total: int = None) -> list[Self]:
        selector = CSSSelector(selector)
        tags = selector(self.html)

        if len(tags):
            return [HTML(tag) for tag in tags[0:total]]

        return []

    def nth_css(self, selector: str, position: int = 0) -> Self:
        select = self.css(selector) or None

        return None if select is None else select[position]

    def single_css(self, selector: str) -> Self:
        return self.nth_css(selector)
