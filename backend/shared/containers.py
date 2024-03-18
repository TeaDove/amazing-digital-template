from dataclasses import dataclass

from service.heath_service import HeathService
from repository.redis_repository import RedisRepository
from repository.pg_repository import PgRepository


@dataclass
class Container:
    heath_service: HeathService
    redis_repository: RedisRepository


def init_combat_container() -> Container:
    redis_repository = RedisRepository()
    pg_repository = PgRepository()
    heath_service = HeathService(
        redis_repository=redis_repository, pg_repository=pg_repository
    )

    return Container(heath_service=heath_service, redis_repository=redis_repository)
