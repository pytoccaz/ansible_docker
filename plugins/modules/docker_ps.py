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
short_description: Returns information on running containers
description:
  - Retrieves information on running containers using the C(docker ps) command

version_added: 1.0.0

options:
    name_contains:
        description:
            - A search string to filter container list on names
        type: str
        version_added: '2.1.0'
    all:
        description:
            - whether to list stopped containers
        default: false
        type: bool
        version_added: '2.2.0'
'''

RETURN = '''
results:
    description: |
        List of containers running on the target host
    sample:
        - id: e7f4ccdb8680cb1dfca60d57252b031a77d3e060741dda1de662b80c22bf9b60
          created: 10 days ago
          names: web-server
          image: web:latest
          ports: 80/tcp
          status: Up 19 minutes
          command: nginx
    returned: success
    type: list
    elements: dict

'''

EXAMPLES = '''
  - name: List running containers
    pytoccaz.docker.docker_ps:
    register: containers_list

'''
from ansible.module_utils.basic import AnsibleModule


def parse_output(data):
    containers = []
    lines = data.split("\n")
    for line in lines[1:]:
        bits = [bit.strip() for bit in line.split("  ") if bit.strip() != ""]
        if len(bits) == 7:
            containers.append({
                "id": bits[0],
                "image": bits[1],
                "command": bits[2],
                "created": bits[3],
                "status": bits[4],
                "ports": bits[5],
                "names": bits[6],
            })
        elif len(bits) == 6:
            containers.append({
                "id": bits[0],
                "image": bits[1],
                "command": bits[2],
                "created": bits[3],
                "status": bits[4],
                "ports": "",
                "names": bits[5],
            })

    return containers


def docker_ps(module):

    docker_bin = module.get_bin_path("docker", required=True)

    command = [docker_bin, "ps", "--no-trunc"]

    if module.params["all"] is True:
        command.append("--all")

    rc, out, err = module.run_command(command)

    return rc, out.strip(), err.strip()


def main():
    module = AnsibleModule(
        argument_spec=dict(
            name_contains=dict(required=False, type='str'),
            all=dict(required=False, type='bool', default=False),
        ),
        supports_check_mode=True
    )

    name_filter = module.params["name_contains"]
    rc, out, err = docker_ps(module)

    if rc != 0:
        module.fail_json(msg="Error running docker ps. {0}".format(err),
                         rc=rc, stdout=out, stderr=err)
    else:
        if out:
            ret = parse_output(out)

        else:
            ret = []

    if name_filter is not None:
        ret = list(filter(lambda item: name_filter in item["names"], ret))

    module.exit_json(
        changed=False,
        rc=rc,
        stdout=out,
        stderr=err,
        results=ret
    )


if __name__ == "__main__":
    main()
