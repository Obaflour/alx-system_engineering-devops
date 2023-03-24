# Using Puppet to create manifest that kills a process called killmenow.
exec { 'killmenow':
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
path	  => ['/usr/bin','/usr/sbin']
}
