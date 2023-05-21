"""
https://leetcode.com/problems/design-twitter/

Design a simplified version of Twitter where users can post tweets,
follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:
    - Twitter()
        * Initializes your twitter object.
    - void postTweet(int userId, int tweetId)
        * Composes a new tweet with ID tweetId by the user userId.
        * Each call to this function will be made with a unique tweetId.
    - List<Integer> getNewsFeed(int userId)
        * Retrieves the 10 most recent tweet IDs in the user's news feed.
        * Each item in the news feed must be posted by users who the user followed or by the user themself.
        * Tweets must be ordered from most recent to least recent.
    - void follow(int followerId, int followeeId):
        * The user with ID followerId started following the user with ID followeeId.
    - void unfollow(int followerId, int followeeId):
        * The user with ID followerId started unfollowing the user with ID followeeId.

Example 1:
    - Input:
        * ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
        * [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
    - Output:
        * [null, null, [5], null, null, [6, 5], null, [5]]
    - Explanation:
        * Twitter twitter = new Twitter();
        * twitter.postTweet(1, 5);
            > User 1 posts a new tweet (id = 5).
        * twitter.getNewsFeed(1);
            > User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
        * twitter.follow(1, 2);
            > User 1 follows user 2.
        * twitter.postTweet(2, 6);
            > User 2 posts a new tweet (id = 6).
        * twitter.getNewsFeed(1);
            > User 1's news feed should return a list with 2 tweet ids -> [6, 5].
            > Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
        * twitter.unfollow(1, 2);
            > User 1 unfollows user 2.
        * twitter.getNewsFeed(1);
            > User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.

Constraints:
    * 1 <= userId, followerId, followeeId <= 500
    * 0 <= tweetId <= 10^4
    * All the tweets have unique IDs.
    * At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
"""

from collections import defaultdict
from typing import List
import heapq


class Twitter:
    """Twitter data structure.

    Attributes:
        count (int): count of tweets
        tweets (defaultdict): dictionary of users to map their tweets
        follows (defaultdict): dictionary of users to map who they follow
    """

    def __init__(self):
        """Initialize Twitter data structure."""
        self.count = 0  # count of tweets

        # Create a dictionary of users to map their tweets
        # Note the dictionary is a list because a user can post multiple tweets
        # Count will represent the number of tweets a user has posted.
        #   - This will help determine the latest tweet.
        self.tweets = defaultdict(list)  # {userId: [(tweetId, count)]}

        # Create a dictionary of users to map who they follow
        # Note the dictionary is a set because a user can only follow another user once
        self.follows = defaultdict(set)  # {userId: [followeeId]}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """Add the tweetId to the userId's list of tweets.
           After adding the tweetId, decrement the count so that the most recent tweet has the highest count.

        Algorithm: Hash MAP
        Time Complexity: O(1)
        Space Complexity: O(1)

        Args:
            userId (int): the user that is posting the tweet
            tweetId (int): the tweet that is being posted
        """
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """Retrieve the 10 most recent tweets in the user's news feed

        Algorithm: Min Heap
        Time Complexity: O(10*logn)
        Space Complexity: O(n)

        Args:
            userId (int): the user that is requesting the news feed
        """

        # Create a list to store the 10 latest tweets
        tweets = []

        # Create a min heap to help determine latest tweets.
        # Note the heap is a list but will be heapified using heapq.heapify().
        minHeap = []

        # Add the user's tweets to the heap.
        # This is noted in the problem description.
        self.follows[userId].add(userId)

        # Iterate through the user's follows
        for follweeId in self.follows[userId]:
            # If the follweeId has tweets, add the latest tweet to the heap
            if follweeId in self.tweets:
                index = len(self.tweets[follweeId]) - 1  # Get the latest tweet index
                count, tweetId = self.tweets[follweeId][index]
                minHeap.append([count, tweetId, follweeId, index - 1])

        # Heapify the min heap to determine the latest tweets
        heapq.heapify(minHeap)

        # Iterate through the min heap and while the number of tweets is less than 10
        while minHeap and len(tweets) < 10:
            # Get the latest tweet and add it to the list of tweets
            count, tweetId, follweeId, index = heapq.heappop(minHeap)
            tweets.append(tweetId)

            # If the follweeId has more tweets, add the latest tweet to the heap
            # Note the index is decremented to get the next latest tweet
            if index >= 0:
                count, tweetId = self.tweets[follweeId][index]
                heapq.heappush(minHeap, [count, tweetId, follweeId, index - 1])

        # Return the latest tweets
        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        """Add the followeeId to the followerId's set of follows

        Algorithm: Hash SET
        Time Complexity: O(1)
        Space Complexity: O(1)

        Args:
            followerId (int): the user that is following
            followeeId (int): the user that is being followed
        """
        self.follows[followeeId].add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """Remove the followeeId from the followerId's set of follows

        Algorithm: Hash SET
        Time Complexity: O(1)
        Space Complexity: O(1)

        Args:
            followerId (int): the user that is following
            followeeId (int): the user that is being followed
        """
        # This is to prevent an error from being thrown if the followerId is not following the followeeId
        if self.followeeId in self.follows[followerId]:
            self.follows[followeeId].remove(followerId)
