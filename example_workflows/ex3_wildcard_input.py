from cosmos.lib.ezflow.taskGraph import TaskGraph, Split, Add, Map, Reduce
from tools import ECHO, MD5Sum
from cosmos.Workflow.cli import CLI

cli = CLI()
WF = cli.parse_args() # parses command line arguments

####################
# Workflow
####################

dag = ( TaskGraph()
    |Add| [ ECHO(tags={'word':'hello'}), ECHO(tags={'word':'world'}) ]
    |Reduce| ([],MD5Sum)
)

dag.create_dag_img('/tmp/ex.svg')

#################
# Run Workflow
#################

dag.add_to_workflow(WF)
WF.run()