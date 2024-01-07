from typing import Any, Self

from lxml.html import fromstring, HtmlElement
from lxml.cssselect import CSSSelector


class HTML:
    def __init__(self, html: (str or HtmlElement)) -> None:
        self.html = fromstring(html) if isinstance(html, str) else html

    def __repr__(self) -> str:
        return f'<Tag {self.html.tag} [{hex(id(self))}]>'

    def __getitem__(self, attr: str) -> Any:
        return self.html.attrib.get(attr)

    def text(self) -> str:
        return self.html.text_content()

    def css(self, selector: str, total: int = None) -> list[Self]:
        selector = CSSSelector(selector)
        tags = selector(self.html)

        if len(tags):
            return [HTML(tag) for tag in tags[0:total]]

        return None

    def single_css(self, selector: str) -> Self:
        select = self.css(selector)

        return None if select is None else select[0]
