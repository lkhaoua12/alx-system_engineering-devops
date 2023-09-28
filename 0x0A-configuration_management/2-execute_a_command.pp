# an exec ressource to kill a procces

exec {'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
