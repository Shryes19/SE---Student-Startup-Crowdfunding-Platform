"""Line/code coverage tests for the assigned spam-scoring application."""
from spam_scoring import score_message, classify, filter_inbox, inbox_status


def test_spam_words_and_punctuation_are_scored():
    assert score_message("FREE! winner, prize. urgent cash", False, 0) == 10


def test_uppercase_word_scores_when_not_spam_word():
    assert score_message("HELLO NORMAL", False, 0) == 2


def test_link_count_above_three_adds_four():
    assert score_message("hello", False, 4) == 4


def test_link_count_one_to_three_adds_one():
    assert score_message("hello", False, 1) == 1


def test_known_sender_score_is_clamped_to_zero():
    assert score_message("hello", True, 0) == 0


def test_known_sender_reduces_positive_score():
    assert score_message("free", True, 1) == 0


def test_classify_all_labels():
    assert classify(8) == "spam"
    assert classify(4) == "suspicious"
    assert classify(0) == "clean"


def test_filter_inbox_counts_each_label():
    messages = [("free winner prize urgent", False, 0), ("free free", False, 0), ("hello", False, 0)]
    assert filter_inbox(messages) == {"spam": 1, "suspicious": 1, "clean": 1}


def test_filter_inbox_empty_input():
    assert filter_inbox([]) == {"spam": 0, "suspicious": 0, "clean": 0}


def test_inbox_status_empty():
    assert inbox_status({"spam": 0, "suspicious": 0, "clean": 0}) == "empty"


def test_inbox_status_flooded():
    assert inbox_status({"spam": 6, "suspicious": 2, "clean": 2}) == "flooded"


def test_inbox_status_noisy():
    assert inbox_status({"spam": 3, "suspicious": 4, "clean": 3}) == "noisy"


def test_inbox_status_healthy():
    assert inbox_status({"spam": 1, "suspicious": 4, "clean": 5}) == "healthy"
