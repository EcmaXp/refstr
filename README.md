refstr
======

This module provides string that can be referenced.

## Example

### refstr[...]

```python
from typing import Union

from refstr import refstr


def import_string(name: Union[str, refstr[...]]):
    module, sep, attr = name.replace(':', '.').rpartition('.')
    return getattr(__import__(module), attr)

print(import_string("sys.version") == import_string("sys:version"))
```

### refstr[T]

```python
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, TypeVar, Union

from refstr import refstr


T = TypeVar("T")


def generic_get(obj: T, name: Union[str, refstr[T]]) -> Any:
    return getattr(obj, name)


@dataclass(frozen=True)
class Pos:
    x: int
    y: int
    z: int

    def get(self, name: Union[str, refstr[Pos]]) -> int:
        return generic_get(self, name)


pos = Pos(x=100, y=49, z=0)

print("x", generic_get(pos, "x"))
print("y", pos.get("y"))
print("z", pos.z)
```
