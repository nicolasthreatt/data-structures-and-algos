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

#include <cassert>
#include <chrono>
#include <optional>
#include <random>
#include <vector>

class Job {
public:
    Job(int maxPages = 10) {
        unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
        std::mt19937 gen(seed);
        std::uniform_int_distribution<int> dist(1, maxPages);
        pages = dist(gen);
    }

    void printPage() {
        if (pages > 0) pages -= 1;
    }

    bool checkComplete() const {
        return pages == 0;
    }

    int getPages() const {
        return pages;
    }

private:
    int pages;
};

class PrintQueue {
public:
    void enqueue(Job* job) {
        items.push_back(job);
    }

    std::optional<Job*> dequeue() {
        if (items.empty()) return nullptr;

        Job* job = items.front();
        items.erase(items.begin());

        return job;
    }

    std::optional<Job*> peek() const {
        if (items.empty()) return nullptr;

        return items.front();
    }

    size_t size() const {
        return items.size();
    }

    bool isEmpty() const {
        return items.empty();
    }

private:
    std::vector<Job*> items;
};

class Printer {
public:
    Printer() : currentJob(nullptr) {}

    void getJob(PrintQueue& queue) {
        currentJob = queue.dequeue().value();
    }

    bool printJob(Job* job) {
        currentJob = job;
        while (job->getPages() > 0) {
            job->printPage();
        }
        return currentJob->checkComplete();
    }

    Job* getCurrentJob() const {
        return currentJob;
    }

private:
    Job* currentJob;
};

int main() {

    {
        PrintQueue queue;

        assert(queue.isEmpty());
        assert(queue.size() == 0);
        assert(queue.dequeue() == nullptr);
        assert(queue.peek() == nullptr);
    }

    {
        Job job(10);

        int initialPages = job.getPages();
        assert(initialPages >= 1);
        assert(initialPages <= 10);

        while (!job.checkComplete()) {
            job.printPage();
        }

        assert(job.getPages() == 0);
        assert(job.checkComplete());
    }

    {
        PrintQueue queue;
        Printer printer;

        printer.getJob(queue);
        assert(printer.getCurrentJob() == nullptr);
    }

    {
        PrintQueue queue;
        Printer printer;

        Job* job = new Job(5);
        queue.enqueue(job);

        printer.getJob(queue);
        assert(printer.getCurrentJob() != nullptr);

        bool completed = printer.printJob(printer.getCurrentJob());
        assert(completed == true);
        assert(printer.getCurrentJob()->checkComplete());

        delete job;
    }

    {
        PrintQueue queue;
        Printer printer;

        Job* job1 = new Job(5);
        Job* job2 = new Job(5);
        Job* job3 = new Job(5);

        queue.enqueue(job1);
        queue.enqueue(job2);
        queue.enqueue(job3);

        assert(queue.size() == 3);

        printer.getJob(queue);
        assert(printer.printJob(printer.getCurrentJob()));

        printer.getJob(queue);
        assert(printer.printJob(printer.getCurrentJob()));

        printer.getJob(queue);
        assert(printer.printJob(printer.getCurrentJob()));

        assert(queue.isEmpty());

        delete job1;
        delete job2;
        delete job3;
    }

    return 0;
}
