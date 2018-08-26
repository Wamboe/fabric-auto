from fabric.api import *

"""def host_type():
    run('uname -s')

def folderCre():
    run('mkdir example')
    r = run('ls')
    r.failed"""
    
env.hosts = ['ipaddr']

def get_files():
    result = get(remote_path='/data1/csvs/archive2/*.gz', local_path='/data1/csvs/incoming')
    result.failed

def extract():
    local('tar xzvf /data1/csvs/incoming/*.tar.gz')


