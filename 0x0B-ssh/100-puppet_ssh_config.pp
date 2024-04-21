# Setup SSH configuration file

file_line { 'Turn off password authentication':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => 'PasswordAuthentication yes',
}

file_line { 'Configure the private key identity file':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^#?\s*IdentityFile.*',
}
