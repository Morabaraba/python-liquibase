## Python Liquibase

Home brewed wrapper library to make [liquibase](https://www.liquibase.org/) callable from python in the same vein as [python-closure](https://github.com/miracle2k/python-closure) with an extension or two.

```
git clone python-liquibase
cd python-liquibase
pip install -e .
./get-liquibase.sh
./get-postgresql.sh # or ./get-mysql.sh
python -m liquibase # or `liquibase-run` as created by setup.py
```

### Extentions

`liquibase.ext.diff` and `liquibase.ext.update` contain helper functions to use [`diffChangeLog`](http://www.liquibase.org/documentation/diff.html) and `updateSQL` more easily.

For a source example `liquibase/test.py`:

```py
from liquibase.ext.diff import changelog
from liquibase.ext.update import sql_utf8


def main():
        changelog_parameters = None
        liquibase_properties = None # by setting these to None we will try to load liquibase.config if not configured we will sys.exit

        generated_sql = sql_utf8(changelog(changelog_parameters, liquibase_properties))

        print(generated_sql)


if __name__ == '__main__':
        main()
```

and a postgres config `liquibase/config.py`:

```py
liquibase_properties = {
	'url' : 'jdbc:postgresql://localhost:5432/WORKING_DATABASE_WE_WANT_TO_CHANGE',
	'driver' : 'org.postgresql.Driver',
	'classpath' : 'postgresql-42.2.0.jar',
	'username' : 'postgres',
	'password' : ''
}

changelog_parameters = {
	'referenceUsername' : 'postgres',
	'referencePassword' : '',
	'referenceUrl' : 'jdbc:postgresql://localhost:5432/EXAMPLE_DATABASE_WITH_LATEST_DDL',
	#'referenceDriver' : 'org.postgresql.Driver',
}
```

if all went well and you executed `python liquibase/test.py` you should have a autogenerated SQL `Update Database Script` to change 
the tables of your `WORKING_DATABASE_WE_WANT_TO_CHANGE` to match `EXAMPLE_DATABASE_WITH_LATEST_DDL`. 

**WARNING** there might be `DROP` statements so review the SQL before just running it on your live database.

Note `referenceDriver` is commented out. You should be able to compare database across different db technology; your millage my vary.

Finally remember to read [THE PROBLEM WITH DATABASE DIFFS](http://www.liquibase.org/2007/06/the-problem-with-database-diffs.html).
### Version Numbering 

Will use the liquibase version number currently `3.5.3` and post-fix the date of the python package eg `3.5.3.180312`.

### Naming Convention and Python 2 Support

This is a helper library so I just decided on some names and ran with it. If you like the idea but disagree with the layout or structure create an issue.

Personally I would like to merge with one of the py-liquibase modules on pip. But I needed this today.

I'm lucky to only use py3. If this library does not work on py2 please create a pull request.

### Thanks

Thanks to /u/nvoxland and other liquibase contributors without his work and contribution my little toy project will have no existence;
and /u/miracle2k who's code I used as a base for this library.

### License

Apache License 2.0