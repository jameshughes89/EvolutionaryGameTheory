import pytest
from hypothesis import given
from hypothesis import strategies as st

from src.games import (
    battle_of_the_sexes,
    chicken,
    deadlock,
    hawk_dove,
    matching_pennies,
    prisoners_dilemma,
    stag_hunt,
    ultimatum,
    volunteer_dilemma,
    volunteer_dilemma_quantum,
)


@given(
    move_player_fight=st.booleans(),
    move_opponent_fight=st.booleans(),
    preferred_together_payoff=st.integers(min_value=-10, max_value=10),
    unpreferred_together_payoff=st.integers(min_value=-10, max_value=10),
    preferred_alone_payoff=st.integers(min_value=-10, max_value=10),
)
def test_battle_of_the_sexes_varied_moves_and_payoffs_returns_expected_payoffs(
    move_player_fight,
    move_opponent_fight,
    preferred_together_payoff,
    unpreferred_together_payoff,
    preferred_alone_payoff,
):
    payoff_player, payoff_opponent = battle_of_the_sexes(
        move_player_fight,
        move_opponent_fight,
        preferred_together_payoff,
        unpreferred_together_payoff,
        preferred_alone_payoff,
    )
    if move_player_fight and move_opponent_fight:
        assert payoff_player == preferred_together_payoff
        assert payoff_opponent == unpreferred_together_payoff
    elif not move_player_fight and not move_opponent_fight:
        assert payoff_player == unpreferred_together_payoff
        assert payoff_opponent == preferred_together_payoff
    elif move_player_fight and not move_opponent_fight:
        assert payoff_player == preferred_alone_payoff
        assert payoff_opponent == preferred_alone_payoff
    else:
        assert payoff_player == 0
        assert payoff_opponent == 0


@given(
    move_player_swerve=st.booleans(),
    move_opponent_swerve=st.booleans(),
    tie_payoff=st.integers(min_value=-10, max_value=10),
    win_payoff=st.integers(min_value=-10, max_value=10),
    lose_payoff=st.integers(min_value=-10, max_value=10),
    crash_payoff=st.integers(min_value=-10, max_value=10),
)
def test_chicken_varied_moves_and_payoffs_returns_expected_payoffs(
    move_player_swerve,
    move_opponent_swerve,
    tie_payoff,
    win_payoff,
    lose_payoff,
    crash_payoff,
):
    payoff_player, payoff_opponent = chicken(
        move_player_swerve,
        move_opponent_swerve,
        tie_payoff,
        win_payoff,
        lose_payoff,
        crash_payoff,
    )
    if move_player_swerve and move_opponent_swerve:
        assert payoff_player == tie_payoff
        assert payoff_opponent == tie_payoff
    elif move_player_swerve and not move_opponent_swerve:
        assert payoff_player == lose_payoff
        assert payoff_opponent == win_payoff
    elif not move_player_swerve and move_opponent_swerve:
        assert payoff_player == win_payoff
        assert payoff_opponent == lose_payoff
    else:
        assert payoff_player == crash_payoff
        assert payoff_opponent == crash_payoff


@given(
    move_player_cooperate=st.booleans(),
    move_opponent_cooperate=st.booleans(),
    player_cooperate_cooperate_payoff=st.integers(min_value=-10, max_value=10),
    player_defect_defect_payoff=st.integers(min_value=-10, max_value=10),
    player_cooperate_defect_payoff=st.integers(min_value=-10, max_value=10),
    player_defect_cooperate_payoff=st.integers(min_value=-10, max_value=10),
    opponent_cooperate_cooperate_payoff=st.integers(min_value=-10, max_value=10),
    opponent_defect_defect_payoff=st.integers(min_value=-10, max_value=10),
    opponent_cooperate_defect_payoff=st.integers(min_value=-10, max_value=10),
    opponent_defect_cooperate_payoff=st.integers(min_value=-10, max_value=10),
)
def test_deadlock_varied_moves_and_payoffs_returns_expected_payoffs(
    move_player_cooperate,
    move_opponent_cooperate,
    player_cooperate_cooperate_payoff,
    player_defect_defect_payoff,
    player_cooperate_defect_payoff,
    player_defect_cooperate_payoff,
    opponent_cooperate_cooperate_payoff,
    opponent_defect_defect_payoff,
    opponent_cooperate_defect_payoff,
    opponent_defect_cooperate_payoff,
):
    payoff_player, payoff_opponent = deadlock(
        move_player_cooperate,
        move_opponent_cooperate,
        player_cooperate_cooperate_payoff,
        player_defect_defect_payoff,
        player_cooperate_defect_payoff,
        player_defect_cooperate_payoff,
        opponent_cooperate_cooperate_payoff,
        opponent_defect_defect_payoff,
        opponent_cooperate_defect_payoff,
        opponent_defect_cooperate_payoff,
    )
    if move_player_cooperate and move_opponent_cooperate:
        assert payoff_player == player_cooperate_cooperate_payoff
        assert payoff_opponent == opponent_cooperate_cooperate_payoff
    elif not move_player_cooperate and not move_opponent_cooperate:
        assert payoff_player == player_defect_defect_payoff
        assert payoff_opponent == opponent_defect_defect_payoff
    elif move_player_cooperate and not move_opponent_cooperate:
        assert payoff_player == player_cooperate_defect_payoff
        assert payoff_opponent == opponent_cooperate_defect_payoff
    else:
        assert payoff_player == player_defect_cooperate_payoff
        assert payoff_opponent == opponent_defect_cooperate_payoff


@given(
    move_player_hawk=st.booleans(),
    move_opponent_hawk=st.booleans(),
    resource_payoff=st.integers(min_value=-10, max_value=10),
    cost=st.integers(min_value=-10, max_value=10),
)
def test_hawk_dove_varied_moves_and_payoffs_returns_expected_payoffs(
    move_player_hawk,
    move_opponent_hawk,
    resource_payoff,
    cost,
):
    payoff_player, payoff_opponent = hawk_dove(
        move_player_hawk,
        move_opponent_hawk,
        resource_payoff,
        cost,
    )
    if move_player_hawk and move_opponent_hawk:
        assert payoff_player == (resource_payoff - cost) / 2
        assert payoff_opponent == (resource_payoff - cost) / 2
    elif not move_player_hawk and not move_opponent_hawk:
        assert payoff_player == resource_payoff / 2
        assert payoff_opponent == resource_payoff / 2
    elif move_player_hawk and not move_opponent_hawk:
        assert payoff_player == resource_payoff
        assert payoff_opponent == 0
    else:
        assert payoff_player == 0
        assert payoff_opponent == resource_payoff


@given(
    move_player_heads=st.booleans(),
    move_opponent_heads=st.booleans(),
)
def test_matching_pennies_varied_moves_returns_expected_payoffs(
    move_player_heads,
    move_opponent_heads,
):
    payoff_player, payoff_opponent = matching_pennies(move_player_heads, move_opponent_heads)
    if move_player_heads and move_opponent_heads:
        assert payoff_player == 1
        assert payoff_opponent == -1
    elif not move_player_heads and not move_opponent_heads:
        assert payoff_player == 1
        assert payoff_opponent == -1
    elif move_player_heads and not move_opponent_heads:
        assert payoff_player == -1
        assert payoff_opponent == 1
    else:
        assert payoff_player == -1
        assert payoff_opponent == 1


@given(
    move_player_cooperate=st.booleans(),
    move_opponent_cooperate=st.booleans(),
    reward_payoff=st.integers(min_value=-10, max_value=10),
    punishment_payoff=st.integers(min_value=-10, max_value=10),
    temptation_payoff=st.integers(min_value=-10, max_value=10),
    sucker_payoff=st.integers(min_value=-10, max_value=10),
)
def test_prisoners_dilemma_varied_moves_and_payoffs_returns_expected_payoffs(
    move_player_cooperate,
    move_opponent_cooperate,
    reward_payoff,
    punishment_payoff,
    temptation_payoff,
    sucker_payoff,
):
    payoff_player, payoff_opponent = prisoners_dilemma(
        move_player_cooperate,
        move_opponent_cooperate,
        reward_payoff,
        punishment_payoff,
        temptation_payoff,
        sucker_payoff,
    )
    if move_player_cooperate and move_opponent_cooperate:
        assert payoff_player == reward_payoff
        assert payoff_opponent == reward_payoff
    elif not move_player_cooperate and not move_opponent_cooperate:
        assert payoff_player == punishment_payoff
        assert payoff_opponent == punishment_payoff
    elif move_player_cooperate and not move_opponent_cooperate:
        assert payoff_player == sucker_payoff
        assert payoff_opponent == temptation_payoff
    else:
        assert payoff_player == temptation_payoff
        assert payoff_opponent == sucker_payoff


@given(
    move_player_stag=st.booleans(),
    move_opponent_stag=st.booleans(),
    stag_together_payoff=st.integers(min_value=-10, max_value=10),
    hare_alone_payoff=st.integers(min_value=-10, max_value=10),
    hare_together_payoff=st.integers(min_value=-10, max_value=10),
    stag_alone_payoff=st.integers(min_value=-10, max_value=10),
)
def test_stag_hunt_varied_moves_and_payoffs_returns_expected_payoffs(
    move_player_stag,
    move_opponent_stag,
    stag_together_payoff,
    hare_alone_payoff,
    hare_together_payoff,
    stag_alone_payoff,
):
    payoff_player, payoff_opponent = stag_hunt(
        move_player_stag,
        move_opponent_stag,
        stag_together_payoff,
        hare_alone_payoff,
        hare_together_payoff,
        stag_alone_payoff,
    )
    if move_player_stag and move_opponent_stag:
        assert payoff_player == stag_together_payoff
        assert payoff_opponent == stag_together_payoff
    elif not move_player_stag and not move_opponent_stag:
        assert payoff_player == hare_together_payoff
        assert payoff_opponent == hare_together_payoff
    elif move_player_stag and not move_opponent_stag:
        assert payoff_player == stag_alone_payoff
        assert payoff_opponent == hare_alone_payoff
    else:
        assert payoff_player == hare_alone_payoff
        assert payoff_opponent == stag_alone_payoff


@given(
    move_player_fair=st.booleans(),
    move_opponent_accept=st.booleans(),
    fair_payoff=st.integers(min_value=-10, max_value=10),
    unfair_payoff_player=st.integers(min_value=-10, max_value=10),
    unfair_payoff_opponent=st.integers(min_value=-10, max_value=10),
    reject_payoff=st.integers(min_value=-10, max_value=10),
)
def test_ultimatum_varied_offers_and_payoffs_returns_expected_payoffs(
    move_player_fair,
    move_opponent_accept,
    fair_payoff,
    unfair_payoff_player,
    unfair_payoff_opponent,
    reject_payoff,
):
    payoff_player, payoff_opponent = ultimatum(
        move_player_fair,
        move_opponent_accept,
        fair_payoff,
        unfair_payoff_player,
        unfair_payoff_opponent,
        reject_payoff,
    )
    if move_player_fair and move_opponent_accept:
        assert payoff_player == fair_payoff
        assert payoff_opponent == fair_payoff
    elif move_player_fair and not move_opponent_accept:
        assert payoff_player == reject_payoff
        assert payoff_opponent == reject_payoff
    elif not move_player_fair and move_opponent_accept:
        assert payoff_player == unfair_payoff_player
        assert payoff_opponent == unfair_payoff_opponent
    else:
        assert payoff_player == reject_payoff
        assert payoff_opponent == reject_payoff


@given(
    moves_players_volunteer=st.lists(st.booleans(), min_size=1, max_size=10),
    volunteer_payoff=st.integers(min_value=-10, max_value=10),
    public_payoff=st.integers(min_value=-10, max_value=10),
    non_volunteer_payoff=st.integers(min_value=-10, max_value=10),
)
def test_volunteer_dilemma_varied_moves_and_payoffs_returns_expected_payoffs(
    moves_players_volunteer,
    volunteer_payoff,
    public_payoff,
    non_volunteer_payoff,
):
    payoffs = volunteer_dilemma(
        moves_players_volunteer,
        volunteer_payoff,
        public_payoff,
        non_volunteer_payoff,
    )
    if any(moves_players_volunteer):
        for move_volunteer, payoff in zip(moves_players_volunteer, payoffs):
            if move_volunteer:
                assert payoff == volunteer_payoff
            else:
                assert payoff == public_payoff
    else:
        for payoff in payoffs:
            assert payoff == non_volunteer_payoff


@given(
    moves_players_volunteer=st.lists(st.booleans(), min_size=1, max_size=10),
    volunteer_payoff=st.integers(min_value=-10, max_value=10),
    public_payoff=st.integers(min_value=-10, max_value=10),
    non_volunteer_payoff=st.integers(min_value=-10, max_value=10),
)
def test_volunteer_dilemma_quantum_varied_moves_and_payoffs_returns_expected_payoffs(
    moves_players_volunteer,
    volunteer_payoff,
    public_payoff,
    non_volunteer_payoff,
):
    payoffs = volunteer_dilemma_quantum(
        moves_players_volunteer,
        volunteer_payoff,
        public_payoff,
        non_volunteer_payoff,
    )
    number_of_volunteers = moves_players_volunteer.count(True)
    if number_of_volunteers > 0:
        for move_volunteer, payoff in zip(moves_players_volunteer, payoffs):
            if move_volunteer:
                expected_payoff = public_payoff + (volunteer_payoff / number_of_volunteers)
                assert payoff == pytest.approx(expected_payoff)
            else:
                assert payoff == public_payoff
    else:
        for payoff in payoffs:
            assert payoff == non_volunteer_payoff
