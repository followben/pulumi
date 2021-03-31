# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ... import _enums as _root_enums
from ... import _inputs as _root_inputs
from ... import outputs as _root_outputs
from ._enums import *

__all__ = ['RubberTreeArgs', 'RubberTree']

@pulumi.input_type
class RubberTreeArgs:
    def __init__(__self__, *,
                 diameter: pulumi.Input['Diameter'],
                 type: pulumi.Input['RubberTreeVariety'],
                 container: Optional[pulumi.Input['_root_inputs.ContainerArgs']] = None,
                 farm: Optional[pulumi.Input[Union['Farm', str]]] = None,
                 size: Optional[pulumi.Input['TreeSize']] = None):
        """
        The set of arguments for constructing a RubberTree resource.
        """
        if diameter is None:
            diameter = 6
        pulumi.set(__self__, "diameter", diameter)
        if type is None:
            type = 'Burgundy'
        pulumi.set(__self__, "type", type)
        if container is not None:
            pulumi.set(__self__, "container", container)
        if farm is None:
            farm = '(unknown)'
        if farm is not None:
            pulumi.set(__self__, "farm", farm)
        if size is None:
            size = 'medium'
        if size is not None:
            pulumi.set(__self__, "size", size)

    @property
    @pulumi.getter
    def diameter(self) -> pulumi.Input['Diameter']:
        return pulumi.get(self, "diameter")

    @diameter.setter
    def diameter(self, value: pulumi.Input['Diameter']):
        pulumi.set(self, "diameter", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input['RubberTreeVariety']:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input['RubberTreeVariety']):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def container(self) -> Optional[pulumi.Input['_root_inputs.ContainerArgs']]:
        return pulumi.get(self, "container")

    @container.setter
    def container(self, value: Optional[pulumi.Input['_root_inputs.ContainerArgs']]):
        pulumi.set(self, "container", value)

    @property
    @pulumi.getter
    def farm(self) -> Optional[pulumi.Input[Union['Farm', str]]]:
        return pulumi.get(self, "farm")

    @farm.setter
    def farm(self, value: Optional[pulumi.Input[Union['Farm', str]]]):
        pulumi.set(self, "farm", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input['TreeSize']]:
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input['TreeSize']]):
        pulumi.set(self, "size", value)


@pulumi.input_type
class _RubberTreeState:
    def __init__(__self__, *,
                 farm: Optional[pulumi.Input[Union['Farm', str]]] = None):
        """
        Input properties used for looking up and filtering RubberTree resources.
        """
        if farm is None:
            farm = '(unknown)'
        if farm is not None:
            pulumi.set(__self__, "farm", farm)

    @property
    @pulumi.getter
    def farm(self) -> Optional[pulumi.Input[Union['Farm', str]]]:
        return pulumi.get(self, "farm")

    @farm.setter
    def farm(self, value: Optional[pulumi.Input[Union['Farm', str]]]):
        pulumi.set(self, "farm", value)


class RubberTree(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 container: Optional[pulumi.Input[pulumi.InputType['_root_inputs.ContainerArgs']]] = None,
                 diameter: Optional[pulumi.Input['Diameter']] = None,
                 farm: Optional[pulumi.Input[Union['Farm', str]]] = None,
                 size: Optional[pulumi.Input['TreeSize']] = None,
                 type: Optional[pulumi.Input['RubberTreeVariety']] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a RubberTree resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RubberTreeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a RubberTree resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param RubberTreeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RubberTreeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 container: Optional[pulumi.Input[pulumi.InputType['_root_inputs.ContainerArgs']]] = None,
                 diameter: Optional[pulumi.Input['Diameter']] = None,
                 farm: Optional[pulumi.Input[Union['Farm', str]]] = None,
                 size: Optional[pulumi.Input['TreeSize']] = None,
                 type: Optional[pulumi.Input['RubberTreeVariety']] = None,
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
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RubberTreeArgs.__new__(RubberTreeArgs)

            __props__.__dict__['container'] = container
            if diameter is None:
                diameter = 6
            if diameter is None and not opts.urn:
                raise TypeError("Missing required property 'diameter'")
            __props__.__dict__['diameter'] = diameter
            if farm is None:
                farm = '(unknown)'
            __props__.__dict__['farm'] = farm
            if size is None:
                size = 'medium'
            __props__.__dict__['size'] = size
            if type is None:
                type = 'Burgundy'
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__['type'] = type
        super(RubberTree, __self__).__init__(
            'plant:tree/v1:RubberTree',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            farm: Optional[pulumi.Input[Union['Farm', str]]] = None) -> 'RubberTree':
        """
        Get an existing RubberTree resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RubberTreeState.__new__(_RubberTreeState)

        __props__.__dict__['farm'] = farm
        __props__.__dict__['container'] = None
        __props__.__dict__['diameter'] = None
        __props__.__dict__['size'] = None
        __props__.__dict__['type'] = None
        return RubberTree(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def container(self) -> pulumi.Output[Optional['_root_outputs.Container']]:
        return pulumi.get(self, "container")

    @property
    @pulumi.getter
    def diameter(self) -> pulumi.Output['Diameter']:
        return pulumi.get(self, "diameter")

    @property
    @pulumi.getter
    def farm(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "farm")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[Optional['TreeSize']]:
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output['RubberTreeVariety']:
        return pulumi.get(self, "type")

