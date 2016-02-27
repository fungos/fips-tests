#
# Test fips features:
# - fips_generate REQUIRES parameter:
#	This is an explicity build dependency order where to generate 
#	something, we must first build something else.
#

#
# This will generate things to be consumed by other compilations
#
fips_begin_app(util_generate_requires cmdline)
	fips_files(generator.cc)
fips_end_app()

# To be able to compile this we require that the application 
# 'util_generate_requires' be built before
fips_begin_app(test_generate_requires cmdline)
    fips_files(main.cc)
    fips_generate(FROM testgenerator.py REQUIRES util_generate_requires)
fips_end_app()
