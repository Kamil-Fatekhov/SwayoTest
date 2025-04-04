#Получаем из нашего URL host и port, чтобы подключиться к серверу
def make_url(url: str):
    try:
        ind = url.index("://") + 3
        protocol = url[:ind - 3]
        rest = url[ind:]
        if "/" in rest:
            path = rest[rest.index("/"):]
            host = rest[:rest.index("/")]
        else:
            host = rest
            path = "/"
        if ":" in host:
            host, port = host.split(":")
            port = int(port)
        else: port = 80
        return protocol, host, port, path
    except ValueError as e:
        raise ValueError(f"Wrong url {url}")