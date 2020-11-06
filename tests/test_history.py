import os
import pytest
from kindle_news_assistant.history import History


@pytest.fixture
def history_instance(tmpdir):
    absolute_path = os.path.join(str(tmpdir), "userdata/history.txt")
    return History(absolute_path)


def test_append_and_contains(history_instance):
    article_id = "1"
    assert history_instance.contains(article_id) is False

    history_instance.append(article_id)
    assert history_instance.contains(article_id)


def test_extend(history_instance):
    article_ids = ["1", "2"]
    for article_id in article_ids:
        assert history_instance.contains(article_id) is False

    history_instance.extend(article_ids)
    for article_id in article_ids:
        assert history_instance.contains(article_id)


def test_remove_ids_other_than(history_instance):
    article_ids = ["1", "2"]
    remove_other_than = ["2"]

    history_instance.extend(article_ids)
    history_instance.remove_ids_other_than(remove_other_than)

    assert history_instance.contains("1") is False
    assert history_instance.contains("2")
