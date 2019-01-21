#!/usr/bin/python3
"""pack and deploy content to server
"""
from fabric.api import local, env, run, put, runs_once
from datetime import datetime
import os
env.hosts = ['35.231.156.161', '34.73.64.44']
env.user = 'ubuntu'


@runs_once
def do_pack():
    """pack all content within web_static
    into a .tgz archive
    The archive will be put in versions/
    """
    if not os.path.exists("versions"):
        local("mkdir versions")
    now = datetime.now()
    name = "versions/web_static_{}.tgz".format(
        now.strftime("%Y%m%d%H%M%S")
    )
    cmd = "tar -cvzf {} {}".format(name, "web_static")
    result = local(cmd)
    if not result.failed:
        return name


def do_deploy(archive_path):
    """deploy package to remote server
    Arguments:
        archive_path: path to archive to deploy
    """
    if not archive_path or not os.path.exists(archive_path):
        return False
    put(archive_path, '/tmp')
    ar_name = archive_path[archive_path.find("/") + 1: -4]
    try:
        run('mkdir -p /data/web_static/releases/{}/'.format(ar_name))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'.format(
                ar_name, ar_name
        ))
        run('rm /tmp/{}.tgz'.format(ar_name))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(
                ar_name, ar_name
        ))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            ar_name
        ))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ \
            /data/web_static/current'.format(
            ar_name
        ))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """pack web_static content and deploy it to web servers
    """
    pack = do_pack()
    if pack:
        return do_deploy(pack)
    return False

@runs_once
def clean_local(number):
    a = [
        (k, os.path.getmtime("versions/" + k))
        for k in os.listdir('versions') if "web_static" in k
    ]
    a.sort(key=lambda x: x[1])
    if number == 0 or number == 1:
        a = a[:-1]
    if number == 2:
        a = a[:-2]
    for f in a:
        os.remove("versions/" + f[0])
    return a

def do_clean(number=0):
    """clean old versions
    Arguments:
        number: number of versions to keep. 0 or 1 if keep newest,
        2 if keep newest and second newest
    """
    a = clean_local(number)
