import logging
import sys

_logger: logging.Logger | None = None


def setup_logger(env: str) -> None:
    global _logger

    _logger = logging.getLogger()
    handler = logging.StreamHandler(sys.stdout)

    match env:
        case "dev":
            _logger.setLevel(logging.DEBUG)
            handler.setLevel(logging.DEBUG)
        case "prod":
            _logger.setLevel(logging.INFO)
            handler.setLevel(logging.INFO)
        case _:
            raise ValueError(f'env: "prod" or "dev" expected, got "{env}"')

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    _logger.addHandler(handler)


def get_logger() -> logging.Logger:
    if _logger is None:
        raise Exception("logger was not initialized")
    return _logger
