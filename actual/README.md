Jenkins Actual
==============

Deploys Jenkins master node to Linode.

Requirements
------------

A Linode account.

Role Variables
--------------

None currently.

Dependencies
------------

None currently.

Example Playbook
----------------

```yaml
- hosts: jenkins-actual 
  roles:
     - { role: edwardtheharris.actual, x: 42 }
```

License
-------

Unlicense

Author Information
------------------

[Xander Harris](https://github.com/edwardtheharris)
