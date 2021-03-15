# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = [
    'FooArgs',
]

@pulumi.input_type
class FooArgs:
    def __init__(__self__, *,
                 a: bool,
                 c: int,
                 e: str,
                 b: Optional[bool] = None,
                 d: Optional[int] = None,
                 f: Optional[str] = None):
        pulumi.set(__self__, "a", a)
        pulumi.set(__self__, "c", c)
        pulumi.set(__self__, "e", e)
        if b is not None:
            pulumi.set(__self__, "b", b)
        if d is not None:
            pulumi.set(__self__, "d", d)
        if f is not None:
            pulumi.set(__self__, "f", f)

    @property
    @pulumi.getter
    def a(self) -> bool:
        return pulumi.get(self, "a")

    @a.setter
    def a(self, value: bool):
        pulumi.set(self, "a", value)

    @property
    @pulumi.getter
    def c(self) -> int:
        return pulumi.get(self, "c")

    @c.setter
    def c(self, value: int):
        pulumi.set(self, "c", value)

    @property
    @pulumi.getter
    def e(self) -> str:
        return pulumi.get(self, "e")

    @e.setter
    def e(self, value: str):
        pulumi.set(self, "e", value)

    @property
    @pulumi.getter
    def b(self) -> Optional[bool]:
        return pulumi.get(self, "b")

    @b.setter
    def b(self, value: Optional[bool]):
        pulumi.set(self, "b", value)

    @property
    @pulumi.getter
    def d(self) -> Optional[int]:
        return pulumi.get(self, "d")

    @d.setter
    def d(self, value: Optional[int]):
        pulumi.set(self, "d", value)

    @property
    @pulumi.getter
    def f(self) -> Optional[str]:
        return pulumi.get(self, "f")

    @f.setter
    def f(self, value: Optional[str]):
        pulumi.set(self, "f", value)


