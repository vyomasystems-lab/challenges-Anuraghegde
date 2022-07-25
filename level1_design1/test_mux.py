# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
# import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    # for i in range(30):
    #     dut.sel.value = i
    #     x = 5
    #     dut.inp{i}.value = x

    #     await Timer(2, units='ns')
    #     assert dut.out.value == x, f"Mux result is incorrect for inp{i}"

    A = 3
    dut.inp30.value = A
    await Timer(2, units='ns')
    assert dut.out.value == A, f"Mux output is incorrrect: {dut.out.value} != 3"