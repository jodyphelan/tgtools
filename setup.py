import setuptools

version = [l.strip() for l in open("tgtools/__init__.py") if "version" in l][0].split('"')[1]

setuptools.setup(

	name="tgtools",

	version=version,
	packages=["tgtools"],
	license="GPLv3",
	long_description="tgtools command line tool",
    entry_points = {
		'console_scripts': ['tgtools=tgtools.cli:main'],
	},
)
