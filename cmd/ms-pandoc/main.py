import asyncio
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[2].__str__()  # noqa: E402
sys.path.append(root)  # noqa: E402

from internal.config import Config
from internal.logger import get_logger, setup_logger
from internal.app import App


def main() -> None:
    setup_logger(Config().ENV)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    app = App()
    logger = get_logger()

    loop.create_task(app.run())

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        logger.info("Gracefully shutting down")
        loop.run_until_complete(app.stop())
        loop.close()
        logger.info("Shut down completed")


if __name__ == '__main__':
    main()
