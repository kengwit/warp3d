
README
------

Documents, examples and Python script to support
analyzing Representative Volume Element (RVE) models often
used to study micro-mechanical material behavior.

3D_PBCs_Rect_Prism (pptx, PDF)
-------------------------------
 
Recommend reading this document first. 
 
Theoretical basis and practical implementation of periodic displacement 
boundary conditions for three-dimensional representative volume element 
(RVE) finite-element models. Implementation details for WARP3D. 

Shows classical homogenization framework with total
displacement field decomposed into a macroscopic strain-driven part and 
a periodic fluctuation. Slides derive the resulting multi-point constraint 
(MPC) equations required to enforce periodicity on rectangular prism RVEs 
with paired boundary nodes. Discusses homogeneous and inhomogeneous MPCs 
and WARP3D’s requirement that all MPC equations be homogeneous. 
Motivates the use of dummy nodes connected by stiff link elements 
to represent nonzero macroscopic strain terms. 

A fully worked verification example demonstrates suppression 
of rigid-body modes, construction and reduction of MPCs, and consistency 
of the computed strain field across the RVE. 

Appendix_L.pdf
--------------

Extracted appendix from WARP3D User Manual for periodic
boundary conditions.

manual.pdf
----------
 
Describes use of the Python script rpc_mpc_generator.py to
create a ready-to-use file of constraints in WARP3D format to model
rectangular prism RVEs.

rpc_mpc_generator.py
--------------------

Tested on Python 3.11. Imports standard Python packages.
Example input file: input_to_Python_script_example_problem.inp

warp3d.inp, coords_incid.inp, rve_generated_constraints.inp
------------------------------------------------------------

Input file for the 8-element rectangular prism model. warp3d.inp
includes the coords_incid.inp and rve_generated_constraints.inp files.
warp3d.inp is ready-to-run.

manual directory
----------------

LaTeX file (manual.tex) and figures for the manual.pdf
