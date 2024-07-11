#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['54.236.43.3', '100.25.38.88']

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    """
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split('/')[-1]
        file_name_no_ext = file_name.split('.')[0]

        put(archive_path, '/tmp/{}'.format(file_name))

        run('mkdir -p /data/web_static/releases/{}/'.format(file_name_no_ext))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(file_name, file_name_no_ext))

        run('rm /tmp/{}'.format(file_name))

        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(file_name_no_ext, file_name_no_ext))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(file_name_no_ext))

        run('rm -rf /data/web_static/current')

        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(file_name_no_ext))

        print("New version deployed!")
        return True
    except:
        return False

