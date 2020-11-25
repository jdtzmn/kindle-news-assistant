from .videos import Video as Video
from typing import Any

VIDEOS_TAGS: Any
VIDEO_PROVIDERS: Any

class VideoExtractor:
    config: Any = ...
    parser: Any = ...
    top_node: Any = ...
    candidates: Any = ...
    movies: Any = ...
    def __init__(self, config: Any, top_node: Any) -> None: ...
    def get_embed_code(self, node: Any): ...
    def get_embed_type(self, node: Any): ...
    def get_width(self, node: Any): ...
    def get_height(self, node: Any): ...
    def get_src(self, node: Any): ...
    def get_provider(self, src: Any): ...
    def get_video(self, node: Any): ...
    def get_iframe_tag(self, node: Any): ...
    def get_video_tag(self, node: Any): ...
    def get_embed_tag(self, node: Any): ...
    def get_object_tag(self, node: Any): ...
    def get_videos(self): ...