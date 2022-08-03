
import sys
import importlib

sys.modules['cocotb.simulator'] = importlib.import_module("cocotb_stub_sim.stub.cocotb.simulator")

from cocotb import *
