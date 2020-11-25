from . import urls as urls
from typing import Any, Optional

log: Any
chunk_size: int
thumbnail_size: Any
minimal_area: int

def image_to_str(image: Any): ...
def str_to_image(s: Any): ...
def prepare_image(image: Any): ...
def image_entropy(img: Any): ...
def square_image(img: Any): ...
def clean_url(url: Any): ...
def fetch_url(url: Any, useragent: Any, referer: Optional[Any] = ..., retries: int = ..., dimension: bool = ...): ...
def fetch_image_dimension(url: Any, useragent: Any, referer: Optional[Any] = ..., retries: int = ...): ...

class Scraper:
    url: Any = ...
    imgs: Any = ...
    top_img: Any = ...
    config: Any = ...
    useragent: Any = ...
    def __init__(self, article: Any) -> None: ...
    def largest_image_url(self): ...
    def calculate_area(self, img_url: Any, dimension: Any): ...
    def satisfies_requirements(self, img_url: Any): ...
    def thumbnail(self): ...