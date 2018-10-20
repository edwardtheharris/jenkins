Jenkins Master Node
===================

Deploys to Linode a Jenkins Master node with the name jenkins-actual.

Requirements
------------

This requires a [special fork](https://github.com/edwardtheharris/ansible) of [Ansible](https://github.com/ansible/ansible) located [here](https://github.com/edwardtheharris/ansible).

APB Variables
--------------

A description of the settable variables for this APB should go here, including any variables that are in defaults/main.yml, vars/main.yml, apb.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (i.e. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other APBs/roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your APB (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: servers
  roles:
     - { role: edwardtheharris.jenkins, variable_name: 42 }
```

License
-------

BSD

Author Information
------------------

Xander Harris is a DevOps Engineer with a terrible habbit of doing too much accounting.
