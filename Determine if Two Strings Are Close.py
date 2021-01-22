#Determine if Two Strings Are Close

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        w1 = Counter(word1)
        w2 = Counter(word2)

        letters1 = [x for x in w1.keys()]
        letters2 = [x for x in w2.keys()]

        freq1 = [x for x in w1.values()]
        freq2 = [x for x in w2.values()]

        return sorted(letters1) == sorted(letters2) and sorted(freq1) == sorted(freq2)