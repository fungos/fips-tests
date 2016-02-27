#
# Test fips features:
# - fips_file_ex
#
fips_begin_app(test_fips_files_ex cmdline)
	# exclude.cpp is bad and we do not want, but include.* are good
    fips_files_ex(src inclu*.* EXCEPT exclu*.*)
    
	# resets dir to current directory as fips_files_ex and fips_src
	# changes the directory to the one in their first parameters
	# so that if we want we can continue working with files there
    fips_dir(".")
	fips_files(main.cc)
fips_end_app()
