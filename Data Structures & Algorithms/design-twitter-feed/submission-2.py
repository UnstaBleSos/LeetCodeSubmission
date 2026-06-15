class Twitter:

    def __init__(self):
        self.globalCounter = 0
        self.userFollowes = {}
        self.userTweets = {}
         
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.globalCounter+=1
        if userId not in self.userTweets:
            self.userTweets[userId]= []
        self.userTweets[userId].append((self.globalCounter,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        maxHeap = []
        
        visibleUser = {userId}
        if userId in self.userFollowes:
            visibleUser.update(self.userFollowes[userId])
        
        for users in visibleUser:
            if users in self.userTweets:
                i = len(self.userTweets[users])-1
                item = self.userTweets[users][i]
                heapq.heappush(maxHeap,(-item[0],item[1],users,i))
                
        while maxHeap and len(result)<10:
            topElem = heapq.heappop(maxHeap)
            tweetId = topElem[1]
            result.append(tweetId)

            user = topElem[2]
            nextuser = topElem[3]-1
            
            if nextuser >= 0:
                tweet = self.userTweets[user][nextuser]
                heapq.heappush(maxHeap,(-tweet[0],tweet[1],user,nextuser))
             
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userFollowes:
            self.userFollowes[followerId] = set()
        self.userFollowes[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userFollowes:
            self.userFollowes[followerId].discard(followeeId)
        
