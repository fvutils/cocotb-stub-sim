class RegressionManager(object):

    _entry = None
    _inst  = None

    def __init__(self, dut, tests):
        self._dut = dut
        self._ev = None
        self._outcome = None
        RegressionManager._inst = self

    def execute(self):
        """Wraps the 'entry' method to look like a cocotb test"""
        import cocotb
        test_c = cocotb.decorators.test()
        test_cc = test_c(self.entry)
        test_init_outcome = cocotb.outcomes.capture(
            test_cc,
            self._dut)

        test = test_init_outcome.get()

        cocotb.scheduler._add_test(test)

    def event(self, ev):
        print("--> Event")
        print("<-- Event")

    async def entry(self, dut):
        await RegressionManager._entry(self._dut)

    def _handle_result(self, test):
        """Receives the status of a test"""
        self._outcome = test._outcome

    def _execute(self):
        self.execute()

    @property
    def outcome(self):
        return self._outcome

    @classmethod
    def from_discovery(cls, dut):
        return RegressionManager(dut, [])

    @classmethod
    def inst(cls):
        return cls._inst
