import random

from .emojis import EMOJI_LIST

class RandomEmoji:
  @staticmethod
  def oneEmoji():
    return random.choice(EMOJI_LIST)
  
  @staticmethod
  def many(n = 3):
    return [random.choice(EMOJI_LIST for _ in range(n))]
  
  @staticmethod
  def string(n = 5, separator = " "):
    return separator.join(RandomEmoji.many(n))
