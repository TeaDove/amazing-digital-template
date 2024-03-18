from dataclasses import dataclass

from shared.base import logger
from typing import Awaitable, Callable
from repository.redis_repository import RedisRepository
from repository.pg_repository import PgRepository


class CheckFailed(Exception):
    ...


@dataclass
class HeathService:
    redis_repository: RedisRepository
    pg_repository: PgRepository

    def __post_init__(self) -> None:
        self.checks: dict[str, Callable[[], Awaitable]] = {
            "redis": self.redis_repository.health,
            "pg": self.pg_repository.health,
        }

    async def check(self) -> None:
        for service_name, checker in self.checks.items():
            try:
                await checker()
            except Exception as exc:
                raise CheckFailed(f"Check failed for {service_name}") from exc
            else:
                logger.debug(f"{service_name} check passed")
