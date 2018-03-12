from sys import exit
from liquibase import run_output

try:
	from liquibase import config
except:
	config = None

import tempfile


def sql_run(parameters=None, properties=None):
	if not parameters:
		parameters = getattr(config, 'sql_parameters', None)
		if not parameters:
			exit('could not read "sql_parameters" from config.')
	
	if not properties:
		properties = getattr(config, 'liquibase_properties', None)
		if not properties:
			exit('could not read "liquibase_properties" from config.')
	
	args = []
	
	for p, v in properties.items():
		args.append('--{}={}'.format(p, v))

	for p, v in parameters.items():
		args.append('--{}={}'.format(p, v))
	
	args.append('updateSQL')
	output = run_output(*args)
	return output
	
def sql(parameters=None, properties=None):
	if isinstance(parameters, (str, bytes)):
		with tempfile.NamedTemporaryFile(suffix='xml') as temp:
			temp.write(parameters)
			temp.flush()
			return sql_run({'changeLogFile': temp.name}, properties)
	return sql_run(parameters, properties)
	
