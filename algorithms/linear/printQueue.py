"""
Prompt
    - Create 3 classes that, together, model how a printer could take jobs
      out of a print queue

Requirements
    - PrintQueue class
        + Follows the queue data structure implementation
    - Job class
        + pages attribute - random, 1 to 10
        + print_page() - decrement pages
        + check_complete()
    - Printer class
        + get_job() - account for the case where PrintQueue.items is empty
        + print_job()
"""

import random


class PrintQueue:

    def __init__(self) -> None:
        self.items = []

    def enqueue(self, item) -> None:
        self.items.insert(0, item)

    def dequeue(self):
        if self.items:
            return self.items.pop()

        return None

    def peek(self):
        if self.items:
            return self.items[-1]

        return None

    def size(self) -> int:
        return len(self.items)
    
    def is_empty(self) -> bool:
        return self.items == []


class Job:
    def __init__(self) -> None:
        self.pages = random.randint(1, 11)

    def print_page(self) -> None:
        if self.pages > 0:
            self.pages -= 1

    def check_complete(self) -> None:
        return self.pages == 0


class Printer:

    def __init__(self) -> None:
        self.current_job = None

    def get_job(self, print_queue):
        try:
            self.current_job = print_queue.dequeue()
        except IndexError:  # Queue is empty
            return "No more jobs to print"

    def print_page(self, job) -> str:
        while job.pages > 0:
            job.print_page()

        if job.check_complete():
            return "Printing comlete."
        else:
            return "An error occurred."