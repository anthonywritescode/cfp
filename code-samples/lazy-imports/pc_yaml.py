import functools

import yaml

Loader = getattr(yaml, 'CSafeLoader', yaml.SafeLoader)
yaml_load = functools.partial(yaml.load, Loader=Loader)


def _load_manifest_forward_compat(contents: str) -> object:
    obj = yaml_load(contents)
    if isinstance(obj, dict):
        raise AssertionError('unsupported')
    else:
        return obj
