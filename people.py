import copy
class Solution(object):

    def valid(self, curr, people):
        cnt = 0
        for p in curr:
            if p[0] >= people[0]:
                cnt += 1
        return cnt == people[1]

    def helper(self, dict, curr):

        print 'helper', curr, dict
        curr_len = len(curr)
        if not dict:
            return True

        for k in dict:
            if k > curr_len:
                print ('skip', k, dict)
                continue

            for people in dict[k]:
                if self.valid(curr, people):
                    curr_copy = copy.deepcopy(curr)
                    dict_copy = copy.deepcopy(dict)
                    dict_copy[k].remove(people)
                    if not dict_copy[k]:
                        del dict_copy[k]
                    curr_copy.append(people)
                    ret = self.helper(dict_copy, curr_copy)
                    if ret:
                        print ('we are good', curr)
                        return ret
        return False

    def reconstructQueue(self, people):

        # key is k
        dict = {}
        for person in people:
            k = person[1]
            if not k in dict:
                dict[k] = []
            dict[k].append(person)
        print dict

        return self.helper(dict, [])

a = Solution()
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
a.reconstructQueue(people)
