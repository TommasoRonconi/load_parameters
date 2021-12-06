####################################################################
# In order to read parameter file
import argparse
import importlib.util

####################################################################
# Import parameter file:

parser = argparse.ArgumentParser( description = 'options' )
parser.add_argument( '--parm',
                     dest = 'parm',
                     default = "",
                     help = 'path to parameter file')
args = parser.parse_args()

parms_spec = importlib.util.spec_from_file_location( "parameters", args.parm )
parms_module = importlib.util.module_from_spec( parms_spec )
parms_spec.loader.exec_module( parms_module )

####################################################################
# do something with parameters:

print( 'the answer is ', parms_module.int_parameter )

print( parms_module.string_parameter )

parms_module.function_parameter()

