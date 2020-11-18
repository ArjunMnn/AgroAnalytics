class Solution:
	def power(self, A):
	    n = int(A)
	    if n==1:
	        return 0
	    def Log2(x):
            if x == 0:
                return false;
         
            return (math.log10(x)/math.log10(2));
        return 1 if (math.ceil(Log2(n))==math.floor(Log2(n))) else 0