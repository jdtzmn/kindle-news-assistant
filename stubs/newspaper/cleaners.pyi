from .utils import ReplaceSequence as ReplaceSequence
from typing import Any

class DocumentCleaner:
    config: Any = ...
    parser: Any = ...
    remove_nodes_re: str = ...
    regexp_namespace: str = ...
    nauthy_ids_re: Any = ...
    nauthy_classes_re: Any = ...
    nauthy_names_re: Any = ...
    div_to_p_re: str = ...
    caption_re: str = ...
    google_re: str = ...
    entries_re: str = ...
    facebook_re: str = ...
    facebook_braodcasting_re: str = ...
    twitter_re: str = ...
    tablines_replacements: Any = ...
    contains_article: str = ...
    def __init__(self, config: Any) -> None: ...
    def clean(self, doc_to_clean: Any): ...
    def clean_body_classes(self, doc: Any): ...
    def clean_article_tags(self, doc: Any): ...
    def clean_em_tags(self, doc: Any): ...
    def remove_drop_caps(self, doc: Any): ...
    def remove_scripts_styles(self, doc: Any): ...
    def clean_bad_tags(self, doc: Any): ...
    def remove_nodes_regex(self, doc: Any, pattern: Any): ...
    def clean_para_spans(self, doc: Any): ...
    def get_flushed_buffer(self, replacement_text: Any, doc: Any): ...
    def replace_walk_left_right(self, kid: Any, kid_text: Any, replacement_text: Any, nodes_to_remove: Any) -> None: ...
    def get_replacement_nodes(self, doc: Any, div: Any): ...
    def replace_with_para(self, doc: Any, div: Any) -> None: ...
    def div_to_para(self, doc: Any, dom_type: Any): ...