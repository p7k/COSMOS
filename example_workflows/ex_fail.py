from cosmos.Workflow.models import Workflow
from cosmos.lib.ezflow.taskGraph import TaskGraph, Split, Add, Map
from tools import ECHO, CAT, WC, FAIL

####################
# Workflow
####################

dag = ( TaskGraph()
    |Add| [ ECHO(tags={'word':'hello'}), ECHO(tags={'word':'world'}) ]
    |Split| ([('i',[1,2])],CAT)
    |Map| FAIL
    |Map| WC

)
dag.create_dag_img('/tmp/ex.svg')

#################
# Run Workflow
#################

WF = Workflow.start('Example Fail')
dag.add_to_workflow(WF)
WF.run()
