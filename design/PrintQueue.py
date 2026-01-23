"""
Printer Queue

Design a small system that models how a printer processes print jobs using a queue.

Implement the following classes:

    * PrintQueue
        - Follows the queue data structure (FIFO)
        - enqueue(item): add job to queue
        - dequeue(): remove next job from queue
        - peek(): view next job without removing it
        - size(): number of jobs in queue
        - is_empty(): check if queue is empty

    * Job
        - pages attribute: random integer between 1 and MAX_PAGES
        - print_page(): decrement pages by 1
        - check_complete(): returns True if pages == 0

    * Printer
        - get_job(print_queue): retrieve next job if available
        - print_page(job): prints all pages of a job

Constraints:
    * Job pages range from 1 to 15
    * Printer processes jobs one at a time
    * Queue follows FIFO ordering
"""

import random
from typing import Any, List, Optional


class Job:
    MAX_PAGES = 15

    def __init__(self, pages: int = MAX_PAGES):
        self.pages = random.randint(1, pages)

    def print_page(self):
        if self.pages > 0:
            self.pages -= 1

    def check_complete(self) -> bool:
        return self.pages == 0


class PrintQueue:
    def __init__(self):
        self.items: List[Any] = []

    def enqueue(self, item: Any):
        self.items.insert(0, item)

    def dequeue(self) -> Optional[Job]:
        if self.items:
            return self.items.pop()
        return None

    def peek(self) -> Optional[Job]:
        if self.items:
            return self.items[-1]
        return None

    def size(self) -> int:
        return len(self.items)
    
    def is_empty(self) -> bool:
        return self.items == []


class Printer:
    def __init__(self):
        self.current_job = None

    def get_job(self, print_queue: PrintQueue):
        try:
            self.current_job = print_queue.dequeue()
        except IndexError:  # Queue is empty
            return

    def print_page(self, job) -> bool:
        while job.pages > 0:
            job.print_page()

        return job.check_complete()


if __name__ == "__main__":
    print_queue = PrintQueue()

    assert print_queue.is_empty() is True
    assert print_queue.size() == 0
    assert print_queue.dequeue() is None
    assert print_queue.peek() is None

    job1 = Job(5)
    job2 = Job(5)
    job3 = Job(5)

    print_queue.enqueue(job1)
    print_queue.enqueue(job2)
    print_queue.enqueue(job3)

    assert print_queue.size() == 3
    assert print_queue.peek() == job1  # FIFO

    assert print_queue.dequeue() == job1
    assert print_queue.dequeue() == job2
    assert print_queue.dequeue() == job3
    assert print_queue.is_empty() is True

    job = Job(5)
    initial_pages = job.pages

    assert 1 <= initial_pages <= 5
    assert job.check_complete() is False

    while not job.check_complete():
        job.print_page()

    assert job.pages == 0
    assert job.check_complete() is True

    printer = Printer()
    print_queue = PrintQueue()

    job = Job(5)
    print_queue.enqueue(job)

    printer.get_job(print_queue)
    assert printer.current_job is job

    completed = printer.print_page(printer.current_job)
    assert completed is True
    assert printer.current_job.pages == 0

    empty_queue = PrintQueue()
    printer = Printer()

    result = printer.get_job(empty_queue)
    assert result is None
    assert printer.current_job is None
