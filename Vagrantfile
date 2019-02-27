# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/bionic64"

  config.vm.define "ilp" do |host|
    host.vm.hostname = "ilp"
    host.vm.provider :virtualbox do |vb|
      vb.customize ["modifyvm", :id, "--memory", 1024]
    end

    host.vm.provision "docker" do |d|
      d.run "mysql",
        image: "mysql:5.7",
        args: "-v mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=mysqlpassword -e MYSQL_DATABASE=ilp -p3306:3306"
    end

    config.vm.provision "shell", inline: <<-SCRIPT
      apt update
      apt install -y mysql-client-core-5.7
      apt install -y python3-pip
    SCRIPT

    # Expose port for MySQL
    host.vm.network :forwarded_port, guest: 3306, host: 3306
  end
end
