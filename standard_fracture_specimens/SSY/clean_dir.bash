#!/bin/bash  
#  
/bin/rm -rf  -f *_db   >& /dev/null
/bin/rm -rf  -f *~   >& /dev/null
/bin/rm -rf  wn*   >& /dev/null
/bin/rm -rf  we*   >& /dev/null
/bin/rm -rf  core*  >& /dev/null
/bin/rm -rf  energy*  >& /dev/null
/bin/rm -rf  fort.*  >& /dev/null
/bin/rm -rf  gmon*    >& /dev/null
/bin/rm -rf  gprof*   >& /dev/null
/bin/rm -rf  *messages  >& /dev/null
/bin/rm -rf  *.warp   >& /dev/null
/bin/rm -rf  packet*  >& /dev/null
/bin/rm -rf  step_*  >& /dev/null
/bin/rm -rf  solver*  >& /dev/null
/bin/rm -rf  pardiso*  >& /dev/null
/bin/rm -rf zzz.db  >& /dev/null
/bin/rm -rf *.exo >& /dev/null
/bin/rm -rf *.db >& /dev/null
/bin/rm -rf states_header* >& /dev/null
#  
#  
echo "> done..."
