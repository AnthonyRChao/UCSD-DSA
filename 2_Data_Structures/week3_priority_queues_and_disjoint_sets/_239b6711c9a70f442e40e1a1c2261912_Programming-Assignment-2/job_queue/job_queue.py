# python3

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def leftChild(self, i):
        return 2 * i

    def rightChild(self, i):
        return 2 * i + 1

    def siftDown(self, i):
        minIndex = i
        l = self.leftChild(i)
        r = self.rightChild(i)

        if l <= len(self.nodes) - 1:
            if self.nodes[l][1] < self.nodes[minIndex][1]:
                minIndex = l
            elif self.nodes[l][1] == self.nodes[minIndex][1] and self.nodes[l][0] < self.nodes[minIndex][0]:
                minIndex = l

        if r <= len(self.nodes) - 1:
            if self.nodes[r][1] < self.nodes[minIndex][1]:
                minIndex = r
            elif self.nodes[r][1] == self.nodes[minIndex][1] and self.nodes[r][0] < self.nodes[minIndex][0]:
                minIndex = r

        if minIndex != i:
            self.nodes[i], self.nodes[minIndex] = self.nodes[minIndex], self.nodes[i]
            self.siftDown(minIndex)


    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        self.nodes = [None] + [[x, 0] for x in range(self.num_workers)]

        for i in range(len(self.jobs)):
            self.assigned_workers[i] = self.nodes[1][0]
            self.start_times[i] = self.nodes[1][1]
            self.nodes[1][1] += self.jobs[i]
            self.siftDown(1)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

