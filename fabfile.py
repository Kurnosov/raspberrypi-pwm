import os.path
import datetime

from fabric.api import run, local, cd, lcd, put, env, hosts, hide
from fabric.contrib.files import exists
from time import sleep

env.use_ssh_config = True
env.hosts = ["raspberry_dev"]
print("Uploading to %s" % env.hosts)


def deploy():
    with cd("/tmp"):
        run("rm -f rpio_pwm.c")
        put("rpio-pwm/rpio_pwm.c", "/tmp/")
        run("gcc -Wall -g -O2 -o rpio-pwm rpio_pwm.c")


def kill_servod():
    run("""sudo kill `pgrep -f "./rpio-pwm"`""")
