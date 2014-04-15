A Trip to Mars
==============

Introduction
------------

You and a friend just landed on Mars and are responsible for mapping out the
area so that engineers back on Earth can design a new city there. After being
dropped off, you both decide that it would be easiest for you to split up and
record the locations of major landmarks separately and then put together a
complete map.

.. tikz::

    \centering
    \node[anchor=south west, inner sep=0] (image) at (0,0) {\includegraphics[width=10cm]{/home/tlatorre/Documents/phy237/tensor/mars.png}};
    \draw[step=1cm,gray,very thin] (0,0) grid (10,10);
    \foreach \i in {0,...,10}
    {
        \draw[dashed] (0,\i) -- (10-\i,10);
        \draw[dashed] (\i,0) -- (10,10-\i);
    }
    \draw[->,very thick] (0,0) -- (1,0);
    \draw[->,very thick] (0,0) -- (0,1);
    \draw[->,very thick,dashed] (1,1) -- (2,2);
    \draw[->,very thick,dashed] (1,1) -- (1,2);
    \tikzstyle{every node}=[font=\footnotesize\bfseries];
    \draw[very thick] (5,5) node[right] {Arsia Mons Mosaic};
    \draw[very thick] (7.5,7.5) node[right] {Ascraeus Mons};
    \draw (3,9) node[above] {Mount Eunostos};
    \draw (0.5,7) node[right] {Amazonis Planitia};

You decide to use an orthonormal system (shown as solid arrows), while your
friend decides the landscape is more naturally suited to his choice (the dashed
arrows). You agree on a common origin at the bottom left hand of the image and
begin surveying the land.

After a week, your table looks like this:

.. table:: Your Table

    =================                ===   ====
    Landmark                          x     y
    =================                ===   ====
    Arsia Mons Mosaic                 5     5
    Ascraeus Mons                     7     7.5
    =================                ===   ====

and your friend's table looks like this:

.. table:: Friend's Table

    =================                ====   ====
    Landmark                          x'     y'
    =================                ====   ====
    Amazonis Planitia                0.5    6
    Mount Eunostos                    3     6
    =================                ====   ====

Coordinate Transform
--------------------

You decide it would be best to put all the information in a single table, and
your friend is convinced that his coordinate system is the best, so you give in
and decide to work in his units. You tell him that transforming coordinates is
easy: you know that a vector :math:`\begin{pmatrix}1 \\ 0\end{pmatrix}` in your
coordinate system is equal to the vector :math:`\begin{pmatrix}1 \\
-1\end{pmatrix}` in his coordinate system and that you both have the same
:math:`y` coordinates, so evidently the transformation matrix must be

.. math::

    \Lambda^\nu_{\;\mu} = \begin{pmatrix}1 & 0 \\-1 & 1\end{pmatrix}

so that you can transform coordinates as

.. math::

    x^{\prime\nu} = \Lambda^\nu_{\;\mu} x^\mu

And you compile the complete table

.. table:: Complete Table (Friend's Coordinates)

    =================                ===   ====
    Landmark                          x'     y'
    =================                ===   ====
    Arsia Mons Mosaic                 5     0
    Ascraeus Mons                     7     0.5
    Amazonis Planitia                0.5    6
    Mount Eunostos                    3     6
    =================                ===   ====

The Metric
----------

The next day you both feel pretty good about a job well done and decide to go
hiking to Mount Eunostos. You want to figure out how long it will take, and so
your friend says "No problem, I'll calculate the distance"

.. math::

    \left|x^\mu\right| &= \sqrt{x^{\prime\mu} x^{\prime\mu}} \\
    &= \sqrt{3^2 + 6^2} \\
    &= 6.7

"Woah, hold on there a minute, You aren't using an
orthonormal basis, you can't calculate like that. I took the liberty of making
the complete table in my coordinate system last night."

.. table:: Complete Table (Your Coordinates)

    =================                ===   ====   ====
    Landmark                          x      y     d
    =================                ===   ====   ====
    Arsia Mons Mosaic                 5     5     7.1
    Ascraeus Mons                     7     7.5   10.2
    Amazonis Planitia                0.5    6.5   6.5
    Mount Eunostos                    3     9     9.5
    =================                ===   ====   ====

"You see, the correct distance is 9.5," you say.

"But why was I wrong?"

"Let me show you. First, we'll start with the distance in my coordinate system,
and then switch to your coordinate system."

.. math::

    d^2 &= x^\mu x^\mu \\
    d^2 &= \left(\left(\Lambda^{-1}\right)^\nu_{\;\mu} x^{\prime\mu}\right)
           \left(\left(\Lambda^{-1}\right)^\nu_{\;\alpha}
    x^{\prime\alpha}\right) \\
    d^2 &= \left(\Lambda^{-1}\right)^\nu_{\;\mu}
           \left(\Lambda^{-1}\right)^\nu_{\;\alpha} x^{\prime\mu} x^{\prime\alpha} \\
    d^2 &= g^\prime_{\mu\alpha} x^{\prime\mu} x^{\prime\alpha}

"What is that :math:`g_{\mu\alpha}`?"

"That's the metric. It tells you how to properly measure distances in your
coordinate system."

"What do you mean by proper?"

"I mean it tells you how to compute distances which everyone **regardless of
their coordinate system** can agree on."

"So, to calculate distances in your coordinate system, we need to compute the metric."

.. math::

    g^\prime_{\mu\alpha} &= \left(\Lambda^{-1}\right)^\nu_{\;\mu}
                            \left(\Lambda^{-1}\right)^\nu_{\;\alpha} \\
    &= \sum_\nu \left(\Lambda^{-1}\right)^\nu_{\;\mu}
                \left(\Lambda^{-1}\right)^\nu_{\;\alpha} \\
    &= \left(\Lambda^{-1}\right)^0_{\;\mu} \left(\Lambda^{-1}\right)^0_{\;\alpha} +
       \left(\Lambda^{-1}\right)^1_{\;\mu} \left(\Lambda^{-1}\right)^1_{\;\alpha} \\
    &= \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}

"So, to compute the distance to Mount Eunostos in your coordinate system:"

.. math::

    d^2 &= g^\prime_{\mu\alpha} x^\mu x^\alpha \\
    &= x^\mu \left(g^\prime_{\mu\alpha} x^\alpha\right) \\
    &= \begin{pmatrix}3 & 6\end{pmatrix} \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix}3 \\ 6\end{pmatrix} \\
    &= \begin{pmatrix}3 & 6\end{pmatrix} \begin{pmatrix}12 \\ 9\end{pmatrix} \\
    &= 90

"Therefore, the distance is :math:`\sqrt{90} = 9.5`."

"How come you don't need a metric in your coordinate system," your friend says.

"Well, technically I am using a metric, it's just that the metric in my
orthonormal basis is just equal to the identity :math:`\delta_{\mu\alpha}`. In fact, in special relativity you **have** to use a metric to define useful invariant scalars. It's called the Minkowski metric and is equal to"

.. math::

    g_{\mu\nu} &= 
    \begin{pmatrix}
    1 &    &    &    \\
      & -1 &    &    \\
      &    & -1 &    \\
      &    &    & -1 \\
    \end{pmatrix}
