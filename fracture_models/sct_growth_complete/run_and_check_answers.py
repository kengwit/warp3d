#!/usr/bin/env python3
import sys
import subprocess
import os
import platform
#
print("\n.... Running WARP3D (takes ~ 5 minutes)....")


# ------------------------------------------------------------
# User-defined thread counts for each OS
# ------------------------------------------------------------
macOS_threads  = 15
Linux_threads  = 12
# ------------------------------------------------------------
# Select correct WARP3D driver script and thread count
# ------------------------------------------------------------
system = platform.system()

if system == "Darwin":           # macOS
    warp3d_driver = "warp3d_script_macOS"
    thread_count = macOS_threads
elif system == "Linux":
    warp3d_driver = "warp3d_script_linux"
    thread_count = Linux_threads
else:
    print(f"Unsupported OS: {system}")
    sys.exit(1)

exe_path = os.path.join(os.environ["WARP3D_HOME"], warp3d_driver)

# ------------------------------------------------------------
# Run the first WARP3D job
# ------------------------------------------------------------
cmd1 = f"{exe_path} {thread_count} < warp3d.inp > output"

try:
    subprocess.run(cmd1, shell=True, check=True)
    print("\t.... First run finished.")
except subprocess.CalledProcessError:
    print("ERROR: First WARP3D run failed.")
    sys.exit(1)

#
print("\t.... WARP3D finished.")
print(".... Checking results ...")

filename = "output"
ref_str1 = "0.2203E+07"    # for the J-line (compare first 5 chars)

all_ok = True  # track whether all checks pass

try:
    with open(filename, "r") as f:

        # ------------------------------------------------------------
        # 1. Find: "loading: predisp      step:   200"
        # ------------------------------------------------------------
        for line in f:
            if "loading: predisp      step:   200" in line:
                break
        else:
            print('Did not find "loading: predisp      step:   200"')
            sys.exit(1)

        # ------------------------------------------------------------
        # 2. Find:  domain 0
        # ------------------------------------------------------------
        for line in f:
            if line.startswith("     0  "):
                parts = line.split()
                if len(parts) <= 10:
                    print("\t**** Line 'J            5' has fewer than 11 items.")
                    all_ok = False
                    break
#
                val1 = parts[9]
                print(f"\n\t.... J-value: {val1}")
                if val1[:7] == ref_str1[:7]:
                    print(f"\t.... Matches correct value: {ref_str1[:7]!r}")
                else:
                    print(f"\t**** No match to correct value. Got: {val1[:7]!r}")
                    all_ok = False
                break
        else:
            print('Did not find " 0 domain "')
            sys.exit(1)

except FileNotFoundError:
    print(f'File "{filename}" not found.')
    sys.exit(1)

# Final status
if all_ok:
    print("\n.... Results are correct. Done!")
else:
    print("\n**** One or more result checks FAILED.")
    sys.exit(2)
