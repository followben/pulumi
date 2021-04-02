# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['ComponentArgs', 'Component']

@pulumi.input_type
class ComponentArgs:
    def __init__(__self__, *,
                 a: bool,
                 c: int,
                 e: str,
                 b: Optional[bool] = None,
                 d: Optional[int] = None,
                 f: Optional[str] = None,
                 foo: Optional[pulumi.Input['FooArgs']] = None):
        """
        The set of arguments for constructing a Component resource.
        """
        pulumi.set(__self__, "a", a)
        pulumi.set(__self__, "c", c)
        pulumi.set(__self__, "e", e)
        if b is not None:
            pulumi.set(__self__, "b", b)
        if d is not None:
            pulumi.set(__self__, "d", d)
        if f is not None:
            pulumi.set(__self__, "f", f)
        if foo is not None:
            pulumi.set(__self__, "foo", foo)

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

    @property
    @pulumi.getter
    def foo(self) -> Optional[pulumi.Input['FooArgs']]:
        return pulumi.get(self, "foo")

    @foo.setter
    def foo(self, value: Optional[pulumi.Input['FooArgs']]):
        pulumi.set(self, "foo", value)


class Component(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 a: Optional[bool] = None,
                 b: Optional[bool] = None,
                 c: Optional[int] = None,
                 d: Optional[int] = None,
                 e: Optional[str] = None,
                 f: Optional[str] = None,
                 foo: Optional[pulumi.Input[pulumi.InputType['FooArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a Component resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ComponentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Component resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ComponentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ComponentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 a: Optional[bool] = None,
                 b: Optional[bool] = None,
                 c: Optional[int] = None,
                 d: Optional[int] = None,
                 e: Optional[str] = None,
                 f: Optional[str] = None,
                 foo: Optional[pulumi.Input[pulumi.InputType['FooArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if a is None and not opts.urn:
                raise TypeError("Missing required property 'a'")
            __props__['a'] = a
            __props__['b'] = b
            if c is None and not opts.urn:
                raise TypeError("Missing required property 'c'")
            __props__['c'] = c
            __props__['d'] = d
            if e is None and not opts.urn:
                raise TypeError("Missing required property 'e'")
            __props__['e'] = e
            __props__['f'] = f
            __props__['foo'] = foo
        super(Component, __self__).__init__(
            'example::Component',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter
    def a(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "a")

    @property
    @pulumi.getter
    def b(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "b")

    @property
    @pulumi.getter
    def c(self) -> pulumi.Output[int]:
        return pulumi.get(self, "c")

    @property
    @pulumi.getter
    def d(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "d")

    @property
    @pulumi.getter
    def e(self) -> pulumi.Output[str]:
        return pulumi.get(self, "e")

    @property
    @pulumi.getter
    def f(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "f")

    @property
    @pulumi.getter
    def foo(self) -> pulumi.Output[Optional['outputs.Foo']]:
        return pulumi.get(self, "foo")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

