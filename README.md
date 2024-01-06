# Fly
Fly is a small, yet useful library for web scraping. It's made in base of `LXML`, a Cython-based HTML-parsing library.<br>
Currently more efficient and memory-unintensive compared to BeautifulSoup.

```py
import fly

html = '<a href="http://example.com">hello</a>'
egg = fly.HTML(html)  # Parse the HTML

print(egg.single_css('a')['href'])  # Select a single tag and get the `href` attribute

# -> http://example.com
```

# Installing it
```sh
pip install git+https://github.com/ZSendokame/Penv.git
````