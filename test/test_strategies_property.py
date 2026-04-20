from hypothesis import given
from hypothesis import strategies as st

from src.strategies import (
    always_cooperate,
    always_defect,
    grimm_trigger,
    tit_for_tat,
    tit_for_two_tats,
)

COOPERATE = True
DEFECT = False


@st.composite
def history_varied_cases(draw, min_size=1, max_size=50):
    history = draw(st.lists(st.booleans(), min_size=min_size, max_size=max_size))
    return history


@st.composite
def history_all_cooperate(draw, min_size=1, max_size=50):
    n = draw(st.integers(min_value=min_size, max_value=max_size))
    history = [True] * n
    return history


@st.composite
def history_cooperate_with_one_defect(draw, min_size=1, max_size=50):
    n = draw(st.integers(min_value=min_size, max_value=max_size))
    index = draw(st.integers(min_value=0, max_value=n - 1))
    history = [True] * n
    history[index] = False
    return history


@given(history_varied_cases())
def test_always_cooperate_always_cooperates(opponent_history):
    self_history_irrelevant = []
    assert always_cooperate(self_history_irrelevant, opponent_history) is COOPERATE


@given(history_varied_cases())
def test_always_defect_always_defects(opponent_history):
    self_history_irrelevant = []
    assert always_defect(self_history_irrelevant, opponent_history) is DEFECT


@given(history_varied_cases())
def test_grimm_trigger_if_opponent_always_cooperates_cooperate_else_defect(opponent_history):
    self_history_irrelevant = []
    has_always_cooperated = DEFECT not in opponent_history
    assert grimm_trigger(self_history_irrelevant, opponent_history) is has_always_cooperated


@given(history_all_cooperate())
def test_grimm_trigger_opponent_never_defected_cooperate(opponent_history):
    self_history_irrelevant = []
    assert grimm_trigger(self_history_irrelevant, opponent_history) is COOPERATE


@given(history_cooperate_with_one_defect())
def test_grimm_trigger_opponent_defected_once_defect(opponent_history):
    self_history_irrelevant = []
    assert grimm_trigger(self_history_irrelevant, opponent_history) is DEFECT


# Strategy random_move property tests excluded because of randomness, randomness mocked in unittests


@given(history_varied_cases())
def test_tit_for_tat_copies_opponents_last_move(opponent_history):
    self_history_irrelevant = []
    last_move = opponent_history[-1]
    assert tit_for_tat(self_history_irrelevant, opponent_history) is last_move


@given(history_varied_cases(min_size=2))
def test_tit_for_two_tats_if_opponent_last_two_moves_not_defect_cooperate_else_defect(opponent_history):
    self_history_irrelevant = []
    were_last_two_moves_not_defect = opponent_history[-2:] != [DEFECT, DEFECT]
    assert tit_for_two_tats(self_history_irrelevant, opponent_history) is were_last_two_moves_not_defect
