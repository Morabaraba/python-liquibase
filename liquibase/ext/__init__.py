import os.path

from liquibase import get_jar_classpath


def read_config():
	config = {}
	config_warning = ''
	
	try:
		from liquibase import config as _config
		config = getattr(_config, 'LIQUIBASE', None)
		if not config:
			config_warning = ' "LIQUIBASE" empty in config.'
	except:
		config_warning = ' Could not read "LIQUIBASE" from config.'
	return (config, config_warning)


def arguments2parameters(**kwargs):
	parameters = []
	(config, config_warning) = read_config()
	required = ('url', 'username', 'password', 'classpath')
	for req in required:
		kwargs[req] = kwargs.get(req, config.get(req))
		if kwargs[req] == None:
			exit('"' + req + '" is required.' + config_warning)
	
	if not os.path.isfile(kwargs['classpath']):
		kwargs['classpath'] = get_jar_classpath() + '/' + kwargs['classpath']
		if not os.path.isfile(kwargs['classpath']):
			exit('classpath" ' + kwargs['classpath'] + '" driver could not be found.')
			
	for p, v in kwargs.items():
		parameters.append('--{}={}'.format(p, v))
	return parameters