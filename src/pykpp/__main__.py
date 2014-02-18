import os
from optparse import OptionParser
from mech import Mech

parser = OptionParser()
parser.set_usage("""Usage: python -m pykpp mech.def

Where mech.pykpp is a single file that contains initial
values and reaction definitions according to the KPP
format.
""")

parser.add_option("-v", "--verbose", dest = "verbose", action = "store_true", default = False, help = "Show extended output")

parser.add_option("-a", "--atol", dest = "atol", type = "float", default = 1e-3, help = "absolute tolerance")

parser.add_option("-r", "--rtol", dest = "rtol", type = "float", default = 1e-4, help = "relative tolerance")

parser.add_option("", "--tstart", dest = "tstart", type = "float", default = None, help = "Start time")

parser.add_option("", "--tend", dest = "tend", type = "float", default = None, help = "End time")

parser.add_option("", "--norun", dest = "norun", action = 'store_true', default = False, help = "Don't run")

parser.add_option("", "--dt", dest = "dt", type = "float", default = None, help = "Time step")

parser.add_option("-j", "--jacobian", dest = "jacobian", action="store_true", default = False, help = "Enable use of jacobian")

parser.add_option("-k", "--keywords", dest = "keywords", type="string", default = 'hv,PROD,EMISSION', help = "List of keywords to be ignored in reactants or products (comma delimited; default='hv')")

parser.add_option("-o", "--outpath", dest = "outpath", type="string", default = None, help = "Output path.")

parser.add_option("-m", "--monitor", dest = "monitor", type="string", default = None, help = "Extra monitor values (comma separated string).")

parser.add_option("-s", "--solver", dest = "solver", default = None, help = "solver (default: lsoda; vode; zvode; dopri5; dop853)")

parser.add_option("-c", "--code", dest = "code", default = "", help = "code to solve (exec) after model is compiled and run (unless --norun); out is a keyword for the mechanism that has been generated")

(options, args) = parser.parse_args()

if len(args) == 0:
    parser.print_help()
    exit()
    
outs = []
for arg in args:
    out = Mech(arg, verbose = options.verbose, keywords = [k_.strip() for k_ in options.keywords.split(',')])
    if options.monitor is not None:
        out.monitor = tuple([(None if k not in out.allspcs else out.allspcs.index(k), k) for k in options.monitor.split(',')]) + out.monitor
    if not options.norun:
        runtime = out.run(tstart = options.tstart, tend = options.tend, dt = options.dt, solver = options.solver, jac = options.jacobian, atol = options.atol, rtol = options.rtol)
        print 'Solved in %f seconds' % runtime
        out.output(options.outpath)
    outs.append(out)

if os.path.exists(options.code):
    options.code = file(options.code, 'r').read()
exec(options.code)