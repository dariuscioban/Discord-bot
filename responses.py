"""
This module is responsible with handling the response of the bot when chat commands are used.
"""

__author__ = "dariuscioban@yahoo.com"

import random

DICE_TYPES = {'d4': 4,
              'd6': 6,
              'd8': 8,
              'd10': 10,
              'd12': 12,
              'd20': 20}


def handle_response(message: str) -> str:
    """
    Handle chat message received by bot.

    :param message: Received Message
    :return: Generated response
    """
    msg_args = message.lower().split(' ')

    if len(msg_args) == 1:
        return 'Please specify one of the following dice:' \
               ' d4, d6, d8, d10, d12, d20'

    die = msg_args[1]

    if die not in DICE_TYPES:
        return 'Invalid die. Please use one of the following ' \
               'options: d4, d6, d8, d10, d12, d20'

    return str(roll_die(die))


def roll_die(die: str) -> int:
    """
    Simulate rolling a die with the number of faces corresponding to
    the given die type

    :param die: Die type. Possible values: d4, d6, d8, d10, d12, d20
    :return: Random face of rolled die
    """

    return random.randint(1, DICE_TYPES[die])
