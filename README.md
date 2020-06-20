# Ghidra-BulkPatch
Bulk patch instructions easily. Great for creating nop slides.

## Usage
Make sure to add `BulkPatch.py` to your ghidra script folder.

1. Patch the first instruction of an area you want to patch manually
2. Select the area you want to patch, with the pre-patched instruction as the first address in the selection.
3. Run the script, and it will replicate the first instruction the the rest of the selection.

## Limitations
* Only 64-bit architectures
* Only continuous blocks of instructions

Feel free to create a PR for any of these limitations
