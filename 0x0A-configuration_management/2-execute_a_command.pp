# define an exec ressourse that kills the killmenow procces.
exec {'killmenow': 
  command => 'pkill killmenow',
  provider => 'shell',
}
