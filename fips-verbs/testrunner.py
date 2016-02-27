# build a config and run all test_* targets

import re
from mod import log, project

#-------------------------------------------------------------------------------
def run(fips_dir, proj_dir, args) :
    p = re.compile('test_', re.I)
    if len(args) > 0 :
        cfg_name = args[0]
        project.gen(fips_dir, proj_dir, cfg_name)
        project.build(fips_dir, proj_dir, cfg_name) 
        success, targets = project.get_target_list(fips_dir, proj_dir, cfg_name)
        if success :
            app_targets = [tgt for tgt in targets if targets[tgt] == 'app' and p.match(tgt)]
            for app in app_targets :
                project.run(fips_dir, proj_dir, cfg_name, app, None, None)
    else :
        log.error("config name expected!")

#-------------------------------------------------------------------------------
def help() :
    log.info(log.YELLOW +
             'fips testrunner [config-name]\n' +
             log.DEF +
             '    build a config and run all test targets')
