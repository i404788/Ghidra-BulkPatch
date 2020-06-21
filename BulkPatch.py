# Write the selected memory (including patches) back to a copy of the binary file
#@author i404788
#@category Memory
#@keybinding 
#@menupath 
#@toolbar 

import shutil
import jarray
import os
from ghidra.app.plugin.assembler import Assemblers

def main():
    print("Patch starting at 0x%08x (%d bytes)"%(start_addr.getOffset(),size))
    tool = state.getTool()
    mem = currentProgram.getMemory()
    assembler = Assemblers.getAssembler(mem.program)
    arch_len = 4 # TODO: 4 = 64bit arch

    if int(currentSelection.getFirstRange().getMinAddress().unsignedOffset) % 4 != 0:
        print("Make sure your selection is on the grid of instructions (multiple of 4 or 2 usually)")
        return

    addr = currentSelection.getFirstRange().getMinAddress()
    size = int(currentSelection.getFirstRange().getLength())
    data_buffer = jarray.zeros(arch_len,"b") 
    mem.getBytes(addr, data_buffer)

    i = 1
    while i < size // arch_len:
      addr = addr.add(arch_len)
            assembler.patchProgram(data_buffer, addr)
      i += 1
    
main()
