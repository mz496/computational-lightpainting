#!/usr/bin/bash

source env/bin/activate
env/bin/pip-compile requirements/requirements.in
env/bin/pip-sync requirements/requirements.txt
