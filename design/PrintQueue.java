/*
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
*/
package design;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.Random;

public class PrintQueue {

    private final List<Job> items;

    public PrintQueue() {
        items = new ArrayList<>();
    }

    public void enqueue(Job job) {
        items.add(job);
    }

    public Optional<Job> dequeue() {
        if (items.isEmpty()) return Optional.empty();

        return Optional.of(items.remove(0));
    }

    public Optional<Job> peek() {
        if (items.isEmpty()) return Optional.empty();

        return Optional.of(items.get(0));
    }

    public int size() {
        return items.size();
    }

    public boolean isEmpty() {
        return items.isEmpty();
    }
}

class Job {
    private int pages;
    private static final int MAX_PAGES = 15;

    public Job() {
        Random rand = new Random();
        this.pages = 1 + rand.nextInt(MAX_PAGES); // Random between 1 and 15
    }

    public Job(int maxPages) {
        Random rand = new Random();
        this.pages = 1 + rand.nextInt(Math.min(maxPages, MAX_PAGES));
    }

    public int getPages() {
        return pages;
    }

    public void printPage() {
        if (pages > 0) pages -= 1;
    }

    public boolean checkComplete() {
        return pages == 0;
    }
}

class Printer {
    private Job currentJob;

    public Job getCurrentJob() {
        return currentJob;
    }

    public void getJob(PrintQueue queue) {
        currentJob = queue.dequeue().orElse(null);
    }

    public boolean printJob(Job job) {
        if (job == null) return false;

        while (!job.checkComplete()) {
            job.printPage();
        }

        return job.checkComplete();
    }
}

class PrintQueueTest {
    public static void main(String[] args) {
        PrintQueue queue = new PrintQueue();
        assert queue.isEmpty();
        assert queue.size() == 0;
        assert queue.dequeue() == null;
        assert queue.peek() == null;

        Job job = new Job(10);
        int pages = job.getPages();
        assert pages >= 1 && pages <= 10;

        while (!job.checkComplete()) {
            job.printPage();
        }
        assert job.getPages() == 0;
        assert job.checkComplete();

        Printer printer = new Printer();
        printer.getJob(queue);
        assert printer.getCurrentJob() == null;

        Job job2 = new Job(5);
        queue.enqueue(job2);
        printer.getJob(queue);
        assert printer.getCurrentJob() != null;
        boolean completed = printer.printJob(printer.getCurrentJob());
        assert completed;
        assert printer.getCurrentJob().checkComplete();
    }
}
