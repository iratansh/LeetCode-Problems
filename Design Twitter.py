class Twitter:
    def __init__(self):
        self.time = 0 
        self.tweets = defaultdict(list)  
        self.follows = defaultdict(set)  

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1  

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
  
        if userId in self.tweets:
            for tweet in self.tweets[userId][-10:]: 
                heapq.heappush(heap, tweet)

        for followee in self.follows[userId]:
            if followee in self.tweets:
                for tweet in self.tweets[followee][-10:]:
                    heapq.heappush(heap, tweet)

        return [heapq.heappop(heap)[1] for _ in range(min(10, len(heap)))]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
