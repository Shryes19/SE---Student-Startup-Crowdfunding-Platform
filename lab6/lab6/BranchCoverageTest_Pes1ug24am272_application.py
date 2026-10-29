"""Branch coverage tests for every decision in spam_scoring.py."""
from spam_scoring import score_message, classify, filter_inbox, inbox_status


def test_spam_word_branch_true_and_false():
    assert score_message("free hello", False, 0) == 2


def test_uppercase_fallback_true_and_false():
    assert score_message("HELLO hello", False, 0) == 1
    assert score_message("hey", False, 0) == 0


def test_spam_word_punctuation_normalization():
    assert score_message("FREE! winner, prize. urgent cash", False, 0) == 10


def test_link_count_greater_than_three():
    assert score_message("hello", False, 4) == 4


def test_link_count_between_one_and_three():
    assert score_message("hello", False, 2) == 1


def test_zero_links():
    assert score_message("hello", False, 0) == 0


def test_known_sender_negative_score_is_clamped():
    assert score_message("hello", True, 0) == 0


def test_known_sender_nonnegative_score_not_clamped():
    assert score_message("free free", True, 0) == 1


def test_unknown_sender_skips_penalty():
    assert score_message("free", False, 0) == 2


def test_classify_spam_boundary_and_above():
    assert classify(8) == "spam"
    assert classify(12) == "spam"


def test_classify_suspicious_boundary_and_middle():
    assert classify(4) == "suspicious"
    assert classify(7) == "suspicious"


def test_classify_clean_below_four():
    assert classify(3) == "clean"


def test_filter_inbox_mixed_messages():
    msgs = [("free winner prize urgent", False, 0), ("free free", False, 0), ("hello", False, 0)]
    assert filter_inbox(msgs) == {"spam": 1, "suspicious": 1, "clean": 1}


def test_filter_inbox_empty_list():
    assert filter_inbox([]) == {"spam": 0, "suspicious": 0, "clean": 0}


def test_inbox_status_empty():
    assert inbox_status({"spam": 0, "suspicious": 0, "clean": 0}) == "empty"


def test_inbox_status_flooded_above_half():
    assert inbox_status({"spam": 6, "suspicious": 2, "clean": 2}) == "flooded"


def test_inbox_status_exactly_half_is_not_flooded():
    assert inbox_status({"spam": 5, "suspicious": 3, "clean": 2}) == "noisy"


def test_inbox_status_noisy_above_point_two():
    assert inbox_status({"spam": 3, "suspicious": 4, "clean": 3}) == "noisy"


def test_inbox_status_exactly_point_two_is_healthy():
    assert inbox_status({"spam": 2, "suspicious": 4, "clean": 4}) == "healthy"


def test_inbox_status_healthy_below_point_two():
    assert inbox_status({"spam": 1, "suspicious": 4, "clean": 5}) == "healthy"
