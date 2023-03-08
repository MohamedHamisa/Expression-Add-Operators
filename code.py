from collections import defaultdict

class Solution:
    def addOperators(self, num, target):

        def getNext(location, first, second, valid, string):
            if location is len(num)-1:
                return [string] if first+second == target else []
            integer, char = int(num[location+1]), num[location+1]
            track = getNext(location+1, first+second, integer, integer, string+"+"+char)+
            getNext(location+1, first+second, -integer, -integer, string+"-"+char)+
            getNext(location+1, first, second*integer, integer, string+"*"+char)
            if valid != 0:
                time, merge = second//valid, valid*10+integer if valid > 0 else valid*10-integer
                track += getNext(location+1, first, time * merge, merge, string+char)
            return track
        return getNext(0, 0, int(num[0]), int(num[0]), num[0])
