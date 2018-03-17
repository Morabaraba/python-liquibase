from sys import exit
import tempfile

from liquibase import run_output
from liquibase.ext import arguments2parameters
from liquibase.ext.diff import changelog


def sql_run(**kwargs):
	parameters = arguments2parameters(**kwargs)
	parameters.append('updateSQL')
	output = run_output(*parameters)
	return output


def sql(changeLogText=None, **kwargs):
	if isinstance(changeLogText, (str, bytes)):
		with tempfile.NamedTemporaryFile(suffix='xml') as temp:
			temp.write(changeLogText)
			temp.flush()
			kwargs['changeLogFile'] = temp.name
			return sql_run(**kwargs)
	return sql_run(**kwargs)


def changelog_sql(**kwargs):
	changes = changelog(**kwargs)
	generated_sql = sql(changes)
	return generated_sql


def sql_utf8(changeLogText=None, **kwargs):
	return sql(changeLogText, **kwargs).decode('utf-8')


def changelog_sql_utf8(**kwargs):
	return changelog_sql(**kwargs).decode('utf-8')