
import sys
import importlib

sys.modules['cocotb.simulator'] = importlib.import_module("cocotb_stub_sim.stub.simulator")
sys.modules['cocotb.regression'] = importlib.import_module("cocotb_stub_sim.stub.regression")

from cocotb import *

def run(coro):
    pass

