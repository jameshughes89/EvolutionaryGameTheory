import pytest

from evogt.games import (
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

FIGHT = True
BALLET = False
SWERVE = True
DONT_SWERVE = False
COOPERATE = True
DEFECT = False
HAWK = True
DOVE = False
HEADS = True
TAILS = False
STAG = True
HARE = False
FAIR = ACCEPT = True
UNFAIR = REJECT = False
VOLUNTEER = True
DONT_VOLUNTEER = False


@pytest.mark.parametrize(
    "move_player_fight, move_opponent_fight, expected",
    [
        (FIGHT, FIGHT, (3, 2)),
        (FIGHT, BALLET, (0, 0)),
        (BALLET, FIGHT, (0, 0)),
        (BALLET, BALLET, (2, 3)),
    ],
)
def test_battle_of_the_sexes_default_parameters_returns_expected(move_player_fight, move_opponent_fight, expected):
    payoff = battle_of_the_sexes(move_player_fight, move_opponent_fight)
    assert payoff == expected


@pytest.mark.parametrize(
    "move_player_fight, move_opponent_fight, fight_payoff, ballet_payoff, mismatch_payoff, expected",
    [
        (FIGHT, FIGHT, 5, 3, 1, (5, 3)),
        (FIGHT, BALLET, 5, 3, 1, (1, 1)),
        (BALLET, FIGHT, 5, 3, 1, (0, 0)),
        (BALLET, BALLET, 5, 3, 1, (3, 5)),
    ],
)
def test_battle_of_the_sexes_custom_parameters_returns_expected(
    move_player_fight,
    move_opponent_fight,
    fight_payoff,
    ballet_payoff,
    mismatch_payoff,
    expected,
):
    payoff = battle_of_the_sexes(move_player_fight, move_opponent_fight, fight_payoff, ballet_payoff, mismatch_payoff)
    assert payoff == expected


@pytest.mark.parametrize(
    "move_player_swerve, move_opponent_swerve, expected",
    [
        (SWERVE, SWERVE, (0, 0)),
        (SWERVE, DONT_SWERVE, (-1, 1)),
        (DONT_SWERVE, SWERVE, (1, -1)),
        (DONT_SWERVE, DONT_SWERVE, (-1000, -1000)),
    ],
)
def test_chicken_default_parameters_returns_expected(move_player_swerve, move_opponent_swerve, expected):
    payoff = chicken(move_player_swerve, move_opponent_swerve)
    assert payoff == expected


@pytest.mark.parametrize(
    "move_player_swerve, move_opponent_swerve, tie_payoff, win_payoff, lose_payoff, crash_payoff, expected",
    [
        (SWERVE, SWERVE, 1, 2, 3, 4, (1, 1)),
        (SWERVE, DONT_SWERVE, 1, 2, 3, 4, (3, 2)),
        (DONT_SWERVE, SWERVE, 1, 2, 3, 4, (2, 3)),
        (DONT_SWERVE, DONT_SWERVE, 1, 2, 3, 4, (4, 4)),
    ],
)
def test_chicken_custom_parameters_returns_expected(
    move_player_swerve,
    move_opponent_swerve,
    tie_payoff,
    win_payoff,
    lose_payoff,
    crash_payoff,
    expected,
):
    payoff = chicken(move_player_swerve, move_opponent_swerve, tie_payoff, win_payoff, lose_payoff, crash_payoff)
    assert payoff == expected


@pytest.mark.parametrize(
    "move_player_cooperate, move_opponent_cooperate, expected",
    [
        (COOPERATE, COOPERATE, (1, 1)),
        (COOPERATE, DEFECT, (0, 3)),
        (DEFECT, COOPERATE, (3, 0)),
        (DEFECT, DEFECT, (2, 2)),
    ],
)
def test_deadlock_default_parameters_returns_expected(move_player_cooperate, move_opponent_cooperate, expected):
    payoff = deadlock(move_player_cooperate, move_opponent_cooperate)
    assert payoff == expected


@pytest.mark.parametrize(
    "move_player_cooperate, "
    "move_opponent_cooperate, "
    "player_cooperate_cooperate_payoff, "
    "player_defect_defect_payoff, "
    "player_defect_cooperate_payoff, "
    "player_cooperate_defect_payoff, "
    "opponent_cooperate_cooperate_payoff, "
    "opponent_defect_defect_payoff, "
    "opponent_cooperate_defect_payoff, "
    "opponent_defect_cooperate_payoff, "
    "expected",
    [
        (COOPERATE, COOPERATE, 1, 2, 3, 4, 5, 6, 7, 8, (1, 5)),
        (COOPERATE, DEFECT, 1, 2, 3, 4, 5, 6, 7, 8, (3, 7)),
        (DEFECT, COOPERATE, 1, 2, 3, 4, 5, 6, 7, 8, (4, 8)),
        (DEFECT, DEFECT, 1, 2, 3, 4, 5, 6, 7, 8, (2, 6)),
    ],
)
def test_deadlock_custom_parameters_returns_expected(
    move_player_cooperate,
    move_opponent_cooperate,
    player_cooperate_cooperate_payoff,
    player_defect_defect_payoff,
    player_defect_cooperate_payoff,
    player_cooperate_defect_payoff,
    opponent_cooperate_cooperate_payoff,
    opponent_defect_defect_payoff,
    opponent_cooperate_defect_payoff,
    opponent_defect_cooperate_payoff,
    expected,
):
    payoff = deadlock(
        move_player_cooperate,
        move_opponent_cooperate,
        player_cooperate_cooperate_payoff,
        player_defect_defect_payoff,
        player_defect_cooperate_payoff,
        player_cooperate_defect_payoff,
        opponent_cooperate_cooperate_payoff,
        opponent_defect_defect_payoff,
        opponent_cooperate_defect_payoff,
        opponent_defect_cooperate_payoff,
    )
    assert payoff == expected


@pytest.mark.parametrize(
    "move_played_hawk, move_opponent_hawk, expected",
    [
        (HAWK, HAWK, (-1, -1)),
        (HAWK, DOVE, (2, 0)),
        (DOVE, HAWK, (0, 2)),
        (DOVE, DOVE, (1, 1)),
    ],
)
def test_hawk_dove_default_parameters_returns_expected(move_played_hawk, move_opponent_hawk, expected):
    payoff = hawk_dove(move_played_hawk, move_opponent_hawk)
    assert payoff == expected


@pytest.mark.parametrize(
    "move_played_hawk, " "move_opponent_hawk, " "resource_payoff, " "cost, " "expected",
    [
        (HAWK, HAWK, 6, 10, (-2, -2)),
        (HAWK, DOVE, 6, 10, (6, 0)),
        (DOVE, HAWK, 6, 10, (0, 6)),
        (DOVE, DOVE, 6, 10, (3, 3)),
    ],
)
def test_hawk_dove_custom_parameters_returns_expected(
    move_played_hawk, move_opponent_hawk, resource_payoff, cost, expected
):
    payoff = hawk_dove(move_played_hawk, move_opponent_hawk, resource_payoff, cost)
    assert payoff == expected


@pytest.mark.parametrize(
    "move_player_heads, move_opponent_heads, expected",
    [
        (HEADS, HEADS, (1, -1)),
        (HEADS, TAILS, (-1, 1)),
        (TAILS, HEADS, (-1, 1)),
        (TAILS, TAILS, (1, -1)),
    ],
)
def test_matching_pennies_default_parameters_returns_expected(move_player_heads, move_opponent_heads, expected):
    payoff = matching_pennies(move_player_heads, move_opponent_heads)
    assert payoff == expected


@pytest.mark.parametrize(
    "move_player_cooperate, move_opponent_cooperate, expected",
    [
        (COOPERATE, COOPERATE, (-1, -1)),
        (COOPERATE, DEFECT, (-3, 0)),
        (DEFECT, COOPERATE, (0, -3)),
        (DEFECT, DEFECT, (-2, -2)),
    ],
)
def test_prisoners_dilemma_default_parameters_returns_expected(
    move_player_cooperate, move_opponent_cooperate, expected
):
    payoff = prisoners_dilemma(move_player_cooperate, move_opponent_cooperate)
    assert payoff == expected


@pytest.mark.parametrize(
    "move_player_cooperate, "
    "move_opponent_cooperate, "
    "reward_payoff, "
    "punishment_payoff, "
    "temptation_payoff, "
    "sucker_payoff, "
    "expected",
    [
        (COOPERATE, COOPERATE, 3, 0, 5, -1, (3, 3)),
        (COOPERATE, DEFECT, 3, 0, 5, -1, (-1, 5)),
        (DEFECT, COOPERATE, 3, 0, 5, -1, (5, -1)),
        (DEFECT, DEFECT, 3, 0, 5, -1, (0, 0)),
    ],
)
def test_prisoners_dilemma_custom_parameters_returns_expected(
    move_player_cooperate,
    move_opponent_cooperate,
    reward_payoff,
    punishment_payoff,
    temptation_payoff,
    sucker_payoff,
    expected,
):
    payoff = prisoners_dilemma(
        move_player_cooperate,
        move_opponent_cooperate,
        reward_payoff,
        punishment_payoff,
        temptation_payoff,
        sucker_payoff,
    )
    assert payoff == expected


@pytest.mark.parametrize(
    "move_player_stag, move_opponent_stag, expected",
    [
        (STAG, STAG, (4, 4)),
        (STAG, HARE, (0, 3)),
        (HARE, STAG, (3, 0)),
        (HARE, HARE, (2, 2)),
    ],
)
def test_stag_hunt_default_parameters_returns_expected(move_player_stag, move_opponent_stag, expected):
    payoff = stag_hunt(move_player_stag, move_opponent_stag)
    assert payoff == expected


@pytest.mark.parametrize(
    "move_player_stag, "
    "move_opponent_stag, "
    "stag_together_payoff, "
    "hare_alone_payoff, "
    "hare_together_payoff, "
    "stag_alone_payoff, "
    "expected",
    [
        (STAG, STAG, 6, 4, 2, 0, (6, 6)),
        (STAG, HARE, 6, 4, 2, 0, (0, 4)),
        (HARE, STAG, 6, 4, 2, 0, (4, 0)),
        (HARE, HARE, 6, 4, 2, 0, (2, 2)),
    ],
)
def test_stag_hunt_custom_parameters_returns_expected(
    move_player_stag,
    move_opponent_stag,
    stag_together_payoff,
    hare_alone_payoff,
    hare_together_payoff,
    stag_alone_payoff,
    expected,
):
    payoff = stag_hunt(
        move_player_stag,
        move_opponent_stag,
        stag_together_payoff,
        hare_alone_payoff,
        hare_together_payoff,
        stag_alone_payoff,
    )
    assert payoff == expected


@pytest.mark.parametrize(
    "move_player_fair, move_opponent_accept, expected",
    [
        (FAIR, ACCEPT, (5, 5)),
        (FAIR, REJECT, (0, 0)),
        (UNFAIR, ACCEPT, (8, 2)),
        (UNFAIR, REJECT, (0, 0)),
    ],
)
def test_ultimatum_default_parameters_returns_expected(move_player_fair, move_opponent_accept, expected):
    payoff = ultimatum(move_player_fair, move_opponent_accept)
    assert payoff == expected


@pytest.mark.parametrize(
    "move_player_fair, move_opponent_accept, fair_payoff, unfair_player_payoff, unfair_opponent_payoff, expected",
    [
        (FAIR, ACCEPT, 10, 15, 5, (10, 10)),
        (FAIR, REJECT, 10, 15, 5, (0, 0)),
        (UNFAIR, ACCEPT, 10, 15, 5, (15, 5)),
        (UNFAIR, REJECT, 10, 15, 5, (0, 0)),
    ],
)
def test_ultimatum_custom_parameters_returns_expected(
    move_player_fair,
    move_opponent_accept,
    fair_payoff,
    unfair_player_payoff,
    unfair_opponent_payoff,
    expected,
):
    payoff = ultimatum(
        move_player_fair, move_opponent_accept, fair_payoff, unfair_player_payoff, unfair_opponent_payoff
    )
    assert payoff == expected


@pytest.mark.parametrize(
    "moves_players_volunteer, expected",
    [
        ((VOLUNTEER, VOLUNTEER), (0, 0)),
        ((VOLUNTEER, DONT_VOLUNTEER), (0, 1)),
        ((DONT_VOLUNTEER, VOLUNTEER), (1, 0)),
        ((DONT_VOLUNTEER, DONT_VOLUNTEER), (-10, -10)),
        ((VOLUNTEER, VOLUNTEER, DONT_VOLUNTEER), (0, 0, 1)),
        ((VOLUNTEER, DONT_VOLUNTEER, DONT_VOLUNTEER), (0, 1, 1)),
        ((DONT_VOLUNTEER, VOLUNTEER, DONT_VOLUNTEER), (1, 0, 1)),
        ((DONT_VOLUNTEER, DONT_VOLUNTEER, VOLUNTEER), (1, 1, 0)),
        ((DONT_VOLUNTEER, DONT_VOLUNTEER, DONT_VOLUNTEER), (-10, -10, -10)),
        ((VOLUNTEER, VOLUNTEER, VOLUNTEER), (0, 0, 0)),
    ],
)
def test_volunteer_dilemma_default_parameters_returns_expected(moves_players_volunteer, expected):
    payoff = volunteer_dilemma(moves_players_volunteer)
    assert payoff == expected


@pytest.mark.parametrize(
    "moves_players_volunteer, volunteer_payoff, public_payoff, no_volunteer_payoff, expected",
    [
        ((VOLUNTEER, VOLUNTEER), 1, 2, 3, (1, 1)),
        ((VOLUNTEER, DONT_VOLUNTEER), 1, 2, 3, (1, 2)),
        ((DONT_VOLUNTEER, VOLUNTEER), 1, 2, 3, (2, 1)),
        ((DONT_VOLUNTEER, DONT_VOLUNTEER), 1, 2, 3, (3, 3)),
        ((VOLUNTEER, VOLUNTEER, DONT_VOLUNTEER), 1, 2, 3, (1, 1, 2)),
        ((VOLUNTEER, DONT_VOLUNTEER, DONT_VOLUNTEER), 1, 2, 3, (1, 2, 2)),
        ((DONT_VOLUNTEER, VOLUNTEER, DONT_VOLUNTEER), 1, 2, 3, (2, 1, 2)),
        ((DONT_VOLUNTEER, DONT_VOLUNTEER, VOLUNTEER), 1, 2, 3, (2, 2, 1)),
        ((DONT_VOLUNTEER, DONT_VOLUNTEER, DONT_VOLUNTEER), 1, 2, 3, (3, 3, 3)),
        ((VOLUNTEER, VOLUNTEER, VOLUNTEER), 1, 2, 3, (1, 1, 1)),
    ],
)
def test_volunteer_dilemma_custom_parameters_returns_expected(
    moves_players_volunteer, volunteer_payoff, public_payoff, no_volunteer_payoff, expected
):
    payoff = volunteer_dilemma(moves_players_volunteer, volunteer_payoff, public_payoff, no_volunteer_payoff)
    assert payoff == expected


@pytest.mark.parametrize(
    "moves_players_volunteer, expected",
    [
        ((VOLUNTEER, VOLUNTEER), (1.5, 1.5)),
        ((VOLUNTEER, DONT_VOLUNTEER), (1, 2)),
        ((DONT_VOLUNTEER, VOLUNTEER), (2, 1)),
        ((DONT_VOLUNTEER, DONT_VOLUNTEER), (0, 0)),
        ((VOLUNTEER, VOLUNTEER, DONT_VOLUNTEER), (1.5, 1.5, 2)),
        ((VOLUNTEER, DONT_VOLUNTEER, DONT_VOLUNTEER), (1, 2, 2)),
        ((DONT_VOLUNTEER, VOLUNTEER, DONT_VOLUNTEER), (2, 1, 2)),
        ((DONT_VOLUNTEER, DONT_VOLUNTEER, VOLUNTEER), (2, 2, 1)),
        ((DONT_VOLUNTEER, DONT_VOLUNTEER, DONT_VOLUNTEER), (0, 0, 0)),
        ((VOLUNTEER, VOLUNTEER, VOLUNTEER), (1.666667, 1.666667, 1.666667)),
    ],
)
def test_volunteer_dilemma_quantum_default_parameters_returns_expected(moves_players_volunteer, expected):
    payoff = volunteer_dilemma_quantum(moves_players_volunteer)
    assert payoff == pytest.approx(expected)


@pytest.mark.parametrize(
    "moves_players_volunteer, volunteer_payoff, public_payoff, no_volunteer_payoff, expected",
    [
        ((VOLUNTEER, VOLUNTEER), 3, 4, 9, (5.5, 5.5)),
        ((VOLUNTEER, DONT_VOLUNTEER), 3, 4, 9, (7, 4)),
        ((DONT_VOLUNTEER, VOLUNTEER), 3, 4, 9, (4, 7)),
        ((DONT_VOLUNTEER, DONT_VOLUNTEER), 3, 4, 9, (9, 9)),
        ((VOLUNTEER, VOLUNTEER, DONT_VOLUNTEER), 3, 4, 9, (5.5, 5.5, 4)),
        ((VOLUNTEER, DONT_VOLUNTEER, DONT_VOLUNTEER), 3, 4, 9, (7, 4, 4)),
        ((DONT_VOLUNTEER, VOLUNTEER, DONT_VOLUNTEER), 3, 4, 9, (4, 7, 4)),
        ((DONT_VOLUNTEER, DONT_VOLUNTEER, VOLUNTEER), 3, 4, 9, (4, 4, 7)),
        ((DONT_VOLUNTEER, DONT_VOLUNTEER, DONT_VOLUNTEER), 3, 4, 9, (9, 9, 9)),
        ((VOLUNTEER, VOLUNTEER, VOLUNTEER), 3, 4, 9, (5, 5, 5)),
    ],
)
def test_volunteer_dilemma_quantum_custom_parameters_returns_expected(
    moves_players_volunteer, volunteer_payoff, public_payoff, no_volunteer_payoff, expected
):
    payoff = volunteer_dilemma_quantum(moves_players_volunteer, volunteer_payoff, public_payoff, no_volunteer_payoff)
    assert payoff == expected
