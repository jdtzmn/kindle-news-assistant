from .exceptions import *
from .sgml import *
from . import http as http, mixin as mixin
from .datetimes import registerDateHandler as registerDateHandler
from .encodings import convert_to_utf8 as convert_to_utf8
from .sanitizer import replace_doctype as replace_doctype
from .urls import convert_to_idn as convert_to_idn, make_safe_absolute_uri as make_safe_absolute_uri
from .util import FeedParserDict as FeedParserDict
from typing import Any, Optional

PREFERRED_XML_PARSERS: Any
SUPPORTED_VERSIONS: Any
LooseFeedParser: Any
StrictFeedParser: Any

def parse(url_file_stream_or_string: Any, etag: Optional[Any] = ..., modified: Optional[Any] = ..., agent: Optional[Any] = ..., referrer: Optional[Any] = ..., handlers: Optional[Any] = ..., request_headers: Optional[Any] = ..., response_headers: Optional[Any] = ..., resolve_relative_uris: Optional[Any] = ..., sanitize_html: Optional[Any] = ...): ...
