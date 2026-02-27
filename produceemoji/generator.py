import random

from .emojis import EMOJI_LIST

class RandomEmoji:
  @staticmethod
  def oneEmoji():
    return random.choice(EMOJI_LIST)
  
