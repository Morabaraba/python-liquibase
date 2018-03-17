from liquibase.ext.diff import changelog
from liquibase.ext.update import sql_utf8

# see config.py you don't have to import LIQUIBASE or pass it on to methods if you defined it in `liquibase.config`
try:
	from liquibase.config import LIQUIBASE
except:
	LIQUIBASE = {
		'url' : 'jdbc:postgresql://localhost:5432/DB_WE_WANT_TO_CREATE_DIFF_FOR',
		'driver' : 'org.postgresql.Driver',
		'classpath' : 'postgresql.jar',
		'username' : 'postgresql',
		'password' : '',
		# Required Diff Parameters
		'referenceUsername' : 'postgresql',
		'referencePassword' : '',
		'referenceUrl' : 'jdbc:postgresql://localhost:5432/DB_WITH_CHANGES',
		# 'referenceDriver' : 'org.postgresql.Driver',
	}

	
def main():
	# only pass LIQUIBASE if you don't want to use `.liquibase.configLIQUIBASE` defaults.
	generated_sql = sql_utf8(changelog(**LIQUIBASE), **LIQUIBASE)
	print(generated_sql)


if __name__ == '__main__':
	main()