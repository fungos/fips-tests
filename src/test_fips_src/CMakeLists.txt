#
# Test fips features:
# - fips_src
#
fips_begin_app(test_files_src cmdline)
    # sample/broken.c redefines main, so we exclude this directory
    fips_src(src NO_RECURSE)

	# resets dir to current directory as fips_files_ex and fips_src
	# changes the directory to the one in their first parameters
	# so that if we want we can continue working with files there
    fips_dir(".")
	fips_files(main.cc)
fips_end_app()
