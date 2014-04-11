Index Notation
==============

Introduction
------------

Before working with tensors, it is helpful to introduce a new notation for
working with the standard vectors and matrices familiar in linear algebra. In
linear algebra, and multivariable calculus operations with vectors and matrices
are typically expressed by some symbol where the operation is *implied*. For
example, the dot product between two vectors :math:`u` and :math:`v` is
expressed as

.. math::

    \mathbf{u} \cdot \mathbf{v} =
    \begin{pmatrix} u_1 & u_2 & \cdots \end{pmatrix}
    \begin{pmatrix} v_1 \\ v_2 \\ \vdots \end{pmatrix}

Where the actual operation of dotting the vectors is implied. In the new index
notation, the operation will be described explicitly in terms of the components
of each vector. In the case of the dot product, then we will write

.. math::

    \mathbf{u} \cdot \mathbf{v} = \sum_i u_i v_i

where :math:`a_i` is the :math:`i\mathrm{th}` element of a.

Similarly, whereas in linear algebra one would write the operation of a matrix
:math:`A` on a vector :math:`\mathbf{w}`, :math:`\mathbf{w} = M\mathbf{v}` as

.. math::

    \begin{pmatrix} w_1 \\ w_2 \\ \vdots \end{pmatrix} =
    \begin{pmatrix}
        a_{11} & a_{12} & \cdots & a_{1n} \\
        a_{21} & a_{22} & \cdots & a_{2n} \\
        \vdots & \vdots & \ddots & \vdots \\
    \end{pmatrix}
    \begin{pmatrix} v_1 \\ v_2 \\ \vdots \end{pmatrix}

In the index notation, this operation is expressed as

.. math::

    w_i = \sum_j a_{ij} v_j

which can be read as "the :math:`i\mathrm{th}` element of :math:`b` is equal to
the dot product of :math:`a` with the :math:`i\mathrm{th}` row of :math:`M`."

One nice thing about the new notation is that since everything is written in
terms of components, which are just numbers, everything commutes. For example,
the product of two matrices :math:`A` and :math:`B` is written in index notation
as

.. math::

    c_{ij} &= \sum_k a_{ik} b_{kj} &= \sum_k b_{kj} a_{ik}

.. note::
    Of course, the fundamental composition of transformations which :math:`AB`
    represents still does not commute in general, i.e.

    .. math::

        \sum_k a_{ik} b_{kj} &\neq \sum_k a_{kj} b_{ik}

Einstein Convention
-------------------

If you look back, you'll notice that in every case where we have a repeated
index in a product, there is always a sum over that index. The Einstein
convention is to just drop writing the sum explicitly, and assume that every
time a repeated index appears in a product, the sum is *implied*, i.e. we can
write

.. math::

    c &= \mathbf{u} \cdot \mathbf{v} \qquad &\Leftrightarrow \qquad c &= u_i v_i \\
    w &= A \mathbf{v}                \qquad &\Leftrightarrow \qquad w_i &= a_{ij} v_j \\
    C &= A B                         \qquad &\Leftrightarrow \qquad c_{ij} &= a_{ik} b_{kj}


