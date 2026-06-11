def battle_of_the_sexes(
    move_player_fight: bool,
    move_opponent_fight: bool,
    preferred_together_payoff: float = 3,
    unpreferred_together_payoff: float = 2,
    preferred_alone_payoff: float = 0,
) -> tuple[float, float]:
    """
    Return the players' payoff based on the player's and opponent's moves in the Battle of the sexes game. Here, the
    player is considered to prefer the fighting activity, while the opponent prefers ballet.

    This game models a situation where two players have different preferences for two activities but would rather
    attend an activity together than alone. The game captures the tension between individual preferences and the
    desire for mutual cooperation.

    The default values are set to follow the typical payoff structure of the game, commonly referred to as "Battle of
    the Sexes (1)", but they can be adjusted as needed. The condition preferred_together_payoff >
    unpreferred_together_payoff > preferred_alone_payoff should be followed to ensure that both players prefer mutual
    cooperation (attending the event together) over mutual defection while still preferring their respective activities.

    A variation of the game referred to as "Battle of the Sexes (2)" sets a reward of 1 for a player attending their
    preferred activity alone, which can be achieved by setting the preferred_alone_payoff to 1. This variation maintains
    the same strategic dynamics as the original game while also rewarding the player for attending their respective
    preferred activity.

    Below is the payoff matrix:

                                                    Opponent
                                    F                                       B
               +------------------------------------------+------------------------------------------+
            F  | preferred_together, unpreferred_together |    preferred_alone, preferred_alone      |
    Player     +------------------------------------------+------------------------------------------+
            B  |                  0, 0                    | unpreferred_together, preferred_together |
               +------------------------------------------+------------------------------------------+

    Where F is fight (True) and B is ballet (False).

    :param move_player_fight: Player's move (activity), True for fight, False for ballet
    :param move_opponent_fight: Opponent's move (activity), True for fight, False for ballet
    :param preferred_together_payoff: Player's payoff for attending their preferred event together
    :param unpreferred_together_payoff: Player's payoff for attending their unpreferred event together
    :param preferred_alone_payoff: Player's payoff when attending their preferred event alone
    :return: Tuple containing the (player, opponent) payoff as a function of both players' moves (activities)
    """
    if move_player_fight and move_opponent_fight:
        return (preferred_together_payoff, unpreferred_together_payoff)
    elif not move_player_fight and not move_opponent_fight:
        return (unpreferred_together_payoff, preferred_together_payoff)
    elif move_player_fight and not move_opponent_fight:
        return (preferred_alone_payoff, preferred_alone_payoff)
    else:
        return (0, 0)


def chicken(
    move_player_swerve: bool,
    move_opponent_swerve: bool,
    tie_payoff: float = 0,
    win_payoff: float = 1,
    lose_payoff: float = -1,
    crash_payoff: float = -1000,
) -> tuple[float, float]:
    """
    Return the players' payoff based on the player's and opponent's moves in the Chicken game. This game may also be
    formulated to match the Hawk-Dove game or Snowdrift game.

    This game models a situation where two players are driving towards each other on a collision course. Each player
    has two options: to swerve (avoid the collision) or to stay straight (not swerve).

    The default values are set to follow a typical payoff structure of the game, but they can be adjusted as needed.
    The default crash payoff is set to an arbitrarily large negative value to create a catastrophic risk associated
    with crashing. The condition win_payoff > tie_payoff > lose_payoff > crash_payoff should be followed to ensure
    that both players prefer winning over tying, tying over losing, and losing over crashing.

    Below is the payoff matrix:

                                            Opponent
                                Sw                       St
                +------------------------------+-------------------------------+
            Sw  |    tie_payoff, tie_payoff    |    lose_payoff, win_payoff    |
    Player      +------------------------------+-------------------------------+
            St  |    win_payoff, lose_payoff   |    crash_payoff, crash_payoff |
                +------------------------------+-------------------------------+

    Where Sw is swerve (True) and St is straight/don't swerve (False).

    :param move_player_swerve: Player's move, True for swerve, False for don't swerve
    :param move_opponent_swerve: Opponent's move, True for swerve, False for don't swerve
    :param tie_payoff: Payoff for both players if both swerve
    :param win_payoff: Payoff for the player who doesn't swerve when the opponent swerves
    :param lose_payoff: Payoff for the player who swerves when the opponent doesn't swerve
    :param crash_payoff: Payoff for both players if neither swerves
    :return: Tuple containing the (player, opponent) payoff as a function of both players' moves
    """
    if move_player_swerve and move_opponent_swerve:
        return (tie_payoff, tie_payoff)
    elif not move_player_swerve and not move_opponent_swerve:
        return (crash_payoff, crash_payoff)
    elif not move_player_swerve and move_opponent_swerve:
        return (win_payoff, lose_payoff)
    else:
        return (lose_payoff, win_payoff)


def deadlock(
    move_player_cooperate: bool,
    move_opponent_cooperate: bool,
    player_cooperate_cooperate_payoff: float = 1,
    player_defect_defect_payoff: float = 2,
    player_cooperate_defect_payoff: float = 0,
    player_defect_cooperate_payoff: float = 3,
    opponent_cooperate_cooperate_payoff: float = 1,
    opponent_defect_defect_payoff: float = 2,
    opponent_cooperate_defect_payoff: float = 3,
    opponent_defect_cooperate_payoff: float = 0,
) -> tuple[float, float]:
    """
    Return the players' payoff based on the player's and opponent's moves in the Deadlock game.

    This game models a situation where two players can either cooperate or defect. The players make their decisions
    simultaneously without knowing the other's choice. Unlike the Prisoner's Dilemma, both players prefer mutual
    defection over mutual cooperation, so it is always in the best interest of both players to defect, regardless of
    the opponent's move.

    The naming of the payoff parameters is structured such that the first part indicates who obtains the payoff,
    the second part indicates the player's move, and the third part indicates the opponent's move. For example,
    opponent_defect_cooperate_payoff refers to the opponent's payoff when the player defects and the opponent
    cooperates.

    The default values are set to follow a typical payoff structure of the game, but they can be adjusted as needed.
    The condition player_defect_cooperate_payoff > player_defect_defect_payoff > player_cooperate_cooperate_payoff
    > player_cooperate_defect_payoff and opponent_defect_cooperate_payoff > opponent_defect_defect_payoff >
    opponent_cooperate_cooperate_payoff > opponent_cooperate_defect_payoff should be followed to ensure that both
    players prefer defecting against a cooperating opponent over mutual defection, mutual defection over mutual
    cooperation, and mutual cooperation over cooperating against a defecting opponent.

    Below is the payoff matrix:

                                            Opponent
                                C                               D
               +----------------------------------+--------------------------------------+
            C  | player_cooperate_cooperate,      | player_cooperate_defect,             |
               | opponent_cooperate_cooperate     | opponent_cooperate_defect            |
    Player     +----------------------------------+--------------------------------------+
            D  | player_defect_cooperate,         | player_defect_defect,                |
               | opponent_defect_cooperate        | opponent_defect_defect               |
               +----------------------------------+--------------------------------------+

    Where C is cooperate (True) and D is defect (False).

    :param move_player_cooperate: Player's move, True for cooperate, False for defect
    :param move_opponent_cooperate: Opponent's move, True for cooperate, False for defect
    :param player_cooperate_cooperate_payoff: Player's payoff for mutual cooperation
    :param player_defect_defect_payoff: Player's payoff for mutual defection
    :param player_cooperate_defect_payoff: Player's payoff for cooperating against a defecting opponent
    :param player_defect_cooperate_payoff: Player's payoff for defecting against a cooperating opponent
    :param opponent_cooperate_cooperate_payoff: Opponent's payoff for mutual cooperation
    :param opponent_defect_defect_payoff: Opponent's payoff for mutual defection
    :param opponent_cooperate_defect_payoff: Opponent's payoff for defecting against a cooperating opponent
    :param opponent_defect_cooperate_payoff: Opponent's payoff for cooperating against a defecting opponent
    :return: Tuple containing the (player, opponent) payoff as a function of both players' moves
    """
    if move_player_cooperate and move_opponent_cooperate:
        return (player_cooperate_cooperate_payoff, opponent_cooperate_cooperate_payoff)
    elif not move_player_cooperate and not move_opponent_cooperate:
        return (player_defect_defect_payoff, opponent_defect_defect_payoff)
    elif not move_player_cooperate and move_opponent_cooperate:
        return (player_defect_cooperate_payoff, opponent_defect_cooperate_payoff)
    else:
        return (player_cooperate_defect_payoff, opponent_cooperate_defect_payoff)


def hawk_dove(
    move_player_hawk: bool, move_opponent_hawk: bool, resource_payoff: float = 2, cost: float = 4
) -> tuple[float, float]:
    """
    Return the players' payoff based on the player's and opponent's moves in the Hawk-Dove game. Maynard Smith used the
    term "Hawk-Dove" to describe the game in the context of animal conflict where "Hawk" represents an aggressive
    strategy and "Dove" represents a peaceful strategy.

    This game models a situation where two players can either adopt an aggressive strategy (Hawk) or a peaceful strategy
    (Dove) when competing for a shared resource. Two Hawks engage in a conflict where each is assumed to win half the
    time while incurring the cost of the conflict, thus their payoff is (resource_payoff - cost)/2.

    The default values are from Maynard Smith and are set to follow a typical payoff structure of the game, but they
    can be adjusted as needed. The condition resource_payoff > (resource_payoff - cost)/2 > resource_payoff/2 > 0
    should be followed to ensure that both players prefer winning the resource without conflict over sharing it
    peacefully, sharing it peacefully over losing the resource, and losing the resource over engaging in a conflict.
    If the resource_payoff is greater than the cost, then hawk becomes the dominant strategy for both players. If the
    resource_payoff is less than the cost, then there exists a mixed strategy equilibrium.

    Below is the payoff matrix:

                                                Opponent
                                H                            D
                +---------------------------+--------------------+
            H   | (resource_payoff-cost)/2, |  resource_payoff   |
    Player      | (resource_payoff-cost)/2  |  0                 |
                +---------------------------+--------------------+
            D   |   0,                      | resource_payoff/2, |
                |   resource_payoff         | resource_payoff/2  |
                +---------------------------+--------------------+

    Where H is hawk (True) and D is dove (False).

    :param move_player_hawk: Player's move, True for hawk, False for dove
    :param move_opponent_hawk: Opponent's move, True for hawk, False for dove
    :param resource_payoff: Payoff for winning the resource in its entirety
    :param cost: Cost incurred from engaging in a conflict
    :return: Tuple containing the (player, opponent) payoff as a function of both players' moves
    """
    if move_player_hawk and move_opponent_hawk:
        return ((resource_payoff - cost) / 2, (resource_payoff - cost) / 2)
    elif not move_player_hawk and not move_opponent_hawk:
        return (resource_payoff / 2, resource_payoff / 2)
    elif move_player_hawk and not move_opponent_hawk:
        return (resource_payoff, 0)
    else:
        return (0, resource_payoff)


def matching_pennies(move_player_heads: bool, move_opponent_heads: bool) -> tuple[int, int]:
    """
    Return the players' payoff based on the player's and opponent's moves in the Matching Pennies game.

    The game is a zero-sum game where one player's gain is the other player's loss. The player wins when both players
    choose the same side, and the opponent wins when they choose different sides.

    Below is the payoff matrix:

                                    Opponent
                            H                   T
                +----------------------+---------------------+
            H   |       1, -1          |      -1, 1          |
    Player      +----------------------+---------------------+
            T   |      -1, 1           |       1, -1         |
                +----------------------+---------------------+

    Where H is heads (True) and T is tails (False).

    :param move_player_heads: Player's move, True for heads, False for tails
    :param move_opponent_heads: Opponent's move, True for heads, False for tails
    :return: Tuple containing the (player, opponent) payoff as a function of both players' moves
    """
    if move_player_heads and move_opponent_heads:
        return (1, -1)
    elif not move_player_heads and not move_opponent_heads:
        return (1, -1)
    elif move_player_heads and not move_opponent_heads:
        return (-1, 1)
    else:
        return (-1, 1)


def prisoners_dilemma(
    move_player_cooperate: bool,
    move_opponent_cooperate: bool,
    reward_payoff: float = -1,
    punishment_payoff: float = -2,
    temptation_payoff: float = 0,
    sucker_payoff: float = -3,
) -> tuple[float, float]:
    """
    Return the player's payoff based on the player's and opponent's moves in the Prisoner's Dilemma game.

    This game models a situation where two players can either cooperate with each other or defect (betray) each other.
    The players make their decisions simultaneously without knowing the other's choice.

    The default values are set for the classic version of the game, but in general the condition temptation
    > reward > punishment > sucker should be followed to ensure the game behaves as expected. The payoff
    relationship reward_payoff > punishment_payoff ensures that mutual cooperation is more beneficial than mutual
    defection, while temptation_payoff > reward_payoff and punishment_payoff > sucker_payoff ensure that defecting
    against a cooperating opponent is the dominant strategy.

    When an iterative version of the game is played, the condition 2*reward_payoff > temptation_payoff + sucker_payoff
    should also be followed to prevent the strategy of alternating between cooperation and defection giving a greater
    reward than mutual cooperation.

    Below is the payoff matrix:

                                            Opponent
                                C                               D
               +----------------------------------+--------------------------------------+
            C  |   reward_payoff, reward_payoff   |   sucker_payoff, temptation_payoff   |
    Player     +----------------------------------+--------------------------------------+
            D  | temptation_payoff, sucker_payoff | punishment_payoff, punishment_payoff |
               +----------------------------------+--------------------------------------+

    Where C is cooperate (True) and D is defect (False).

    :param move_player_cooperate: Player's move, True for cooperate, False for defect
    :param move_opponent_cooperate: Opponent's move, True for cooperate, False for defect
    :param reward_payoff: Reward payoff for mutual cooperation
    :param punishment_payoff: Punishment payoff for mutual defection
    :param temptation_payoff: Temptation payoff --- reward for defecting against a cooperating opponent
    :param sucker_payoff: Sucker payoff --- reward for cooperating against a defecting opponent
    :return: Tuple containing the (player, opponent) payoff as a function of both players' moves
    """
    if move_player_cooperate and move_opponent_cooperate:
        return (reward_payoff, reward_payoff)
    elif not move_player_cooperate and not move_opponent_cooperate:
        return (punishment_payoff, punishment_payoff)
    elif not move_player_cooperate and move_opponent_cooperate:
        return (temptation_payoff, sucker_payoff)
    else:
        return (sucker_payoff, temptation_payoff)


def stag_hunt(
    move_player_stag: bool,
    move_opponent_stag: bool,
    stag_together_payoff: float = 4,
    hare_alone_payoff: float = 3,
    hare_together_payoff: float = 2,
    stag_alone_payoff: float = 0,
) -> tuple[float, float]:
    """
    Return the players' payoff based on the player's and opponent's moves in the Stag Hunt game.

    This game models a situation where two players can either cooperate to hunt a stag or individually hunt a hare.
    Hunting a stag requires mutual cooperation, while hunting a hare can be done alone.

    The default values are set to follow a typical payoff structure of the game, but they can be adjusted as needed.
    The condition stag_together_payoff > hare_alone_payoff >= hare_together_payoff > stag_alone_payoff should be
    followed to ensure that both players prefer mutual cooperation (hunting stag) over mutual defection (hunting hare)
    while still preferring hunting hare alone over hunting stag alone.

    Below is the payoff matrix:

                                                Opponent
                                S                            H
                +--------------------------------+------------------------------+
            S   |  stag_together, stag_together  |   stag_alone, hare_alone     |
    Player      +--------------------------------+------------------------------+
            H   |    hare_alone, stag_alone      | hare_together, hare_together |
                +---------------------------------+-----------------------------+

    Where S is hunting stag (True) and H is hunting hare (False).

    :param move_player_stag: Player's move, True for stag, False for hare
    :param move_opponent_stag: Opponent's move, True for stag, False for hare
    :param stag_together_payoff: Player's payoff for hunting stag together
    :param hare_alone_payoff: Player's payoff for hunting hare alone
    :param hare_together_payoff: Player's payoff for hunting hare together
    :param stag_alone_payoff: Player's payoff for hunting stag alone
    :return: Tuple containing the (player, opponent) payoff as a function of both players' moves
    """
    if move_player_stag and move_opponent_stag:
        return (stag_together_payoff, stag_together_payoff)
    elif not move_player_stag and not move_opponent_stag:
        return (hare_together_payoff, hare_together_payoff)
    elif move_player_stag and not move_opponent_stag:
        return (stag_alone_payoff, hare_alone_payoff)
    else:
        return (hare_alone_payoff, stag_alone_payoff)


def ultimatum(
    move_player_fair: bool,
    move_opponent_accept: bool,
    fair_payoff: float = 5,
    unfair_player_payoff: float = 8,
    unfair_opponent_payoff: float = 2,
    reject_payoff: float = 0,
) -> tuple[float, float]:
    """
    Return the player's payoff based on the player's and opponent's moves in the Ultimatum game.

    This game models a situation where one player (the proposer) offers a fair or unfair split of a sum of money to
    another player (the responder). The responder can either accept or reject the offer. If the offer is accepted,
    both players receive the proposed split. If the offer is rejected, both players receive nothing.

    The default values are set to follow a typical payoff structure of the game, but they can be adjusted as needed.
    The condition unfair_player_payoff > fair_payoff > reject_payoff and fair_payoff > unfair_opponent_payoff
    > reject_payoff should be followed to ensure that both players prefer fair offers over rejections while still
    preferring unfair offers from the player over fair offers.

    A more general case of this game exists allowing the player to choose the amount to offer the opponent, but is not
    implemented here.

    Below is the payoff matrix:

                                                        Opponent
                                        A                                   R
                +---------------------------------------------+------------------------------+
            F  |          fair_payoff, fair_payoff            | reject_payoff, reject_payoff |
    Player     +----------------------------------------------+------------------------------+
            U  | unfair_player_payoff, unfair_opponent_payoff | reject_payoff, reject_payoff |
               +----------------------------------------------+------------------------------+

    Where F is fair (True), U is unfair (False), A is accept (True), and R is reject (False).

    :param move_player_fair: Player's move, True for fair offer, False for unfair offer
    :param move_opponent_accept: Opponent's move, True for accept, False for reject
    :param fair_payoff: Player's payoff for a fair offer that is accepted
    :param unfair_player_payoff: Player's payoff for an unfair offer that is accepted
    :param unfair_opponent_payoff: Opponent's payoff for an unfair offer that is accepted
    :param reject_payoff: Payoff for both players if the offer is rejected
    :return: Tuple containing the (player, opponent) payoff as a function of both players' moves
    """
    if move_player_fair and move_opponent_accept:
        return (fair_payoff, fair_payoff)
    elif not move_player_fair and move_opponent_accept:
        return (unfair_player_payoff, unfair_opponent_payoff)
    else:
        return (reject_payoff, reject_payoff)


def volunteer_dilemma(
    moves_players_volunteer: tuple[bool, ...],
    volunteer_payoff: float = 0,
    public_payoff: float = 1,
    no_volunteer_payoff: float = -10,
) -> tuple[float, ...]:
    """
    Return the players' payoffs based on the groups' moves in the Volunteer Dilemma game. This is an n-player game.

    This game models a situation where multiple players can choose to volunteer to perform a task that benefits the
    group, where volunteering incurs a personal cost.

    If only two players are involved, the game is equivalent to the Chicken game, where volunteering is analogous to
    swerving and not volunteering is analogous to staying straight.

    The default values are set to follow a typical payoff structure of the game, but they can be adjusted as needed.
    The condition public_payoff > volunteer_payoff > no_volunteer_payoff should be followed to ensure that all players
    prefer at least one player volunteering over no players volunteering, while still preferring not to volunteer if
    another player is volunteering.

    Each player's payoff follows the structure:
        - If at least one player volunteers:
            - Volunteering players receive volunteer_payoff
            - Non-volunteering players receive public_payoff
        - If no players volunteer:
            - All players receive no_volunteer_payoff

    Here, moves_players_volunteer is a tuple of boolean values where each value represents whether a player volunteers
    (True) or not (False).

    :param moves_players_volunteer: Tuple of players' moves, True for volunteer, False for not volunteer
    :param volunteer_payoff: Payoff for players who volunteer (payoff includes cost of volunteering --- benefit - cost)
    :param public_payoff: Payoff for all players if at least one player volunteers
    :param no_volunteer_payoff: Payoff for all players if no players volunteer
    :return: Tuple containing the payoffs for all players as a function of their moves in order of players
    """
    if any(moves_players_volunteer):
        return tuple(
            volunteer_payoff if player_volunteer else public_payoff for player_volunteer in moves_players_volunteer
        )
    else:
        return tuple(no_volunteer_payoff for _ in moves_players_volunteer)


def volunteer_dilemma_quantum(
    moves_players_volunteer: tuple[bool, ...],
    volunteer_payoff: float = -1,
    public_payoff: float = 2,
    no_volunteer_payoff: float = 0,
) -> tuple[float, ...]:
    """
    Return the players' payoffs based on the groups' moves in the Quantum Volunteer Dilemma game. This is an n-player
    game. This variation introduces a quantum aspect to the traditional volunteer dilemma.

    This game models a situation where multiple players can choose to volunteer to perform a task that benefits the
    group. Unlike the base Volunteer Dilemma, the cost of volunteering is shared among the volunteers.

    The default values are from Koh, Kumar, and Goh 2025, and are set to follow a typical payoff structure of the game,
    but they can be adjusted as needed. The condition that public_payoff > (public_payoff - volunteer_payoff) >
    no_volunteer_payoff should be followed to ensure that all players prefer at least one player volunteering over no
    players volunteering, while still preferring not to volunteer if another player is volunteering.

    Each player's payoff follows the structure:
        - If at least one player volunteers:
            - Volunteering players receive public_payoff - (volunteer_payoff / number_of_volunteers)
            - Non-volunteering players receive public_payoff
        - If no players volunteer:
            - All players receive no_volunteer_payoff

    Here, moves_players_volunteer is a tuple of boolean values where each value represents whether a player volunteers
    (True) or not (False).

    :param moves_players_volunteer: Tuple of players' moves, True for volunteer, False for not volunteer
    :param volunteer_payoff: Cost of volunteering to be subtracted from public_payoff and shared among volunteers
    :param public_payoff: Payoff for all players if at least one player volunteers
    :param no_volunteer_payoff: Payoff for all players if no players volunteer
    :return: Tuple containing the payoffs for all players as a function of their moves in order of players
    """
    number_of_volunteers = moves_players_volunteer.count(True)
    if number_of_volunteers > 0:
        return tuple(
            public_payoff + (volunteer_payoff / number_of_volunteers) if player_volunteer else public_payoff
            for player_volunteer in moves_players_volunteer
        )
    else:
        return tuple(no_volunteer_payoff for _ in moves_players_volunteer)
