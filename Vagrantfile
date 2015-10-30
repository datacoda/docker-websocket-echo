# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.synced_folder ".", "/vagrant", disabled: true

  config.vm.provider "docker" do |d|
    d.vagrant_vagrantfile = "host/Vagrantfile"
    d.build_dir = "."
    d.has_ssh = false
    d.ports = ["8080:8080"]
    d.cmd = [ "8080" ]
  end
end
