# Site konfigürasyonları
SITES = {
    "Hacker News": {
        "url": "https://news.ycombinator.com",
        "selectors": {
            "container": "tr.athing",
            "title": "a.titlelink",
            "link": "a.titlelink",
            "summary": ""  # HN'de özet yok
        }
    },
    "TechCrunch": {
        "url": "https://techcrunch.com",
        "selectors": {
            "container": "div.post-block",
            "title": "a.post-block__title__link",
            "link": "a.post-block__title__link",
            "summary": "div.post-block__content"
        }
    },
    "The Verge": {
        "url": "https://www.theverge.com/tech",
        "selectors": {
            "container": "div.c-entry-box--compact",
            "title": "h2 a",
            "link": "h2 a",
            "summary": "p.c-entry-box--compact__body"
        }
    },
    # Ek kaynaklar için buraya ekleyebilirsiniz
    # "Ars Technica": {
    #     "url": "https://arstechnica.com/tech/",
    #     "selectors": {
    #         "container": "article",
    #         "title": "h2 a",
    #         "link": "h2 a",
    #         "summary": "p.excerpt"
    #     }
    # }
}