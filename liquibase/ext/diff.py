from sys import exit

from liquibase import run_output
try:
	from liquibase import config
except:
	config = None


liquibase_properties = {
	'url' : '',
	'driver' : '',
	'classpath' : '',
	'username' : '',
	'password' : ''
}
''' a dict representing `liquibase.properties` file'''


changelog_parameters = {
	'referenceUsername' : '',
	'referencePassword' : '',
	'referenceUrl' : '',
	'referenceDriver' : '',
}
''' a dict representing the arguments passed to `diffChangeLog`'''


def changelog(parameters=None, properties=None):
	if not parameters:
		parameters = getattr(config, 'changelog_parameters', None)
		if not parameters:
			exit('could not read "changelog_parameters" from config.')
	
	if not properties:
		properties = getattr(config, 'liquibase_properties', None)
		if not properties:
			exit('could not read "liquibase_properties" from config.')
	
	args = []
	
	for p, v in properties.items():
		args.append('--{}={}'.format(p, v))

	for p, v in parameters.items():
		args.append('--{}={}'.format(p, v))
	
	args.append('diffChangeLog')
	output = run_output(*args)
	return output


def changelog_utf8(parameters=None, properties=None):
	return changelog(parameters, properties).decode('utf-8')