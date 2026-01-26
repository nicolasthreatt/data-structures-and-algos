/*
Design Twitter
https://leetcode.com/problems/design-twitter/

Design a simplified version of Twitter where users can:
    - Post tweets
    - Follow/unfollow another user
    - Able to see the 10 most recent tweets in the user's news feed.

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
        * [
            "Twitter", "postTweet", "getNewsFeed", "follow",
            "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"
          ]
        * [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
    - Output:
        * [null, null, [5], null, null, [6, 5], null, [5]]
    - Explanation:
        * Twitter twitter = new Twitter();
        * twitter.postTweet(1, 5);
            + User 1 posts a new tweet (id = 5).
        * twitter.getNewsFeed(1);
            + User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
        * twitter.follow(1, 2);
            + User 1 follows user 2.
        * twitter.postTweet(2, 6);
            + User 2 posts a new tweet (id = 6).
        * twitter.getNewsFeed(1);
            + User 1's news feed should return a list with 2 tweet ids -> [6, 5].
            + Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
        * twitter.unfollow(1, 2);
            > User 1 unfollows user 2.
        * twitter.getNewsFeed(1);
            + User 1's news feed should return a list with 1 tweet id -> [5],
              since user 1 is no longer following user 2.

Constraints:
    * 1 <= userId, followerId, followeeId <= 500
    * 0 <= tweetId <= 10^4
    * All the tweets have unique IDs.
    * At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
*/
package design;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Set;

class Twitter {
    private static final int MAX_TWEETS_PER_FEED = 10;

    static class HeapEntry {
        final int time, tweetId, userId, index;
        HeapEntry(int time, int tweetId, int userId, int index) {
            this.time = time; this.tweetId = tweetId; this.userId = userId; this.index = index;
        }
    };

    static class Tweet {
        final int time, id;
        Tweet(int time, int id) { this.time = time; this.id = id; }
    };

    private int posts = 0;
    private final Map<Integer, List<Tweet>> tweets = new HashMap<>();      // {userId: timeline[]}
    private final Map<Integer, Set<Integer>> followees = new HashMap<>();  // {followerId: followeeIds[]}

    public Twitter() {}

    public void postTweet(int userId, int tweetId) {
        tweets.computeIfAbsent(userId, k -> new ArrayList<>()).add(new Tweet(++posts, tweetId));
    }

    public List<Integer> getNewsFeed(int userId) {
        List<Integer> feed = new ArrayList<>(MAX_TWEETS_PER_FEED);

        // Create MAX heap to keep track of the latest MAX_TWEETS_PER_FEED for each user's feed
        PriorityQueue<HeapEntry> maxHeap =
            new PriorityQueue<>((a, b) -> Integer.compare(b.time, a.time));

        // Add User tweets to Heap
        // Users should see OWN tweets
        addTweets(userId, maxHeap);

        // Add FOLLOWEES tweets to Heap
        // Users should see FOLLOWEES tweets
        Set<Integer> users = followees.get(userId);
        if (users != null) {
            for (int followerId : users) {
                addTweets(followerId, maxHeap);
            }
        }

        // Add tweets from heap to the user's feed
        // Heap will now contain the at most the latest MAX_TWEETS_PER_FEED based on their post times
        while (!maxHeap.isEmpty() && feed.size() < MAX_TWEETS_PER_FEED) {
            HeapEntry latest = maxHeap.poll();
            feed.add(latest.tweetId);

            if (latest.index >= 0) {
                List<Tweet> timeline = tweets.get(latest.userId);
                Tweet tweet = timeline.get(latest.index);

                maxHeap.offer(new HeapEntry(tweet.time, tweet.id, latest.userId, latest.index - 1));
            }
        }

        return feed;
    }

    public void follow(int followerId, int followeeId) {
        if (followerId == followeeId) return;

        followees.computeIfAbsent(followerId, k -> new HashSet<>()).add(followeeId);
    }
    
    public void unfollow(int followerId, int followeeId) {
        if (followerId == followeeId) return;

        Set<Integer> followers = followees.get(followerId);
        if (followers != null) {
            followers.remove(followeeId);
        }
    }

    private void addTweets(int userId, PriorityQueue<HeapEntry> heap) {
        List<Tweet> timeline = tweets.get(userId);
        if (timeline == null || timeline.isEmpty()) return;

        int idx = timeline.size() - 1;
        Tweet t = timeline.get(idx);
        heap.offer(new HeapEntry(t.time, t.id, userId, idx - 1));
    }

}
