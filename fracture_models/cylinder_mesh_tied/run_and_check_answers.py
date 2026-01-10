#!/usr/bin/env python3
import sys
import subprocess
import os
import platform
#
print("\n.... Running WARP3D (takes < 1 minute)....")
#
# ------------------------------------------------------------
# User-defined thread counts for each OS
# ------------------------------------------------------------
macOS_threads  = 15
Linux_threads  = 12
# ------------------------------------------------------------
# Select correct WARP3D driver script and thread count
# ------------------------------------------------------------
system = platform.system()
#
if system == "Darwin":           # macOS
    warp3d_driver = "warp3d_script_macOS"
    thread_count = macOS_threads
elif system == "Linux":
    warp3d_driver = "warp3d_script_linux"
    thread_count = Linux_threads
else:
    print(f"Unsupported OS: {system}")
    sys.exit(1)
#
exe_path = os.path.join(os.environ["WARP3D_HOME"], warp3d_driver)
# ------------------------------------------------------------
# Run: warp3d_script_macOS 5 < warp3d.inp > output_first
# ------------------------------------------------------------
cmd1 = f"{exe_path} {thread_count} < warp3d.inp > output_first"
result1 = subprocess.run(cmd1, shell=True)
if result1.returncode != 0:
    print("ERROR: First WARP3D run failed.")
    sys.exit(1)
#
print("\t.... First run finished.")
#
# ------------------------------------------------------------
# Run: warp3d_script_macOS 5 < warp3d_restart.inp > output
# ------------------------------------------------------------
cmd2 = f"{exe_path} {thread_count} < warp3d_restart.inp > output"
result2 = subprocess.run(cmd2, shell=True)
if result2.returncode != 0:
    print("ERROR: Restart WARP3D run failed.")
    sys.exit(1)
#
print("\t.... Restart run finished.")
print(".... Checking results after running restart...")
#
filename = "output"
ref_str1 = "0.3379E+01"    # for the J-line (compare first 5 chars)
ref_str2 = "0.5198E-01"    # for the I_T13-line (compare first 5 chars)
#
all_ok = True  # track whether all checks pass
#
try:
    with open(filename, "r") as f:

        # ------------------------------------------------------------
        # 1. Find:  domain id: J33
        # ------------------------------------------------------------
        for line in f:
            if line.startswith(" domain id: J33"):
                break
        else:
            print('Did not find "domain id: J33"')
            sys.exit(1)

        # ------------------------------------------------------------
        # 2. Find:  J            5
        # ------------------------------------------------------------
        for line in f:
            if line.startswith(" J            5 "):
                parts = line.split()
                if len(parts) <= 10:
                    print("\t**** Line 'J            5' has fewer than 11 items.")
                    all_ok = False
                    break

                val1 = parts[10]
                print(f"\n\t.... J-value: {val1}")
                if val1[:5] == ref_str1[:5]:
                    print(f"\t.... Matches correct value: {ref_str1[:5]!r}")
                else:
                    print(f"\t**** No match to correct value. Got: {val1[:5]!r}")
                    all_ok = False
                break
        else:
            print('Did not find " J            5 "')
            sys.exit(1)

        # ------------------------------------------------------------
        # 3. Continue reading; find:  I_T13        5
        # ------------------------------------------------------------
        for line in f:
            if line.startswith(" I_T13        5"):
                parts = line.split()
                if len(parts) <= 10:
                    print("\t**** Line 'I_T13        5' has fewer than 11 items.")
                    all_ok = False
                    break

                val2 = parts[10]
                print(f"\n\t.... I_T13-value: {val2}")
                if val2[:5] == ref_str2[:5]:
                    print(f"\t.... Matches correct value: {ref_str2[:5]!r}")
                else:
                    print(f"\t**** No match to correct value. Got {val2[:5]!r}")
                    all_ok = False
                break
        else:
            print('Did not find " I_T13        5"')
            sys.exit(1)

except FileNotFoundError:
    print(f'File "{filename}" not found.')
    sys.exit(1)

# Final status
if all_ok:
    print("\n.... Results are correct. Done!")
    cleanup_files = [
      "wnfd0000002",
      "cylinder.db",
      "output_first",
      "output",
      "energy",
      "model.text",
      "wnd0000002_text",
      "wes0000002_text" ]
    for fname in cleanup_files:
       try:
        if os.path.exists(fname):
            os.remove(fname)
       except Exception:
        pass  
    sys.exit(0)
else:
    print("\n**** One or more result checks FAILED.")
    sys.exit(2)
