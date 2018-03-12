from distutils.core import setup

setup(
    name="liquibase",
    description="Liquibase packaged for Python",
    version="3.5.3",
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            "liquibase-run = liquibase:main",
            "liquibase-changelog = liquibase.diff:changelog",
            "liquibase-sql = liquibase.update:sql",
        ]
    },
)