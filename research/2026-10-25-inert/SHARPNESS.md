# The second split-prime lattice really occurs

The local upper bound of two lattices cannot be replaced by one uniformly
over these families. This statement concerns lattices, not sharpness of the
global point-count exponent.

For any positive integer m, put

\[
 B=4m^2(m^2+1),\quad
 P=(1,1+2m^2),\quad
 Q=(m^2,-m(m^2+2)).
\]

Both P and Q lie on y^2=x^3+B, by direct expansion. Moreover, with

\[
 g=\begin{pmatrix}1&1\\-3m&m\end{pmatrix},\qquad\det g=4m,
\]

one has the exact identity

\[
 (4m)^{-2} f_P(X-3mY,X+mY)
   =X^4-6m^2X^2Y^2-8m(m^2+2)XY^3-3m^4Y^4=f_Q(X,Y).
\]

If m=p^e with p>3 and e in {1,2}, this is a primitive integral matrix
of determinant valuation e, as well as the identity matrix of valuation 0.
Here n=m and d=4(m^2+1), which is nonsquare and satisfies (d/p)=1.
The two row lattices have different indices locally, so they are distinct.
The inverse transformation has primitive representative

\[
 \begin{pmatrix}m&-1\\3m&1\end{pmatrix}
\]

and also has determinant 4m. It provides the nonunit-x branch of the
classification, since x(Q)=m^2 and v_p(y(Q))=e.

For example, d=104 and n=5 give B=2600,
P=(1,51), Q=(25,-135), and g=((1,1),(-15,5)). For e=2, take d=2504,
n=25, B=1565000, P=(1,1251), Q=(625,-15675).

The parameter d varies in this construction. The examples do not show that
every split prime produces a second global lattice for any given fixed d,
nor that the factor 2^w is required in an optimal point-count bound.
