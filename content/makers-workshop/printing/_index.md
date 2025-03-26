+++
title = "3D Print a Personalised Cushion"
weight = 4
+++

## OpenCushion
OpenCushion is a project that allows users to customise and 3D print wheelchair cushions using flexible materials, with the aim of evenly distributing pressure and minimising discomfort and the risk of pressure sores. The design is essentially a lattice of varying density, with areas that are subject to high pressure using a lower density lattice and vice versa. As these cushions can be made with most standard consumer-level 3D printers, they can be more affordable as well as geographically and financially accessible.

## 3D Printing
Compared to purchasing a cushion from a shop, 3D printing one is probably outside of most people's comfort zone. Though it's easier than ever to access a 3D printer, with many hobbyists owning one and printers generally available in most makerspaces, the process may still seem daunting for inexperienced makers or anyone not quite confident enough to troubleshoot or resolve any issues. For this reason, we are asking participants to configure and begin a print of their personalised 3D printed cushion.

I have come up with three ways in which we can create personalised cushions:
1. Using Python and a library called FullControl we can turn a pressure map into a 3D printable cushion model. This doesn't require and CAD or slicer software typically used in 3D printing.
2. Using slicer software we slice a 3D model of a cushion, with only the lattice (infill) structure. Using Python and the pressure map we then personalise the density of the previously generated GCODE.
3. For users without access to a pressure map, a third way of creating a cushion, involves using a feature of modern slicing software and SVG drawings of pressure maps. This is the method you will be focusing on in the workshop, proceed to the task page to learn more.