import random


def always_cooperate(history_self: list[bool], history_opponent: list[bool]) -> bool:
    """
    Always cooperate, regardless of any past moves

    Move histories have no effect on this strategy.

    :param history_self: List of all the player's past moves in the series
    :param history_opponent: List of all the opponent's past moves in the series
    :return: Always True (cooperate)
    """
    return True


def always_defect(history_self: list[bool], history_opponent: list[bool]) -> bool:
    """
    Always defect, regardless of any past moves

    Move histories have no effect on this strategy.

    :param history_self: List of all the player's past moves in the series
    :param history_opponent: List of all the opponent's past moves in the series
    :return: Always False (defect)
    """
    return False


def grimm_trigger(history_self: list[bool], history_opponent: list[bool]) -> bool:
    """
    Cooperate until the opponent defects once, then always defect

    :param history_self: List of all the player's past moves in the series
    :param history_opponent: List of all the opponent's past moves in the series
    :return: True for cooperate, False for defect
    """
    if not history_opponent:
        return True
    if False in history_opponent:
        return False
    else:
        return True


def random_move(history_self: list[bool], history_opponent: list[bool]) -> bool:
    """
    Randomly cooperate or defect with equal probability.

    Move histories have no effect on this strategy.

    :param history_self: List of all the player's past moves in the series
    :param history_opponent: List of all the opponent's past moves in the series
    :return: True for cooperate, False for defect
    """
    return random.choice([True, False])


def tit_for_tat(history_self: list[bool], history_opponent: list[bool]) -> bool:
    """
    Cooperate unless the opponent's previous move was a defect, in which case the player defects

    :param history_self: List of all the player's past moves in the series
    :param history_opponent: List of all the opponent's past moves in the series
    :return: True for cooperate, False for defect
    """
    if not history_opponent:
        return True
    if history_opponent[-1] is False:
        return False
    else:
        return True


def tit_for_two_tats(history_self: list[bool], history_opponent: list[bool]) -> bool:
    """
    Cooperate unless the opponent's last two moves were defects, in which case the player defects

    :param history_self: List of all the player's past moves in the series
    :param history_opponent: List of all the opponent's past moves in the series
    :return: True for cooperate, False for defect
    """
    if len(history_opponent) < 2:
        return True
    if history_opponent[-1] is False and history_opponent[-2] is False:
        return False
    else:
        return True
