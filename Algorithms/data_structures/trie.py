class TrieNode:
  def __init__(self, char, is_word=False):
    self.char = char
    self.children = {}
    self.is_word = is_word

  def insert(self, s):
    if not s:
      self.is_word = True
      return
    elif s[0] not in self.children:
      self.children[s[0]] = TrieNode(s[0])
    self.children[s[0]].insert(s[1:])

  def find(self, s, find_full_word=False):
    if not s:
      if find_full_word:
        return self.is_word
      else:
        return True
    elif s[0] not in self.children:
      return False
    else:
      return self.children[s[0]].find(s[1:], find_full_word)

class Trie:
  def __init__(self, words=None):
    self.root = TrieNode('')
    if words:
      for word in words:
        self.insert(word)

  def insert(self, word):
    self.root.insert(word)

  def find(self, word, find_full_word=False):
    return self.root.find(word, find_full_word)

  def __contains__(self, item):
    if type(item) is str:
      return self.find(item)
    return False
