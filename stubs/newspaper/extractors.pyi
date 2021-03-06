from . import urls as urls
from .utils import StringReplacement as StringReplacement, StringSplitter as StringSplitter
from typing import Any, Optional

log: Any
MOTLEY_REPLACEMENT: Any
ESCAPED_FRAGMENT_REPLACEMENT: Any
TITLE_REPLACEMENTS: Any
PIPE_SPLITTER: Any
DASH_SPLITTER: Any
UNDERSCORE_SPLITTER: Any
SLASH_SPLITTER: Any
ARROWS_SPLITTER: Any
COLON_SPLITTER: Any
SPACE_SPLITTER: Any
NO_STRINGS: Any
A_REL_TAG_SELECTOR: str
A_HREF_TAG_SELECTOR: str
RE_LANG: str
good_paths: Any
bad_chunks: Any
bad_domains: Any

class ContentExtractor:
    config: Any = ...
    parser: Any = ...
    language: Any = ...
    stopwords_class: Any = ...
    def __init__(self, config: Any) -> None: ...
    def update_language(self, meta_lang: Any) -> None: ...
    def get_authors(self, doc: Any): ...
    def get_publishing_date(self, url: Any, doc: Any): ...
    def get_title(self, doc: Any): ...
    def split_title(self, title: Any, splitter: Any, hint: Optional[Any] = ...): ...
    def get_feed_urls(self, source_url: Any, categories: Any): ...
    def get_favicon(self, doc: Any): ...
    def get_meta_lang(self, doc: Any): ...
    def get_meta_content(self, doc: Any, metaname: Any): ...
    def get_meta_img_url(self, article_url: Any, doc: Any): ...
    def get_meta_type(self, doc: Any): ...
    def get_meta_description(self, doc: Any): ...
    def get_meta_keywords(self, doc: Any): ...
    def get_meta_data(self, doc: Any): ...
    def get_canonical_link(self, article_url: Any, doc: Any): ...
    def get_img_urls(self, article_url: Any, doc: Any): ...
    def get_first_img_url(self, article_url: Any, top_node: Any): ...
    def get_urls(self, doc_or_html: Any, titles: bool = ..., regex: bool = ...): ...
    def get_category_urls(self, source_url: Any, doc: Any): ...
    def extract_tags(self, doc: Any): ...
    def calculate_best_node(self, doc: Any): ...
    def is_boostable(self, node: Any): ...
    def walk_siblings(self, node: Any): ...
    def add_siblings(self, top_node: Any): ...
    def get_siblings_content(self, current_sibling: Any, baseline_score_siblings_para: Any): ...
    def get_siblings_score(self, top_node: Any): ...
    def update_score(self, node: Any, add_to_score: Any) -> None: ...
    def update_node_count(self, node: Any, add_to_count: Any) -> None: ...
    def is_highlink_density(self, e: Any): ...
    def get_score(self, node: Any): ...
    def get_node_gravity_score(self, node: Any): ...
    def nodes_to_check(self, doc: Any): ...
    def is_table_and_no_para_exist(self, e: Any): ...
    def is_nodescore_threshold_met(self, node: Any, e: Any): ...
    def post_cleanup(self, top_node: Any): ...
