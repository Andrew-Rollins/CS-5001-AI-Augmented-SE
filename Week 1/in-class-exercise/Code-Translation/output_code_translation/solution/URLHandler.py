class URLHandler:
    def __init__(self, url: str):
        self.url = url

    def get_scheme(self) -> str:
        scheme_end = self.url.find("://")
        if scheme_end != -1:
            return self.url[:scheme_end]
        return ""

    def get_host(self) -> str:
        scheme_end = self.url.find("://")
        if scheme_end != -1:
            url_without_scheme = self.url[scheme_end + 3:]
            host_end = url_without_scheme.find("/")
            if host_end != -1:
                return url_without_scheme[:host_end]
            return url_without_scheme
        return ""

    def get_path(self) -> str:
        scheme_end = self.url.find("://")
        if scheme_end != -1:
            url_without_scheme = self.url[scheme_end + 3:]
            host_end = url_without_scheme.find("/")
            if host_end != -1:
                return url_without_scheme[host_end:]
        return ""

    def get_query_params(self) -> dict:
        params = {}
        query_start = self.url.find("?")
        fragment_start = self.url.find("#")
        if query_start != -1:
            # Determine end of query string
            end = fragment_start if fragment_start != -1 else len(self.url)
            query_string = self.url[query_start + 1:end]
            if query_string:
                while True:
                    pos = query_string.find("&")
                    if pos == -1:
                        break
                    token = query_string[:pos]
                    equal_pos = token.find("=")
                    if equal_pos != -1:
                        key = token[:equal_pos]
                        value = token[equal_pos + 1:]
                        params[key] = value
                    query_string = query_string[pos + 1:]
                # Process the last (or only) token
                equal_pos = query_string.find("=")
                if equal_pos != -1:
                    key = query_string[:equal_pos]
                    value = query_string[equal_pos + 1:]
                    params[key] = value
        return params

    def get_fragment(self) -> str:
        fragment_start = self.url.find("#")
        if fragment_start != -1:
            return self.url[fragment_start + 1 :]
        return ""
