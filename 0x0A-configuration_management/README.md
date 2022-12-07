Requirements
Bash Scripts
Allowed editors: vi, vim, emacs.
All your files will be interpreted/compiled on Ubuntu 20.04 LTS.
All your files should end with a new line.
Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
Your Puppet manifests must run without error.
Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about.
Your Puppet manifests files must end with the extension .pp.
Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.
Install puppet
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
You do not need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.

Puppet 5 Docs

Install puppet-lint
$ gem install puppet-lint
0. Create a file - Using Puppet, create a file in /tmp. - 0-create_a_file.pp.

Requirements:

File path is /tmp/school
File permission is 0744
File owner is www-data
File group is www-data
File contains I love Puppet
