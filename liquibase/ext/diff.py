from sys import exit

from liquibase.ext import arguments2parameters, read_config
from liquibase import run_output


def changelog(**kwargs):
	(config, config_warning) = read_config()
	required = ('referenceUrl', 'referenceUsername', 'referencePassword', 'referenceUrl')
	for req in required:
		kwargs[req] = kwargs.get(req, config.get(req))
		if kwargs[req] == None:
			exit('"' + req + '" is required.' + config_warning)
			
	parameters = arguments2parameters(**kwargs)
	parameters.append('diffChangeLog')
	output = run_output(*parameters)
	return output


def changelog_utf8(**kwargs):
	return changelog(**kwargs).decode('utf-8')