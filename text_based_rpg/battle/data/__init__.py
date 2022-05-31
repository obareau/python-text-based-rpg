"""
This module is an interface to the package's data.json file.
"""

import os
import json

DATA = json.load(
    open(
        os.path.dirname(
            os.path.realpath(__file__)
        ) + "/data.json"
    )
)
"""dict: The parsed data.json file."""

def _make_messages():
    """
    Create a dictionary of the message templates, prefixed for both the play and
    the enemy.

    Returns
    -------
    dict
        The created dictionary.

    """
    messages = {}

    for entity_name, entity_prefix in DATA["prefixes"].items():
        entity_messages = {
            message_name: f"{entity_prefix} {message}"
            for message_name, message in DATA["templates"].items()
        }


        messages[entity_name] = entity_messages

    return messages

DATA["messages"] = _make_messages()
