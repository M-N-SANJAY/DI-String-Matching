'''
Algorithm :-
  We loop through the string s.
  If we get s[i] == 'I'.
    we put left to the array perm.
    we increase the value of left by one.
  If we get s[i] == D.
    we put right to the array perm.
    we decrease the value of right by 1.
  at last, we need to append one more element.
  The missing element, which is stored in both left and right pointers , so we can append the left/right pointer value to the list.
'''
def diStringMatch(self, s):
    left = 0
    right = len(s)
    ans = []
    for i in s:
        if i == "I":
            ans.append(left)
            left += 1
        else:
            ans.append(right)
            right -= 1
    ans.append(left)
    return ans
