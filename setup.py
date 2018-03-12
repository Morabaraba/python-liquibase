from distutils.core import setup

setup(
    name="liquibase",
    description="Liquibase packaged for Python",
    version="3.5.3.180312",
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            "liquibase-run = liquibase:main",
            "liquibase-ext-changelog = liquibase.ext.diff:changelog_utf8",
            "liquibase-ext-sql = liquibase.ext.update:sql_utf8",
            "liquibase-ext-changelog-sql = liquibase.ext.update:changelog_sql_utf8",
        ]
    },
)