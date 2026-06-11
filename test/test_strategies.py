import random

import pytest

from evogt.strategies import (
    always_cooperate,
    always_defect,
    grim_trigger,
    random_move,
    tit_for_tat,
    tit_for_two_tats,
)


def test_always_cooperate_no_history_returns_true():
    assert always_cooperate([], []) is True


@pytest.mark.parametrize(
    "history_self, history_opponent",
    [
        ([True], [False]),
        ([False, False], [True, True]),
        ([True, False, True], [False, True, False]),
    ],
)
def test_always_cooperate_with_history_returns_true(history_self, history_opponent):
    assert always_cooperate(history_self, history_opponent) is True


def test_always_defect_no_history_returns_false():
    assert always_defect([], []) is False


@pytest.mark.parametrize(
    "history_self, history_opponent",
    [
        ([True], [False]),
        ([False, False], [True, True]),
        ([True, False, True], [False, True, False]),
    ],
)
def test_always_defect_with_history_returns_false(history_self, history_opponent):
    assert always_defect(history_self, history_opponent) is False


def test_grim_trigger_no_history_returns_true():
    assert grim_trigger([], []) is True


@pytest.mark.parametrize(
    "history_self, history_opponent",
    [
        ([True], [True]),
        ([False, False], [True, True]),
        ([True, False, True], [True, True, True]),
    ],
)
def test_grim_trigger_with_history_opponent_has_not_defected_returns_true(history_self, history_opponent):
    assert grim_trigger(history_self, history_opponent) is True


@pytest.mark.parametrize(
    "history_self, history_opponent",
    [
        ([True], [False]),
        ([False, False], [True, False]),
        ([True, False, True], [False, True, True]),
    ],
)
def test_grim_trigger_with_history_opponent_has_defected_returns_false(history_self, history_opponent):
    assert grim_trigger(history_self, history_opponent) is False


@pytest.mark.parametrize("return_value", [True, False])
@pytest.mark.parametrize(
    "history_self, history_opponent",
    [
        ([], []),
        ([True], [False]),
        ([False, True], [True, False]),
        ([True, False, True], [False, True, False]),
    ],
)
def test_random_move_arbitrary_history_returns_random_choice(history_self, history_opponent, return_value, mocker):
    mocker.patch("random.choice", return_value=return_value)
    assert random_move(history_self, history_opponent) is return_value
    random.choice.assert_called_once_with([True, False])


def test_random_move_same_rng_seed_returns_same_moves():
    rng_first = random.Random(101)
    rng_second = random.Random(101)
    moves_first = [random_move([], [], rng=rng_first) for _ in range(10)]
    moves_second = [random_move([], [], rng=rng_second) for _ in range(10)]
    assert moves_first == moves_second


def test_random_move_with_rng_does_not_use_global_random(mocker):
    mocker.patch("random.choice")
    random_move([], [], rng=random.Random(101))
    random.choice.assert_not_called()


def test_tit_for_tat_no_history_returns_true():
    assert tit_for_tat([], []) is True


@pytest.mark.parametrize(
    "history_self, history_opponent",
    [
        ([True], [True]),
        ([False, False], [False, True]),
        ([False, False, True], [False, False, True]),
    ],
)
def test_tit_for_tat_with_history_opponent_cooperate_last_move_returns_true(history_self, history_opponent):
    assert tit_for_tat(history_self, history_opponent) is True


@pytest.mark.parametrize(
    "history_self, history_opponent",
    [
        ([True], [False]),
        ([False, False], [True, False]),
        ([False, False, True], [True, False, False]),
    ],
)
def test_tit_for_tat_with_history_opponent_defect_last_move_returns_false(history_self, history_opponent):
    assert tit_for_tat(history_self, history_opponent) is False


@pytest.mark.parametrize(
    "history_self, history_opponent",
    [
        ([], []),
        ([True], [True]),
        ([False], [False]),
    ],
)
def test_tit_for_two_tats_insufficient_history_returns_true(history_self, history_opponent):
    assert tit_for_two_tats(history_self, history_opponent) is True


@pytest.mark.parametrize(
    "history_self, history_opponent",
    [
        ([True, True], [True, True]),
        ([True, False], [True, False]),
        ([False, True], [False, True]),
        ([False, True, False], [False, True, False]),
    ],
)
def test_tit_for_two_tats_with_history_opponent_not_defect_last_two_moves_returns_true(history_self, history_opponent):
    assert tit_for_two_tats(history_self, history_opponent) is True


@pytest.mark.parametrize(
    "history_self, history_opponent",
    [
        ([True, False], [False, False]),
        ([True, False, True], [False, False, False]),
        ([False, True, False], [True, False, False]),
    ],
)
def test_tit_for_two_tats_with_history_opponent_defect_last_two_moves_returns_false(history_self, history_opponent):
    assert tit_for_two_tats(history_self, history_opponent) is False
