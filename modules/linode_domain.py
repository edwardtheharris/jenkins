#!/usr/bin/python
"""Module for manging Linode domains."""
import os
import linode_api4
from linode_api4 import Domain
from ansible.module_utils.basic import AnsibleModule

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: my_sample_module

short_description: This is my sample module

version_added: "2.4"

description:
    - "This is my longer description explaining my sample module"

options:
    name:
        description:
            - This is the message to send to the sample module
        required: true
    new:
        description:
            - Control to demo if the result of this module is changed or not
        required: false

extends_documentation_fragment:
    - azure

author:
    - Your Name (@yourhandle)
'''

EXAMPLES = '''
# Pass in a message
- name: Test with a message
  my_new_test_module:
    name: hello world

# pass in a message and have changed true
- name: Test with a message and changed output
  my_new_test_module:
    name: hello world
    new: true

# fail the module
- name: Test failure of the module
  my_new_test_module:
    name: fail me
'''

RETURN = '''
original_message:
    description: The original name param that was passed in
    type: str
message:
    description: The output message that the sample module generates
'''


def add_subdomain(module, client):
    """Create a subdomain."""
    domain = client.domains(Domain.domain == module.params.get('domain'))[0]

    subdomain = domain.record_create('A',
                                     target=module.params.get('target'),
                                     name=module.params.get('name'),
                                     ttl_sec=300)

    return {
        'changed': True,
        'domain': domain.domain,
        'subdomain': subdomain.name,
        'ttl_sec': subdomain.ttl_sec
    }


def del_subdomain(module, client):
    """Delete a subdomain."""
    subdomains = client.domains(
        Domain.domain == module.params.get('domain'))[0]

    for subd in subdomains:
        if subd.name == module.params.get('name'):
            subd.delete()

    return {
        'changed': True,
        'subdomain': module.params.get('name')
    }


def linode_domain():
    """Add or remove a Linode domain."""
    module_args = {
        'domain': {
            'type': 'str'
        },
        'name': {
            'type': 'str',
            'required': True,
        },
        'state': {
            'type': 'str',
            'required': True,
            'choices': ['absent', 'present']
        },
        'type': {
            'type': 'str',
            'choices': ['domain', 'subdomain']
        },
        'target': {
            'type': 'str'
        }
    }

    result = {'changed': False,
              'subdomain': '',
              'domain': '',
              'target': ''}

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    client = linode_api4.LinodeClient(os.environ.get('LINODE_TOKEN'))

    result = add_subdomain(module, client)

    # use whatever logic you need to determine whether or not this module
    # made any modifications to your target
    # if module.params['new']:
    #    result['changed'] = True

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    if module.params['name'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    """Execute main module."""
    linode_domain()


if __name__ == '__main__':
    main()
