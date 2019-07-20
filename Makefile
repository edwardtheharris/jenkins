.PHONY: check
check:
	ansible-playbook -t linode --check site.yml

.PHONY: linode
linode:
	ansible-playbook -t linode site.yml
