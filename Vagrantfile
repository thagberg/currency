# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "precise32"
  
  # The url from where the 'config.vm.box' box will be fetched if it
  # doesn't already exist on the user's system.
  config.vm.box_url = "http://files.vagrantup.com/precise32.box"

  # Enable the Puppet provisioner, with will look in manifests
  config.vm.synced_folder ".", "/vagrant", :owner => "www-data", :mount_options => ["umask=0000","dmask=0000","fmask=0000"]
  config.vm.network :private_network, ip: "192.168.250.250"
end
