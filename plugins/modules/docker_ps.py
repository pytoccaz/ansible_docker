#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2023 Olivier Bernard (@pytoccaz)
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later
# Credits: Jose Angel Munoz (@imjoseangel) for his module community.docker.docker_stack_info.py of which this programm is an adaptation

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = '''
---
module: docker_ps
author: "Olivier Bernard (@pytoccaz)"
short_description: Return information on running containers
description:
  - Retrieve information on running containers using the `docker ps` command

'''

RETURN = '''
results:
    description: |
        List of containers running on the target host
    sample:
        - {"ID": "0274311aef78", "RunningFor": "10 days ago", "Names": "ansible", ...}
    returned: always
    type: list
    elements: dict

'''

EXAMPLES = '''
  - name: List running containers
    pytoccaz.docker.docker_ps:
    register: containers_list

'''

import json
from ansible.module_utils.basic import AnsibleModule


def docker_ps(module):
    docker_bin = module.get_bin_path('docker', required=True)
    rc, out, err = module.run_command(
        [docker_bin, "ps", "--format=json"])

    return rc, out.strip(), err.strip()


def main():
    module = AnsibleModule(
        argument_spec={
        },
        supports_check_mode=True
    )

    rc, out, err = docker_ps(module)

    if rc != 0:
        module.fail_json(msg="Error running docker stack. {0}".format(err),
                         rc=rc, stdout=out, stderr=err)
    else:
        if out:
            ret = list(
                json.loads(outitem)
                for outitem in out.splitlines())

        else:
            ret = []

        module.exit_json(changed=False,
                         rc=rc,
                         stdout=out,
                         stderr=err,
                         results=ret)


if __name__ == "__main__":
    main()
