lazy-imports
============

slides: https://docs.google.com/presentation/d/1HHCxAuYxlOn6GKv3CyvWd_qcCA6pFZ4RpO4JdMMRlo0/edit?usp=sharing


### checkouts

clone these repos beforehand:

- https://github.com/pycqa/pyflakes
- https://github.com/asottile/babi

### interactive sessions

(about existing lazy paradigms)

```console
$ python3.13 lazy_ann.py
...
$ python3.14 lazy_ann.py
...
$ python3.14
```

```pycon
>>> # python 3.14
>>> import lazy_ann
>>> print(lazy_ann.f.__annotations__)
```
___

(about lazy imports)

```pycon
>>> # python3.15
>>> lazy import json
>>> print(globals()['json'])
...
>>> json
...
>>> print(globals()['json'])
...
```

___

pyflakes demo

```console
$ python3 -m pyflakes --version
...
$ best-of -n 10 -- python3 -m pyflakes --version
...
$ python3 -m pyflakes --help
...
$ best-of -n 10 -- python3 -m pyflakes --help
...
$ babi pyflakes/cli.py  # edit the one import to lazy
$ best-of -n 10 -- python3 -m pyflakes --version
...
```

___

pyflakes demo again

```console
$ python3 -Ximporttime -c 'import pyflakes.api'
...
$ importtime-waterfall pyflakes.api
...
$ importtime-waterfall --har pyflakes.api | xclip -sel c
...
```

___

(babi circular import)

```console
$ babi babi/file.py  # edit the `TYPE_CHECKING` out
$ babi babi/file.py  # oh no!
$ nano babi/file.py  # make it lazy
$ babi babi/file.py  # hooray!
```

___

spiders

```pycon
>>> lazy import does_not_exist
>>> ...
>>> does_not_exist
...
```
___

un-lazy import

```console
$ babi pc_yaml.py  # show contents
$ best-of -n 10 -- python3 -c 'import pc_yaml'
...
$ babi pc_yaml.py  # make it lazy
$ best-of -n 10 -- python3 -c 'import pc_yaml'  # not faster!?
...
$ babi pc_yaml.py  # comment out the assignments
$ best-of -n 10 -- python3 -c 'import pc_yaml'  # yay faster!
...
$ babi pc_yaml.py  # uncomment assignments
$ flake8 pc_yaml.py
...
$ babi pc_yaml.py  # use lazy_static
$ best-of -n 10 -- python3 -c 'import pc_yaml'  # still fast!
...
```
