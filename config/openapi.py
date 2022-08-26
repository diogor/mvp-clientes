def __filter_endpoints(endpoint: tuple) -> bool:
    path = endpoint[0]
    if path.startswith("/qitech-webhook/") or path.startswith("/steps/"):
        return False
    return True


def preprocessing_filter(endpoints):
    return list(filter(__filter_endpoints, endpoints))
