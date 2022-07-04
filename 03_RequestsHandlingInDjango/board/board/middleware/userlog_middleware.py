import time

class UserLog:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        response = self.get_response(request)

        log_time = time.strftime('%H:%M:%S %d.%m.%Y', time.localtime())
        url = request.build_absolute_uri()
        http_method = request.META.get('REQUEST_METHOD')

        log_string = ';'.join([log_time, url, http_method]) + '\n'

        with open("board/logs/output.txt", "a") as file:
            file.write(log_string)

        return response