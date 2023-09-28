# define an exec ressourse that kills the killmenow procces.
exec {'killmenow': 
  command => 'pkill -f "killmenow"',
  path => '/bin:/usr/bin',
  refreshonly => true,
}

# notify the exec resource to tun whene refreshed.
notify {'run killmenow':
  subscribe => Exec['killmenow'],
}
