from debug_utils import LOG_CURRENT_EXCEPTION


def init():
    try:
        import {{cookiecutter.mod_pkg}}
    except Exception:
        LOG_CURRENT_EXCEPTION()


def fini():
    pass
