.. _pytoccaz.docker.docker_ps_module:


*************************
pytoccaz.docker.docker_ps
*************************

**Return information on running containers**



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Retrieve information on running containers using the ``docker ps`` command







Examples
--------

.. code-block:: yaml

    - name: List running containers
        pytoccaz.docker.docker_ps:
      register: containers_list



Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>results</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>success</td>
                <td>
                            <div>List of containers running on the target host</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{&#x27;id&#x27;: &#x27;e7f4ccdb8680cb1dfca60d57252b031a77d3e060741dda1de662b80c22bf9b60&#x27;, &#x27;created&#x27;: &#x27;10 days ago&#x27;, &#x27;names&#x27;: &#x27;web-server&#x27;, &#x27;image&#x27;: &#x27;web:latest&#x27;, &#x27;ports&#x27;: &#x27;80/tcp&#x27;, &#x27;status&#x27;: &#x27;Up 19 minutes&#x27;, &#x27;command&#x27;: &#x27;nginx&#x27;}]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Olivier Bernard (@pytoccaz)
