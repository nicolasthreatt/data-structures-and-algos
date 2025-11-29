/*
Doordash Interview Question

Given a streaming data of the form (timestamp, value),
find the maximum value in the stream in the last X seconds.

Assume time is monotonically increasing.
Assume time is in the order of seconds.
max_value() function finds the max in the last X seconds.

Example:
    StreamProcessor(5) // last 5 seconds
    set_value(0, 5)
    set_value(1, 6)
    set_value(2, 4)
    max_value(3) = 6 -> always the current time
*/

#include <algorithm>
#include <deque>
#include <utility>

class StreamProcessor {

private:
    int x; // Last x seconds
    std::deque<std::pair<int, int>> queue; // FIFO: (timestamp, value)

public:
    /* Initializer */
    StreamProcessor(int x) : x(x) {}

    /**
     * Remove all elements older than cur_t - x.
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    void remove_old(int cur_t) {
        while (!queue.empty() && queue.front().first <= cur_t - x) {
            queue.pop_front();
        }
    }

    /**
     * Set value at time t to v.
     *
     * 1. Remove outdated timestamps.
     * 2. Append (t, v) to the queue.
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    void set_value(int t, int v) {
        remove_old(t);
        queue.emplace_back(t, v);
    }

    /**
     * Get the max value in the last x seconds.
     *
     * 1. Remove outdated timestamps.
     * 2. Return max value in the queue.
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    int max_value(int cur_t) {
        remove_old(cur_t);
        int max_val = queue.front().second;
        for (const auto &p : queue) {
            max_val = std::max(max_val, p.second);
        }
        return max_val;
    }
};
