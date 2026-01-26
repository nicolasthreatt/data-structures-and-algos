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

#include <cassert>
#include <queue>
#include <set>
#include <vector>
#include <unordered_map>
#include <unordered_set>

class Twitter {
private:
    static constexpr int kMaxFeed = 10;

    struct HeapEntry {
        int time;
        int tweetId;
        int userId;
        int index;
        HeapEntry(int time, int tweetId, int userId, int index)
            : time(time), tweetId(tweetId), userId(userId), index(index) {}
    };

    struct HeapEntryCmp {
        bool operator()(const HeapEntry& a, const HeapEntry& b) const {
            return a.time < b.time;  // b should come before a
        }
    };

    struct Tweet {
        int time;
        int id;
        Tweet(int t, int i) : time(t), id(i) {}
    };

    int posts = 0;
    std::unordered_map<int, std::vector<Tweet>> tweets;          // {userId: timeline[]}
    std::unordered_map<int, std::unordered_set<int>> followees;  // {followerId: followeeIds[]}

    void addTweets(
        int userId,
        std::priority_queue<HeapEntry, std::vector<HeapEntry>, HeapEntryCmp>& maxHeap
    ) {
        auto it = tweets.find(userId);
        if (it == tweets.end()) return;

        const auto& timeline = it->second;
        if (timeline.empty()) return;

        int idx = static_cast<int>(timeline.size()) - 1;
        const Tweet& tweet = timeline.at(idx);

        maxHeap.emplace(tweet.time, tweet.id, userId, idx - 1);
    }

public:
    Twitter() {}

    void postTweet(int userId, int tweetId) {
        tweets[userId].emplace_back(++posts, tweetId);
    }

    std::vector<int> getNewsFeed(int userId) {
        std::vector<int> feed;  // vector<tweetId>
        std::priority_queue<HeapEntry, std::vector<HeapEntry>, HeapEntryCmp> maxHeap;

        // Add User tweets to Heap
        // Users should see OWN tweets
        addTweets(userId, maxHeap);

        // Add FOLLOWEES tweets to Heap
        // Users should see FOLLOWEES tweets
        auto it = followees.find(userId);
        if (it != followees.end()) {
            for (const int followeeId : it->second) {
                addTweets(followeeId, maxHeap);
            }
        }

        // Add tweets from heap to the user's feed
        // Heap will now contain the at most the latest kMaxFeed tweets based on post times
        while (!maxHeap.empty() && feed.size() < kMaxFeed) {
            const HeapEntry& latest = maxHeap.top();
            feed.emplace_back(latest.tweetId);

            if (latest.index >= 0) {
                const auto& timeline = tweets.at(latest.userId);
                const Tweet& tweet = timeline.at(latest.index);

                maxHeap.emplace(tweet.time, tweet.id, latest.userId, latest.index - 1);
            }

            maxHeap.pop();
        }

        return feed;
    }
    
    void follow(int followerId, int followeeId) {
        if (followerId == followeeId) return;

        followees[followerId].insert(followeeId);
    }

    void unfollow(int followerId, int followeeId) {
        if (followerId == followeeId) return;

        auto it = followees.find(followerId);
        if (it != followees.end()) {
            it->second.erase(followeeId);
        }
    }
};

int main() {
    Twitter twitter;

    // Prompt Example
    twitter.postTweet(1, 5);
    assert(twitter.getNewsFeed(1) == std::vector<int>({5}));

    twitter.follow(1, 2);
    twitter.postTweet(2, 6);
    assert(twitter.getNewsFeed(1) == std::vector<int>({6, 5}));

    twitter.unfollow(1, 2);
    assert(twitter.getNewsFeed(1) == std::vector<int>({5}));

    // Single User, Multiple Tweets
    twitter.postTweet(1, 7);
    twitter.postTweet(1, 8);
    twitter.postTweet(1, 9);
    assert(twitter.getNewsFeed(1) == std::vector<int>({9, 8, 7, 5}));

    // Follow User With No Tweets
    twitter.follow(1, 3);
    assert(twitter.getNewsFeed(1) == std::vector<int>({9, 8, 7, 5}));

    // Add User Post
    twitter.postTweet(3, 10);
    assert(twitter.getNewsFeed(1) == std::vector<int>({10, 9, 8, 7, 5}));

    // Unfollow
    twitter.unfollow(1, 3);
    assert(twitter.getNewsFeed(1) == std::vector<int>({9, 8, 7, 5}));

    // More Tweets Than Max Limit
    Twitter twitter2;
    for (int i = 1; i <= 15; ++i) {
        twitter2.postTweet(1, i);
    }
    assert(twitter2.getNewsFeed(1) ==
           std::vector<int>({15, 14, 13, 12, 11, 10, 9, 8, 7, 6}));

    // Multiple Users, Late Messages
    Twitter twitter3;
    twitter3.postTweet(1, 101); // t1
    twitter3.postTweet(2, 201); // t2
    twitter3.postTweet(1, 102); // t3
    twitter3.postTweet(3, 301); // t4
    twitter3.follow(1, 2);
    twitter3.follow(1, 3);
    assert(twitter3.getNewsFeed(1) ==
           std::vector<int>({301, 102, 201, 101}));

    // Follow, Unfollow
    Twitter twitter4;
    twitter4.follow(1, 2);
    twitter4.follow(1, 2);
    twitter4.unfollow(1, 2);
    twitter4.unfollow(1, 2);
    twitter4.follow(1, 2);
    twitter4.postTweet(2, 42);
    assert(twitter4.getNewsFeed(1) == std::vector<int>({42}));

    return 0;
}
