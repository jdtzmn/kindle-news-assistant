"""Methods to aid in constructing an epub book."""
import os
from typing import List, Union, cast
from datetime import datetime
from newspaper.article import Article
from ebooklib import epub
from kindle_news_assistant.safe_open import mkdirs

BOOK_PATH = "../../userdata/issue.epub"


def construct_chapter_content(article: Article) -> str:
    """Construct a chapter from an article. Will add a header to the article if it is necessary.

    :param article: The article to use when constructing chapter content.
    :return: An html string of the chapter's content.
    """
    if not "<h1>" in article.article_html:
        return f"""
            <section>
                <h1>{article.title}</h1>
                {article.article_html}
            </section>"""
    return article.article_html


def construct_book_from(articles: List[Article]):
    """Construct an epub book from a list of articles.

    :param articles: The article list to construct a book from
    :return: The absolute path of the constructed epub book
    """
    book = epub.EpubBook()

    # Metadata
    now = datetime.now()
    book.set_identifier("news-assistant-" + now.strftime("%c"))
    book.set_title("News from " + now.strftime("%d %B, %Y"))
    book.set_language("en")
    book.add_author("News Assistant")

    # Chapters
    chapters: List[epub.EpubHtml] = []
    for index, article in enumerate(articles):
        chapter = epub.EpubHtml(
            title=article.title,
            file_name=f"article{index}.xhtml",
        )
        chapter.set_content(construct_chapter_content(article))

        book.add_item(chapter)
        chapters.append(chapter)

    # Table of Contents
    book.toc = chapters

    # Navigation Files
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # CSS Styles
    main_css = epub.EpubItem(
        uid="style_main",
        file_name="style/main.css",
        media_type="text/css",
        content=BOOK_CSS_STYLE,
    )
    book.add_item(main_css)

    # Book Spine
    book.spine = cast(List[Union[str, epub.EpubHtml]], ["nav"]) + cast(
        List[Union[str, epub.EpubHtml]], chapters
    )

    # Save Book
    dirname = os.path.dirname(__file__)
    absolute_path = os.path.join(dirname, BOOK_PATH)
    mkdirs(os.path.dirname(absolute_path))  # Ensure that directories have been created
    epub.write_epub(absolute_path, book)

    return absolute_path


# This is the CSS styling that will be added to the epub.
BOOK_CSS_STYLE = """
@namespace epub "http://www.idpf.org/2007/ops";

body {
    font-family: Cambria, Liberation Serif, Bitstream Vera Serif, Georgia, Times, Times New Roman, serif;
}

h2 {
    text-align: left;
    text-transform: uppercase;
    font-weight: 200;     
}

ol {
        list-style-type: none;
}

ol > li:first-child {
        margin-top: 0.3em;
}

nav[epub|type~='toc'] > ol > li > ol  {
    list-style-type:square;
}

nav[epub|type~='toc'] > ol > li > ol > li {
        margin-top: 0.3em;
}

"""
