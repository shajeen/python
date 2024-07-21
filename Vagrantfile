Vagrant.configure("2") do |config|
  config.vm.define "docker-python-core" do |docker_cpp_core|
    docker_cpp_core.vm.provider "docker" do |d|
      d.image = "python-core-latest"
      d.cmd = ["/usr/sbin/sshd", "-D"]
      current_working_directory = Dir.pwd.gsub('\\', '/')
      d.volumes = ["#{current_working_directory}:/workspace"]
      d.ports = ["1004:22"] # Only map port 22 to 1001
      d.name = "python-core"
    end

    docker_cpp_core.ssh.username = "root"
    docker_cpp_core.ssh.private_key_path = ["ssh/vagrant_docker_key"]
    docker_cpp_core.ssh.port = 1004 # Connect using port 1001
  end
end