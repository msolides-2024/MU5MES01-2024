
# Basic tools
In this class we will use the following open-source numerical tools:

- `gmsh`: Advanced meshing tool (https://gmsh.info)

- `dolfinx`: the finite element library, see https://docs.fenicsproject.org/dolfinx/v0.6.0/python/api.html.

     FEniCSx is a popular open-source computing platform for solving partial differential equations (PDEs). FEniCSx enables users to quickly translate scientific models into efficient finite element code. With the high-level Python and C++ interfaces to FEniCSx, it is easy to get started, but FEniCSx offers also powerful capabilities for more experienced programmers. FEniCSx runs on a multitude of platforms ranging from laptops to high-performance clusters.

- `ufl` (Unified Form Language): https://fenics.readthedocs.io/projects/ufl/en/latest/manual/introduction.html

    The Unified Form Language is an embedded domain specific language
    for definition of variational forms intended for finite element
    discretization. More precisely, it defines a fixed interface for choosing
    finite element spaces and defining expressions for weak forms in a
    notation close to the mathematical one.

- `pyvista`:
    pyvista - PyVista package for 3D plotting and mesh analysis (https://docs.pyvista.org).

- `paraview`: ParaView is an open-source, multi-platform data analysis and visualization application (https://www.paraview.org).

You find below some useful online references classified by topic

# FEniCS
* Website https://fenicsproject.org
* Documentation
   1. First this tutorial, Chap 2 being the good starting point: https://jsdokken.com/dolfinx-tutorial/index.html
   2. https://docs.fenicsproject.org/dolfinx/v0.6.0/python/
   4. UFL: https://fenics.readthedocs.io/projects/ufl/en/latest/manual.html
   5. Source https://github.com/FEniCS/dolfinx
   6. Examples of application to solid mechanics: 
        - https://newfrac.github.io/fenicsx-fracture/
 
# Version control
* https://github.com/numerical-mooc/numerical-mooc/blob/master/lessons/00_getting_started/00_04_Intro_to_git.md
* https://git-scm.com/videos
* https://rogerdudler.github.io/git-guide/index.fr.html


# Python

## Getting started
* [**Python crash course**](http://nbviewer.ipython.org/github/barbagroup/AeroPython/blob/master/lessons/00_Lesson00_QuickPythonIntro.ipynb) by Lorena Barba
* http://nbviewer.jupyter.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-0-Scientific-Computing-with-Python.ipynb
* http://nbviewer.jupyter.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-1-Introduction-to-Python-Programming.ipynb
* http://cs231n.github.io/python-numpy-tutorial/

## About Jupyter notebook
* https://github.com/numerical-mooc/numerical-mooc/blob/master/lessons/00_getting_started/00_02_Installing_Jupyter.md
* https://github.com/numerical-mooc/numerical-mooc/blob/master/lessons/00_getting_started/00_03_Intro_to_Jupyter_notebook.md

## Further references
* https://scipy-lectures.github.io
* https://github.com/jrjohansson/scientific-python-lectures
* http://cs231n.github.io/python-numpy-tutorial/
* http://www.pefarrell.org/wp-content/uploads/2015/05/pythonfenics.pdf
* [**Scientific computing with python**](https://github.com/jrjohansson/scientific-python-lectures)
* [Matplotlib tutorial 1](http://matplotlib.org/users/pyplot_tutorial.html)
* [Matplotlib tutorial 2](http://www.loria.fr/~rougier/teaching/matplotlib/)
* [Defining Functions in Python](http://nbviewer.ipython.org/urls/bitbucket.org/cfdpython/cfd-python-class/raw/master/lessons/11%2520-%2520Defining%2520Function%2520in%2520Python.ipynb) by Lorena Barba
* [ipython](http://ipython.org/)
* [Python doc on the web](https://wiki.python.org/moin/BeginnersGuide/Programmers)
* [numpy](http://www.numpy.org/)
* [python codying style](http://www.python.org/dev/peps/pep-0008/)
* https://sahandsaba.com/thirty-python-language-features-and-tricks-you-may-not-know.html
* https://learnxinyminutes.com/docs/python3/
* http://jrjohansson.github.io/numericalpython.html

# FEM
I strongly suggest to read this book by Szabo and Babuska:
* https://classes.engineering.wustl.edu/2009/fall/mase5510 and in particular:
[Chapters_12.pdf](https://classes.engineering.wustl.edu/2009/fall/mase5510/Chapters_12.pdf),
[Chapters_3.pdf](https://classes.engineering.wustl.edu/2009/fall/mase5510/Chapter_3.pdf),
[Chapters_4.pdf](https://classes.engineering.wustl.edu/2009/fall/mase5510/Chapter_4.pdf),
[Chapters_5.pdf](https://classes.engineering.wustl.edu/2009/fall/mase5510/Chapter_5.pdf),
[Chapters_6.pdf](https://classes.engineering.wustl.edu/2009/fall/mase5510/Chapter_6.pdf),
[Chapters_78.pdf](https://classes.engineering.wustl.edu/2009/fall/mase5510/Chapters_78.pdf),
[AppendixAB.pdf](https://classes.engineering.wustl.edu/2009/fall/mase5510/Appendices_AB.pdf),
[AppendixC.pdf](https://classes.engineering.wustl.edu/2009/fall/mase5510/Appendix_C.pdf)

You can look also to
* http://antoinelegay.free.fr/Calcul_des_structures_par_elements_finis_Legay.pdf
* http://www.colorado.edu/engineering/cas/courses.d/NFEM.d/

This quite complete book by Peter Wriggers (Nonlinear finite element) is freely available in pdf form with your university account:
* https://link.springer.com/content/pdf/10.1007%2F978-3-540-71001-1.pdf

# Continuum mechanics and elasticity 
* [Continuum mechanics (1D) by J.J. Marigo Jean-Jacques Marigo](https://cel.archives-ouvertes.fr/cel-01023392)
* http://www.brown.edu/Departments/Engineering/Courses/En221/Notes/notes.html
* [Elasticity and fracture, Jean-Jacques Marigo](https://moodle.polytechnique.fr/pluginfile.php/30014/mod_resource/content/1/ElasticiteRupture.pdf)
* [Plasticity and fracture, Pierre Suquet](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwjdspXjqcfdAhXLA8AKHVHjBHIQFjAAegQIBxAC&url=http%3A%2F%2Fperso.ensta-paristech.fr%2F~mbonnet%2Fmec551%2Fmec551.pdf&usg=AOvVaw3JK3d0dJbSyeduYs3DCsqU)
* http://solidmechanics.org/ (e.g. http://solidmechanics.org/text/Chapter3_2/Chapter3_2.htm)

