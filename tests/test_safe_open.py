import os
import pytest
from kindle_news_assistant.safe_open import mkdirs, safe_open


@pytest.mark.parametrize(
    "path,directory_structure", [("a/b/c/d.txt", "a/b/c"), ("a.txt", ".")]
)
def test_mkdirs(tmpdir, path, directory_structure):
    absolute_path = os.path.join(str(tmpdir), path)
    mkdirs(absolute_path)
    absolute_structure = os.path.join(str(tmpdir), directory_structure)
    assert os.path.isdir(absolute_structure)


def test_safe_open(tmpdir):
    path = "data/file.txt"
    absolute_path = os.path.join(str(tmpdir), path)
    with safe_open(absolute_path, "a+") as file:
        content = "test"
        file.write(content)
        file.seek(0)
        assert file.read() == content
