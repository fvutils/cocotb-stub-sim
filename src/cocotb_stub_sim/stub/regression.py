class RegressionManager(object):

    _entry = None

    def __init__(self, dut, tests):
        self._dut = dut
        self._ev = None

    def execute(self):
        """Wraps the 'entry' method to look like a cocotb test"""
        import cocotb
        test_c = cocotb.decorators.test()
        test_cc = test_c(self.entry)
        test_init_outcome = cocotb.outcomes.capture(
            test_cc,
            self._dut)

        test = test_init_outcome.get()
        print("outcome: %s" % str(test))

        cocotb.scheduler._add_test(test)

    def event(self, ev):
        print("--> Event")
        print("<-- Event")

    async def entry(self, dut):
        await RegressionManager._entry(self._dut)

    def _handle_result(self, *args, **kwargs):
        print("TODO: _handle_result %s %s" % (str(args), str(kwargs)))

    def _execute(self):
        self.execute()

    @classmethod
    def from_discovery(cls, dut):
        return RegressionManager(dut, [])
