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

Since

.. math::

    \left(\Lambda^{-1}\right)^\nu_{\;\mu} =
    \begin{pmatrix}
    1 & 0 \\
    1 & 1
    \end{pmatrix}

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

Contra vs Covariant
-------------------

After arriving at Mount Eunostos, you decide to hike to the top. You'd like to
get there as quick as possible. Luckily you created an elevation map the day
before, :math:`h(x,y)`.

"The elevation of this mountain, :math:`h(x,y)` is pretty complicated, but
locally it just looks like this"

.. math::

    h(x,y) &\approx x + y

or, in tensor notation

.. math::

    h(x^\mu) &\approx x^0 + x^1

"Great! Let's calculate the path of steepest ascent from our current spot," your friend says.

.. math::

    \nabla h =
    \begin{pmatrix}
    \frac{\partial h}{\partial x} \\
    \frac{\partial h}{\partial y}
    \end{pmatrix}
    = \begin{pmatrix} 1 \\ 1 \end{pmatrix}

"Ok, cool, but I'd actually like to know the gradient in **my** coordinate
system. Don't worry, I know how to do it," your friend says.

.. math::

    \nabla h^\prime = \Lambda^\nu_{\;\mu} \nabla h^\mu =
    \begin{pmatrix}
    1 & 0 \\
    -1 & 1 \\
    \end{pmatrix}
    \begin{pmatrix} 1 \\ 1 \end{pmatrix} =
    \begin{pmatrix} 1 \\ 0 \end{pmatrix}

"Wrong," you say.

"Why am I wrong? The gradient of the elevation is a vector, and you showed me
how to transform vectors."

"The gradient of the elevation is a vector, but it is a **covariant** vector.
And covariant vectors don't transform in the same way."

"Wait, what?"

"There are two kinds of vectors, **contravariant** and **covariant**. You are
probably most familiar with **contravariant** vectors. These are the vectors
used in Newton's classic laws for example, and the types of vectors which
represent the location of objects. But, there are also **covariant** vectors
which look like a vector but don't transform in the same way. I think the right
way to think about it is this: when you describe something as a vector you are
describing some *real physical object* with a set of numbers. When you change
coordinate systems, and then look at the same *real* object in the different
coordinate system you will describe it using some other numbers. It turns out
that how you transform those numbers from one frame to the next *depends on the
physical object you are describing*. And, in this case, the gradient of a
scalar function doesn't transform like location vectors.

"So, how does it transform?"

"Let's see if we can figure it out. We know that the elevation is a scalar function and so we can describe it using your coordinates as follows:"

.. math::

    h(x^\prime,y^\prime) &= h(x^\mu) \\
    &= h\left(\left(\Lambda^{-1}\right)^\nu_{\;\mu} x^{\prime\mu}\right) \\
    &= h\left(\begin{pmatrix}1 & 0 \\ 1 & 1\end{pmatrix} \begin{pmatrix}x^\prime \\ y^\prime\end{pmatrix}\right) \\
    &= h\left(\begin{pmatrix}x^\prime \\ x^\prime + y^\prime\end{pmatrix}\right) \\
    &= 2 x^\prime + y^\prime

and therefore, you should have gotten

.. math::

    \nabla h^\prime = \begin{pmatrix}2 \\ 1\end{pmatrix}

We can work out the correct transformation law by looking at the gradient in
your coordinate system and expanding with the chain rule.

.. math::

    \nabla h^\prime &=
    \begin{pmatrix}
    \frac{\partial h^\prime}{\partial x^\prime} \\
    \frac{\partial h^\prime}{\partial y^\prime}
    \end{pmatrix} \\
    &=
    \begin{pmatrix}
    \frac{\partial h}{\partial x} \frac{\partial x}{\partial x^\prime} + 
    \frac{\partial h}{\partial y} \frac{\partial y}{\partial x^\prime} \\
    \frac{\partial h}{\partial y} \frac{\partial y}{\partial y^\prime} + 
    \frac{\partial h}{\partial x} \frac{\partial x}{\partial y^\prime} \\
    \end{pmatrix} \\
    &=
    \begin{pmatrix}
    \frac{\partial x}{\partial x^\prime} & \frac{\partial y}{\partial x^\prime} \\
    \frac{\partial x}{\partial y^\prime} & \frac{\partial y}{\partial y^\prime}
    \end{pmatrix}
    \begin{pmatrix}
    \frac{\partial h}{\partial x} \\
    \frac{\partial h}{\partial y}
    \end{pmatrix} \\
    &=
    \left(\Lambda^{-1}\right)^T \nabla h

"So, you see, instead of transforming with a factor of :math:`\Lambda`, this
type of vector transforms with a factor of :math:`\left(\Lambda^{-1}\right)^T`.
These types of vectors, *covariant vectors*, are written with a **subscript**
instead of a superscript like covariant vectors. So, we should write the
gradient of the elevation in tensor notation as :math:`\nabla h_\mu`. Let's double check that we get the right answer."

.. math::

    \nabla h^\prime_\nu &= \left(\Lambda^{-1}\right)^T \nabla h \\
    &= \left(\Lambda^{-1}\right)_\nu^{\;\mu} \nabla h_\mu \\
    &=
    \begin{pmatrix}
    1 & 1 \\
    0 & 1 \\
    \end{pmatrix}
    \begin{pmatrix}
    1 \\ 1
    \end{pmatrix} \\
    &= \begin{pmatrix} 2 \\ 1\end{pmatrix}

"Awesome! It all makes so much sense," your friend says.

And you hike up to the top of Mount Eunostos and enjoy the view!
