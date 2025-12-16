/*
Maximum Matching of Players With Trainers
https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

You are given a 0-indexed integer array players,
where players[i] represents the ability of the ith player.

You are also given a 0-indexed integer array trainers,
where trainers[j] represents the training capacity of the jth trainer.

The ith player can match with the jth trainer
if the player's ability is less than or equal to the trainer's training capacity.

The ith player can be matched with at most one trainer,
and the jth trainer can be matched with at most one player.

Return the maximum number of matchings between players and trainers that satisfy these conditions.

Example 1:
    Input: players = [4,7,9], trainers = [8,2,5,8]
    Output: 2
    Explanation:
        One of the ways we can form two matchings is as follows:
            - players[0] can be matched with trainers[0] since 4 <= 8.
            - players[1] can be matched with trainers[3] since 7 <= 8.
        It can be proven that 2 is the maximum number of matchings that can be formed.

Example 2:
    Input: players = [1,1,1], trainers = [10]
    Output: 1
    Explanation:
        The trainer can be matched with any of the 3 players.
        Each player can only be matched with one trainer, so the maximum answer is 1.

Constraints:
    * 1 <= players.length, trainers.length <= 10^5
    * 1 <= players[i], trainers[j] <= 10^9
*/

#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

class MaxMatchPlayersAndTrainers {
public:

    // Algorithm(s) Used: Greedy, Two Pointers
    // Time Complexity: O(nlog(n))
    // Space Complexity O(1)
    int matchPlayersAndTrainersI(vector<int>& players, vector<int>& trainers) {
        sort(players.begin(), players.end());
        sort(trainers.begin(), trainers.end());

        int i = 0;  // Greed/Child Index (Global Optimal)
        int j = 0;  // Cookie Index
        while (i < players.size() && j < trainers.size()) {
            if (players[i] <= trainers[j]) {  // Greedy Choice - Enough Cookies for Child
                i++;  // Local Optimal Solution
            }
            j++;
        }

        return i;
    }
};

int main() {
    MaxMatchPlayersAndTrainers Solution;

    // (players, trainers, expected)
    vector<tuple<vector<int>, vector<int>, int>> test_cases = {
        {{4, 7, 9}, {8, 2, 5, 8}, 2},
        {{1, 1, 1}, {10}, 1},
        {{5}, {4}, 0},
        {{2, 3, 4}, {1, 2, 3}, 2},
        {{1, 2, 3}, {3, 3, 3}, 3},
        {{10, 20}, {5, 5, 5}, 0},
        {{1}, {1}, 1},
    };

    vector<int (MaxMatchPlayersAndTrainers::*)(vector<int>&, vector<int>&)> funcs = {
        &MaxMatchPlayersAndTrainers::matchPlayersAndTrainersI,
    };

    for (auto func : funcs) {
        for (auto& tc : test_cases) {
            vector<int> players, trainers;
            int expected;
            tie(players, trainers, expected) = tc;

            int result = (Solution.*func)(players, trainers);
            assert(result == expected);
        }
    }

    return 0;
}
