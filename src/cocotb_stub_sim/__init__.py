
import sys
import importlib
import traceback

sys.modules['cocotb.simulator'] = importlib.import_module("cocotb_stub_sim.stub.simulator")
sys.modules['cocotb.regression'] = importlib.import_module("cocotb_stub_sim.stub.regression")

from cocotb import *

def run(entry):
    from .stub.regression import RegressionManager
    from .stub.mgr import Mgr

    RegressionManager._entry = entry
    try:
        import cocotb
        cocotb._initialise_testbench([])
    except Exception as e:
        print("Exception: %s" % str(e), flush=True)
        traceback.print_exc()
    mgr = Mgr.inst()

    mgr.run()
    

