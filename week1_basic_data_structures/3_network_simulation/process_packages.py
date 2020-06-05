# python3

from collections import namedtuple, deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque([])

    def process(self, request):
        while self.finish_time and self.finish_time[0] <= request[0]:
            self.finish_time.popleft()
        
        if self.size <= len(self.finish_time):
            return Response(True, -1)

        if len(self.finish_time) == 0:
            self.finish_time.append(request[0] + request[1])
            return Response(False, request[0])

        current_response = Response(False, self.finish_time[-1])
        self.finish_time.append(self.finish_time[-1] + request[1])
        return current_response
            

def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
