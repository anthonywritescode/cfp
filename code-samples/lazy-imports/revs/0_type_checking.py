from __future__ import annotations

from typing import TYPE_CHECKING

lazy from typing_extensions import Self


class C:
    ...

    @classmethod
    def from_cfg(cls, cfg: dict[str, object]) -> Self:
        ...
