class Solution(object):
	def reverseWords(self, s):
		"""
		:type s: str
		:rtype: str
		"""
	
		tmp = s.split(' ')
		
		while '' in tmp:
			tmp.remove('')
		tmp.reverse()
		tmp = ' '.join(tmp)
		return(tmp)

a = Solution()
s1 = "the sky is blue"
s2 = "reverse words in a string"
print a.reverseWords(s1)
print a.reverseWords(s2)
