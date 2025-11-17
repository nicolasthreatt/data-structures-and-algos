"""
Weighted Moving Average Programming Challenge

Problem Description:
- You are given a series of trades.
- Each trade has:
    1. key
    2. value
    3. quantity
    4. sequence number
- For each trade, print the weighted moving average (WMA) of all trades for that key.
- Round the average to two decimal places.
- If the sequence number for a trade is less than the previous trade for the same key, ignore it.
  Do not print or factor it into the WMA.

Formula:
    Mx+1 = ((Mx * Qx) + (vx+1 * qx+1)) / Qx+1
Where:
    M = weighted moving average
    Q = total quantity so far
    q = current trade quantity
    v = current trade value

Input:
- Semicolon-delimited string of trades.
- Each trade: comma-delimited key,value,quantity,sequence_number
- key: string, value: float, quantity: positive int, sequence: positive int

Example Input:
    ES,2000,5,1;ES,2050,5,2;SPX,3000,10,3

Expected Output:
    ES: 2000.00
    ES: 2025.00
    SPX: 3000.00

Notes:
- Handle multiple keys separately.
- Skip trades that have a lower sequence number than the last seen for that key.
- Each output line is "{key}: {weighted moving average for key}"
"""

class WeightedMovingAverage:
    def __init__(self):
        self.averages: dict = {}

    def process_trade(self, key: str, value: float, quantity: int, seq: int) -> float:
        """
        Process a single trade and update WMA for the key.
        Returns the updated WMA, or None if trade is skipped.
        """
        if key not in self.averages:
            self.averages[key] = (0.0, 0, 0)

        curr_avg, total_qty, last_seq = self.averages[key]

        if seq < last_seq:
            return None

        new_qty = total_qty + quantity
        new_avg = ((curr_avg * total_qty) + (value * quantity)) / new_qty

        self.averages[key] = (new_avg, new_qty, seq)

        return new_avg

    def process_trades(self, trades_str: str) -> list:
        """
        Process a semicolon-delimited string of trades.
        Returns list of formatted WMA strings.
        """
        trades: list = trades_str.split(';')
        results: list = []

        for trade in trades:
            key, value, quantity, seq = trade.split(',')
            value = float(value)
            quantity = int(quantity)
            seq = int(seq)

            new_avg = self.process_trade(key, value, quantity, seq)
            if new_avg is not None:
                results.append(f"{key}: {new_avg:.2f}")

        return results


if __name__ == "__main__":
    wma = WeightedMovingAverage()

    # Test Example 1
    input_str = "ES,2000,5,1;ES,2050,5,2;SPX,3000,10,3"
    output = wma.process_trades(input_str)
    expected = ["ES: 2000.00", "ES: 2025.00", "SPX: 3000.00"]
    assert output == expected

    # Test Example 2
    wma = WeightedMovingAverage()  # reset for new test
    input_str = "ES,2000,5,2;ES,2050,5,4"
    output = wma.process_trades(input_str)
    expected = ["ES: 2000.00", "ES: 2025.00"]
    assert output == expected

    # Test Example 3
    wma = WeightedMovingAverage()
    input_str = "ES,2000,5,1;SPY,2050,15,2"
    output = wma.process_trades(input_str)
    expected = ["ES: 2000.00", "SPY: 2050.00"]
    assert output == expected

    # Test Example 4 (out-of-order sequence)
    wma = WeightedMovingAverage()
    input_str = "ES,2000,5,1;ES,2030,15,2;ES,2000,10,1;SPY,2050,15,5;ES,2067,8,6;SPY,2050,5,7"
    output = wma.process_trades(input_str)
    expected = ["ES: 2000.00", "ES: 2025.00", "SPY: 2050.00", "ES: 2054.33", "SPY: 2050.00"]
    assert output == expected

    # Test Example 5 (multiple keys and skipped trade)
    wma = WeightedMovingAverage()
    input_str = "BTC,40000,2,1;ETH,2500,3,2;BTC,41000,1,3;ETH,2400,2,1;BTC,42000,1,2"
    output = wma.process_trades(input_str)
    expected = ["BTC: 40000.00", "ETH: 2500.00", "BTC: 40333.33"]
    assert output == expected
