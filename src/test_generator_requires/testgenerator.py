"""fips imported code generator for testing"""

Version = 1

import os
import genutil
import subprocess
import platform
from mod import log
from mod import util
from mod import settings

# HACK: Find fips-deploy dir the hard way
# TODO: Fips need pass to generators the fips-deploy dir ready to be used
os_name = platform.system().lower()
extension = ""
proj_path = os.path.normpath('{}/..'.format(os.path.dirname(os.path.abspath(__file__))))
items = settings.load(proj_path)
if not items:
    items = {'config': settings.get_default('config')}

# HACK: even setting PROJECT in fips_setup does not work here without a way to get the
# fips-deploy path, so we force to search in Project for windows as it is the default
if os_name == "windows":
    extension = ".exe"

deploy_path = util.get_deploy_dir("../fips", "fips-tests", {'name': items['config']})

#-------------------------------------------------------------------------------
def get_generator_path() :
    """find generator_binary exectuable, fail if not exists"""

    bin_path = os.path.abspath('{}/generator_binary{}'.format(deploy_path, extension))
    print "TRY: " + bin_path
    if not os.path.isfile(bin_path) :
        os_name = platform.system().lower()
        bin_path = '{}/generator_binary{}'.format(proj_path, extension)
        bin_path = os.path.normpath(bin_path)
        print "TRY: " + bin_path
        
        if not os.path.isfile(bin_path) :
            log.error("generator_binary executable not found")

    print "FOUND: " + bin_path
    return bin_path

#-------------------------------------------------------------------------------
def generateHeader(hdrPath, funcName) :
    with open(hdrPath, 'w') as f :
        f.write("// #version:{}#\n".format(Version))
        f.write("extern void "+ funcName +"(void);\n")

#-------------------------------------------------------------------------------
def generateSource(srcPath, funcName) :
    with open(srcPath, 'w') as f :
        f.write("// #version:{}#\n".format(Version))
        f.write("#include <stdio.h>\n")
        f.write("void "+ funcName +"() {\n")
        f.write('    printf("Hello from '+ funcName +'!\\n");\n')
        f.write("}\n")

#-------------------------------------------------------------------------------
def generate(input, out_src, out_hdr) :
    if genutil.isDirty(Version, [input], [out_src, out_hdr]) :
        proc = subprocess.Popen([get_generator_path()], stdout=subprocess.PIPE)
        function_name, std_err = proc.communicate()
        print "GENERATING FUNCTION: " + function_name

        generateHeader(out_hdr, function_name)
        generateSource(out_src, function_name)
