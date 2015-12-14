---
title: Python for Statisticians
author:  K. Jarrod Millman \newline
   \small Division of Biostatistics \newline
   \small University of California, Berkeley
date: \small SciPy India 2015 \newline
   \footnotesize IIT Bombay
...

---

\begin{columns}
    \begin{column}{0.58\textwidth}
       \begin{figure}
          \includegraphics{figs/pfse.pdf}
       \end{figure}
    \end{column}
    \begin{column}{0.38\textwidth}
        Python for Statisticians
        \begin{itemize}
            \item Statistical computing landscape
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

## History of statistical programming

\begin{columns}
    \begin{column}{0.58\textwidth}
       Once upon a time, statistical programming involved
       calling Fortan subroutines directly.
       \vspace{1em}

       S provided a common environment to interactively
       explore data.
       \vspace{1em}

       R is now widely used by statisticians and data scientists.
    \end{column}
    \begin{column}{0.38\textwidth}
        \begin{itemize}
            \item Fortan (1950s)
            \item APL (1960s)
            \item S (1970s)
            \item R (1990s)
        \end{itemize}
    \end{column}
\end{columns}

## Computationally intensive statistical methods

- Resampling methods: bootstrap, permutation methods
- Markov Chain Monte Carlo
- Kernel density estimation
- Neural networks

## Concepts in Computing with Data (Stat 133)

![](figs/undergrad_v_stat133.png)

## Why Python?

- "General" purpose language
- "Batteries included" --- networking, database, etc.
- Popular for wide-range of scientific applications
- Growing number of libraries for specialized statistical applications
    - Pandas, sklearn, statmodels

## Python in the statistics curriculum

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

## Example: Effect of treatment in a randomized controlled experiment \small (www.stat.berkeley.edu/~stark/Teach/S240/Notes/lec1.pdf)

11 pairs of rats, each pair from the same litter.

\vfill

Randomly---by coin tosses---put one of each pair into
``enriched'' environment; other sib gets ''normal'' environment.

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
