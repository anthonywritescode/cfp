from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self


class C:
    ...

    @classmethod
    def from_cfg(cls, cfg: dict[str, object]) -> Self:
        ...
