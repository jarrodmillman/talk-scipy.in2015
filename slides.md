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
\hfill \tiny Credit: \url{en.wikipedia.org/wiki/Marchant_calculator} \hspace{.6cm}

## History of statistical programming

\begin{columns}
    \begin{column}{0.60\textwidth}
       \vspace{4em}

       Once upon a time, statistical programming involved
       calling Fortan subroutines directly.
       \vspace{1em}

       S provided a common environment to interactively
       explore data.
    \end{column}
    \begin{column}{0.47\textwidth}
        \vspace{1cm}
        \begin{itemize}
            \item Fortan (1950s)
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
\column{.48\textwidth}

![](figs/monte_carlo.png)

\column{.52\textwidth}

~~~~~~~~Python
>>> x = 2*random(10**8) - 1
>>> y = 2*random(10**8) - 1
>>> length = sqrt(x**2 + y**2)
>>> in_circle = length <= 1
>>> 4 * in_circle.mean()
3.14152224
~~~~~~~~

\columnsend

## Deep learning

![](figs/deeplearning.png)

## Stat 133: Concepts in Computing with Data

![](figs/undergrad_v_stat133.png)

## Why Python?

- \textcolor{blue}{General} purpose language with \textcolor{blue}{batteries included}
- Popular for wide-range of \textcolor{blue}{scientific applications}
- Growing number of libraries \textcolor{blue}{statistical applications}
    - Pandas, sklearn, statmodels

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

## permute

![](figs/permute1.png)

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
$(1, 2, \dots, n)$
\begin{align*}
p(x_1, \dots, x_n) &= p(x_{\pi(1)}, \dots, x_{\pi(n)})
\end{align*}

## Exchangeability II

Exchangeability is closely related to the notion of \emph{independent and
identically-distributed} (iid) random variables.

- iid random variables are exchangeable.

- But, simple random \textcolor{blue}{sampling without replacement} produces an
  exchangeable, but \textbf{not} independent, sequence of random variables.

## Two sample problem

- \textcolor{blue}{Question} Does a given fertilizer increase the yield of a
  certain crop?

- \textcolor{blue}{Experiment} Apply the fertilizer to exactly half of the field.
  Measure crop yield in the two halves.

## Two sample (aside: experimental design)

To avoid confounding

- divide the field into small, equally-sized blocks
- 

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

## Collaborators

![](figs/collaborators.png)
