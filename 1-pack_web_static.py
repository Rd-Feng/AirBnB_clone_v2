#!/usr/bin/python3
"""pack all content within web_static
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """pack all content within web_static
    into a .tgz archive
    """
    now = datetime.now()
    name = "web_static_{}.tgz".format(
        now.strftime("%Y%m%d%H%M%S")
    )
    cmd = "tar -cvzf {} {}".format(name, "web_static")
    result = local(cmd)
    if not result.failed:
        return name
