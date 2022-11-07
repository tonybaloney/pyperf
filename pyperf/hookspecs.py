import pluggy

hookspec = pluggy.HookspecMarker("pyperf")


@hookspec
def before_func():
    ...


@hookspec
def after_func():
    ...
