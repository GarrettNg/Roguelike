import tcod as libtcod

import textwrap


class Message:
    def __init__(self, text, color=libtcod.white):
        self.text = text
        self.color = color


class MessageLog:
    def __init__(self, x, width, height):
        self.messages = []
        self.x = x
        self.width = width
        self.height = height

    def add_message(self, message):
        # Split message lines if too long
        new_msg_lines = textwrap.wrap(message.text, self.width)

        for line in new_msg_lines:
            # Remove first line if buffer is full
            if len(self.messages) == self.height:
                del self.messages[0]

            self.messages.append(Message(line, message.color))