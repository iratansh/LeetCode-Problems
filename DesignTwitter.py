class Twitter:
    def __init__(self):
        self.count = 0
        self.tweet = defaultdict(list)
        self.follow = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.follow[userId].add(userId)
        for followeeId in self.follow[userId]:
            if followeeId in self.tweet:
                i = len(self.tweet[followeeId]) - 1
                count, tweetId = self.tweet[followeeId][i] 
                minHeap.append([count, tweetId, followeeId, i - 1])
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, i = heapq.heappop(minHeap)
            res.append(tweetId)
            if i >= 0:
                count, tweetId = self.tweet[followeeId][i] 
                heapq.heappush(minHeap, [count, tweetId, followeeId, i - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow[followerId]:
            self.follow[followerId].remove(followeeId)
