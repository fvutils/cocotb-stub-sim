
import sys
import importlib
import traceback

sys.modules['cocotb.simulator'] = importlib.import_module("cocotb_stub_sim.stub.simulator")
sys.modules['cocotb.regression'] = importlib.import_module("cocotb_stub_sim.stub.regression")

from cocotb import *

def tearDown():
    """Clean-up leftover state to ensure that future tests run properly"""
    from .stub.mgr import Mgr

    Mgr.init()

def run(entry):
    import cocotb
    from .stub.regression import RegressionManager
    from .stub.mgr import Mgr

    RegressionManager._entry = entry
    try:
        cocotb._initialise_testbench([])
    except Exception as e:
        print("Exception: %s" % str(e), flush=True)
        traceback.print_exc()
    mgr = Mgr.inst()

    mgr.run()

    rgr = RegressionManager.inst()

    if rgr.outcome is None:
        raise Exception("Internal error - no result")
    elif isinstance(rgr.outcome, cocotb.outcomes.Error):
        raise Exception("Test failed: %s" % str(rgr.outcome.error))
    else:
        """Test status is OK"""
        pass


    

