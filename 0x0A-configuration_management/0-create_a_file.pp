/**
 * Create a file in /tmp with specific permissions, owner, and group.
 *
 * @file_path: The path to the file to be created.
 * @permissions: The file permissions (e.g., '0744').
 * @owner: The owner of the file.
 * @group: The group of the file.
 * @content: The content to be written to the file.
 */
file { '/tmp/school':
  ensure	=> 'file',
  mode	=> '0744',
  owner	=> 'www-data',
  group	=> 'www-data',
  content	=> 'I love Puppet',
}
