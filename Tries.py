
#  Suppose we have a list of words, we want to store them.
# Dictionary provides O(1) time for searching and inserting, but it takes a lot of space.
# Trie is a space efficient method which takes O(n) time for insertion and search.


class TrieNode:
	def __init__(self, letter='*'):
		self.val = letter
		self.children = {}
		self.completeString = False
		return



class Trie:

	def __init__(self):
		self.root = TrieNode()
		return


	def insert(self, word):
		node  = self.root

		for c in word:
			if c in node.children:
				node = node.children[c]
			else:
				newnode = TrieNode(c)
				node.children[c] = newnode
				node = newnode

		node.completeString = True
		return


	def search(self, word):
		node = self.root

		for c in word:
			if c in node.children:
				node = node.children[c]
			else:
				return False

		if node.completeString:
			return True
		return False



	def remove(self, word):    #We can write better remove by actually removing suffix

		node = self.root

		for c in word:
			node = node.children[c]

		node.completeString = False
		return




words = ['string', 'stringify', 'stress', 'strung', 'step']


trie = Trie()

for w in words:
	trie.insert(w)


print(trie.search('stringify'))
trie.insert('hello')
print(trie.search('hello'))