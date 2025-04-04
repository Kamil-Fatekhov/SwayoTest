"""Реализация классов для HTTP - запроса и HTTP - ответа """
from typing_extensions import Self

class HTTPRequest():

    def __init__(self, method: str, path: str, headers: dict, body: str):
        self.method = method
        self.path = path
        self.headers = headers
        self.body = body

    def to_bytes(self)-> bytes:
       headers = "\r\n".join(f"{k}: {v}" for k, v in self.headers.items())
       return f"{self.method} {self.path} HTTP/1.1\r\n{headers}\r\n\r\n{self.body}".encode('utf-8')

    @classmethod
    def from_bytes(cls, data: bytes) -> Self:
        decoded_data = data.decode()
        tmp, _, body = decoded_data.partition("\r\n\r\n")
        tmp_head = tmp.split("\r\n")
        method, path, _ = tmp_head[0].split()

        headers= {}

        for elem in tmp_head[1:]:
            if ":" in elem:
                k, v = elem.split(":", 1)
                headers[k.strip()] = v.strip()
        return cls(method, path, headers, body)

class HTTPResponse():

    def __init__(self, status_code: int, body: str, headers: dict):
        self.status_code = status_code
        self.body = body
        self.headers = headers

    def to_bytes(self)-> bytes:
        headers = "\r\n".join(f"{k}: {v}" for k, v in self.headers.items())
        return f"{self.method} {self.path} HTTP/1.1 \r\n{headers}\r\n\r\n{self.body}".encode('utf-8')

    @classmethod
    def from_bytes(cls, data: bytes)-> Self:
        decoded_data = data.decode()
        tmp, _, body = decoded_data.partition("\r\n\r\n")
        tmp_head = tmp.split("\r\n")

        _, status_code, _ = tmp_head[0].split(" ", 2)

        headers = {}

        for elem in tmp_head[1:]:
            if ":" in elem:
                k, v = elem.split(":", 1)
                headers[k.strip()] = v.strip()

        return cls(int(status_code), body, headers)
