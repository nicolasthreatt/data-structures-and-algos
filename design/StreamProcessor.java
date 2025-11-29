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
package design;

import java.util.ArrayDeque;
import java.util.Deque;

public class StreamProcessor {
    private final int x;
    private final Deque<int[]> queue; // FIFO: (timestamp, value)

    /* Initializer */
    public StreamProcessor(int x) {
        this.x = x;
        this.queue = new ArrayDeque<>();
    }

    /**
     * Remove all elements older than curTime - x.
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    private void removeOld(int curTime) {
        while (!queue.isEmpty() && queue.peekFirst()[0] <= curTime - x) {
            queue.pollFirst();
        }
    }

    /**
     * Set value at time t to v.
     *
     * 1. Remove outdated timestamps.
     * 2. Append (t, v) to queue.
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public void setValue(int t, int v) {
        removeOld(t);
        queue.offerLast(new int[]{t, v});
    }

    /**
     * Return the maximum value in the last x seconds.
     *
     * 1. Remove outdated timestamps.
     * 2. Scan queue for max.
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public int maxValue(int curTime) {
        removeOld(curTime);
        int max = Integer.MIN_VALUE;
        for (int[] pair : queue) {
            max = Math.max(max, pair[1]);
        }
        return max;
    }
}
