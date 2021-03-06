import argparse
from typing import Any, Callable, Iterable, Iterator, List, Match, Optional, Pattern, Tuple, Union

__version_info__: Any
DEFAULT_MENU_CURSOR: str
DEFAULT_MENU_CURSOR_STYLE: Any
DEFAULT_MENU_HIGHLIGHT_STYLE: Any
DEFAULT_CYCLE_CURSOR: bool
DEFAULT_CLEAR_SCREEN: bool
DEFAULT_PREVIEW_SIZE: float
DEFAULT_SEARCH_KEY: str
DEFAULT_SEARCH_CASE_SENSITIVE: bool
DEFAULT_SEARCH_HIGHLIGHT_STYLE: Any
DEFAULT_SHORTCUT_KEY_HIGHLIGHT_STYLE: Any
DEFAULT_SHORTCUT_PARENTHESES_HIGHLIGHT_STYLE: Any
DEFAULT_EXIT_ON_SHORTCUT: bool
DEFAULT_ACCEPT_KEYS: Any
DEFAULT_SHOW_SEARCH_HINT: bool
DEFAULT_SHOW_SHORTCUT_HINTS: bool
MIN_VISIBLE_MENU_ENTRIES_COUNT: int

class InvalidStyleError(Exception): ...
class NoMenuEntriesError(Exception): ...
class PreviewCommandFailedError(Exception): ...

def wcswidth(text: str) -> int: ...
def static_variables(**variables: Any) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...

class BoxDrawingCharacters:
    horizontal: str = ...
    vertical: str = ...
    upper_left: str = ...
    upper_right: str = ...
    lower_left: str = ...
    lower_right: str = ...

class TerminalMenu:
    class Search:
        def __init__(self, menu_entries: Iterable[str], search_text: Optional[str]=..., case_senitive: bool=..., show_search_hint: bool=...) -> None: ...
        @property
        def matches(self) -> List[Tuple[int, Match[str]]]: ...
        @property
        def search_regex(self) -> Optional[Pattern[str]]: ...
        @property
        def search_text(self) -> Optional[str]: ...
        @search_text.setter
        def search_text(self, text: Optional[str]) -> None: ...
        @property
        def change_callback(self) -> Optional[Callable[[], None]]: ...
        @change_callback.setter
        def change_callback(self, callback: Optional[Callable[[], None]]) -> None: ...
        @property
        def occupied_lines_count(self) -> int: ...
        def __bool__(self) -> bool: ...
        def __contains__(self, menu_index: int) -> bool: ...
        def __len__(self) -> int: ...
    class View:
        def __init__(self, menu_entries: Iterable[str], search: TerminalMenu.Search, viewport: TerminalMenu.Viewport, cycle_cursor: bool=...) -> None: ...
        def update_view(self) -> None: ...
        def increment_selected_index(self) -> None: ...
        def decrement_selected_index(self) -> None: ...
        @property
        def selected_index(self) -> Optional[int]: ...
        @selected_index.setter
        def selected_index(self, value: int) -> None: ...
        @property
        def selected_displayed_index(self) -> Optional[int]: ...
        def __iter__(self) -> Iterator[Tuple[int, int, str]]: ...
    class Viewport:
        def __init__(self, num_menu_entries: int, title_lines_count: int, preview_lines_count: int, search_lines_count: int) -> None: ...
        def keep_visible(self, cursor_position: Optional[int], refresh_terminal_size: bool=...) -> None: ...
        def update_terminal_size(self) -> None: ...
        @property
        def lower_index(self) -> int: ...
        @property
        def upper_index(self) -> int: ...
        @property
        def viewport(self) -> Tuple[int, int]: ...
        @property
        def size(self) -> int: ...
        @property
        def num_menu_entries(self) -> int: ...
        @property
        def title_lines_count(self) -> int: ...
        @property
        def preview_lines_count(self) -> int: ...
        @preview_lines_count.setter
        def preview_lines_count(self, value: int) -> None: ...
        @property
        def search_lines_count(self) -> int: ...
        @search_lines_count.setter
        def search_lines_count(self, value: int) -> None: ...
        @property
        def must_scroll(self) -> bool: ...
    def __init__(self, menu_entries: Iterable[str], title: Optional[Union[str, Iterable[str]]]=..., menu_cursor: Optional[str]=..., menu_cursor_style: Optional[Iterable[str]]=..., menu_highlight_style: Optional[Iterable[str]]=..., cycle_cursor: bool=..., clear_screen: bool=..., preview_command: Optional[Union[str, Callable[[str], str]]]=..., preview_size: float=..., search_key: Optional[str]=..., search_case_sensitive: bool=..., search_highlight_style: Optional[Iterable[str]]=..., shortcut_key_highlight_style: Optional[Iterable[str]]=..., shortcut_parentheses_highlight_style: Optional[Iterable[str]]=..., exit_on_shortcut: bool=..., accept_keys: Iterable[str]=..., show_search_hint: bool=..., show_shortcut_hints: bool=...): ...
    def show(self) -> Optional[int]: ...
    @property
    def chosen_accept_key(self) -> Optional[str]: ...
    @property
    def chosen_menu_entry(self) -> Optional[str]: ...
    @property
    def chosen_menu_index(self) -> Optional[int]: ...

class AttributeDict(dict):
    def __getattr__(self, attr: str) -> Any: ...
    def __setattr__(self, attr: str, value: Any) -> None: ...

def get_argumentparser() -> argparse.ArgumentParser: ...
def parse_arguments() -> AttributeDict: ...
def main() -> None: ...
