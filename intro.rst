Index Notation
==============

Before working with tensors, it is helpful to introduce a new notation for
working with the standard vectors and matrices familiar in linear algebra. In
linear algebra, and multivariable calculus operations with vectors and matrices
are typically expressed by some symbol where the operation is *implied*. For
example, the dot product between two vectors :math:`a` and :math:`b` is
expressed as

.. math::

    \mathbf{a} \cdot \mathbf{b}

Where the actual operation of dotting the vectors is implied. In the new index
notation, the operation will be described explicitly in terms of the components
of each vector. In the case of the dot product, then we will write

.. math::

    \mathbf{a} \cdot \mathbf{b} = \sum_i a_i b_i

where :math:`a_i` is the :math:`i\mathrm{th}` element of a.

Similarly, whereas in linear algebra one would write the operation of a matrix
:math:`A` on a vector :math:`\mathbf{v}`, :math:`\mathbf{u} = A\mathbf{v}` as

.. math::

    \begin{pmatrix} u_1 \\ u_2 \\ \vdots \end{pmatrix} =
    \begin{pmatrix}
        a_{11} & a_{12} & \cdots & a_{1n} \\
        a_{21} & a_{22} & \cdots & a_{2n} \\
        \vdots & \vdots & \ddots & \vdots \\
    \end{pmatrix}
    \begin{pmatrix} v_1 \\ v_2 \\ \vdots \end{pmatrix}

In the index notation, this operation is expressed as

.. math::

    u_i = \sum_j A_{ij} v_j
