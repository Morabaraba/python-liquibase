from liquibase.ext.diff import changelog
from liquibase.ext.update import sql_utf8


def main():
	changelog_parameters = None
	liquibase_properties = None # by setting these to None we will try to load liquibase.config if not configured it will err
	
	generated_sql = sql_utf8(changelog(changelog_parameters, liquibase_properties))
	
	print(generated_sql)


if __name__ == '__main__':
	main()