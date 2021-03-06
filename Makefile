.PHONY: check
check:
	# ansible-playbook -t linode --check site.yml
	ansible-playbook -t init --check site.yml
	ansible-playbook -t common --check site.yml

.PHONY: linode
linode:
	ansible-playbook -t linode site.yml

.PHONY: init
init:
	ansible-playbook -t init site.yml

.PHONY: common
common:
	ansible-playbook -t common site.yml
