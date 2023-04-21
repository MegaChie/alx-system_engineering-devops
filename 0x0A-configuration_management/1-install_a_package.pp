--- comment text
- hosts: all
  become: true
  vars:
    package: flask
  tasks:
    -name: install flask package
    apt: name={{ package }} state=latest
