---
title: Python for Statisticians
subtitle: (\texttt{permute}---Permutation tests and confidence sets for Python)
author:  K. Jarrod Millman \newline
   \small Division of Biostatistics \newline
   \small University of California, Berkeley
date: \small SciPy India 2015 \newline
   \footnotesize IIT Bombay
   \vspace{.4cm}
   \vspace{.4cm}
   \tiny \url{http://www.jarrodmillman.com/talks/scipyindia2015/python_for_statisticians.pdf}
...

---

\begin{columns}
    \begin{column}{0.50\textwidth}
       \begin{figure}
          \includegraphics{figs/pfse.pdf}
       \end{figure}
    \end{column}
    \begin{column}{0.50\textwidth}
        Python for Statisticians
        \begin{itemize}
            \item Statistical computing
            \item Permutation testing
        \end{itemize}
    \end{column}
\end{columns}

# Statistical computing landscape

## History of statistical computing (at Berkeley)

\begin{columns}
    \begin{column}{0.38\textwidth}
        \begin{itemize}
            \item Census data
            \item Bombing research (WWII)
            \item DEC PDP-11/45 (1974)
        \end{itemize}
    \end{column}
    \begin{column}{0.58\textwidth}
       \begin{figure}
          \includegraphics{figs/563px-Marchant_SilentSpeed-8D.png}
       \end{figure}
    \end{column}
\end{columns}
\hfill \tiny Credit: \url{en.wikipedia.org/wiki/Marchant_calculator}

## History of statistical programming

\begin{columns}
    \begin{column}{0.60\textwidth}
       \vspace{4em}

       Once upon a time, statistical programming involved
       calling Fortran subroutines directly.
       \vspace{1em}

       S provided a common environment to interactively
       explore data.
    \end{column}
    \begin{column}{0.47\textwidth}
        \vspace{1cm}
        \begin{itemize}
            \item Fortran (1950s)
            \item APL (1960s)
            \item S (1970s)
            \item R (1990s)
            \item Python (1990s)
        \end{itemize}
    \end{column}
\end{columns}
\begin{columns}
    \begin{column}{0.30\textwidth}
    \end{column}
    \begin{column}{0.67\textwidth}
        \begin{figure}
           \includegraphics{figs/410px-APL-keybd2.svg.png}
        \end{figure}
    \end{column}
\end{columns}
\hfill \tiny Credit: en.wikipedia.org/wiki/APL_(programming_language)

## Monte Carlo

```python
>>> from numpy import sqrt
>>> from numpy.random import random
```
\columnsbegin
\column{.45\textwidth}

![](figs/monte_carlo2.png)

\column{.55\textwidth}

~~~~~~~~Python
>>> x = 2*random(10**8) - 1
>>> y = 2*random(10**8) - 1
>>> length = sqrt(x**2 + y**2)
>>> in_circle = length <= 1
>>> 4 * in_circle.mean()
3.14152224
~~~~~~~~

\columnsend

## Resampling

- Bootstrap
- Permutation tests

## Deep learning

![](figs/deeplearning.png)

\hfill \url{arxiv.org/abs/1506.00619}

## Stat 133: Concepts in Computing with Data

![](figs/undergrad_v_stat133.png)

## Why Python?

- \textcolor{blue}{General} purpose language with \textcolor{blue}{batteries included}
- Popular for wide-range of \textcolor{blue}{scientific applications}
- Growing number of libraries \textcolor{blue}{statistical applications}
    - \href{http://pandas.pydata.org/}{\texttt{pandas}}, \href{http://scikit-learn.org/}{\texttt{scikit-learn}}, \href{http://statsmodels.sourceforge.net/}{\texttt{statsmodels}}

## Stat 94: Foundations of Data Science


![](figs/data-rgarner.jpg)
\hfill \tiny Credit: \url{www.dailycal.org/2015/09/02/uc-berkeley-piloting-new-data-science-class-fall}

## \url{data8.org}

![](figs/data8.png)

## More Python in the statistics curriculum

- Stat 159/259: Reproducible and Collaborative Statistical Data Science
- Stat 222: Masters of Statistics Capstone Project
- Stat 243: Introduction to Statistical Computing


# Permutation testing

---

Permutation tests (sometimes referred to as randomization, re-randomization, or
exact tests) are a \textcolor{blue}{nonparametric approach to statistical
significance testing}.

---

- Permutation tests were developed to test hypotheses for which relabeling the
  observed data was justified by \emph{exchangeability} of the observed random
  variables.

- In these situations, the \textcolor{blue}{conditional distribution of the test
  statistic under the null hypothesis} is completely determined by the fact that
  all relabelings of the data are equally likely.

## Exchangeability

A sequence $X_1, X_2, X_3, \dots, X_n$ of random
variables is \textcolor{blue}{exchangeable} if their joint distribution is invariant to
permutations of the indices; that is, for all permutations $\pi$ of
$1, 2, \dots, n$
\begin{align*}
p(x_1, \dots, x_n) &= p(x_{\pi(1)}, \dots, x_{\pi(n)})
\end{align*}

## Exchangeability II

Exchangeability is closely related to the notion of \emph{independent and
identically-distributed} (iid) random variables.

- iid random variables are exchangeable.

- But, simple random \textcolor{blue}{sampling without replacement} produces an
  exchangeable, but \textbf{not} independent, sequence of random variables.

## Effect of treatment in a randomized controlled experiment \small \url{www.stat.berkeley.edu/~stark/Teach/S240/Notes/lec1.pdf}

11 pairs of rats, each pair from the same litter.

\vfill

Randomly---by coin tosses---put one of each pair into
"enriched" environment; other sib gets "normal" environment.

\vfill

After 65 days, measure cortical mass (mg).

\vfill

\footnotesize \begin{tabular}{lrrrrrrrrrrr}
treatment & 689& 656& 668& 660& 679& 663& 664& 647& 694& 633& 653 \cr
control & 657& 623& 652& 654& 658& 646& 600& 640& 605& 635& 642 \cr
\hline
difference & 32&  33&  16&   6&  21&  17&  64&   7&  89&  -2&  11
\end{tabular}

\vfill

\textcolor{green}{How should we analyze the data?}

## Informal Hypotheses \small \url{www.stat.berkeley.edu/~stark/Teach/S240/Notes/lec1.pdf}

\textcolor{blue}{Null hypothesis:} treatment has "no effect."

\vspace{.5cm}

\textcolor{blue}{Alternative hypothesis:} treatment increases cortical mass.

\vspace{1cm}

Suggests 1-sided test for an increase.

## Test contenders \small \url{www.stat.berkeley.edu/~stark/Teach/S240/Notes/lec1.pdf}

\begin{itemize}
        \item 2-sample Student $t$-test:
              $$ 
              \frac{\mbox{mean(treatment) - mean(control)}}
                   {\mbox{pooled estimate of SD of difference of means}}
              $$
        \item 1-sample Student $t$-test on the differences:
              $$
              \frac{\mbox{mean(differences)}}{\mbox{SD(differences)}/\sqrt{11}}
              $$
              Better, since littermates are presumably more homogeneous.
        \item Permutation test using $t$-statistic of differences:
              same statistic, different way to calculate $P$-value.
              Even better?
\end{itemize}

## Strong null hypothesis \small \url{www.stat.berkeley.edu/~stark/Teach/S240/Notes/lec1.pdf}

\textcolor{blue}{Treatment has no effect whatsoever---as if cortical mass were
assigned to each rat before the randomization.}

\vfill

Then equally likely that the rat with the heavier cortex will be assigned
to treatment or to control, independently across littermate pairs.

\vfill

Gives $2^{11} = 2,048$ equally likely possibilities:

\small \begin{tabular}{lrrrrrrrrrrr}
difference & $\pm$32& $\pm$33& $\pm$16& $\pm$6& $\pm$21& $\pm$17&
             $\pm$64& $\pm$7& $\pm$89& $\pm$2& $\pm$11
\end{tabular}

\vfill

For example, just as likely to observe original differences as

\small \begin{tabular}{lrrrrrrrrrrr}
        difference & -32& -33& -16& -6& -21& -17& -64& -7& -89& -2& -11
\end{tabular}

## Weak null hypothesis \small \url{www.stat.berkeley.edu/~stark/Teach/S240/Notes/lec1.pdf}

\textcolor{blue}{On average across pairs, treatment makes no difference.}

## Alternatives \small \url{www.stat.berkeley.edu/~stark/Teach/S240/Notes/lec1.pdf}

\textcolor{blue}{Individual's response depends only on that individual's assignment}

\vfill

Special cases: shift, scale, etc.

\vfill

\textcolor{blue}{Interactions/Interference: my response could depend on whether you are assigned to treatment or control.}


## Assumptions of the tests \small \url{www.stat.berkeley.edu/~stark/Teach/S240/Notes/lec1.pdf}

\begin{itemize}
        \item 2-sample $t$-test:
              \textcolor{blue}{masses are iid sample from normal distribution,
              same unknown variance, same unknown mean.}
              Tests weak null hypothesis (plus normality, independence, non-interference, etc.).
        \item 1-sample $t$-test on the differences:
              \textcolor{blue}{mass differences are iid sample from normal
              distribution, unknown variance, zero mean.}
              Tests weak null hypothesis (plus normality, independence, non-interference, etc.)
        \item Permutation test:
              \textcolor{blue}{Randomization fair, independent across pairs.}
              Tests strong null hypothesis.
\end{itemize}
Assumptions of the permutation test are true by design: That's how treatment
was assigned.

## Student $t$-test calculations \small \url{www.stat.berkeley.edu/~stark/Teach/S240/Notes/lec1.pdf}

Mean of differences:  26.73mg

Sample SD of differences:  27.33mg

$t$-statistic: $26.73/(27.33/\sqrt{11}) = 3.244$

$P$-value for 1-sided $t$-test:  0.0044

\vfill

\textcolor{blue}{Why do cortical weights have normal distribution?}

\vfill

\textcolor{blue}{Why is variance of the difference between treatment and control
the same for different litters?}

\vfill

\textcolor{blue}{Treatment and control are {\em dependent\/} because assigning
a rat to treatment excludes it from the control group, and vice versa.}

\vfill

\textcolor{blue}{Does $P$-value depend on assuming differences
are iid sample from a normal distribution?  If we reject the null, is that because
there is a treatment effect, or because the other assumptions are wrong?}

## Permutation $t$-test calculations \small \url{www.stat.berkeley.edu/~stark/Teach/S240/Notes/lec1.pdf}

Could enumerate all $2^{11} = 2,048$ equally likely possibilities.
Calculate $t$-statistic for each.

$P$-value is
$$
        P = \frac{\mbox{number of possibilities with $t \ge 3.244$}}{\mbox{2,048}}
$$
(For mean instead of $t$, would be $2/2,048 =  0.00098$.)

\vfill

For more pairs, impractical to enumerate, but can simulate:

\vfill

Assign a random sign to each difference.
Compute $t$-statistic
Repeat 100,000 times
$$
        P \approx \frac{\mbox{number of simulations with $t \ge 3.244$}}{\mbox{100,000}}
$$

## Compute

```python
from itertools import product
from numpy import array, sqrt

t = [689, 656, 668, 660, 679, 663, 664, 647, 694, 633, 653]
c = [657, 623, 652, 654, 658, 646, 600, 640, 605, 635, 642]
d = array(t) - array(c)
n = len(d)

x = array(list(product([1, -1], repeat=11)))
exact = x * d
dist = exact.mean(axis=1) / (exact.std(axis=1) / sqrt(n))
```

## Simulate ($n \gg 11$) 

```python
from numpy import array, sqrt
from numpy.random import binomial as binom

t = [689, 656, 668, 660, 679, 663, 664, 647, ...]
c = [657, 623, 652, 654, 658, 646, 600, 640, ...]
d = array(t) - array(c)
n = len(d)

reps = 100000
x = 1 - 2 * binom(1, .5, n*reps)
x.shape = (reps, n)
sim = x * d
dist = sim.mean(axis=1) / (sim.std(axis=1) / sqrt(n))
```

## Compare

```python
>>> from numpy import mean
>>> observed_ts = d.mean() / (d.std() / sqrt(n))
>>> mean(dist >= observed_ts)
0.0009765625
```

(versus 0.0044 for 1-sided $t$-test)

## Visualize

```python
import matplotlib.pyplot as plt
from numpy import linspace
from scipy.stats import t

plt.hist(dist, 100, histtype='bar', normed=True)
plt.axvline(observed_ts, color='red')
df = n - 1
x = linspace(t.ppf(0.0001, df), t.ppf(0.9999, df), 100)
plt.plot(x, t.pdf(x, df), lw=2, alpha=0.6)
plt.show()
```

## Visualize

![](figs/one_sample_1.png)

## \href{https://github.com/statlab/permute}{\texttt{permute}}

![](figs/permute1.png)

## Collaborators

![](figs/collaborators.png)
