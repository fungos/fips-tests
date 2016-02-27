cmake_minimum_required(VERSION 2.8)

# include the fips main cmake file
get_filename_component(FIPS_ROOT_DIR "../fips" ABSOLUTE)
include("${FIPS_ROOT_DIR}/cmake/fips.cmake")

include_directories(src)

fips_setup()
fips_project(fips-tests)
fips_add_subdirectory(src/test_generator_requires)
fips_add_subdirectory(src/test_fips_files_ex)
fips_add_subdirectory(src/test_fips_src)
fips_finish()
