#  Report 2 - Part II
*MU5MES01 - 2023/24 - C.Lestringant, D.Duhamel, S. Neukirch*

The key concepts introduced in the second part of the class are

- Introduction to nonlinear elasticity
- FEniCSx implementation of a non-linear elastic model
- Use of a Newton solver for the solution of nonlinear problems
- Solution of quasi-static rate-independent problems by load-stepping (progressive increment of a single loading parameter)
- Solution of (linear and nonlinear) dynamic problems
- Discussion of the issues arising in the numerical solutions of nonlinear systems: possible non-convergence, convergence to an unstable solution, need for the introduction of imperfections, etc…


Your report should summarize and present synthetically your work on these items using the classical example of snapping of a beam as a model problem. We give below some hints on how to write the report. Personal analyses and comments are particularly welcome. You are not obliged to follow the questions step by step, but you should include in your report the key concepts and results.


**Some suggestions:**

- Write concisely and effectively.
- Comment your results.
- The quality of the figures is important.
- Report only the minimal number of figures (of excellent quality) to effectively communicate your results.
- You can write in English or French.
- Use Latex for writing your report.
- In the written report you should correctly formulate each mathematical problem solved but you should not report all the details of the derivation of the formulation. You will be asked about that during the oral examination.

**Important informations:**
  - Deadline: **Wednesday 11 December 2024, 11pm**.
  - **The maximal length of the report is 4 pages (plus a title page).**
  - To submit your report:
      - An electronic version should be uploaded on [moodle](https://moodle-sciences-23.sorbonne-universite.fr/course/view.php?id=2359), it should include
          1. your report in pdf format named as `MES01-CR2-studentname1-studentname2.pdf` (file with a different naming scheme will not be accepted and evaluated).
          2. the code/files you used to obtain your results, namely the *.py and/or *.ipynb files.
  - We will evaluate the quality of the presentation (language, typesetting, and figures). Being able to effectively communicate your results is important for your future.
  - Consider the questions marked with (#) *only* if you are sufficiently advanced with the other questions; these questions are not required if you are aiming at marks < 12/20.

# Nonlinear snapping of a beam

This project aims at numerically studying the dynamics of the snapping instability of a beam and compare the finite element solutions with the experimental results detailed in [1] (the reference can be found in the github folder). We advise you to start by taking a look at the paper (you don't need to go through all the details).

In your simulations, you will consider a 2D  hyperelastic, rectangular beam (length: $L$, cross-section: $h$), clamped at both ends. We recommend you use a neo-Hookean hyperelastic model with rescaled Young's modulus $E=1$ and Poisson's ratio $\nu=0.25$.

## Part 0. Implicit Newmark solver

In order to study the dynamic response of the structure, you first need to implement an implicit Newmark solver for a nonlinear hyperelastic problem.

Start from the notebook `implicit_newmark_flexion_clamp_given_to_class.ipynb`. You need to fill-in the gaps in the notebook.

**Question 0.1:** Compute the transverse vibration frequency of the clamped-clamped 2D hyperelastic beam for $\Delta L=0$. How close is it from the prediction of 1D beam theory?

**Question 0.2(#):** How does this vibration frequency evolve with the amplitude of the load? (increase the transverse pre-load $f$) 

## Part 1. First loading step: axial buckling

See instructions in Part I.

## Part 2. Second loading step: quasi-static snap-through

See instructions in Part I.

## Part 3. Dynamic snap-through

We now compute the dynamic response of the structure when the transverse load $f$ is progressively decreased to negative values from $0$, starting from the solution `u_saved` obtained at the end of Part 1. In this part, you will make use of the dynamic Newmark solver that you implemented in Part 0.

**Question 3.1:** Which Dirichlet boundary conditions will you use in this part? 

**Question 3.2:** Implement a time-dependent transverse loading where you decrease $f$ from $0$ at constant speed `loading_speed` until it reaches the value `t_cutoff*loading_speed` at time `t_cutoff` using

```
def load_eval(t):
    if t <= t_cutoff:
        return -t*loading_speed
    else:
        return -t_cutoff*loading_speed
```
To get started with this part, you can set the loading parameters to
```
t_cutoff=10
loading_speed=0.005
```
Apply this loading scenario to the bucked structure (i.e. starting from the solution `u_saved` obtained in part 1, for $\Delta L=0.05$). Don't forget to initialize you loading loop by the solution `u_saved`. Choose a value of the time step `dt` so that your implicit solver converges. Try increasing this value: is the solver always converging?

**Question 3.3:** Plot the time evolution of the mid-point position $w(t)$ and compare it with the measurements shown in the figure 3 in [1].

**Question 3.4:**  Compare the dynamic response $w(f)$ with the quasi-static evolution computed in Part 2. Check that you obtain an identical response when the loading speed is sufficiently low.

**Question 3.5 (#):** Plot the shape of the deformed beam during snap-through when the midpoint of the beam is on the same horizontal line as the two ends, i.e. when $w(t)=0$. Is it symmetric or asymmetric? Compare with the prediction in [1].

**Question 3.6 (#):** Try increasing the value of $\Delta L$ (typically to $\Delta L=0.08$). How does the dynamic response vary? Does the solver always converge?

**Question 3.7 (#):** At the end of the snapping dynamics, the system vibrates. What are these vibrations? Measure the vibration frequency, and compare it with (i) the value obtained in Part 0 and (ii) the value found in [1]. 

## References

[1] Dynamics of snapping beams and jumping poppers, Pandey, A., Moulton, D. E., Vella, D. and Holmes, D. P., Europhysics Letters 105 (2014)



<!-- Local Variables: -->
<!-- fill-column: 80 -->
<!-- End: -->
