from functools import lru_cache

import punq

from choice_paralysis.src.domain.match.provider import MatchProvider


def setup_container() -> punq.Container:
    container = punq.Container()

    # Register Domain Providers
    container.register(MatchProvider)

    return container


@lru_cache(1)
def get_container() -> punq.Container:
    return setup_container()
