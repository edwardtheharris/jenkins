.PHONY: check
check:
	# ansible-playbook -t linode --check site.yml
	ansible-playbook -t common --check site.yml

.PHONY: linode
linode:
	ansible-playbook -t linode site.yml

.PHONY: common
common:
	ansible-playbook -t common site.yml
