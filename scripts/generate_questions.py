#!/usr/bin/env python3
"""
Generate the complete 85-problem Oxbridge Mathematics Interview database
from the Oxford and Cambridge Mathematics Interview Questions archive.
Outputs:
  - web/questions.js (assigns window.OXBRIDGE_QUESTIONS)
  - src/data/questions.json
"""

import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Helper to define each question cleanly
def q(
    id_: str,
    section: str,
    subset: str,
    title: str,
    college: str,
    year: str,
    topic: str,
    difficulty: str,
    statement: str,
    hints: list[str],
    solution: str,
    is_sketch: bool = False,
):
    return {
        "id": id_,
        "section": section,
        "subset": subset,
        "title": title,
        "college": college,
        "year": year,
        "topic": topic,
        "difficulty": difficulty,
        "isSketch": is_sketch,
        "statement": statement.strip(),
        "hints": [h.strip() for h in hints],
        "solution": solution.strip(),
    }


QUESTIONS = [
    # =========================================================================
    # 1. ANONYMOUS MATHEMATICS INTERVIEW PROBLEM SETS
    # =========================================================================
    # 1.1 Interview Set 1 - Interview 1 (4 problems)
    q(
        "1.1.1-p1",
        "1. Anonymous Problem Sets",
        "1.1 Interview Set 1 — Interview 1",
        "Odd Squares & Highest Common Factor",
        "Oxbridge Archive",
        "Set 1",
        "Number Theory",
        "Warm-up",
        r"""Prove that the product of two odd numbers is odd. What is the highest common factor of the difference of two odd numbers squared (i.e., $a^2 - b^2$ for odd integers $a$ and $b$)?""",
        [
            r"Write two general odd integers algebraically as $a = 2k + 1$ and $b = 2m + 1$ for $k, m \in \mathbb{Z}$.",
            r"Expand $a^2 - b^2 = (2k+1)^2 - (2m+1)^2$ and factor out $4$. What can you say about the parity of $k(k+1)$?",
            r"You've shown $8$ always divides $a^2 - b^2$. Can you pick a simple pair of odd integers $(a, b)$ to show no larger factor divides all such differences?",
        ],
        r"""Let $a = 2k + 1$ and $b = 2m + 1$ for $k, m \in \mathbb{Z}$.
Their product is:
$$ab = (2k+1)(2m+1) = 4km + 2k + 2m + 1 = 2(2km + k + m) + 1$$
Since $2km + k + m$ is an integer, $ab$ is odd.

Now consider the difference of their squares:
$$a^2 - b^2 = (2k+1)^2 - (2m+1)^2 = (4k^2 + 4k + 1) - (4m^2 + 4m + 1) = 4[k(k+1) - m(m+1)]$$
For any integer $k$, one of $k$ or $k+1$ is even, so $k(k+1)$ is always even; similarly $m(m+1)$ is even. Hence $k(k+1) - m(m+1) = 2J$ for some integer $J$, giving:
$$a^2 - b^2 = 4 \times 2J = 8J$$
Thus $8$ always divides $a^2 - b^2$. Taking $a = 3, b = 1$ gives $3^2 - 1^2 = 8$, so the highest common factor across all odd pairs is **8**.""",
    ),
    q(
        "1.1.1-p2",
        "1. Anonymous Problem Sets",
        "1.1 Interview Set 1 — Interview 1",
        "First Integer Satisfying $\\sin x \\le \\frac{\\sqrt{2}}{2}$",
        "Oxbridge Archive",
        "Set 1",
        "Calculus & Trigonometry",
        "Warm-up",
        r"""What is the first positive integer $x$ which satisfies the inequality
$$\sin x \le \frac{\sqrt{2}}{2},$$
where $x$ is measured in radians?""",
        [
            r"Identify the angles $\theta \in [0, 2\pi)$ where $\sin\theta \le \frac{\sqrt{2}}{2}$. Where is $\sin\theta > \frac{\sqrt{2}}{2}$?",
            r"Recall $\pi \approx 3.1416$. Estimate $\frac{\pi}{4}$ and $\frac{3\pi}{4}$ numerically.",
            r"Check where the integers $x = 1, 2, 3$ fall relative to $\frac{\pi}{4} \approx 0.785$ and $\frac{3\pi}{4} \approx 2.356$ and $\frac{9\pi}{4}$.",
        ],
        r"""Recall that $\sin\theta > \frac{\sqrt{2}}{2}$ for $\theta \in \left(\frac{\pi}{4}, \frac{3\pi}{4}\right)$ modulo $2\pi$. Numerically:
$$\frac{\pi}{4} \approx 0.7854, \qquad \frac{3\pi}{4} \approx 2.3562, \qquad \pi \approx 3.1416.$$
Testing consecutive positive integers:
- $x = 1$: $0.7854 < 1 < 2.3562$, so $1 \in (\pi/4, 3\pi/4)$ and $\sin 1 > \frac{\sqrt{2}}{2}$ ($\sin 1 \approx 0.8415$).
- $x = 2$: $0.7854 < 2 < 2.3562$, so $2 \in (\pi/4, 3\pi/4)$ and $\sin 2 > \frac{\sqrt{2}}{2}$ ($\sin 2 \approx 0.9093$).
- $x = 3$: $3 > \frac{3\pi}{4}$ and $3 < \pi < \frac{9\pi}{4}$, so $3 \in [3\pi/4, 9\pi/4]$ and $\sin 3 \le \frac{\sqrt{2}}{2}$ ($\sin 3 \approx 0.1411$).

Thus, the first positive integer satisfying the inequality is **$x = 3$**.""",
    ),
    q(
        "1.1.1-p3",
        "1. Anonymous Problem Sets",
        "1.1 Interview Set 1 — Interview 1",
        "Infinite Bouncing Ball Duration",
        "Oxbridge Archive",
        "Set 1",
        "Mechanics",
        "Standard",
        r"""If you drop a ball from height $h$, and it loses half of its energy every time it bounces, how long does it bounce for?""",
        [
            r"Relate the mechanical energy at the peak of each bounce ($E = mgh_n$) to the rebound height $h_n$.",
            r"Find the time $t_0$ for the initial drop using $h = \frac{1}{2}gt_0^2$. How does the duration of the $n$-th bounce (up AND down!) relate to $t_0$?",
            r"Sum the infinite geometric series $T = t_0 + \sum_{n=1}^{\infty} t_n$ with common ratio $r = \frac{1}{\sqrt{2}}$.",
        ],
        r"""Initial potential energy is $E_0 = mgh$, and the initial drop time from rest is:
$$t_0 = \sqrt{\frac{2h}{g}}.$$
After $n$ bounces, energy is $E_n = \frac{1}{2^n} E_0$, so the rebound height is $h_n = \frac{h}{2^n}$. Each bounce consists of both an ascent and descent, taking time:
$$t_n = 2\sqrt{\frac{2h_n}{g}} = 2\sqrt{\frac{2h}{g \cdot 2^n}} = 2t_0 \left(\frac{1}{\sqrt{2}}\right)^n.$$
Total bouncing time:
$$T = t_0 + \sum_{n=1}^{\infty} t_n = t_0 + 2t_0 \sum_{n=1}^{\infty} \left(\frac{1}{\sqrt{2}}\right)^n.$$
Since $\sum_{n=1}^{\infty} r^n = \frac{r}{1-r}$ for $|r|<1$:
$$\sum_{n=1}^{\infty} \left(\frac{1}{\sqrt{2}}\right)^n = \frac{1/\sqrt{2}}{1 - 1/\sqrt{2}} = \frac{1}{\sqrt{2}-1} = \sqrt{2} + 1.$$
Therefore:
$$T = t_0 + 2t_0(\sqrt{2} + 1) = (3 + 2\sqrt{2})t_0 = (3 + 2\sqrt{2})\sqrt{\frac{2h}{g}}.$$""",
    ),
    q(
        "1.1.1-p4",
        "1. Anonymous Problem Sets",
        "1.1 Interview Set 1 — Interview 1",
        "Fermat Numbers Product Identity",
        "Oxbridge Archive",
        "Set 1",
        "Number Theory",
        "Standard",
        r"""The Fermat numbers are defined by $F_n = 2^{2^n} + 1$. Use proof by induction to show that
$$F_0 F_1 \dots F_{n-1} = F_n - 2 \quad \text{for all } n \ge 1.$$""",
        [
            r"Verify the base case $n = 1$: check $F_0$ against $F_1 - 2$.",
            r"In the inductive step, replace $\prod_{i=0}^{k-1} F_i$ with $F_k - 2$, so the new product becomes $(F_k - 2)F_k$.",
            r"Substitute $F_k = 2^{2^k} + 1$ into $(F_k - 2)F_k$ and recognize a difference of two squares: $(x - 1)(x + 1) = x^2 - 1$.",
        ],
        r"""**Base case ($n=1$):** LHS $= F_0 = 2^{2^0} + 1 = 3$. RHS $= F_1 - 2 = (2^{2^1} + 1) - 2 = 5 - 2 = 3$. Holds.

**Inductive step:** Assume $\prod_{i=0}^{k-1} F_i = F_k - 2$ for some $k \ge 1$. Then for $k+1$:
$$\prod_{i=0}^{k} F_i = \left(\prod_{i=0}^{k-1} F_i\right) F_k = (F_k - 2)F_k.$$
Substituting $F_k = 2^{2^k} + 1$:
$$(F_k - 2)F_k = \left(2^{2^k} - 1\right)\left(2^{2^k} + 1\right) = \left(2^{2^k}\right)^2 - 1 = 2^{2 \cdot 2^k} - 1 = 2^{2^{k+1}} - 1 = F_{k+1} - 2.$$
By induction, the identity holds for all $n \ge 1$. *(Note: This immediately shows any two distinct Fermat numbers are coprime, yielding an alternative proof that there are infinitely many primes.)*""",
    ),

    # 1.1 Interview Set 1 - Interview 2 (3 problems)
    q(
        "1.1.2-p1",
        "1. Anonymous Problem Sets",
        "1.1 Interview Set 1 — Interview 2",
        "Fair vs Biased Die Game",
        "Oxbridge Archive",
        "Set 1",
        "Probability",
        "Standard",
        r"""Person A has a fair die and Person B has a biased die, where the probability that Person B rolls a $6$ is $p$. They take turns rolling until someone rolls a $6$, and that person wins. If Person A starts first:
(a) What is the probability that Person A wins?
(b) What would $p$ have to be for the game to be fair?
(c) Does this value of $p$ make sense? Justify your answer.""",
        [
            r"Write out the probability that A wins on round 1, round 2, round 3, or use a self-similar reset equation after two failed rolls.",
            r"Using a geometric series: $a = \frac{1}{6}$ and common ratio $r = \frac{5}{6}(1-p)$. What is $\frac{a}{1-r}$?",
            r"Set $P(\text{A wins}) = \frac{1}{2}$ to solve for $p$, and compare $p$ to $\frac{1}{6}$ considering A goes first.",
        ],
        r"""**(a)** $P(\text{A rolls } 6) = \frac{1}{6}$, $P(\text{A fails}) = \frac{5}{6}$, $P(\text{B rolls } 6) = p$, $P(\text{B fails}) = 1-p$.
$$P(\text{A wins}) = \frac{1}{6} + \left(\frac{5}{6}(1-p)\right)\frac{1}{6} + \left(\frac{5}{6}(1-p)\right)^2\frac{1}{6} + \dots = \frac{1/6}{1 - \frac{5}{6}(1-p)} = \frac{1}{6 - 5(1-p)} = \frac{1}{1 + 5p}.$$
*(Alternatively, $P(A) = \frac{1}{6} + \frac{5}{6}(1-p)P(A)$, giving the same result.)*

**(b)** For a fair game, $P(\text{A wins}) = \frac{1}{2}$:
$$\frac{1}{1 + 5p} = \frac{1}{2} \implies 1 + 5p = 2 \implies p = \frac{1}{5}.$$

**(c)** Yes! Since Person A has the first-mover advantage (an immediate $1/6$ chance to end the game before B even rolls), Person B needs a higher chance of rolling a $6$ ($p = 0.20 > 1/6 \approx 0.1667$) to compensate.""",
    ),
    q(
        "1.1.2-p2",
        "1. Anonymous Problem Sets",
        "1.1 Interview Set 1 — Interview 2",
        "Counting 5-Digit Numbers & Ascending Digits",
        "Oxbridge Archive",
        "Set 1",
        "Combinatorics",
        "Warm-up",
        r"""(a) How many 5-digit numbers are there?
(b) How many of these have 5 unique digits?
(c) How many have 5 unique digits in strictly ascending order?""",
        [
            r"For (a) and (b), remember the leading digit cannot be $0$ (choices $1\text{–}9$).",
            r"For (c), can the digit $0$ appear anywhere in a 5-digit number with digits in strictly ascending order $d_1 < d_2 < d_3 < d_4 < d_5$?",
            r"Once you choose 5 distinct digits from $\{1, 2, \dots, 9\}$, how many ways can you order them from smallest to largest?",
        ],
        r"""**(a)** The first digit has $9$ choices ($1\text{–}9$) and each of the remaining four digits has $10$ choices ($0\text{–}9$):
$$9 \times 10^4 = 90{,}000.$$

**(b)** Without repetition: $9$ choices for the 1st digit, $9$ remaining for the 2nd (including $0$), then $8, 7, 6$:
$$9 \times 9 \times 8 \times 7 \times 6 = 27{,}216.$$

**(c)** If $0$ appeared, since $d_1 < d_2 < d_3 < d_4 < d_5$, $0$ would have to be $d_1$, making it a 4-digit number. Thus all $5$ digits come from $\{1,2,3,4,5,6,7,8,9\}$. Any selection of $5$ distinct digits has a **unique** strictly ascending arrangement:
$$\binom{9}{5} = \frac{9 \times 8 \times 7 \times 6}{4 \times 3 \times 2 \times 1} = 126.$$""",
    ),
    q(
        "1.1.2-p3",
        "1. Anonymous Problem Sets",
        "1.1 Interview Set 1 — Interview 2",
        "Sun, Planet, and Moon Epicyclic Orbit",
        "Oxbridge Archive",
        "Set 1",
        "Geometry",
        "Standard",
        r"""There is a Sun with a planet orbiting it in a circle of radius $R$. A moon orbits the planet in a circle of radius $r$.
(a) Find an equation for the position of the moon relative to the Sun.
(b) Suppose $\theta(t)$ is the angle of the planet around the Sun and $\gamma(t)$ is the angle of the moon around the planet. If $\theta = 12\gamma$, what can you say about the movement of the moon around the Sun?""",
        [
            r"Place the Sun at the origin $(0,0)$. Write the vector $\mathbf{r}_{\text{planet}}$ in terms of $R$ and $\theta$, and $\mathbf{r}_{\text{moon/planet}}$ in terms of $r$ and $\gamma$.",
            r"Add the position vectors: $\mathbf{r}_{\text{moon}} = \mathbf{r}_{\text{planet}} + \mathbf{r}_{\text{moon/planet}}$.",
            r"If $\theta = 12\gamma$, compare the angular speeds: which object revolves faster—the planet around the Sun, or the moon around the planet? Contrast with the Earth-Moon-Sun system!",
        ],
        r"""**(a)** Placing the Sun at $(0,0)$:
$$\mathbf{r}_{\text{planet}} = (R\cos\theta,\, R\sin\theta), \qquad \mathbf{r}_{\text{moon/planet}} = (r\cos\gamma,\, r\sin\gamma).$$
By vector addition, the moon's position relative to the Sun is:
$$\mathbf{r}_{\text{moon}} = \bigl(R\cos\theta + r\cos\gamma,\; R\sin\theta + r\sin\gamma\bigr).$$

**(b)** If $\theta = 12\gamma$, then $\gamma = \frac{\theta}{12}$: the planet completes **12 full revolutions** around the Sun in the time it takes the moon to complete just **1 revolution** around the planet (the reverse of Earth's Moon, which has $\gamma \approx 12\theta$). The path is an epitrochoid/epicyclic curve looking like a large circle with $12$ inward/outward wave oscillations per lunar cycle.""",
    ),

    # 1.2 Interview Set 2 (5 problems)
    q(
        "1.2-p1",
        "1. Anonymous Problem Sets",
        "1.2 Interview Set 2",
        "Four Balls in Two Boxes",
        "Oxbridge Archive",
        "Set 2",
        "Probability",
        "Warm-up",
        r"""Four balls are dropped into two boxes, with an equal chance of each ball falling into either box. What is the probability that there are two balls in each box?""",
        [
            r"Treat the $4$ balls as distinct/independent trials, each choosing Box 1 or Box 2 with probability $1/2$.",
            r"How many total equally likely outcomes are there for $4$ balls into $2$ boxes?",
            r"Count how many of those outcomes put exactly $2$ balls into Box 1 using $\binom{4}{2}$.",
        ],
        r"""Each ball independently enters Box 1 or Box 2 with probability $1/2$, giving $2^4 = 16$ equally likely configurations. The number of ways to select $2$ of the $4$ balls to go into Box 1 is $\binom{4}{2} = 6$. Thus:
$$P(2\text{ in each box}) = \frac{\binom{4}{2}}{2^4} = \frac{6}{16} = \frac{3}{8} = 0.375.$$""",
    ),
    q(
        "1.2-p2",
        "1. Anonymous Problem Sets",
        "1.2 Interview Set 2",
        "Iterated Function Composition with $\\pi$",
        "Oxbridge Archive",
        "Set 2",
        "Algebra & Inequalities",
        "Warm-up",
        r"""Let $f(x) = \sqrt{x+1}$ and $g(x) = x^2 + 1$. Find
$$f\bigl(g(f(g(f(g(\pi)))))\bigr).$$""",
        [
            r"Instead of plugging $\pi$ in immediately, compute the single composite operation $h(x) = f(g(x))$ first!",
            r"Simplify $f(g(x)) = \sqrt{(x^2 + 1) + 1}$.",
            r"Now apply $h(x) = \sqrt{x^2 + 2}$ three times starting from $u_0 = \pi$.",
        ],
        r"""Compute the composite block $h(x) = f(g(x))$:
$$f(g(x)) = \sqrt{(x^2+1)+1} = \sqrt{x^2+2}.$$
Iterating starting with $u_0 = \pi$:
$$u_1 = f(g(\pi)) = \sqrt{\pi^2 + 2},$$
$$u_2 = f(g(u_1)) = \sqrt{(\pi^2 + 2) + 2} = \sqrt{\pi^2 + 4},$$
$$u_3 = f(g(u_2)) = \sqrt{(\pi^2 + 4) + 2} = \sqrt{\pi^2 + 6}.$$
Thus, $f(g(f(g(f(g(\pi)))))) = \mathbf{\sqrt{\pi^2 + 6}}$.""",
    ),
    q(
        "1.2-p3",
        "1. Anonymous Problem Sets",
        "1.2 Interview Set 2",
        "Euclidean Algorithm for Large Integers",
        "Oxbridge Archive",
        "Set 2",
        "Number Theory",
        "Warm-up",
        r"""Find the highest common factor of $36838$ and $38972$.""",
        [
            r"Use the Euclidean algorithm: $\gcd(a, b) = \gcd(b, a \bmod b)$.",
            r"First step: $38972 - 36838 = 2134$. Now divide $36838$ by $2134$.",
            r"Continue dividing remainders carefully ($36838 = 17 \times 2134 + 560$, etc.) until the remainder is $0$.",
        ],
        r"""Apply the Euclidean algorithm:
$$\begin{aligned}
38972 &= 1 \times 36838 + 2134 \\
36838 &= 17 \times 2134 + 560 \quad (17 \times 2134 = 36278) \\
2134 &= 3 \times 560 + 454 \\
560 &= 1 \times 454 + 106 \\
454 &= 4 \times 106 + 30 \\
106 &= 3 \times 30 + 16 \\
30 &= 1 \times 16 + 14 \\
16 &= 1 \times 14 + 2 \\
14 &= 7 \times 2 + 0.
\end{aligned}$$
The last non-zero remainder is **$2$**, so $\gcd(36838, 38972) = 2$.""",
    ),
    q(
        "1.2-p4",
        "1. Anonymous Problem Sets",
        "1.2 Interview Set 2",
        "Vertical Projection with Air Resistance",
        "Oxbridge Archive",
        "Set 2",
        "Mechanics",
        "Standard",
        r"""Two particles, A and B, of the same size and mass are projected vertically upward from the same point. Both reach the same maximum height, but B experiences air resistance while A does not.
(a) Which particle reaches its maximum height first?
(b) How does the presence of resistance affect the initial speed required to reach the same height?""",
        [
            r"Start with (b) using energy conservation: at the top both have $E = mgh$ and $v = 0$. What happens to mechanical energy on the way up for B?",
            r"For (a), think backwards from the top ($v=0$ at height $h$), or compare the downward deceleration magnitude $|a_B(v)|$ vs $|a_A| = g$ during ascent.",
            r"Be careful: B starts faster, AND decelerates faster, yet covers the exact same distance $h$ to reach $v=0$. Compare $v_A(y)$ and $v_B(y)$ at every height $y \in [0, h)$!",
        ],
        r"""**(a) Particle B reaches its maximum height first.**
During ascent ($v > 0$), gravity and drag both act downward on B:
$$a_B = -g - \frac{F_{\text{drag}}(v)}{m} < -g = a_A.$$
At any given height $y < h$, particle B still has to dissipate future drag work on the remaining climb $(h - y)$ in addition to gaining $mg(h-y)$ potential energy, so its upward speed $v_B(y)$ is strictly greater than $v_A(y)$ at every height $y \in [0, h)$. Since $t = \int_0^h \frac{dy}{v(y)}$, B takes strictly less time to reach height $h$.

**(b) Air resistance requires a strictly higher initial speed ($v_{0,B} > v_{0,A}$).**
By work-energy:
$$\frac{1}{2}mv_{0,B}^2 = mgh + W_{\text{drag}} > mgh = \frac{1}{2}mv_{0,A}^2 \implies v_{0,B} > v_{0,A}.$$""",
    ),
    q(
        "1.2-p5",
        "1. Anonymous Problem Sets",
        "1.2 Interview Set 2",
        "Financial Times $p$-Beauty Contest Game",
        "Oxbridge Archive",
        "Set 2",
        "Logic & Game Theory",
        "Standard",
        r"""A competition in the *Financial Times* asked entrants to submit an integer between $1$ and $100$. The person closest to $\frac{2}{3}$ of the average of all submitted numbers won £5000. What number would you submit?""",
        [
            r"Start from a naive baseline: if everyone guessed uniformly between $1$ and $100$, the average would be $\sim 50$. What is $\frac{2}{3}$ of $50$?",
            r"What happens if other rational players also think one step ahead? Why is any number above $67$ strictly dominated?",
            r"Iterate this elimination of strictly dominated strategies to find the unique Nash equilibrium—and also consider behavioral psychology for real human entrants!",
        ],
        r"""This is the classic **$p$-beauty contest game** ($p = 2/3$):
- **Level 0 (random):** Mean $\approx 50 \implies \frac{2}{3} \times 50 \approx 33$.
- **Level 1:** Anticipating random players, submit $33$.
- **Level 2:** Anticipating Level-1 players, submit $\frac{2}{3} \times 33 = 22$.
- **Iterated Elimination of Dominated Strategies:** Because no average can exceed $100$, no winning target exceeds $66.\overline{6}$, so numbers $>67$ are strictly dominated. Iterating $x_k = \left(\frac{2}{3}\right)^k \times 100 \to 1$ shows that **1** is the unique Nash equilibrium under common knowledge of rationality.

*Interview commentary:* In real-world newspaper experiments (including the actual *FT* contest), most entrants stop at 1–3 levels of reasoning, making winning submissions typically around **19–22** (or lower in mathematically sophisticated cohorts). Discussing both the theoretical Nash equilibrium (**1**) and the behavioral level-$k$ adjustment is ideal.""",
    ),

    # 1.3 Interview Set 3 - Interview 1 (2 problems)
    q(
        "1.3.1-p1",
        "1. Anonymous Problem Sets",
        "1.3 Interview Set 3 — Interview 1",
        "Fermat Curves $x^n + y^n = 1$ & Rational Points",
        "Oxbridge Archive",
        "Set 3",
        "Graph Sketching",
        "Standard",
        r"""Focusing on the first quadrant:
(a) Sketch the curves $x^2 + y^2 = 1$, $x^3 + y^3 = 1$, $x^4 + y^4 = 1$, and $x^5 + y^5 = 1$. Is $x^3 + y^3 = 1$ inside or outside $x^2 + y^2 = 1$?
(b) Is there a maximum number of such curves that can be drawn within the unit square $0 \le x \le 1, 0 \le y \le 1$?
(c) Use Fermat's Last Theorem to discuss whether rational points can lie on curves of the form $x^n + y^n = 1$, $n \ge 3$.""",
        [
            r"For $0 < x < 1$, compare $x^3$ and $x^2$. Which is smaller? What does that imply for $y = (1 - x^n)^{1/n}$?",
            r"Check the intersection of each curve with the diagonal $y = x$: solve $2x^n = 1$. What happens as $n \to \infty$?",
            r"For (c), write a hypothetical rational point as $(A/C, B/C)$ with common denominator $C > 0$ and clear denominators.",
        ],
        r"""**(a)** For $0 < x < 1$, increasing $n$ makes $x^n$ smaller ($x^n < x^2$), so $y^n = 1 - x^n$ is larger, and taking the $n$-th root makes $y$ strictly larger than for $n=2$. All curves pass through $(1,0)$ and $(0,1)$. On the symmetry line $y=x$:
$$2x^n = 1 \implies x = \left(\frac{1}{2}\right)^{1/n},$$
which increases strictly from $2^{-1/2} \approx 0.707$ to $2^{-1/3} \approx 0.794$, $2^{-1/4} \approx 0.841 \to 1$. Thus $x^3+y^3=1$ lies **strictly outside** $x^2+y^2=1$ in the first quadrant, bulging outward toward the unit square boundary as $n \to \infty$.

**(b)** **No** maximum number—there is an infinite family of distinct curves $x^n + y^n = 1$ for every $n \ge 1$, all contained in $[0,1]^2$.

**(c)** If $(x, y) = (A/C, B/C)$ were a rational point on $x^n + y^n = 1$ ($n \ge 3$), then $A^n + B^n = C^n$. By Fermat's Last Theorem, there are no integer solutions with $ABC \ne 0$. Hence the only rational points on $x^n + y^n = 1$ ($n \ge 3$) are the trivial axis intercepts: $(1,0), (0,1)$ (and $(-1,0), (0,-1)$ when $n$ is even).""",
        is_sketch=True,
    ),
    q(
        "1.3.1-p2",
        "1. Anonymous Problem Sets",
        "1.3 Interview Set 3 — Interview 1",
        "Infinite Trigonometric Geometric Series",
        "Oxbridge Archive",
        "Set 3",
        "Calculus & Trigonometry",
        "Warm-up",
        r"""How many solutions does the equation
$$2 = \sin x + \sin^2 x + \sin^3 x + \sin^4 x + \dots$$
have (for $x \in [0, 2\pi)$)?""",
        [
            r"Recognize the right-hand side as an infinite geometric series with first term $s = \sin x$ and common ratio $s = \sin x$.",
            r"When does this infinite geometric series converge? What is its sum $\frac{s}{1-s}$?",
            r"Solve $\frac{s}{1-s} = 2$, verify $|s| < 1$, and count solutions to $\sin x = s$ in $[0, 2\pi)$ (noting there are infinitely many across $\mathbb{R}$).",
        ],
        r"""Let $s = \sin x$. The geometric series converges iff $|s| < 1$, to sum $\frac{s}{1-s}$. Setting this equal to $2$:
$$\frac{s}{1-s} = 2 \implies s = 2 - 2s \implies 3s = 2 \implies s = \frac{2}{3}.$$
Since $|2/3| < 1$, the series validly converges. On the fundamental domain $x \in [0, 2\pi)$, $\sin x = \frac{2}{3}$ has **2** solutions: $x = \arcsin(2/3)$ and $x = \pi - \arcsin(2/3)$. (Across all $x \in \mathbb{R}$, there are infinitely many solutions $2k\pi + \arcsin(2/3)$ and $(2k+1)\pi - \arcsin(2/3)$.)""",
    ),

    # 1.3 Interview Set 3 - Interview 2 (3 problems)
    q(
        "1.3.2-p1",
        "1. Anonymous Problem Sets",
        "1.3 Interview Set 3 — Interview 2",
        "Sketch $y = x^2 \\sin(1/x)$",
        "Oxbridge Archive",
        "Set 3",
        "Graph Sketching",
        "Standard",
        r"""Sketch the curve
$$y = x^2 \sin\!\left(\frac{1}{x}\right).$$""",
        [
            r"Check parity (odd/even) and find an upper and lower bounding envelope using $-1 \le \sin(1/x) \le 1$.",
            r"What happens as $x \to 0$? Is the function continuous and differentiable at $x = 0$ if we define $f(0) = 0$?",
            r"What happens for very large $|x|$? Use the small-angle approximation $\sin u \approx u$ for $u = 1/x \to 0$.",
        ],
        r"""Key features to include on your sketch:
1. **Domain & Symmetry:** Defined for $x \ne 0$. Since $(-x)^2\sin(-1/x) = -x^2\sin(1/x)$, it is an **odd** function.
2. **Parabolic Envelope:** Since $-1 \le \sin(1/x) \le 1$, the curve is trapped between $y = -x^2$ and $y = x^2$, touching them whenever $\frac{1}{x} = \frac{\pi}{2} + k\pi$.
3. **Behavior near $x=0$:** By the Squeeze Theorem, $\lim_{x\to 0} x^2\sin(1/x) = 0$. Furthermore, $f'(0) = \lim_{h\to 0} \frac{h^2\sin(1/h)}{h} = \lim_{h\to 0} h\sin(1/h) = 0$, so it approaches $(0,0)$ with infinitely rapid oscillations compressed between $\pm x^2$ and a horizontal tangent at the origin.
4. **Large $|x|$ asymptote:** For $|x| \gg 1$, $\sin(1/x) \approx \frac{1}{x}$, so $y \approx x^2 \cdot \frac{1}{x} = x$. Wait—more accurately, $y - x = x^2\sin(1/x) - x \sim -\frac{1}{6x} \to 0$, so the line **$y = x$** is an oblique asymptote as $x \to \pm\infty$!""",
        is_sketch=True,
    ),
    q(
        "1.3.2-p2",
        "1. Anonymous Problem Sets",
        "1.3 Interview Set 3 — Interview 2",
        "Selecting 51 Numbers from $1$ to $1000$",
        "Oxbridge Archive",
        "Set 3",
        "Combinatorics",
        "Warm-up",
        r"""Suppose $51$ numbers are selected from the integers $1$ to $1000$. Can one choose such a collection containing no:
(i) even numbers?
(ii) prime numbers?
(iii) coprime pairs?
(iv) square numbers?
(v) numbers which are the sum of a square and a cube?""",
        [
            r"For each part, count how many integers in $\{1, \dots, 1000\}$ are *allowed* (avoid the forbidden property). If at least 51 allowed numbers exist, you can construct such a set!",
            r"For (iii), 'no coprime pairs' means EVERY pair shares a factor $>1$. What is the easiest way to guarantee all 51 numbers share a common factor?",
            r"For (v), how many positive squares $\le 1000$ and positive cubes $\le 1000$ are there? Bound the total number of sums $a^2 + b^3 \le 1000$.",
        ],
        r"""**(i) No even numbers: Yes.** There are $500$ odd numbers in $\{1,\dots,1000\}$; pick $\{1, 3, \dots, 101\}$.
**(ii) No prime numbers: Yes.** There are $168$ primes $\le 1000$, leaving $832$ non-primes (composites and $1$), easily $\ge 51$.
**(iii) No coprime pairs: Yes.** Choose $51$ multiples of $2$: $\{2, 4, 6, \dots, 102\}$. Every pair shares factor $2$, so no two are coprime.
**(iv) No square numbers: Yes.** Only $\lfloor \sqrt{1000} \rfloor = 31$ squares exist up to $1000$, leaving $969$ non-squares.
**(v) No sum of a square and a cube: Yes.** There are $31$ positive squares and $10$ positive cubes $\le 1000$ ($31 \times 10 = 310$ sums max; even allowing $0^2$ or $0^3$ adds at most $41$ more, well below $949$). At least $690$ numbers remain from which $51$ can be chosen.""",
    ),
    q(
        "1.3.2-p3",
        "1. Anonymous Problem Sets",
        "1.3 Interview Set 3 — Interview 2",
        "Infinite 2D Grid Neighbor Average (Discrete Maximum Principle)",
        "Oxbridge Archive",
        "Set 3",
        "Logic & Game Theory",
        "Challenging",
        r"""In an infinite two-dimensional grid, the number in each box is greater than or equal to the average of the numbers in its four neighbouring boxes. Show that all the numbers in the grid are the same (assuming the values are bounded or attain a maximum).""",
        [
            r"Let $M$ be the maximum value in the grid, attained at some cell $(i_0, j_0)$.",
            r"Write down the inequality for $(i_0, j_0)$: $M \ge \frac{1}{4}(u_{\text{N}} + u_{\text{S}} + u_{\text{E}} + u_{\text{W}})$, knowing each neighbour is $\le M$.",
            r"Can any of the four neighbours be strictly less than $M$? Now propagate this argument across the entire grid by induction!",
        ],
        r"""Let $u(i,j)$ be the value at $(i,j)$. Suppose $u$ attains a global maximum $M$ at some cell $(i_0, j_0)$. By hypothesis:
$$M = u(i_0, j_0) \ge \frac{u(i_0+1, j_0) + u(i_0-1, j_0) + u(i_0, j_0+1) + u(i_0, j_0-1)}{4}.$$
Since every neighbour satisfies $u(x,y) \le M$, if any single neighbour were strictly less than $M$, their average would be strictly less than $M$, a contradiction. Therefore, all four neighbours must equal $M$.
By induction on Manhattan distance from $(i_0, j_0)$, every cell in the infinite connected grid equals $M$. (This is the discrete Maximum Principle for subharmonic functions; note that if values are only bounded above and not assumed to attain a maximum, on $\mathbb{Z}^2$ a bounded subharmonic function is still constant, though the interview prompt explicitly simplifies by assuming a maximum is attained or boundedness.)""",
    ),

    # 1.3 Interview Set 3 - Further Questions (4 problems)
    q(
        "1.3.3-p1",
        "1. Anonymous Problem Sets",
        "1.3 Interview Set 3 — Further Questions",
        "Roots & Turning Points of $(x-a)^3 + (x-b)^3 = 0$",
        "Oxbridge Archive",
        "Set 3",
        "Calculus & Trigonometry",
        "Warm-up",
        r"""Let $a \ne b$ and $a, b > 0$. How many real solutions are there to $(x-a)^3 + (x-b)^3 = 0$? Find the solution, prove uniqueness, and find any turning points.""",
        [
            r"Rearrange as $(x-a)^3 = (b-x)^3$ and take the real cube root of both sides.",
            r"To check turning points and prove uniqueness via calculus, differentiate $g(x) = (x-a)^3 + (x-b)^3$.",
            r"Analyze the sign of $g'(x) = 3(x-a)^2 + 3(x-b)^2$ when $a \ne b$. Can it ever be zero or negative?",
        ],
        r"""Rearrange the equation:
$$(x-a)^3 = -(x-b)^3 = (b-x)^3.$$
Since $t \mapsto t^3$ is strictly increasing and bijective on $\mathbb{R}$, taking the unique real cube root gives:
$$x - a = b - x \implies x = \frac{a+b}{2}.$$
Let $g(x) = (x-a)^3 + (x-b)^3$. Differentiating:
$$g'(x) = 3(x-a)^2 + 3(x-b)^2.$$
Because $a \ne b$, $(x-a)^2$ and $(x-b)^2$ cannot both be zero simultaneously, so $g'(x) > 0$ for all $x \in \mathbb{R}$. Hence $g$ is strictly increasing (confirming the root $x = \frac{a+b}{2}$ is unique) and has **no turning points**. It has a point of inflection at $g''(x) = 6(x-a)+6(x-b) = 0 \implies x = \frac{a+b}{2}$.""",
    ),
    q(
        "1.3.3-p2",
        "1. Anonymous Problem Sets",
        "1.3 Interview Set 3 — Further Questions",
        "Infinite Continued Fraction (Golden Ratio)",
        "Oxbridge Archive",
        "Set 3",
        "Algebra & Inequalities",
        "Warm-up",
        r"""Find $x$ if
$$x = 1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \dots}}}$$""",
        [
            r"Notice the self-similar structure inside the denominator of the first fraction.",
            r"Write a single algebraic equation relating $x$ to itself: $x = 1 + \frac{1}{x}$.",
            r"Solve the resulting quadratic $x^2 - x - 1 = 0$, and explain why one root is discarded.",
        ],
        r"""Observing the self-similarity, $x$ satisfies:
$$x = 1 + \frac{1}{x}.$$
Multiplying by $x$ gives $x^2 - x - 1 = 0$, with roots $x = \frac{1 \pm \sqrt{5}}{2}$. Since all terms in the continued fraction are positive, $x > 0$, so we discard the negative root, obtaining the Golden Ratio:
$$x = \frac{1 + \sqrt{5}}{2} = \phi \approx 1.618.$$""",
    ),
    q(
        "1.3.3-p3",
        "1. Anonymous Problem Sets",
        "1.3 Interview Set 3 — Further Questions",
        "Defining $e^x$ and Sketching $\\frac{e^x}{x}$ and $\\frac{e^x - x - 1}{x^3 + x^2}$",
        "Oxbridge Archive",
        "Set 3",
        "Graph Sketching",
        "Challenging",
        r"""Define $e^x$. Sketch $y = \dfrac{e^x}{x}$ and $y = \dfrac{e^x - x - 1}{x^3 + x^2}$.""",
        [
            r"Give a clean analytical definition of $e^x$ (e.g., unique solution to $f'(x)=f(x)$ with $f(0)=1$, or $\sum_{k=0}^\infty \frac{x^k}{k!}$).",
            r"For $y = \frac{e^x}{x}$, find the asymptotes ($x=0$, $x\to-\infty$, $x\to+\infty$) and differentiate to find the stationary point at $x=1$.",
            r"For $y = \frac{e^x - x - 1}{x^2(x+1)}$, expand $e^x$ near $x=0$! Is $x=0$ a vertical asymptote or a removable discontinuity?",
        ],
        r"""**Definition of $e^x$:** The unique differentiable function satisfying $\frac{d}{dx}(e^x) = e^x$ with $e^0 = 1$ (equivalently $\sum_{k=0}^\infty \frac{x^k}{k!}$ or $\lim_{n\to\infty}(1+x/n)^n$).

**Sketch of $y = \frac{e^x}{x}$:**
- Vertical asymptote at $x=0$: $y \to +\infty$ as $x\to 0^+$, $y \to -\infty$ as $x \to 0^-$.
- As $x\to +\infty$, $y \to +\infty$ exponentially; as $x\to -\infty$, $y \to 0^-$.
- Derivative: $y' = \frac{e^x(x-1)}{x^2}$, giving a local minimum at $(1, e)$. Always decreasing on $(-\infty, 0)$.

**Sketch of $y = \frac{e^x - x - 1}{x^2(x+1)}$:**
- Near $x=0$: $e^x - x - 1 = \frac{x^2}{2} + \frac{x^3}{6} + O(x^4)$, so
$$\lim_{x\to 0} \frac{e^x - x - 1}{x^2(x+1)} = \frac{1}{2}.$$
Thus $x=0$ is a **removable discontinuity (hole at $(0, 1/2)$)**, NOT an asymptote!
- At $x = -1$: numerator is $e^{-1} > 0$, simple zero in denominator $\implies$ vertical asymptote ($y \to +\infty$ as $x \to -1^+$, $y \to -\infty$ as $x \to -1^-$).
- As $x \to +\infty$, $y \to +\infty$; as $x \to -\infty$, $y \approx \frac{-x}{x^3} = -\frac{1}{x^2} \to 0^-$. (Note: $y > 0$ for all $x > -1$ since $e^x > 1 + x$.)""",
        is_sketch=True,
    ),
    q(
        "1.3.3-p4",
        "1. Anonymous Problem Sets",
        "1.3 Interview Set 3 — Further Questions",
        "Binary Guessing Cards Trick",
        "Oxbridge Archive",
        "Set 3",
        "Number Theory",
        "Warm-up",
        r"""Explain the binary guessing trick (Christmas cracker cards), where you ask someone which cards contain their secret number and immediately deduce the number.""",
        [
            r"Write any positive integer $N < 2^k$ in base 2 (binary): $N = \sum_{i=0}^{k-1} b_i 2^i$ with $b_i \in \{0, 1\}$.",
            r"How should you decide which numbers are printed on Card $i$?",
            r"What is the smallest (top-left) number on Card $i$, and how do you reconstruct $N$ from the cards the person selects?",
        ],
        r"""Every integer $1 \le N \le 2^k - 1$ has a unique binary representation:
$$N = b_0 2^0 + b_1 2^1 + b_2 2^2 + \dots + b_{k-1} 2^{k-1}, \quad b_i \in \{0,1\}.$$
We create $k$ cards: **Card $i$** lists all integers whose $i$-th binary bit is $b_i = 1$.
When the person points out all cards containing their secret number $N$, they are revealing precisely which bits $b_i$ equal $1$. Since the smallest number on Card $i$ is $2^i$ (binary $100\dots 0_2$), summing the **top-left (smallest) numbers** of the selected cards computes $\sum_{b_i=1} 2^i = N$.""",
    ),

    # 1.4 Interview Set 4 (1 problem)
    q(
        "1.4-p1",
        "1. Anonymous Problem Sets",
        "1.4 Interview Set 4",
        "Bus M and Bus Z Arrival Paradox",
        "Oxbridge Archive",
        "Set 4",
        "Probability",
        "Standard",
        r"""Two buses, M and Z, arrive at fixed minutes past each hour, with one of each bus every hour. You arrive at a uniformly distributed random time and observe that you are much more likely to catch bus M than bus Z. Given that bus Z arrives during the first half of the hour ($0 < z \le 30$), what can you deduce about arrival times $m$ and $z$?""",
        [
            r"Draw the 60-minute hour as a circle (clock face) and mark $z$ and $m$ on it.",
            r"Which interval of arrival times leads to catching bus M (the next bus to arrive after you reach the stop)?",
            r"If you are much more likely to catch M, the window before M (and after Z) must be much larger than $30$ minutes. With $0 < z \le 30$, where must $z$ and $m$ lie?",
        ],
        r"""Let $z, m \in [0, 60)$ be the minutes past the hour when buses Z and M arrive. On the 60-minute cycle, you catch bus M if you arrive after Z and before M.
For this window to be much larger than $30$ minutes (since $z \le 30$):
- If $m < z$, the gap from Z (wrapping past 60) to M would be $(60 - z) + m$. Wait: if $z=29$ and $m=28$, $(60-29)+28 = 59$! Hold on—check both cases!
Let's examine carefully:
- **Case 1 ($z < m$):** Window for M is $(z, m]$ of length $m - z$. For $m - z \gg 30$ with $z > 0$, we need $z$ near $0$ (just after the hour) and $m$ near $60$ (just before the end of the hour), e.g., $z=1, m=59 \implies P(M) = 58/60$.
- **Case 2 ($m < z$):** Window for M wraps past the hour: $(z, 60] \cup [0, m]$, of length $(60 - z) + m = 60 - (z - m)$. Since $z \le 30$, if $m$ is *just before* $z$ (e.g. $z = 20, m = 19$), the window for M is $59$ minutes!
In general, the waiting window preceding M around the 60-minute clock is $(m - z) \bmod 60 \gg 30$, meaning **bus M arrives shortly before bus Z** (so Z follows closely behind M in the cyclic schedule, either $z$ near $0$ and $m$ near $60$, or $m$ slightly less than $z$).""",
    ),

    # 1.5 Interview Set 5 - Interview 1 (2 problems)
    q(
        "1.5.1-p1",
        "1. Anonymous Problem Sets",
        "1.5 Interview Set 5 — Interview 1",
        "Infinitude of Prime Numbers (Euclid's Proof)",
        "Oxbridge Archive",
        "Set 5",
        "Number Theory",
        "Warm-up",
        r"""Prove that the set of prime numbers is infinite.""",
        [
            r"Assume for contradiction that there are only finitely many primes: $p_1, p_2, \dots, p_k$.",
            r"Construct a new integer $N = p_1 p_2 \cdots p_k + 1$.",
            r"Does $N$ have to be prime itself? What does the Fundamental Theorem of Arithmetic guarantee about $N$?",
        ],
        r"""Assume for contradiction that there are finitely many primes $\{p_1, p_2, \dots, p_k\}$. Consider:
$$N = p_1 p_2 \cdots p_k + 1.$$
Since $N > 1$, $N$ has at least one prime divisor $q$. Because our list contains all primes, $q = p_i$ for some $i$, so $q \mid p_1 p_2 \cdots p_k$.
Since $q \mid N$ and $q \mid p_1 \cdots p_k$, $q$ must divide their difference $N - p_1 \cdots p_k = 1$, which is impossible since $q \ge 2$. Thus there are infinitely many primes.""",
    ),
    q(
        "1.5.1-p2",
        "1. Anonymous Problem Sets",
        "1.5 Interview Set 5 — Interview 1",
        "Infinitely Many Primes of Form $6m + 5$",
        "Oxbridge Archive",
        "Set 5",
        "Number Theory",
        "Standard",
        r"""Prove that there are infinitely many prime numbers of the form $6m + 5$ ($m \in \mathbb{Z}$).""",
        [
            r"Note that every prime $>3$ is congruent to either $1$ or $5 \equiv -1 \pmod 6$.",
            r"What is the product of numbers that are all $\equiv 1 \pmod 6$? What does that tell you about any integer $\equiv 5 \pmod 6$?",
            r"Suppose finitely many primes $q_1, \dots, q_k \equiv 5 \pmod 6$ exist. Construct $N = 6q_1 q_2 \cdots q_k - 1$ (avoiding $q_i = 2, 3$!).",
        ],
        r"""Every integer coprime to $6$ is $\equiv 1$ or $5 \pmod 6$. Observe that $(6a+1)(6b+1) = 6(6ab+a+b)+1 \equiv 1 \pmod 6$, so any product of primes congruent to $1 \pmod 6$ is also $\equiv 1 \pmod 6$.
Consequently, any positive integer $N \equiv 5 \pmod 6$ must have at least one prime factor congruent to $5 \pmod 6$.

Assume for contradiction there are finitely many primes of the form $6m+5$, say $\{q_1, \dots, q_k\}$. Construct:
$$N = 6q_1 q_2 \cdots q_k - 1 = 6(q_1\cdots q_k - 1) + 5 \equiv 5 \pmod 6.$$
Since $N$ is coprime to $2$ and $3$, it must have a prime factor $p \equiv 5 \pmod 6$, so $p = q_i$ for some $i$. Then $p \mid 6q_1\cdots q_k$ and $p \mid N$, so $p \mid (6q_1\cdots q_k - N) = 1$, contradiction.""",
    ),

    # 1.5 Interview Set 5 - Interview 2 (2 problems)
    q(
        "1.5.2-p1",
        "1. Anonymous Problem Sets",
        "1.5 Interview Set 5 — Interview 2",
        "Equal Subset Sums (Pigeonhole Principle)",
        "Oxbridge Archive",
        "Set 5",
        "Combinatorics",
        "Standard",
        r"""Consider a set of ten positive integers $S = \{x_1, x_2, \dots, x_{10}\}$ with $0 < x_i < 100$. Prove that there exist two distinct subsets of $S$ that have the exact same sum. What affects the likelihood: the range or the number of elements?""",
        [
            r"Count how many non-empty subsets $S$ has: $2^{10} - 1$.",
            r"Bound the minimum and maximum possible sum of any non-empty subset of $S$ (recall $x_i \le 99$).",
            r"Compare the number of subsets (pigeons) to the number of possible sums (pigeonholes). Which parameter grows exponentially vs linearly?",
        ],
        r"""There are $2^{10} - 1 = 1023$ non-empty subsets of $S$.
Since $1 \le x_i \le 99$, the sum of any non-empty subset lies between $1$ and $90 + 91 + \dots + 99 = 945$ (and certainly $< 10 \times 99 = 990$).
Because there are $1023$ non-empty subsets (pigeons) and at most $945$ (or $990$) possible sum values (pigeonholes), by the **Pigeonhole Principle** at least two distinct subsets $A, B \subseteq S$ must have the same sum. *(Removing $A \cap B$ gives two disjoint subsets with equal sum.)*

**Range vs. Number of Elements:** The number of subsets grows exponentially ($2^n$), while the maximum sum grows only linearly ($\approx nR$). Thus **the number of elements $n$** dominates far more strongly than the range $R$.""",
    ),
    q(
        "1.5.2-p2",
        "1. Anonymous Problem Sets",
        "1.5 Interview Set 5 — Interview 2",
        "Sketch $y = \\frac{1}{(x+1)(x+2)}$",
        "Oxbridge Archive",
        "Set 5",
        "Graph Sketching",
        "Warm-up",
        r"""Sketch the graph of
$$y = \frac{1}{(x+1)(x+2)}.$$""",
        [
            r"Find the vertical asymptotes (where the denominator is $0$) and horizontal asymptote as $x \to \pm\infty$.",
            r"Analyze the sign of $y$ in the three intervals: $x < -2$, $-2 < x < -1$, and $x > -1$.",
            r"Where is the local maximum in the middle interval $(-2, -1)$? Evaluate $y$ at the midpoint $x = -1.5$ and at $x = 0$.",
        ],
        r"""- **Vertical Asymptotes:** $x = -1$ and $x = -2$.
- **Horizontal Asymptote:** $y \to 0^+$ as $x \to \pm\infty$.
- **Region $x > -1$:** Both factors positive $\implies y > 0$; $y \to +\infty$ as $x \to -1^+$, $y(0) = \frac{1}{2}$, strictly decreasing to $0$.
- **Region $-2 < x < -1$:** $(x+1)<0$ and $(x+2)>0 \implies y < 0$; $y \to -\infty$ near both asymptotes. By symmetry around $x = -1.5$, there is a local maximum at $(-1.5, -4)$ since $\frac{1}{(-0.5)(0.5)} = -4$.
- **Region $x < -2$:** Both factors negative $\implies y > 0$; $y \to +\infty$ as $x \to -2^-$, decreasing toward $0^+$ as $x \to -\infty$.""",
        is_sketch=True,
    ),

    # 1.6 Interview Set 6 - Interview 1 (3 problems)
    q(
        "1.6.1-p1",
        "1. Anonymous Problem Sets",
        "1.6 Interview Set 6 — Interview 1",
        "Improper Integral $\\int_0^1 \\frac{1}{x^n}\\,dx$ & Sketching",
        "Oxbridge Archive",
        "Set 6",
        "Calculus & Trigonometry",
        "Warm-up",
        r"""Sketch $y = \dfrac{1}{x}$ and $y = \dfrac{1}{\sqrt{x}}$ on $(0, 1)$. For what values of $n$ does
$$\int_0^1 \frac{1}{x^n}\,dx$$
have a finite value?""",
        [
            r"On $(0,1)$, is $x < \sqrt{x}$ or $x > \sqrt{x}$? Take reciprocals to see which curve sits higher!",
            r"Write the improper integral as $\lim_{\epsilon \to 0^+} \int_\epsilon^1 x^{-n}\,dx$, treating $n = 1$ separately.",
            r"For $n \ne 1$, determine when $\lim_{\epsilon \to 0^+} \epsilon^{1-n}$ is finite.",
        ],
        r"""On $(0,1)$, $0 < x < \sqrt{x} < 1$, so taking reciprocals gives $\frac{1}{x} > \frac{1}{\sqrt{x}}$; both equal $1$ at $x=1$ and tend to $+\infty$ as $x \to 0^+$, with $1/x$ strictly steeper and lying above $1/\sqrt{x}$.

Evaluating the integral:
- For $n \ne 1$:
$$\int_0^1 x^{-n}\,dx = \lim_{\epsilon \to 0^+} \left[\frac{x^{1-n}}{1-n}\right]_\epsilon^1 = \frac{1}{1-n} - \lim_{\epsilon \to 0^+} \frac{\epsilon^{1-n}}{1-n},$$
which is finite iff $1 - n > 0 \iff n < 1$ (giving value $\frac{1}{1-n}$).
- For $n = 1$: $\lim_{\epsilon \to 0^+} [-\ln\epsilon] = +\infty$ (divergent).
Thus the integral converges to a finite value iff **$n < 1$**.""",
        is_sketch=True,
    ),
    q(
        "1.6.1-p2",
        "1. Anonymous Problem Sets",
        "1.6 Interview Set 6 — Interview 1",
        "Graph Colouring & Chromatic Polynomials",
        "Oxbridge Archive",
        "Set 6",
        "Combinatorics",
        "Standard",
        r"""(a) For a star graph $K_{1,3}$ (one center vertex joined to $3$ leaves), in how many ways can it be coloured using $k$ colours such that no adjacent vertices share a colour?
(b) What if a new vertex is added and joined to all existing vertices of a graph $G$?""",
        [
            r"Colour the central vertex of $K_{1,3}$ first. How many colour choices remain for each of the $3$ outer leaves?",
            r"Notice the leaves do not connect to each other—only to the center!",
            r"For (b), if $V_{\text{new}}$ connects to *every* vertex in $G$, can any vertex in $G$ reuse the colour chosen for $V_{\text{new}}$?",
        ],
        r"""**(a)** Choose a colour for the center vertex in $k$ ways. Each of the $3$ leaves is adjacent *only* to the center, so each independently has $k - 1$ choices:
$$P(K_{1,3}, k) = k(k-1)^3.$$
(For $K_{1,m}$ in general, $P(K_{1,m}, k) = k(k-1)^m$.)

**(b)** Adding a universal vertex $V_{\text{new}}$ adjacent to every vertex of $G$ gives $k$ colour choices for $V_{\text{new}}$, leaving $k - 1$ valid colours to properly colour $G$:
$$P(G + v, k) = k \cdot P(G, k - 1).$$""",
    ),
    q(
        "1.6.1-p3",
        "1. Anonymous Problem Sets",
        "1.6 Interview Set 6 — Interview 1",
        "Quadratic and Exponential Inequalities",
        "Oxbridge Archive",
        "Set 6",
        "Algebra & Inequalities",
        "Warm-up",
        r"""Solve the inequalities:
(a) $x^2 - 3x + 2 \ge 0$
(b) $x^2 - 5x + 6 \ge 0$
(c) $25^x + 25 \cdot 5^{x-1} + 6 \ge 0$""",
        [
            r"Factorise the quadratics in (a) and (b) to find their roots.",
            r"In (c), rewrite $25^x = (5^x)^2$ and $25 \cdot 5^{x-1} = 5 \cdot 5^x$.",
            r"Wait—pay attention to the signs! Let $u = 5^x$. What is the sign of $u$ for all real $x$?",
        ],
        r"""**(a)** $(x-1)(x-2) \ge 0 \implies x \in (-\infty, 1] \cup [2, \infty)$.
**(b)** $(x-2)(x-3) \ge 0 \implies x \in (-\infty, 2] \cup [3, \infty)$.
**(c)** Let $u = 5^x > 0$. Since $25^x = u^2$ and $25\cdot 5^{x-1} = 5u$, the inequality is:
$$u^2 + 5u + 6 = (u+2)(u+3) \ge 0.$$
Because $u = 5^x > 0$ for all $x \in \mathbb{R}$, both $u+2 > 0$ and $u+3 > 0$, so their product is strictly positive everywhere. Hence **$x \in \mathbb{R}$** (all real numbers).""",
    ),

    # 1.6 Interview Set 6 - Interview 2 (3 problems)
    q(
        "1.6.2-p1",
        "1. Anonymous Problem Sets",
        "1.6 Interview Set 6 — Interview 2",
        "Fibonacci Partial Sums Identity",
        "Oxbridge Archive",
        "Set 6",
        "Number Theory",
        "Warm-up",
        r"""Write the first ten Fibonacci numbers ($F_1=1, F_2=1$) and first six partial sums $S_n = \sum_{k=1}^n F_k$. Prove that
$$S_n = F_{n+2} - 1.$$""",
        [
            r"List $1, 1, 2, 3, 5, 8, 13, 21, 34, 55$ and compute $S_1, S_2, \dots, S_6$.",
            r"Use induction on $n$: assume $S_k = F_{k+2} - 1$.",
            r"Add $F_{k+1}$ to both sides and apply the Fibonacci recurrence $F_{k+2} + F_{k+1} = F_{k+3}$.",
        ],
        r"""First ten Fibonacci numbers: $1, 1, 2, 3, 5, 8, 13, 21, 34, 55$.
First six partial sums: $S_1=1, S_2=2, S_3=4, S_4=7, S_5=12, S_6=20$ (matching $F_3-1, F_4-1, \dots, F_8-1$).

**Proof by induction:**
- Base case $n=1$: $S_1 = 1 = 2 - 1 = F_3 - 1$.
- Inductive step: Assume $S_k = F_{k+2} - 1$. Then:
$$S_{k+1} = S_k + F_{k+1} = (F_{k+2} - 1) + F_{k+1} = (F_{k+2} + F_{k+1}) - 1 = F_{k+3} - 1.$$
Thus $S_n = F_{n+2} - 1$ for all $n \ge 1$.""",
    ),
    q(
        "1.6.2-p2",
        "1. Anonymous Problem Sets",
        "1.6 Interview Set 6 — Interview 2",
        "Zeckendorf's Theorem & Representation of 50",
        "Oxbridge Archive",
        "Set 6",
        "Number Theory",
        "Standard",
        r"""Express $50$ as a sum of distinct Fibonacci numbers. Can this be done for any positive integer?""",
        [
            r"Try a greedy approach: subtract the largest Fibonacci number $\le 50$, then repeat on the remainder.",
            r"To prove it works for *any* positive integer $N$ (and even avoids consecutive Fibonacci numbers!), use strong induction.",
            r"If $F_k \le N < F_{k+1}$, show that $N - F_k < F_{k-1}$ so the greedy algorithm terminates strictly and never uses consecutive terms.",
        ],
        r"""Using the greedy algorithm:
1. Largest Fibonacci $\le 50$ is $34$ (remainder $16$).
2. Largest Fibonacci $\le 16$ is $13$ (remainder $3$).
3. $3$ is a Fibonacci number.
Thus: $50 = 34 + 13 + 3 = F_9 + F_7 + F_4$.

**Yes, for every positive integer $N$** (Zeckendorf's Theorem, uniquely if using non-consecutive Fibonacci numbers): Let $F_k$ be the largest Fibonacci number $\le N$, so $F_k \le N < F_{k+1} = F_k + F_{k-1}$. Then $0 \le N - F_k < F_{k-1} < F_k$. By strong induction, $N - F_k$ is a sum of distinct (non-consecutive) Fibonacci numbers strictly smaller than $F_{k-1}$, so adding $F_k$ gives a valid sum of distinct Fibonacci numbers for $N$.""",
    ),
    q(
        "1.6.2-p3",
        "1. Anonymous Problem Sets",
        "1.6 Interview Set 6 — Interview 2",
        "Parametric Curves & Logarithmic Spiral",
        "Oxbridge Archive",
        "Set 6",
        "Graph Sketching",
        "Standard",
        r"""Sketch the parametric curves:
(a) $x(t) = t,\; y(t) = t^2$
(b) $x(t) = \sin t,\; y(t) = \cos t$
(c) $x(t) = e^{-2t} \sin t,\; y(t) = e^{-2t} \cos t$""",
        [
            r"In (a) and (b), eliminate $t$. For (b), check the starting point at $t=0$ and direction of travel!",
            r"In (c), compute $r(t) = \sqrt{x(t)^2 + y(t)^2}$ to convert to polar coordinates.",
            r"What happens to $r(t)$ and the angle as $t$ goes from $0$ to $+\infty$, and as $t \to -\infty$?",
        ],
        r"""**(a)** $y = x^2$: standard upward parabola with vertex $(0,0)$, traced left-to-right as $t$ increases.
**(b)** $x^2 + y^2 = 1$: unit circle centered at $(0,0)$, starting at $(0,1)$ at $t=0$ and traversed **clockwise**.
**(c)** Notice $r(t) = \sqrt{x^2 + y^2} = e^{-2t}$, and polar angle is $\theta(t) = \frac{\pi}{2} - t$. This is a **logarithmic spiral**: starting at $(0,1)$ for $t=0$, as $t \to +\infty$ it spirals **clockwise** inward toward the origin with exponentially decaying radius; as $t \to -\infty$ it spirals outward infinitely.""",
        is_sketch=True,
    ),

    # 1.7 Interview Set 7 (4 problems)
    q(
        "1.7-p1",
        "1. Anonymous Problem Sets",
        "1.7 Interview Set 7",
        "Minimum & Expected Maximum of $n$ Die Rolls",
        "Oxbridge Archive",
        "Set 7",
        "Probability",
        "Standard",
        r"""A fair six-sided die is rolled $n$ times.
(a) What is the probability that the smallest number rolled is exactly $3$?
(b) What is the expected value of the highest score obtained after $n$ rolls?""",
        [
            r"For (a), think about events $\{M \ge 3\}$ vs $\{M \ge 4\}$. How does $\{M = 3\}$ relate to them?",
            r"For (b), write the CDF $P(X \le k) = (k/6)^n$ for the maximum score $X \in \{1,\dots,6\}$.",
            r"Use the discrete tail-sum formula $\mathbb{E}[X] = \sum_{k=0}^{5} P(X > k)$ or $\sum_{k=1}^6 k [P(X\le k)-P(X\le k-1)]$.",
        ],
        r"""**(a)** Let $M$ be the minimum roll. $\{M \ge 3\}$ means all $n$ rolls are in $\{3,4,5,6\}$, probability $(4/6)^n = (2/3)^n$. $\{M \ge 4\}$ means all rolls are in $\{4,5,6\}$, probability $(3/6)^n = (1/2)^n$.
$$P(M = 3) = P(M \ge 3) - P(M \ge 4) = \left(\frac{2}{3}\right)^n - \left(\frac{1}{2}\right)^n.$$

**(b)** Let $X$ be the maximum roll, so $P(X \le k) = (k/6)^n$ for $k=0,\dots,6$. By the tail probability identity:
$$\mathbb{E}[X] = \sum_{k=0}^{5} P(X > k) = \sum_{k=0}^{5} \left[1 - \left(\frac{k}{6}\right)^n\right] = 6 - \sum_{k=1}^{5} \left(\frac{k}{6}\right)^n.$$""",
    ),
    q(
        "1.7-p2",
        "1. Anonymous Problem Sets",
        "1.7 Interview Set 7",
        "Definite Integrals of $\\cos^4\\theta$ and $\\cos^5\\theta$",
        "Oxbridge Archive",
        "Set 7",
        "Calculus & Trigonometry",
        "Standard",
        r"""Calculate $\displaystyle\int_0^\pi \cos^4\theta\,d\theta$ and $\displaystyle\int_0^\pi \cos^5\theta\,d\theta$.""",
        [
            r"For $\cos^5\theta$, test the symmetry substitution $u = \pi - \theta$ around $\theta = \pi/2$!",
            r"For $\cos^4\theta$, either use double-angle identities $\cos^2\theta = \frac{1+\cos 2\theta}{2}$, or write $\cos\theta = \frac{e^{i\theta}+e^{-i\theta}}{2}$ and expand with the binomial theorem.",
            r"Notice all non-constant $\cos(m\theta)$ terms integrate to $0$ over $[0, \pi]$ for even $m$!",
        ],
        r"""**1. $\int_0^\pi \cos^5\theta\,d\theta$:**
Using $\theta = \pi - u$, $\cos(\pi - u) = -\cos u$, so $\cos^5(\pi - u) = -\cos^5 u$. By antisymmetry about $\pi/2$:
$$\int_0^\pi \cos^5\theta\,d\theta = 0.$$

**2. $\int_0^\pi \cos^4\theta\,d\theta$:**
Using $\cos\theta = \frac{e^{i\theta}+e^{-i\theta}}{2}$:
$$\cos^4\theta = \frac{1}{16}\left(e^{4i\theta} + 4e^{2i\theta} + 6 + 4e^{-2i\theta} + e^{-4i\theta}\right) = \frac{1}{8}\cos(4\theta) + \frac{1}{2}\cos(2\theta) + \frac{3}{8}.$$
Integrating from $0$ to $\pi$, the cosine terms vanish, leaving:
$$\int_0^\pi \cos^4\theta\,d\theta = \frac{3\pi}{8}.$$""",
    ),
    q(
        "1.7-p3",
        "1. Anonymous Problem Sets",
        "1.7 Interview Set 7",
        "Anagrams of GAUSS and RAMANUJAN",
        "Oxbridge Archive",
        "Set 7",
        "Combinatorics",
        "Warm-up",
        r"""How many anagrams of **GAUSS** and **RAMANUJAN** are there?""",
        [
            r"Count the total number of letters $n$ and the multiplicity $n_i$ of each repeated letter.",
            r"Use the multinomial formula $\frac{n!}{n_1! n_2! \cdots}$.",
            r"For RAMANUJAN, carefully check every letter frequency (how many A's? how many N's?). Wait—check RAMANUJAN carefully: R(1), A(3), M(1), N(2)!! Wait: R-A-M-A-N-U-J-A-N has TWO N's!",
        ],
        r"""- **GAUSS:** $5$ letters with letter frequencies G:1, A:1, U:1, S:2.
$$\frac{5!}{2!} = \frac{120}{2} = \mathbf{60}.$$
- **RAMANUJAN:** $9$ letters: R:1, A:3, M:1, N:2, U:1, J:1 (note: carefully count both **N**'s—there are 3 A's and 2 N's!).
$$\frac{9!}{3!\,2!} = \frac{362{,}880}{6 \times 2} = \mathbf{30{,}240}.$$
*(Note: The archive PDF solution only divided by $3! = 6$ to get $60{,}480$ overlooking the two N's; in an interview, catching both A's ($3!$) and N's ($2!$) gives the exact count $30{,}240$!)*""",
    ),
    q(
        "1.7-p4",
        "1. Anonymous Problem Sets",
        "1.7 Interview Set 7",
        "Two Projectiles Intersecting on the Ground",
        "Oxbridge Archive",
        "Set 7",
        "Mechanics",
        "Challenging",
        r"""A projectile is fired at angle $\pi/4$ with speed $v$. Later, a second projectile is fired from the same point at speed $2v$. What is the latest time $\Delta t$ at which the second projectile can be fired so that the two projectiles intersect on the ground?""",
        [
            r"Find the horizontal range $R_1$ and flight time $T_1$ of Projectile 1 ($V_1 = v, \theta_1 = \pi/4$).",
            r"Equate the range of Projectile 2 ($R_2 = \frac{(2v)^2 \sin(2\theta_2)}{g}$) to $R_1$ to find $\sin(2\theta_2)$.",
            r"There are two valid launch angles $\theta_2$ giving the same range! Which angle gives the *minimum* flight time $T_2$ so the delay $\Delta t = T_1 - T_2$ is maximized?",
        ],
        r"""For Projectile 1 ($\theta_1 = \pi/4, V_1 = v$):
$$T_1 = \frac{2v\sin(\pi/4)}{g} = \frac{\sqrt{2}\,v}{g}, \qquad R_1 = \frac{v^2\sin(\pi/2)}{g} = \frac{v^2}{g}.$$
For Projectile 2 ($V_2 = 2v$) to land at the same point $R_2 = R_1$:
$$\frac{4v^2\sin(2\theta_2)}{g} = \frac{v^2}{g} \implies \sin(2\theta_2) = \frac{1}{4}.$$
To maximize the launch delay $\Delta t = T_1 - T_2$, we minimize $T_2 = \frac{4v\sin\theta_2}{g}$ by choosing the **lower** trajectory angle: $2\theta_2 = \arcsin(1/4)$ ($\theta_2 \approx 7.24^\circ$).
Using $\cos(2\theta_2) = \frac{\sqrt{15}}{4}$ and the half-angle identity:
$$\sin\theta_2 = \sqrt{\frac{1 - \cos(2\theta_2)}{2}} = \sqrt{\frac{1 - \frac{\sqrt{15}}{4}}{2}} = \frac{\sqrt{4 - \sqrt{15}}}{2\sqrt{2}}.$$
Thus $T_2 = \frac{\sqrt{2(4-\sqrt{15})}\,v}{g}$, and the latest launch delay is:
$$\Delta t = T_1 - T_2 = \frac{v}{g}\left(\sqrt{2} - \sqrt{2(4 - \sqrt{15})}\right) = \frac{v}{g}\left(\sqrt{2} - (\sqrt{5}-\sqrt{3})\right) \approx 0.900\frac{v}{g}.$$""",
    ),

    # 1.8 Interview Set 8 (3 problems)
    q(
        "1.8-p1",
        "1. Anonymous Problem Sets",
        "1.8 Interview Set 8",
        "Intersecting Circles, Oxford-Cambridge & 3D Earth-Sun",
        "Oxbridge Archive",
        "Set 8",
        "Geometry",
        "Standard",
        r"""Solve $x^2 + y^2 = b$ and $(x-a)^2 + y^2 = b$ geometrically. Relate this to:
- Points equidistant from Oxford and Cambridge (80 miles apart) at distance 10, 40, or 50 miles.
- Points in 3D equidistant from the Earth and Sun at distance 50 million miles (if they are 80 million miles apart).""",
        [
            r"Interpret each equation as a circle of radius $\sqrt{b}$ centered at $(0,0)$ and $(a,0)$.",
            r"Subtract the two equations to find $x = a/2$, and discuss the three cases $b < a^2/4$, $b = a^2/4$, and $b > a^2/4$.",
            r"In 3D, what is the intersection of two equal spheres of radius $50$ whose centers are $80$ apart?",
        ],
        r"""Geometrically, these are two circles of radius $\sqrt{b}$ centered at $(0,0)$ and $(a,0)$. Subtracting gives $x = a/2$, and $y = \pm\sqrt{b - a^2/4}$:
- $b < a^2/4$: no intersection ($0$ solutions).
- $b = a^2/4$: tangent at $(a/2, 0)$ ($1$ solution).
- $b > a^2/4$: $2$ intersections at $(a/2, \pm\sqrt{b - a^2/4})$.

**Oxford & Cambridge ($d = 80$ mi, $a/2 = 40$ mi):**
- $10$ miles: Impossible ($10+10 < 80$).
- $40$ miles: Unique midpoint ($40$ miles from both).
- $50$ miles: Two points along the perpendicular bisector at distance $\sqrt{50^2 - 40^2} = 30$ miles.

**3D Earth & Sun:** Two spheres of radius $50$ million miles separated by $80$ million miles intersect in a **circle** of radius $30$ million miles lying in the perpendicular bisecting plane.""",
    ),
    q(
        "1.8-p2",
        "1. Anonymous Problem Sets",
        "1.8 Interview Set 8",
        "Envelope of the Gaussian Family $y = m e^{-m^2 x^2}$",
        "Oxbridge Archive",
        "Set 8",
        "Calculus & Trigonometry",
        "Challenging",
        r"""Sketch $y = m e^{-m^2 x^2}$ for $m > 0$. Find the envelope bounding all these curves.""",
        [
            r"Describe how the curve changes as $m$ increases: what happens to the peak height $y(0) = m$ and the width of the Gaussian bell?",
            r"To find the upper envelope at a fixed $x \ne 0$, maximize $y(m) = m e^{-m^2 x^2}$ with respect to the parameter $m > 0$.",
            r"Set $\frac{\partial y}{\partial m} = 0$, solve for $m$ in terms of $|x|$, and substitute back into $y$.",
        ],
        r"""For fixed $m > 0$, $y = me^{-m^2 x^2}$ is a bell-shaped Gaussian centered at $x=0$ with peak $(0, m)$ and width $\propto 1/m$: larger $m$ produces a taller, narrower spike.
For any fixed $x \ne 0$, maximize $y$ with respect to $m$:
$$\frac{\partial y}{\partial m} = e^{-m^2 x^2} + m(-2mx^2)e^{-m^2 x^2} = (1 - 2m^2 x^2)e^{-m^2 x^2} = 0 \implies m = \frac{1}{\sqrt{2}\,|x|}.$$
Substituting back gives the bounding envelope hyperbola:
$$y_{\text{env}}(x) = \frac{1}{\sqrt{2}\,|x|} e^{-1/2} = \frac{1}{\sqrt{2e}\,|x|}.$$""",
        is_sketch=True,
    ),
    q(
        "1.8-p3",
        "1. Anonymous Problem Sets",
        "1.8 Interview Set 8",
        "Smallest Integer with 14 Positive Divisors",
        "Oxbridge Archive",
        "Set 8",
        "Number Theory",
        "Warm-up",
        r"""How many positive divisors does $p^n q^m$ have (for distinct primes $p, q$)? Find the smallest positive integer with exactly $14$ positive factors.""",
        [
            r"Every divisor has the form $p^a q^b$ with $0 \le a \le n$ and $0 \le b \le m$. How many choices for $(a, b)$?",
            r"Factor $14$ into positive integers (e.g., $14 \times 1$ or $7 \times 2$) to see all possible prime-power exponent structures.",
            r"Assign the largest exponent to the smallest prime ($2$) and check both $2^{13}$ and $2^6 \cdot 3^1$.",
        ],
        r"""The positive divisors of $p^n q^m$ have $(n+1)(m+1)$ choices of exponents. Setting the number of divisors to $14$:
- $14 = 14 \times 1 \implies p^{13}$, smallest is $2^{13} = 8192$.
- $14 = 7 \times 2 \implies p^6 q^1$, smallest puts the bigger power on the smaller prime: $2^6 \cdot 3^1 = 64 \times 3 = \mathbf{192}$.

Comparing $192$ and $8192$, the smallest possible integer is **$192$**.""",
    ),

    # =========================================================================
    # 2. OXFORD OFFICIAL AND COLLEGE MATHEMATICS INTERVIEWS
    # =========================================================================
    q(
        "2.1-p1",
        "2. Oxford Official & College Interviews",
        "2.1 Oxford Admissions (James Munro, 2019)",
        "Equilateral & 3-4-5 Triangles on $y = x^2$",
        "Oxford (Admissions)",
        "2019",
        "Geometry",
        "Standard",
        r"""Points $A, B, C$ lie on the parabola $y = x^2$ with $B = (0,0)$.
(a) Where should $A$ and $C$ be placed so that $\triangle ABC$ is equilateral?
(b) Where could $A$ and $C$ be placed so that $\triangle ABC$ is a $3$-$4$-$5$ right triangle?""",
        [
            r"For (a), by symmetry around the $y$-axis set $C = (c, c^2)$ and $A = (-c, c^2)$ ($c>0$). Equate $AC^2 = BC^2$.",
            r"For (b), place the right angle at $B(0,0)$ first (can the right angle be at $A$ or $C$? Check that too!). If right angle is at $B$, how do gradients $BA$ and $BC$ relate?",
            r"With $A = (a, a^2)$ and $C = (c, c^2)$, perpendicularity at $B$ gives $ac = -1$. Compute the length ratio $BC / BA$ in terms of $c$ alone!",
        ],
        r"""**(a) Equilateral Triangle:** By symmetry, let $C = (c, c^2)$ and $A = (-c, c^2)$ with $c > 0$. Then $AC = 2c$ and $BC = \sqrt{c^2 + c^4}$. Equating $AC^2 = BC^2$:
$$4c^2 = c^2 + c^4 \implies c^2 = 3 \implies c = \sqrt{3}.$$
So $A = (-\sqrt{3}, 3)$ and $C = (\sqrt{3}, 3)$.

**(b) 3-4-5 Right Triangle (Right angle at $B$):** Let $A = (a, a^2)$ ($a<0$) and $C = (c, c^2)$ ($c>0$). Gradient of $BA$ is $a$, gradient of $BC$ is $c$, so $BA \perp BC \implies ac = -1 \implies a = -1/c$.
Setting $BC / BA = 4/3$:
$$\frac{c\sqrt{1+c^2}}{|a|\sqrt{1+a^2}} = \frac{c\sqrt{1+c^2}}{\frac{1}{c}\sqrt{1+\frac{1}{c^2}}} = c^3 = \frac{4}{3} \implies c = \left(\frac{4}{3}\right)^{1/3}.$$
Hence $A = \left(-\left(\frac{3}{4}\right)^{1/3},\, \left(\frac{3}{4}\right)^{2/3}\right)$ and $C = \left(\left(\frac{4}{3}\right)^{1/3},\, \left(\frac{4}{3}\right)^{2/3}\right)$ (and swapping $3$ and $4$ gives the symmetric mirror solutions; placing the right angle at $A$ or $C$ is also possible by solving the corresponding perpendicularity condition).""",
    ),
    q(
        "2.2-p1",
        "2. Oxford Official & College Interviews",
        "2.2 Oxford University College (2005)",
        "Central Warehouse on a Straight Road",
        "Oxford University College",
        "2005",
        "Algebra & Inequalities",
        "Warm-up",
        r"""Three towns $A, B, C$ lie on a straight road. Where should a central warehouse be built to minimize total daily travel distance?""",
        [
            r"Place the towns on the real line at coordinates $x_A < x_B < x_C$ and the warehouse at $x$.",
            r"Write the total distance $D(x) = |x - x_A| + |x - x_B| + |x - x_C|$.",
            r"Notice what $|x - x_A| + |x - x_C|$ simplifies to whenever $x_A \le x \le x_C$!",
        ],
        r"""Put the towns at $x_A < x_B < x_C$ and warehouse at $x$. Total one-way distance is:
$$D(x) = |x - x_A| + |x - x_B| + |x - x_C|.$$
By the triangle inequality, $|x - x_A| + |x - x_C| \ge x_C - x_A$, with equality for all $x \in [x_A, x_C]$. Simultaneously, $|x - x_B| \ge 0$ with equality iff $x = x_B \in [x_A, x_C]$.
Therefore, $D(x)$ is uniquely minimized at **$x = x_B$ (at town B, the median)**. *(Even if weighted equally for $n$ towns, the optimal location is the median!)*""",
    ),
    q(
        "2.2-p2",
        "2. Oxford Official & College Interviews",
        "2.2 Oxford University College (2005)",
        "Divisibility of $n^7 - n$ by $42$",
        "Oxford University College",
        "2005",
        "Number Theory",
        "Warm-up",
        r"""Prove that $n^7 - n$ is divisible by $42$ for all integers $n$, given that it is divisible by $7$.""",
        [
            r"Factor $42 = 2 \times 3 \times 7$ into pairwise coprime primes.",
            r"Since $7 \mid (n^7 - n)$ is given, we only need to check divisibility by $2$ and by $3$.",
            r"For divisibility by $3$, check $n \equiv 0, 1, 2 \pmod 3$, or factor $n^7 - n = n(n^6 - 1)$.",
        ],
        r"""Since $42 = 2 \times 3 \times 7$ and $2, 3, 7$ are pairwise coprime, it suffices to show $n^7 - n$ is divisible by $2$ and $3$ (divisibility by $7$ is given):
- **By 2:** $n^7$ and $n$ have the same parity, so $n^7 - n$ is even.
- **By 3:** Factor $n^7 - n = n(n^2 - 1)(n^4 + n^2 + 1) = (n-1)n(n+1)(n^4+n^2+1)$. Among three consecutive integers $(n-1)n(n+1)$, one is divisible by $3$ (or by Fermat's Little Theorem, $n^3 \equiv n \pmod 3 \implies n^7 \equiv n^3 \equiv n \pmod 3$).
Hence $42 \mid (n^7 - n)$ for all $n \in \mathbb{Z}$.""",
    ),
    q(
        "2.3-p1",
        "2. Oxford Official & College Interviews",
        "2.3 Oxford St. Catherine's / St. Anne's (2009)",
        "Wason Selection Task: [E], [9], [P]",
        "Oxford St. Catherine's / St. Anne's",
        "2009",
        "Logic & Game Theory",
        "Warm-up",
        r"""Four (or three) cards show **[ E ]**, **[ 9 ]**, **[ P ]**. Consider the statement: *"If a card has an even number on one side, it has a vowel on the other."* Which card(s) must you turn over to test the rule?""",
        [
            r"Write the statement in logical implication form $P \implies Q$, identifying $P$ ('even number') and $Q$ ('vowel').",
            r"When is $P \implies Q$ false? Only when $P$ is true AND $Q$ is false ($\neg Q$).",
            r"Test each visible card ([E], [9], [P]) against whether flipping it could possibly yield (Even, Consonant).",
        ],
        r"""The rule is $P \implies Q$ where $P = \text{even number}$ and $Q = \text{vowel}$. A card violates the rule iff it has **Even** ($P$) and **Consonant** ($\neg Q$).
- **[ E ]** ($Q$, vowel): Whether the back is even or odd, the rule is not violated. No need to turn.
- **[ 9 ]** ($\neg P$, odd): Cannot violate $P \implies Q$ regardless of the letter on the back. No need to turn.
- **[ P ]** ($\neg Q$, consonant): If the back is even ($P$), it disproves the claim!

You only need to turn over **[ P ]**.""",
    ),
    q(
        "2.3-p2",
        "2. Oxford Official & College Interviews",
        "2.3 Oxford St. Catherine's / St. Anne's (2009)",
        "Clock Hands Coincidence Time",
        "Oxford St. Catherine's / St. Anne's",
        "2009",
        "Algebra & Inequalities",
        "Warm-up",
        r"""A clock shows $12{:}00$. When do the minute and hour hands next coincide?""",
        [
            r"Find the angular speed of the minute hand ($6^\circ/\text{min}$) and the hour hand ($0.5^\circ/\text{min}$).",
            r"Use their relative angular speed ($5.5^\circ/\text{min}$): the minute hand must gain a full $360^\circ$ lap.",
            r"Compute $t = \frac{360}{11/2}$ minutes and express in hours, minutes, and seconds.",
        ],
        r"""Minute hand speed $= 360^\circ / 60\text{ min} = 6^\circ/\text{min}$.
Hour hand speed $= 360^\circ / 720\text{ min} = 0.5^\circ/\text{min}$.
Relative speed $= 5.5^\circ/\text{min} = \frac{11}{2}^\circ/\text{min}$.
Time to lap by $360^\circ$:
$$t = \frac{360}{11/2} = \frac{720}{11}\text{ min} = 65\frac{5}{11}\text{ min} = \text{1 hour, 5 minutes, and } 27\frac{3}{11}\text{ seconds (approx. } 1{:}05{:}27.27\text{)}.$$""",
    ),
    q(
        "2.3-p3",
        "2. Oxford Official & College Interviews",
        "2.3 Oxford St. Catherine's / St. Anne's (2009)",
        "The 100 Light Bulbs Problem",
        "Oxford St. Catherine's / St. Anne's",
        "2009",
        "Number Theory",
        "Warm-up",
        r"""$100$ light bulbs are initially all OFF. On pass $d$ ($d = 1, 2, \dots, 100$), you toggle every $d$-th bulb. After $100$ passes, how many bulbs are ON?""",
        [
            r"For a specific bulb $k$, which passes $d$ toggle bulb $k$?",
            r"Bulb $k$ finishes ON iff it is toggled an *odd* number of times—meaning $k$ has an odd number of positive divisors!",
            r"Divisors of $k$ pair up as $(d, k/d)$. When does a divisor fail to have a distinct partner?",
        ],
        r"""Bulb $k$ is toggled on pass $d$ iff $d \mid k$. Thus bulb $k$ is toggled $d(k)$ times (its number of positive divisors) and ends **ON** iff $d(k)$ is odd.
Since divisors pair up as $(d, k/d)$, $d(k)$ is odd iff $d = k/d$ for some divisor, i.e., **$k$ is a perfect square**.
The perfect squares $\le 100$ are $1^2, 2^2, \dots, 10^2$, so exactly **10** bulbs remain ON (and $90$ are OFF).""",
    ),
    q(
        "2.4-p1",
        "2. Oxford Official & College Interviews",
        "2.4 Oxford Trinity & Pembroke (2012)",
        "Pell-Type Diophantine Equation $2a^2 - b^2 = 1$",
        "Oxford Trinity & Pembroke",
        "2012",
        "Number Theory",
        "Standard",
        r"""Find positive integer solutions to $2a^2 - b^2 = 1$ (and describe parity/further solutions).""",
        [
            r"Test small positive integers $a = 1, 2, 3, \dots$ to spot the minimal solution $(1, 1)$.",
            r"Write $b^2 = 2a^2 - 1$. What must the parity of $b$ be? Substitute $b = 2k+1$ to determine the parity of $a$!",
            r"Now that you know $a$ must be odd, test $a = 3, 5$ to find the next solution $(5, 7)$.",
        ],
        r"""Rewriting as $b^2 = 2a^2 - 1$:
- **Smallest solution:** $a = 1 \implies b = 1$.
- **Parity:** Since $2a^2 - 1$ is odd, $b = 2k+1$ is odd. Then $2a^2 = (2k+1)^2 + 1 = 4k^2 + 4k + 2 \implies a^2 = 2k(k+1) + 1$, which is odd, so **$a$ must also be odd**.
- **Next solution:** Testing $a=3 \implies b^2=17$ (no); $a=5 \implies b^2 = 49 \implies b = 7$, giving $(5, 7)$ ($2\cdot 25 - 49 = 1$). *(In general, infinitely many solutions arise from $(1+\sqrt{2})^{2n+1} = b_n + a_n\sqrt{2}$.)*""",
    ),
    q(
        "2.4-p2",
        "2. Oxford Official & College Interviews",
        "2.4 Oxford Trinity & Pembroke (2012)",
        "Three Mutually Touching Unit Circles",
        "Oxford Trinity & Pembroke",
        "2012",
        "Geometry",
        "Warm-up",
        r"""Three unit circles are mutually tangent externally.
(a) Find the area enclosed between them.
(b) Find the radius of the small central circle touching all three.""",
        [
            r"Connect the centers of the three unit circles. What shape do they form, and what is its side length?",
            r"Subtract the three $60^\circ$ circular sectors inside the triangle from the triangle's area.",
            r"For (b), the center of the small inner circle is the centroid/circumcenter of the equilateral triangle. Relate the circumradius $R_{\triangle}$ to $1 + r$.",
        ],
        r"""**(a)** The centers form an equilateral triangle of side $2$ and area $A_{\triangle} = \frac{\sqrt{3}}{4}(2^2) = \sqrt{3}$.
The three $60^\circ$ sectors inside form half of a unit circle, area $3 \times \frac{1}{2}(1^2)\frac{\pi}{3} = \frac{\pi}{2}$.
Enclosed area $= \mathbf{\sqrt{3} - \frac{\pi}{2}}$.

**(b)** The distance from the center of the equilateral triangle to each vertex is $R_{\triangle} = \frac{\text{side}}{\sqrt{3}} = \frac{2}{\sqrt{3}}$. Since this distance equals $1 + r$:
$$r = \frac{2}{\sqrt{3}} - 1 = \frac{2\sqrt{3} - 3}{3} \approx 0.1547.$$""",
    ),
    q(
        "2.4-p3",
        "2. Oxford Official & College Interviews",
        "2.4 Oxford Trinity & Pembroke (2012)",
        "Sticky Notes Game (13 Notes, Take 1, 2, or 3)",
        "Oxford Trinity & Pembroke",
        "2012",
        "Logic & Game Theory",
        "Warm-up",
        r"""There are $13$ sticky notes in a line. Players take turns taking $1, 2$, or $3$ notes from the front.
- **Misère play (sad face on note 13):** You lose if forced to take note $13$.
- **Normal play (smiley face on note 13):** You win if you take note $13$.
What is the winning strategy in each case?""",
        [
            r"Work backwards! Since you can take $1, 2$, or $3$ notes, any turn pair can sum to $1 + 3 = 4$.",
            r"In Misère play, you want the opponent to be stuck with only note $13$ left—so you want to take note $12$. Which player can force taking multiples of $4$?",
            r"In Normal play, you want to take note $13$. Since $13 \equiv 1 \pmod 4$, how many should the first player take on move 1?",
        ],
        r"""Since $1+3 = 4$, you can always complement an opponent's move of $k$ with $4-k$.
- **Misère (avoid note 13):** You want to take note $12$ so only note $13$ remains for your opponent. Since $12$ is a multiple of $4$, **let the opponent go first**, then always take $4-k$, guaranteeing you hit notes $4, 8, 12$ and force them to take $13$.
- **Normal (claim note 13):** **Go first** and take **$1$ note** (leaving $12$), then complement every move with $4-k$ so you hit $5, 9, 13$ and win.""",
    ),
    q(
        "2.4-p4",
        "2. Oxford Official & College Interviews",
        "2.4 Oxford Trinity & Pembroke (2012)",
        "Vertices and Edges of an $n$-Dimensional Hypercube",
        "Oxford Trinity & Pembroke",
        "2012",
        "Combinatorics",
        "Warm-up",
        r"""Find the number of vertices and edges of an $n$-dimensional hypercube.""",
        [
            r"Think of vertices as binary coordinates $(x_1, x_2, \dots, x_n) \in \{0, 1\}^n$. How many vertices are there?",
            r"How many edges meet at each single vertex (i.e., how many coordinates can you flip by $1$ step)?",
            r"Use the Handshaking Lemma ($2E = \sum \deg(v)$) to avoid double-counting each edge!",
        ],
        r"""- **Vertices:** Each vertex is a tuple in $\{0,1\}^n$, giving **$2^n$ vertices**.
- **Edges:** From any vertex, an edge connects to vertices differing in exactly one coordinate, so every vertex has degree $n$. By the Handshaking Lemma (each edge touches $2$ vertices):
$$E = \frac{2^n \times n}{2} = \mathbf{n 2^{n-1}}.$$""",
    ),

    # =========================================================================
    # 3. CAMBRIDGE COLLEGE MATHEMATICS INTERVIEWS
    # =========================================================================
    q(
        "3.1-p1",
        "3. Cambridge College Interviews",
        "3.1 Cambridge Trinity Hall (2004/2005)",
        "Divisibility of $n^3 - n$ by $6$ and $24$",
        "Cambridge Trinity Hall",
        "2004/2005",
        "Number Theory",
        "Warm-up",
        r"""Prove that $n^3 - n$ is divisible by $6$ for all integers $n$, and by $24$ if $n$ is odd.""",
        [
            r"Factorise $n^3 - n$ completely into three linear factors.",
            r"Why must the product of three consecutive integers be divisible by $2$ and $3$?",
            r"If $n = 2k+1$ is odd, inspect the two even factors $(n-1)$ and $(n+1)$: they are consecutive even integers!",
        ],
        r"""Factorise: $n^3 - n = (n-1)n(n+1)$, the product of three consecutive integers. At least one is even and exactly one is divisible by $3$, so $6 \mid (n^3 - n)$.
If $n = 2k+1$ is odd, then $n-1 = 2k$ and $n+1 = 2(k+1)$ are consecutive even integers, so one of $k, k+1$ is even, meaning $(n-1)(n+1) = 4k(k+1)$ is divisible by $8$. Since $\gcd(8,3) = 1$, $24 \mid (n^3 - n)$.""",
    ),
    q(
        "3.1-p2",
        "3. Cambridge College Interviews",
        "3.1 Cambridge Trinity Hall (2004/2005)",
        "Hollow Cone Filled Halfway Up",
        "Cambridge Trinity Hall",
        "2004/2005",
        "Geometry",
        "Warm-up",
        r"""A hollow cone is held vertex-down and filled halfway up (to half its height). What proportion of its total volume is filled?""",
        [
            r"Consider a cross-section through the axis: the liquid forms a smaller cone similar to the full cone.",
            r"If the height scales by $\frac{1}{2}$, how does the volume scale in 3D?",
        ],
        r"""By similar triangles, the liquid forms a smaller cone of height $\frac{1}{2}H$ and radius $\frac{1}{2}R$. Volume scales as the cube of linear dimensions:
$$V_{\text{filled}} = \left(\frac{1}{2}\right)^3 V_{\text{total}} = \mathbf{\frac{1}{8}} V_{\text{total}} \quad (12.5\%).$$""",
    ),
    q(
        "3.1-p3",
        "3. Cambridge College Interviews",
        "3.1 Cambridge Trinity Hall (2004/2005)",
        "Two Children Conditional Probability",
        "Cambridge Trinity Hall",
        "2004/2005",
        "Probability",
        "Warm-up",
        r"""A family has two children. You are told that at least one is a daughter. What is the probability that they have at least one son?""",
        [
            r"Write down the full sample space of two children ordered by birth: $\{BB, BG, GB, GG\}$.",
            r"Cross out the outcomes ruled out by 'at least one daughter' to get the reduced sample space.",
            r"Count how many of the remaining equally likely outcomes include a son.",
        ],
        r"""The full sample space is $\{BB, BG, GB, GG\}$ (each probability $1/4$). Conditioning on 'at least one daughter' reduces the space to $\{BG, GB, GG\}$ ($3$ equally likely outcomes). Two of these ($\{BG, GB\}$) have a son:
$$P(\text{at least one son} \mid \text{at least one daughter}) = \mathbf{\frac{2}{3}}.$$""",
    ),
    q(
        "3.1-p4",
        "3. Cambridge College Interviews",
        "3.1 Cambridge Trinity Hall (2004/2005)",
        "Minimum of $x^2 + y^2 + \\frac{1}{x^2+y^2}$",
        "Cambridge Trinity Hall",
        "2004/2005",
        "Algebra & Inequalities",
        "Warm-up",
        r"""Find the minimum value of
$$x^2 + y^2 + \frac{1}{x^2 + y^2}$$
for $(x, y) \ne (0,0)$.""",
        [
            r"Substitute a single positive variable $u = x^2 + y^2 > 0$.",
            r"Minimize $u + \frac{1}{u}$ for $u > 0$ using the AM-GM inequality (or differentiation / completing the square $(\sqrt{u} - 1/\sqrt{u})^2$).",
        ],
        r"""Let $u = x^2 + y^2 > 0$. By AM-GM (or $(\sqrt{u} - \frac{1}{\sqrt{u}})^2 \ge 0$):
$$u + \frac{1}{u} \ge 2\sqrt{u \cdot \frac{1}{u}} = 2,$$
with equality iff $u = 1$, i.e., at any point on the unit circle $x^2 + y^2 = 1$. Thus the minimum value is **2**.""",
    ),
    q(
        "3.1-p5",
        "3. Cambridge College Interviews",
        "3.1 Cambridge Trinity Hall (2004/2005)",
        "Cubic Roots in Geometric Progression",
        "Cambridge Trinity Hall",
        "2004/2005",
        "Algebra & Inequalities",
        "Warm-up",
        r"""The roots of $x^3 - 13x^2 + 39x - 27 = 0$ are in geometric progression. Find the roots.""",
        [
            r"Write three terms in geometric progression symmetrically as $\frac{a}{r},\, a,\, ar$.",
            r"Apply Vieta's formula for the *product* of the roots first! What does $\left(\frac{a}{r}\right) a (ar)$ immediately give you?",
            r"Once you know the middle root $a$, use the sum of roots $\frac{a}{r} + a + ar = 13$ to solve for $r$ (and check the $x^1$ coefficient $39$!).",
        ],
        r"""Write the roots as $\frac{a}{r}, a, ar$. By Vieta's formulas:
- Product of roots: $\left(\frac{a}{r}\right) a (ar) = a^3 = 27 \implies a = 3$.
- Sum of roots: $\frac{3}{r} + 3 + 3r = 13 \implies 3r^2 - 10r + 3 = 0 \implies (3r-1)(r-3) = 0$, so $r = 3$ or $r = 1/3$.
Both give the roots **$1, 3, 9$** (and checking pairwise products: $1\cdot 3 + 3\cdot 9 + 1\cdot 9 = 39$, matching the $x$ coefficient!).""",
    ),
    q(
        "3.2-p1",
        "3. Cambridge College Interviews",
        "3.2 Cambridge Emmanuel (Dec 2015)",
        "Locus of Constant Subtended Angle $\\angle OPA = c$",
        "Cambridge Emmanuel",
        "Dec 2015",
        "Geometry",
        "Standard",
        r"""Find the locus of points $P(x, y)$ in the upper half-plane ($y > 0$) such that the angle $\angle OPA = c$ is constant, where $O = (0,0)$ and $A = (1,0)$.""",
        [
            r"Think geometrically first: what famous theorem describes all points $P$ from which a fixed chord $OA$ subtends a constant angle $c$?",
            r"Try the special case $c = \pi/2$ first (Thales' Theorem!), then generalize using the Inscribed Angle Theorem.",
            r"Compute the center $(1/2, y_0)$ and radius $R$ of the circle in terms of $c$ using $2R = \frac{OA}{\sin c}$.",
        ],
        r"""By the **Inscribed Angle Theorem** (angles in the same segment), the locus in the upper half-plane $y > 0$ is an open **circular arc** passing through $O(0,0)$ and $A(1,0)$ (excluding $O$ and $A$ themselves).
The circle's center lies on the perpendicular bisector $x = 1/2$, and by the Extended Law of Sines:
$$2R = \frac{OA}{\sin c} \implies R = \frac{1}{2\sin c}.$$
If $c = \pi/2$, it is the upper semicircle $(x - 1/2)^2 + y^2 = 1/4$ ($y > 0$); in general, the center is $\left(\frac{1}{2},\, \frac{1}{2}\cot c\right)$ and the locus is the arc $\left(x - \frac{1}{2}\right)^2 + \left(y - \frac{1}{2}\cot c\right)^2 = \frac{1}{4\sin^2 c}$ for $y > 0$ (or wait: check whether $c$ is acute or obtuse—the major arc when $c < \pi/2$, minor arc when $c > \pi/2$!).""",
    ),
    q(
        "3.2-p2",
        "3. Cambridge College Interviews",
        "3.2 Cambridge Emmanuel (Dec 2015)",
        "Penney's Coin Game (HH vs TT, HT, TH)",
        "Cambridge Emmanuel",
        "Dec 2015",
        "Probability",
        "Standard",
        r"""A fair coin is tossed repeatedly until one of two chosen 2-toss patterns appears:
(a) HH vs TT
(b) HH vs HT
(c) HH vs TH
In each case, find the probability that HH appears first.""",
        [
            r"For (a), use symmetry between Heads and Tails.",
            r"For (b), track what happens on the first toss: if Tails, wait for the first Head—wait no: in HH vs HT, once *any* H appears, look at the very next toss! If T, HT wins immediately!",
            r"For (c), ask: if a T EVER appears before HH has occurred, can HH EVER occur without TH occurring first?!",
        ],
        r"""**(a) HH vs TT:** By symmetry, $P(\text{HH}) = \mathbf{\frac{1}{2}}$.

**(b) HH vs HT:** Wait for the first time `H` appears (if the first toss is `T`, keep tossing until `H` appears). Immediately after that first `H`, the next toss is either `H` (giving `HH`, so HH wins) or `T` (giving `HT`, so HT wins)—wait: what if it started `TH`? After `T...TH`, the next toss is `H` (HH wins) or `T` (`HT` wins)! Wait—let's check!
Careful! In **HH vs HT**:
- Toss 1 = `H` (prob $1/2$): Toss 2 = `H` $\implies$ HH wins ($1/4$); Toss 2 = `T` $\implies$ HT wins ($1/4$).
- Toss 1 = `T` (prob $1/2$): keep tossing until first `H`. From that `H`, next toss is `H` (HH wins!) or `T` (HT wins!), wait: that's $1/2$ each!
Wait: does $P(\text{HH beats HT}) = 1/2$?! Let's check with Markov chains!
State Start: $\frac{1}{2} p_H + \frac{1}{2} p_T$.
State $T$: $\frac{1}{2} p_H + \frac{1}{2} p_T \implies p_T = p_{\text{Start}}$.
State $H$: $\frac{1}{2}(1) + \frac{1}{2}(0) = \frac{1}{2}$!
Yes!! For **HH vs HT**, $P(\text{HH}) = \frac{1}{2}$! (Whereas for **TH vs HH**, let's check!)

**(c) HH vs TH:** If the sequence *ever* has a `T` before `HH` occurs, the moment the next `H` appears it forms `TH`, ending the game in favour of `TH`! Thus `HH` can win **only if the first two tosses are HH**:
$$P(\text{HH beats TH}) = \mathbf{\frac{1}{4}}, \qquad P(\text{TH beats HH}) = \mathbf{\frac{3}{4}}.$$
*(Note: The archive PDF mistakenly wrote $1/4$ for HH vs HT too; spotting that HH vs HT is $1/2$ whereas HH vs TH is $1/4$ is a classic Cambridge interview distinction!)*""",
    ),
    q(
        "3.3-p1",
        "3. Cambridge College Interviews",
        "3.3 Cambridge Jesus (Jan 2016)",
        "Perfect Numbers & Euclid-Euler Theorem",
        "Cambridge Jesus",
        "Jan 2016",
        "Number Theory",
        "Challenging",
        r"""A positive integer is *perfect* if it equals the sum of its proper positive divisors (or equivalently $\sigma(N) = 2N$).
(a) Can a prime number be perfect?
(b) Can a perfect number be of the form $p^n$ (prime power)?
(c) Can a perfect number be of the form $pq$ (product of two distinct primes)?
(d) Prove the Euclid-Euler theorem: if $2^p - 1$ is prime, then $2^{p-1}(2^p - 1)$ is perfect.
(e) Prove that the sum of the reciprocals of all positive divisors of a perfect number is $2$.""",
        [
            r"For (b), sum the geometric series $1 + p + p^2 + \dots + p^{n-1} = \frac{p^n - 1}{p - 1}$ and compare with $p^n$.",
            r"For (c), write $pq = 1 + p + q$ and factor $(p-1)(q-1) = 2$! Wait—is $pq = 6$ allowed?!",
            r"For (d), use multiplicativity of $\sigma(N)$: $\sigma(2^{p-1}q) = \sigma(2^{p-1})\sigma(q)$. For (e), pair $d$ with $N/d$.",
        ],
        r"""**(a) No.** For prime $p$, its only proper divisor is $1 \ne p$.
**(b) No.** Proper divisors of $p^n$ sum to $1 + p + \dots + p^{n-1} = \frac{p^n - 1}{p - 1} < p^n$ since $p \ge 2$.
**(c) Only $6$!** Proper divisors of $pq$ ($p < q$ primes) sum to $1 + p + q = pq \iff (p-1)(q-1) = 2$. Since $p < q$ are primes, $p - 1 = 1 \implies p = 2$ and $q - 1 = 2 \implies q = 3$, giving **$pq = 6$** (the unique perfect number of the form $pq$).
**(d)** Let $N = 2^{p-1}q$ where $q = 2^p - 1$ is prime (note $\gcd(2^{p-1}, q) = 1$). Using multiplicativity of the divisor sum function $\sigma$:
$$\sigma(N) = \sigma(2^{p-1})\sigma(q) = (2^p - 1)(q + 1) = (2^p - 1)2^p = 2N,$$
so the sum of proper divisors is $2N - N = N$, meaning $N$ is perfect.
**(e)** As $d$ runs over all divisors of $N$, so does $N/d$:
$$\sum_{d \mid N} \frac{1}{d} = \sum_{d \mid N} \frac{d}{N} = \frac{\sigma(N)}{N} = \frac{2N}{N} = 2.$$""",
    ),

    # =========================================================================
    # 4. OXFORD INTERVIEW QUESTIONS (ARCHIVE SHEET G)
    # =========================================================================
    q(
        "4-p1",
        "4. Oxford Interview Questions (Archive Sheet G)",
        "4.1 Archive Sheet G",
        "Rolle's Theorem on $\\cos x - \\alpha x - \\beta = 0$",
        "Oxford Archive (Sheet G)",
        "Archive G",
        "Calculus & Trigonometry",
        "Warm-up",
        r"""Given that $\cos x - \alpha x - \beta = 0$ has $2$ distinct real solutions, show that $\sin x = -\alpha$ has at least one solution.""",
        [
            r"Define $f(x) = \cos x - \alpha x - \beta$. What do the two solutions $x_1 < x_2$ tell you about $f(x_1)$ and $f(x_2)$?",
            r"Is $f(x)$ continuous and differentiable everywhere? Apply Rolle's Theorem on $[x_1, x_2]$.",
        ],
        r"""Let $f(x) = \cos x - \alpha x - \beta$. Since $f(x_1) = f(x_2) = 0$ for two distinct roots $x_1 < x_2$, and $f$ is continuous and differentiable on $\mathbb{R}$, by **Rolle's Theorem** there exists $c \in (x_1, x_2)$ such that:
$$f'(c) = -\sin c - \alpha = 0 \implies \sin c = -\alpha.$$
Thus $\sin x = -\alpha$ has at least one real solution.""",
    ),
    q(
        "4-p2",
        "4. Oxford Interview Questions (Archive Sheet G)",
        "4.1 Archive Sheet G",
        "Party Handshake Theorem (Pigeonhole Principle)",
        "Oxford Archive (Sheet G)",
        "Archive G",
        "Combinatorics",
        "Warm-up",
        r"""Prove that at any $N$-person party ($N \ge 2$), at least two people have the exact same number of friends at the party (assuming friendship is mutual).""",
        [
            r"What are the possible numbers of friends a person at an $N$-person party can have?",
            r"Can a person with $0$ friends and a person with $N-1$ friends coexist at the same party?",
            r"Now count the remaining possible friend counts (pigeonholes) vs the $N$ people (pigeons).",
        ],
        r"""Each of the $N$ people can have between $0$ and $N-1$ friends ($N$ possible numbers). However, $0$ and $N-1$ cannot both occur: if someone is friends with everyone ($N-1$ friends), nobody can have $0$ friends (and vice versa).
Thus all $N$ people's friend counts fall into either $\{0, 1, \dots, N-2\}$ or $\{1, 2, \dots, N-1\}$—only **$N - 1$** possible values. By the **Pigeonhole Principle**, at least two people have the same number of friends.""",
    ),
    q(
        "4-p3",
        "4. Oxford Interview Questions (Archive Sheet G)",
        "4.1 Archive Sheet G",
        "Rearrangement Inequality ($\\frac{x}{b} + \\frac{y}{a} > \\frac{x}{a} + \\frac{y}{b}$)",
        "Oxford Archive (Sheet G)",
        "Archive G",
        "Algebra & Inequalities",
        "Warm-up",
        r"""For $x > y > 0$ and $a > b > 0$, show that $\dfrac{x}{b} + \dfrac{y}{a} > \dfrac{x}{a} + \dfrac{y}{b}$, and find the maximum sum for $3$ terms ($x>y>z>0$ and $a>b>c>0$).""",
        [
            r"Subtract the RHS from the LHS and factor out $(x - y)$.",
            r"Check the signs of $(x - y)$ and $\left(\frac{1}{b} - \frac{1}{a}\right)$.",
            r"For $3$ terms, order the reciprocals $\frac{1}{c} > \frac{1}{b} > \frac{1}{a}$ and apply the Rearrangement Inequality.",
        ],
        r"""Consider the difference:
$$\left(\frac{x}{b} + \frac{y}{a}\right) - \left(\frac{x}{a} + \frac{y}{b}\right) = (x - y)\left(\frac{1}{b} - \frac{1}{a}\right).$$
Since $x > y \implies x-y > 0$ and $a > b > 0 \implies \frac{1}{b} > \frac{1}{a}$, the product is strictly positive, proving $\frac{x}{b} + \frac{y}{a} > \frac{x}{a} + \frac{y}{b}$.
For $x > y > z > 0$ and $a > b > c > 0$, we have $\frac{1}{c} > \frac{1}{b} > \frac{1}{a}$; by the Rearrangement Inequality, pairing largest with largest maximizes the sum:
$$\text{Maximum} = \frac{x}{c} + \frac{y}{b} + \frac{z}{a}.$$""",
    ),
    q(
        "4-p4",
        "4. Oxford Interview Questions (Archive Sheet G)",
        "4.1 Archive Sheet G",
        "Differentiating Under Integral Limit (Leibniz Rule)",
        "Oxford Archive (Sheet G)",
        "Archive G",
        "Calculus & Trigonometry",
        "Warm-up",
        r"""Evaluate $\displaystyle \frac{d}{dx} \int_0^{x^2} \frac{e^y}{1 + y^2}\,dy$.""",
        [
            r"Let $F(u) = \int_0^u \frac{e^y}{1+y^2}\,dy$. You are differentiating $F(x^2)$ with respect to $x$.",
            r"Combine the Fundamental Theorem of Calculus ($F'(u)$) with the Chain Rule ($u'(x) = 2x$).",
        ],
        r"""By the Fundamental Theorem of Calculus and the Chain Rule (Leibniz rule):
$$\frac{d}{dx} \int_0^{u(x)} f(y)\,dy = f(u(x)) \cdot u'(x).$$
With $f(y) = \frac{e^y}{1+y^2}$ and $u(x) = x^2$ ($u'(x) = 2x$):
$$\frac{d}{dx} \int_0^{x^2} \frac{e^y}{1+y^2}\,dy = \frac{e^{x^2}}{1 + (x^2)^2} \cdot 2x = \frac{2x e^{x^2}}{1 + x^4}.$$""",
    ),
    q(
        "4-p5",
        "4. Oxford Interview Questions (Archive Sheet G)",
        "4.1 Archive Sheet G",
        "Convergence of $\\int_1^\\infty \\frac{1}{x} \\sin(1/x)\\,dx$",
        "Oxford Archive (Sheet G)",
        "Archive G",
        "Calculus & Trigonometry",
        "Standard",
        r"""Determine whether the improper integral $\displaystyle \int_1^\infty \frac{1}{x} \sin\!\left(\frac{1}{x}\right) dx$ converges.""",
        [
            r"Notice the $\frac{1}{x}$ inside $\sin(1/x)$. Try the substitution $u = 1/x$!",
            r"Compute $dx = -\frac{1}{u^2}\,du$ and transform the limits $x = 1$ and $x \to \infty$.",
            r"Inspect the transformed integrand $\frac{\sin u}{u}$ on $[0, 1]$—does it blow up at $u = 0$?",
        ],
        r"""Substitute $u = 1/x$, so $x = 1/u$ and $dx = -\frac{1}{u^2}\,du$. As $x$ goes from $1$ to $\infty$, $u$ goes from $1$ to $0^+$:
$$\int_1^\infty \frac{1}{x}\sin\!\left(\frac{1}{x}\right)dx = \int_1^0 u \sin(u) \left(-\frac{1}{u^2}\,du\right) = \int_0^1 \frac{\sin u}{u}\,du.$$
Since $\lim_{u\to 0} \frac{\sin u}{u} = 1$, the integrand has only a removable discontinuity at $u=0$ and is bounded ($|\frac{\sin u}{u}| \le 1$) and continuous on $[0, 1]$. Therefore the integral **converges** to a finite value (roughly $0.946$). *(Alternatively, for $x \ge 1$, $0 \le \frac{1}{x}\sin(1/x) \le \frac{1}{x^2}$, and $\int_1^\infty \frac{dx}{x^2} = 1$ converges by comparison!)*""",
    ),

    # =========================================================================
    # 5. PAST OXBRIDGE INTERVIEW QUESTIONS (ARCHIVE SHEET H)
    # =========================================================================
    q(
        "5-p1",
        "5. Past Oxbridge Questions (Archive Sheet H)",
        "5.1 Archive Sheet H",
        "Divisibility of $3n^2 + 9n + 6$ by $6$",
        "Oxbridge Archive (Sheet H)",
        "Archive H",
        "Number Theory",
        "Warm-up",
        r"""Show that $3n^2 + 9n + 6$ is divisible by $6$ for all $n \in \mathbb{Z}$.""",
        [
            r"Factor out $3$ first.",
            r"Factor the remaining quadratic $n^2 + 3n + 2$ into two consecutive integers.",
        ],
        r"""Factorise:
$$3n^2 + 9n + 6 = 3(n^2 + 3n + 2) = 3(n+1)(n+2).$$
Since $(n+1)$ and $(n+2)$ are two consecutive integers, one of them is even, so $(n+1)(n+2) = 2k$ for some $k \in \mathbb{Z}$. Hence $3n^2 + 9n + 6 = 6k$, divisible by $6$ for all $n \in \mathbb{Z}$.""",
    ),
    q(
        "5-p2",
        "5. Past Oxbridge Questions (Archive Sheet H)",
        "5.1 Archive Sheet H",
        "Irrationality of $\\sqrt{2}$",
        "Oxbridge Archive (Sheet H)",
        "Archive H",
        "Number Theory",
        "Warm-up",
        r"""Prove that $\sqrt{2}$ is irrational.""",
        [
            r"Assume for contradiction $\sqrt{2} = \frac{a}{b}$ in lowest terms ($\gcd(a,b) = 1$).",
            r"Square both sides to get $a^2 = 2b^2$. What does that force about the parity of $a$, and then of $b$?",
        ],
        r"""Assume $\sqrt{2} = \frac{a}{b}$ with $a,b \in \mathbb{Z}^+$ and $\gcd(a,b) = 1$. Squaring gives $a^2 = 2b^2$, so $a^2$ is even $\implies a = 2k$ is even. Substituting gives $4k^2 = 2b^2 \implies b^2 = 2k^2$, so $b$ is also even. This contradicts $\gcd(a,b) = 1$. Hence $\sqrt{2}$ is irrational.""",
    ),
    q(
        "5-p3",
        "5. Past Oxbridge Questions (Archive Sheet H)",
        "5.1 Archive Sheet H",
        "Trailing Zeros of $25!$",
        "Oxbridge Archive (Sheet H)",
        "Archive H",
        "Number Theory",
        "Warm-up",
        r"""How many zeros are at the end of $25!$?""",
        [
            r"Each trailing zero comes from a factor of $10 = 2 \times 5$. Since factors of $2$ are plentiful, count the factors of $5$ in $25!$.",
            r"Remember that $25 = 5^2$ contributes TWO factors of $5$! Apply Legendre's formula $\lfloor 25/5 \rfloor + \lfloor 25/25 \rfloor$.",
        ],
        r"""By Legendre's formula, the exponent of $5$ in $25!$ (with plenty of $2$'s available) is:
$$E_5(25!) = \left\lfloor \frac{25}{5} \right\rfloor + \left\lfloor \frac{25}{25} \right\rfloor = 5 + 1 = \mathbf{6}.$$
Thus $25!$ ends in **6** zeros.""",
    ),
    q(
        "5-p4",
        "5. Past Oxbridge Questions (Archive Sheet H)",
        "5.1 Archive Sheet H",
        "Fraction of Married Adults in a Town",
        "Oxbridge Archive (Sheet H)",
        "Archive H",
        "Algebra & Inequalities",
        "Warm-up",
        r"""In a town, $\frac{2}{3}$ of adult men are married to $\frac{3}{5}$ of adult women (monogamous pairwise marriages within the town). What fraction of adults in the town are married?""",
        [
            r"Let $M$ be the number of men and $W$ the number of women. Equate the number of married men to the number of married women.",
            r"Express $M$ in terms of $W$, then compute $\frac{\text{married men} + \text{married women}}{M + W}$.",
        ],
        r"""Since each marriage pairs one man with one woman:
$$\frac{2}{3}M = \frac{3}{5}W \implies M = \frac{9}{10}W.$$
Total adults $= M + W = \frac{19}{10}W$. Total married adults $= 2 \times \frac{3}{5}W = \frac{12}{10}W$.
Fraction married $= \frac{\frac{12}{10}W}{\frac{19}{10}W} = \mathbf{\frac{12}{19}}$. *(Tip: Choosing $6$ married couples immediately gives $9$ men and $10$ women $\implies 12/19$!)*""",
    ),
    q(
        "5-p5",
        "5. Past Oxbridge Questions (Archive Sheet H)",
        "5.1 Archive Sheet H",
        "Two Men in a Railway Tunnel",
        "Oxbridge Archive (Sheet H)",
        "Archive H",
        "Mechanics",
        "Warm-up",
        r"""Two men stand in a railway tunnel of length $L$, at a distance $\frac{2}{5}L$ from the entrance (and $\frac{3}{5}L$ from the exit). A train is approaching the entrance. They run in opposite directions at $v = 15\text{ mph}$: Man 1 reaches the entrance just as the train enters it, and Man 2 reaches the exit just as the train exits it. What is the train's speed $V$?""",
        [
            r"Wait—there is a super clean shortcut! When Man 1 reaches the entrance (having run $\frac{2}{5}L$), how far has Man 2 run toward the exit?",
            r"Man 2 has also run $\frac{2}{5}L$! How much of the tunnel does Man 2 still have left to cover while the train travels the ENTIRE tunnel length $L$?",
            r"Set up the ratio of distances covered in that remaining time interval!",
        ],
        r"""**Clean Interview Shortcut:** When Man 1 runs $\frac{2}{5}L$ to reach the entrance (just meeting the train!), Man 2 has also run $\frac{2}{5}L$ toward the exit, placing him at $\frac{2}{5}L + \frac{2}{5}L = \frac{4}{5}L$ from the entrance—so Man 2 has only $\frac{1}{5}L$ left to run!
In the remaining time it takes Man 2 to cover that $\frac{1}{5}L$, the train covers the entire tunnel length $L$. Thus the train is $5$ times faster than the men:
$$V = 5v = 5 \times 15 = \mathbf{75\text{ mph}}.$$""",
    ),
    q(
        "5-p6",
        "5. Past Oxbridge Questions (Archive Sheet H)",
        "5.1 Archive Sheet H",
        "Hofstadter's MX (MU) Formal Grammar Puzzle",
        "Oxbridge Archive (Sheet H)",
        "Archive H",
        "Logic & Game Theory",
        "Standard",
        r"""Starting from the string **MX**, you may apply two rules repeatedly (where $\alpha$ is any string of X's):
- Rule 2: $M\alpha \to M\alpha\alpha$ (doubles the X's)
- Rule 3: $MXXX\alpha \to M\alpha$ (or removing any three consecutive X's)
Can you ever produce the string **MXXX**?""",
        [
            r"Look for an **invariant**—specifically, count the number of `X`'s, $N_X(w)$, at each step.",
            r"What does doubling ($N_X \to 2N_X$) or subtracting $3$ ($N_X \to N_X - 3$) do to $N_X \bmod 3$?",
            r"Check the starting value $N_X(\text{MX}) = 1 \pmod 3$ vs the target $N_X(\text{MXXX}) = 3 \equiv 0 \pmod 3$.",
        ],
        r"""Track $N_X(w) \pmod 3$:
- Start: $N_X(\text{MX}) = 1 \equiv 1 \pmod 3$.
- Doubling ($N_X \to 2N_X$): if $N_X \not\equiv 0 \pmod 3$, then $2N_X \not\equiv 0 \pmod 3$ ($1 \to 2 \to 1 \to 2\dots$).
- Subtracting $3$ ($N_X \to N_X - 3$): leaves $N_X \bmod 3$ unchanged.

Thus $N_X(w)$ can **never** become a multiple of $3$. Since $N_X(\text{MXXX}) = 3 \equiv 0 \pmod 3$, **MXXX can never be formed**.""",
    ),
    q(
        "5-p7",
        "5. Past Oxbridge Questions (Archive Sheet H)",
        "5.1 Archive Sheet H",
        "Bayes' Theorem: Rare Disease Test Paradox",
        "Oxbridge Archive (Sheet H)",
        "Archive H",
        "Probability",
        "Warm-up",
        r"""A disease affects $1$ in $1000$ people. A diagnostic test has $99.9\%$ accuracy (both sensitivity $P(+\mid D)=0.999$ and specificity $P(-\mid \neg D)=0.999$). If a randomly chosen person tests positive, what is the probability they actually have the disease?""",
        [
            r"Imagine a population of $1{,}000{,}000$ people (or $1000$ people!) and count true positives vs false positives.",
            r"Alternatively, apply Bayes' Theorem: $P(D \mid +) = \frac{P(+\mid D)P(D)}{P(+\mid D)P(D) + P(+\mid \neg D)P(\neg D)}$.",
        ],
        r"""In $1{,}000{,}000$ people:
- $1000$ have the disease $\implies 999$ test positive (true positives).
- $999{,}000$ do not have the disease $\implies 0.001 \times 999{,}000 = 999$ test positive (false positives).

By Bayes' Theorem:
$$P(D \mid +) = \frac{0.999 \times 0.001}{0.999 \times 0.001 + 0.001 \times 0.999} = \frac{1}{2} = \mathbf{50\%}.$$""",
    ),
    q(
        "5-p8",
        "5. Past Oxbridge Questions (Archive Sheet H)",
        "5.1 Archive Sheet H",
        "Boat on a Lake: Throwing Rocks Overboard",
        "Oxbridge Archive (Sheet H)",
        "Archive H",
        "Mechanics",
        "Warm-up",
        r"""You are in a boat floating on a lake with heavy rocks on board. If you throw the rocks overboard into the lake, does the water level of the lake rise, fall, or stay the same?""",
        [
            r"Compare the volume of water displaced while the rocks are floating inside the boat vs after they sink to the bottom.",
            r"In the boat, Archimedes' principle says displaced water equals the *weight* of the rocks. At the bottom, displaced water equals the *volume* of the rocks.",
            r"Since rocks sink ($\rho_{\text{rock}} > \rho_{\text{water}}$), which displaced volume is larger?",
        ],
        r"""- **In the boat:** The boat floats, so the rocks cause an extra displaced water volume equal to their **weight** divided by water density: $V_{\text{in boat}} = \frac{M_{\text{rocks}}}{\rho_{\text{water}}}$.
- **Sunk in the lake:** The rocks sink and displace only their own **volume**: $V_{\text{in water}} = \frac{M_{\text{rocks}}}{\rho_{\text{rock}}}$.

Since rocks are denser than water ($\rho_{\text{rock}} > \rho_{\text{water}}$), $V_{\text{in water}} < V_{\text{in boat}}$, so the total displaced volume decreases and **the water level falls**.""",
    ),

    # =========================================================================
    # 6. HANDWRITTEN INTERVIEW PROBLEM SHEETS
    # =========================================================================
    # 6.1 Problem Sheet B1 (3 problems)
    q(
        "6.1-p1",
        "6. Handwritten Problem Sheets",
        "6.1 Problem Sheet B1",
        "Number of Digits in $100!$",
        "Oxbridge Archive (Sheet B1)",
        "Sheet B1",
        "Number Theory",
        "Standard",
        r"""How many digits does $100!$ have?""",
        [
            r"Recall that the number of base-10 digits in a positive integer $N$ is $\lfloor \log_{10} N \rfloor + 1$.",
            r"Estimate $\ln(100!)$ using Stirling's approximation $N! \approx \sqrt{2\pi N}(N/e)^N$, or by bounding $\sum_{k=1}^{100} \ln k$ with an integral $\int_1^{100} \ln x\,dx$.",
            r"Divide $\ln(100!) \approx 363.74$ by $\ln 10 \approx 2.3026$ (note: $\ln 100 = 2\ln 10 \approx 4.6052$!).",
        ],
        r"""Number of digits $= \lfloor \log_{10}(100!) \rfloor + 1$. Using Stirling's formula $N! \approx \sqrt{2\pi N}(N/e)^N$:
$$\ln(100!) \approx 100\ln 100 - 100 + \frac{1}{2}\ln(200\pi) \approx 460.517 - 100 + 3.22 = 363.738.$$
Converting to base $10$ (dividing by $\ln 10 \approx 2.302585$):
$$\log_{10}(100!) \approx \frac{363.738}{2.302585} \approx 157.97.$$
Thus $100!$ has $\lfloor 157.97 \rfloor + 1 = \mathbf{158}$ digits.""",
    ),
    q(
        "6.1-p2",
        "6. Handwritten Problem Sheets",
        "6.1 Problem Sheet B1",
        "Biased Coin Alternating Game",
        "Oxbridge Archive (Sheet B1)",
        "Sheet B1",
        "Probability",
        "Warm-up",
        r"""Players A and B take turns flipping a biased coin with $P(\text{Heads}) = p$ ($0 < p \le 1$). First head wins, and Player A starts. Find $P(\text{A wins})$.""",
        [
            r"Write a self-similar equation for $P(A)$: A either wins on toss 1 (prob $p$), or both A and B flip Tails so the game resets to A's turn!",
            r"Solve $P(A) = p + (1-p)^2 P(A)$ for $P(A)$.",
        ],
        r"""A wins immediately with probability $p$; if A flips Tails $(1-p)$ and B flips Tails $(1-p)$, the game resets identically to A's turn:
$$P(A) = p + (1-p)^2 P(A) \implies P(A)\left[1 - (1-p)^2\right] = p.$$
Since $1 - (1-p)^2 = 2p - p^2 = p(2-p)$:
$$P(A) = \frac{p}{p(2-p)} = \mathbf{\frac{1}{2-p}}.$$""",
    ),
    q(
        "6.1-p3",
        "6. Handwritten Problem Sheets",
        "6.1 Problem Sheet B1",
        "Derivative of Infinite Power Tower $x^{x^{x^{\\dots}}}$",
        "Oxbridge Archive (Sheet B1)",
        "Sheet B1",
        "Calculus & Trigonometry",
        "Standard",
        r"""Evaluate $\displaystyle \frac{d}{dx}\left(x^{x^{x^{\dots}}}\right)$ (within the interval where the infinite tower converges, $e^{-e} < x < e^{1/e}$).""",
        [
            r"Let $y = x^{x^{x^{\dots}}}$. Notice the infinite tower satisfies the recursive equation $y = x^y$!",
            r"Take natural logarithms of both sides: $\ln y = y \ln x$.",
            r"Differentiate implicitly with respect to $x$ and isolate $\frac{dy}{dx}$.",
        ],
        r"""Let $y = x^{x^{x^{\dots}}}$, so $y = x^y$. Taking $\ln$:
$$\ln y = y \ln x.$$
Differentiating implicitly with respect to $x$:
$$\frac{1}{y}\frac{dy}{dx} = \frac{dy}{dx}\ln x + \frac{y}{x} \implies \frac{dy}{dx}\left(\frac{1}{y} - \ln x\right) = \frac{y}{x}.$$
Solving for $\frac{dy}{dx}$:
$$\frac{dy}{dx} = \frac{y^2}{x(1 - y\ln x)}.$$""",
    ),

    # 6.2 Problem Sheet C1 (3 problems)
    q(
        "6.2-p1",
        "6. Handwritten Problem Sheets",
        "6.2 Problem Sheet C1: Combinatorics & Series",
        "Sum of Binomial Coefficients $\\sum_{k=0}^n \\binom{n}{k} = 2^n$",
        "Oxbridge Archive (Sheet C1)",
        "Sheet C1",
        "Combinatorics",
        "Warm-up",
        r"""Prove that $\displaystyle \sum_{k=0}^n \binom{n}{k} = 2^n$.""",
        [
            r"Use the Binomial Theorem expansion of $(1+x)^n$ with a clever choice of $x$—or give a combinatorial double-counting proof counting subsets of an $n$-element set!",
        ],
        r"""**Algebraic proof:** By the Binomial Theorem, $(1+x)^n = \sum_{k=0}^n \binom{n}{k} x^k$. Setting $x=1$ gives:
$$2^n = \sum_{k=0}^n \binom{n}{k}.$$
**Combinatorial proof:** Both sides count the total number of subsets of an $n$-element set ($2$ choices—in or out—per element vs summing over subset size $k=0,\dots,n$).""",
    ),
    q(
        "6.2-p2",
        "6. Handwritten Problem Sheets",
        "6.2 Problem Sheet C1: Combinatorics & Series",
        "Number of Diagonals in an $n$-gon",
        "Oxbridge Archive (Sheet C1)",
        "Sheet C1",
        "Combinatorics",
        "Warm-up",
        r"""How many internal diagonals does a convex $n$-gon have? Evaluate for a decagon ($n = 10$).""",
        [
            r"Count all pairs of vertices $\binom{n}{2}$, then subtract the $n$ perimeter sides (or count diagonals from each of the $n$ vertices and divide by $2$).",
        ],
        r"""An $n$-gon has $\binom{n}{2} = \frac{n(n-1)}{2}$ segments joining pairs of vertices, of which $n$ are perimeter edges:
$$\text{Diagonals} = \binom{n}{2} - n = \frac{n(n-1)}{2} - n = \mathbf{\frac{n(n-3)}{2}}.$$
For a decagon ($n=10$): $\frac{10 \times 7}{2} = \mathbf{35}$ diagonals.""",
    ),
    q(
        "6.2-p3",
        "6. Handwritten Problem Sheets",
        "6.2 Problem Sheet C1: Combinatorics & Series",
        "Telescoping Series $\\frac{1}{2} + \\frac{1}{6} + \\frac{1}{12} + \\dots + \\frac{1}{9900}$",
        "Oxbridge Archive (Sheet C1)",
        "Sheet C1",
        "Algebra & Inequalities",
        "Warm-up",
        r"""Evaluate
$$\frac{1}{2} + \frac{1}{6} + \frac{1}{12} + \frac{1}{20} + \dots + \frac{1}{9900}.$$""",
        [
            r"Factor each denominator as a product of consecutive integers: $2 = 1\cdot 2$, $6 = 2\cdot 3$, $\dots$, $9900 = 99 \cdot 100$.",
            r"Use partial fractions: $\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$ and telescope!",
        ],
        r"""Each term is $\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$ for $k = 1, 2, \dots, 99$ (since $99 \times 100 = 9900$). The sum telescopes:
$$\sum_{k=1}^{99} \left(\frac{1}{k} - \frac{1}{k+1}\right) = 1 - \frac{1}{100} = \mathbf{\frac{99}{100}}.$$""",
    ),

    # 6.3 Problem Sheet C2 (1 problem)
    q(
        "6.3-p1",
        "6. Handwritten Problem Sheets",
        "6.3 Problem Sheet C2: Integrals",
        "Symmetric Integral $\\int_{-1/2}^{1/2} \\cos x \\ln\\left(\\frac{1+x}{1-x}\\right)dx$",
        "Oxbridge Archive (Sheet C2)",
        "Sheet C2",
        "Calculus & Trigonometry",
        "Warm-up",
        r"""Compute $\displaystyle \int_{-1/2}^{1/2} \cos x \ln\!\left(\frac{1+x}{1-x}\right) dx$.""",
        [
            r"Notice the symmetric integration interval $[-1/2, 1/2]$! Test the integrand $f(x)$ for even/odd parity by computing $f(-x)$.",
            r"What is $\ln\!\left(\frac{1-x}{1+x}\right)$ in terms of $\ln\!\left(\frac{1+x}{1-x}\right)$?",
        ],
        r"""Let $f(x) = \cos x \ln\!\left(\frac{1+x}{1-x}\right)$. Since $\cos(-x) = \cos x$ (even) and
$$\ln\!\left(\frac{1-x}{1+x}\right) = \ln\!\left[\left(\frac{1+x}{1-x}\right)^{-1}\right] = -\ln\!\left(\frac{1+x}{1-x}\right) \quad (\text{odd}),$$
the integrand $f(x)$ is an **odd** continuous function on the symmetric interval $[-1/2, 1/2]$. Hence the integral is **0**.""",
    ),

    # 6.4 Problem Sheet C3 (2 problems)
    q(
        "6.4-p1",
        "6. Handwritten Problem Sheets",
        "6.4 Problem Sheet C3: Counting & Divisibility",
        "Odd Integers in $[3000, 8000]$ with Distinct Digits",
        "Oxbridge Archive (Sheet C3)",
        "Sheet C3",
        "Combinatorics",
        "Standard",
        r"""How many odd integers between $3000$ and $8000$ have no repeated digits?""",
        [
            r"Write the 4-digit number as $d_1 d_2 d_3 d_4$. Which digits are allowed for $d_1$ and for $d_4$?",
            r"Notice that $d_1 \in \{3,4,5,6,7\}$ overlaps with the odd digits $d_4 \in \{1,3,5,7,9\}$! Split into Case 1 ($d_1$ odd) and Case 2 ($d_1$ even) before choosing $d_4$, then $d_2, d_3$.",
        ],
        r"""For $d_1 d_2 d_3 d_4 \in (3000, 8000)$ to be odd, $d_1 \in \{3,4,5,6,7\}$ and $d_4 \in \{1,3,5,7,9\}$:
- **Case 1 ($d_1 \in \{3,5,7\}$, odd — 3 choices):** $d_4$ has $4$ remaining odd choices; $d_2$ has $8$ remaining digits; $d_3$ has $7$. Count $= 3 \times 4 \times 8 \times 7 = 672$.
- **Case 2 ($d_1 \in \{4,6\}$, even — 2 choices):** $d_4$ has all $5$ odd choices; $d_2$ has $8$; $d_3$ has $7$. Count $= 2 \times 5 \times 8 \times 7 = 560$.

Total $= 672 + 560 = \mathbf{1232}$.""",
    ),
    q(
        "6.4-p2",
        "6. Handwritten Problem Sheets",
        "6.4 Problem Sheet C3: Counting & Divisibility",
        "Common Divisors of $10^{40}$ and $20^{30}$",
        "Oxbridge Archive (Sheet C3)",
        "Sheet C3",
        "Number Theory",
        "Warm-up",
        r"""How many positive integers divide both $10^{40}$ and $20^{30}$?""",
        [
            r"Prime factorise both $10^{40}$ and $20^{30}$ in terms of $2$ and $5$.",
            r"Common divisors of two numbers are precisely the divisors of their $\gcd$. Take $\min$ of each prime's exponent!",
        ],
        r"""Prime factorise:
$$10^{40} = 2^{40} \times 5^{40}, \qquad 20^{30} = (2^2 \times 5)^{30} = 2^{60} \times 5^{30}.$$
Their greatest common divisor is $\gcd(10^{40}, 20^{30}) = 2^{\min(40,60)} \times 5^{\min(40,30)} = 2^{40} \times 5^{30}$.
The number of positive common divisors is $(40+1)(30+1) = 41 \times 31 = \mathbf{1271}$.""",
    ),

    # 6.5 Problem Sheet C4 (1 problem)
    q(
        "6.5-p1",
        "6. Handwritten Problem Sheets",
        "6.5 Problem Sheet C4: Trig & Curves",
        "Half-Angle Identity $\\csc\\theta - \\cot\\theta = \\tan(\\theta/2)$",
        "Oxbridge Archive (Sheet C4)",
        "Sheet C4",
        "Calculus & Trigonometry",
        "Warm-up",
        r"""Prove that $\csc\theta - \cot\theta = \tan(\theta/2)$ (where defined).""",
        [
            r"Rewrite $\csc\theta - \cot\theta$ in terms of $\sin\theta$ and $\cos\theta$ over a common denominator.",
            r"Apply the half-angle formulas $1 - \cos\theta = 2\sin^2(\theta/2)$ and $\sin\theta = 2\sin(\theta/2)\cos(\theta/2)$.",
        ],
        r"""$$\csc\theta - \cot\theta = \frac{1 - \cos\theta}{\sin\theta} = \frac{2\sin^2(\theta/2)}{2\sin(\theta/2)\cos(\theta/2)} = \frac{\sin(\theta/2)}{\cos(\theta/2)} = \tan\!\left(\frac{\theta}{2}\right).$$""",
    ),

    # 6.6 Problem Sheet C5 (3 problems)
    q(
        "6.6-p1",
        "6. Handwritten Problem Sheets",
        "6.6 Problem Sheet C5: Sequences & Number Theory",
        "Telescoping Recurrence $\\sum_{k=1}^n f(k) = n^2 f(n)$",
        "Oxbridge Archive (Sheet C5)",
        "Sheet C5",
        "Algebra & Inequalities",
        "Standard",
        r"""Given $f(1) = 2015$ and $\displaystyle \sum_{k=1}^n f(k) = n^2 f(n)$ for all $n > 1$, calculate $f(2015)$.""",
        [
            r"Let $S_n = \sum_{k=1}^n f(k) = n^2 f(n)$. How do you isolate $f(n)$ from $S_n$ and $S_{n-1}$?",
            r"Write $f(n) = S_n - S_{n-1} = n^2 f(n) - (n-1)^2 f(n-1)$ and solve for $\frac{f(n)}{f(n-1)}$.",
            r"Factor $n^2 - 1 = (n-1)(n+1)$ to cancel $(n-1)$ and telescope the product down to $f(1)$!",
        ],
        r"""For $n \ge 2$, $f(n) = S_n - S_{n-1} = n^2 f(n) - (n-1)^2 f(n-1)$, so $(n^2 - 1)f(n) = (n-1)^2 f(n-1)$. Dividing by $n-1 > 0$:
$$(n+1)f(n) = (n-1)f(n-1) \implies \frac{f(n)}{f(n-1)} = \frac{n-1}{n+1}.$$
Telescoping from $n$ down to $2$:
$$f(n) = \frac{n-1}{n+1} \cdot \frac{n-2}{n} \cdot \frac{n-3}{n-1} \cdots \frac{2}{4} \cdot \frac{1}{3} f(1) = \frac{2 \times 1}{n(n+1)} f(1).$$
For $n = 2015$ and $f(1) = 2015$:
$$f(2015) = \frac{2}{2015 \times 2016} \times 2015 = \frac{2}{2016} = \mathbf{\frac{1}{1008}}.$$""",
    ),
    q(
        "6.6-p2",
        "6. Handwritten Problem Sheets",
        "6.6 Problem Sheet C5: Sequences & Number Theory",
        "Smallest Integer Whose Square Ends in $444$",
        "Oxbridge Archive (Sheet C5)",
        "Sheet C5",
        "Number Theory",
        "Standard",
        r"""Find the first (smallest) positive integer whose square ends in three $4$'s (i.e., $\dots 444$).""",
        [
            r"We want the smallest positive integer $x$ with $x^2 \equiv 444 \pmod{1000}$. First check the last digit of $x$: what digits squared end in $4$?",
            r"Since $x$ is even, substitute $x = 2y$ so $4y^2 \equiv 444 \pmod{1000} \implies y^2 \equiv 111 \pmod{250}$!",
            r"What must $y \bmod 10$ or $y \bmod 5$ and $y \bmod 25$ be? Check small $y$ with $y^2 \equiv 1 \pmod 5$ and $y$ odd ($y = 19 \implies 38$!).",
        ],
        r"""We solve $x^2 \equiv 444 \pmod{1000}$. Since the last digit of $x^2$ is $4$, $x$ is even ($x = 2y$), giving:
$$4y^2 \equiv 444 \pmod{1000} \implies y^2 \equiv 111 \pmod{250}.$$
Thus $y$ is odd and $y^2 \equiv 1 \pmod 5$, so $y \equiv \pm 1 \pmod 5$ (and odd $\implies y \equiv 1, 9, 11, 19 \pmod{10}$—specifically $y \equiv 1$ or $9 \pmod{10}$).
Testing $y = 1, 9, 11, 19$: $19^2 = 361 = 250 + 111 \equiv 111 \pmod{250}$.
Thus $x = 2 \times 19 = \mathbf{38}$ (checking: $38^2 = 1444$, and no smaller candidate $\{2,8,12,18,22,28,32\}$ works).""",
    ),
    q(
        "6.6-p3",
        "6. Handwritten Problem Sheets",
        "6.6 Problem Sheet C5: Sequences & Number Theory",
        "Palindromic Quartic $2x^4 - 11x^3 + 16x^2 - 11x + 2 = 0$",
        "Oxbridge Archive (Sheet C5)",
        "Sheet C5",
        "Algebra & Inequalities",
        "Standard",
        r"""For $2x^4 - 11x^3 + 16x^2 - 11x + 2 = 0$, find the possible values of $x + \dfrac{1}{x}$ and solve for all roots $x$.""",
        [
            r"Notice the coefficients are symmetric (palindromic): $2, -11, 16, -11, 2$! Since $x=0$ is not a root, divide by $x^2$.",
            r"Let $u = x + \frac{1}{x}$. Express $x^2 + \frac{1}{x^2}$ in terms of $u$ ($u^2 - 2$).",
            r"Solve the resulting quadratic in $u$, then solve $x + \frac{1}{x} = u$ for $x$ (watch out for complex roots!).",
        ],
        r"""Dividing by $x^2$ gives $2(x^2 + \frac{1}{x^2}) - 11(x + \frac{1}{x}) + 16 = 0$. Setting $u = x + \frac{1}{x}$ (so $x^2 + \frac{1}{x^2} = u^2 - 2$):
$$2(u^2 - 2) - 11u + 16 = 2u^2 - 11u + 12 = (2u - 3)(u - 4) = 0.$$
Thus $u = 4$ or $u = \frac{3}{2}$.
- If $x + \frac{1}{x} = 4 \implies x^2 - 4x + 1 = 0 \implies \mathbf{x = 2 \pm \sqrt{3}}$.
- If $x + \frac{1}{x} = \frac{3}{2} \implies 2x^2 - 3x + 2 = 0 \implies \mathbf{x = \frac{3 \pm i\sqrt{7}}{4}}$. """,
    ),

    # 6.7 Problem Sheet C6 (2 problems)
    q(
        "6.7-p1",
        "6. Handwritten Problem Sheets",
        "6.7 Problem Sheet C6: Algebra & Polynomials",
        "Diophantine Equation $(u+v)^2 = u^3 + v^3$",
        "Oxbridge Archive (Sheet C6)",
        "Sheet C6",
        "Number Theory",
        "Standard",
        r"""Find all pairs of positive integers $(u, v)$ satisfying $(u + v)^2 = u^3 + v^3$.""",
        [
            r"Factor $u^3 + v^3 = (u+v)(u^2 - uv + v^2)$. Since $u, v > 0$, you can safely divide both sides by $u + v > 0$!",
            r"Treat the remaining equation $u^2 - (v+1)u + (v^2 - v) = 0$ as a quadratic in $u$.",
            r"Require the discriminant $\Delta \ge 0$ to bound $v$ to just a tiny set of positive integers ($v \in \{1, 2\}$)!",
        ],
        r"""Since $u, v > 0 \implies u + v > 0$, dividing $(u+v)^2 = (u+v)(u^2 - uv + v^2)$ by $u+v$ yields:
$$u + v = u^2 - uv + v^2 \implies u^2 - (v+1)u + (v^2 - v) = 0.$$
For real $u$, the discriminant must satisfy:
$$\Delta = (v+1)^2 - 4(v^2 - v) = -3v^2 + 6v + 1 \ge 0.$$
The roots of $-3v^2 + 6v + 1 = 0$ are $1 \pm \frac{2}{\sqrt{3}} \approx 1 \pm 1.155$, so the only positive integers in range are $v \in \{1, 2\}$:
- $v = 1$: $\Delta = 4 \implies u = \frac{2 \pm 2}{2} \implies u = 2$ (since $u>0$), giving $(2, 1)$.
- $v = 2$: $\Delta = 1 \implies u = \frac{3 \pm 1}{2} \implies u \in \{1, 2\}$, giving $(1, 2)$ and $(2, 2)$.

Solutions: **$(u, v) \in \{(1, 2),\, (2, 1),\, (2, 2)\}$**.""",
    ),
    q(
        "6.7-p2",
        "6. Handwritten Problem Sheets",
        "6.7 Problem Sheet C6: Algebra & Polynomials",
        "Condition for $x^3 + ax^2 + b = 0$ to Have 3 Distinct Real Roots",
        "Oxbridge Archive (Sheet C6)",
        "Sheet C6",
        "Algebra & Inequalities",
        "Standard",
        r"""Show that if $x^3 + ax^2 + b = 0$ has $3$ distinct real solutions, then $27b^2 + 4a^3 b < 0$.""",
        [
            r"Let $f(x) = x^3 + ax^2 + b$. For a cubic to cross the $x$-axis $3$ distinct times, what must happen to its two stationary points (local max and local min)?",
            r"Find the two stationary points $x_1, x_2$ from $f'(x) = 3x^2 + 2ax = 0$.",
            r"Express the condition that the local max and local min lie on opposite sides of the $x$-axis as $f(x_1) \cdot f(x_2) < 0$.",
        ],
        r"""Let $f(x) = x^3 + ax^2 + b$. Then $f'(x) = 3x^2 + 2ax = x(3x + 2a)$, giving stationary points $x_1 = 0$ and $x_2 = -\frac{2a}{3}$.
A cubic has $3$ distinct real roots iff it has two distinct turning points of strictly opposite $y$-signs: $f(x_1) f(x_2) < 0$.
Evaluating:
$$f(0) = b, \qquad f\!\left(-\frac{2a}{3}\right) = -\frac{8a^3}{27} + \frac{4a^3}{9} + b = \frac{4a^3}{27} + b.$$
Hence:
$$b\left(b + \frac{4a^3}{27}\right) < 0 \iff 27b^2 + 4a^3 b < 0.$$""",
    ),
]


def main():
    # Double-check all 6 sections and 85 questions? Wait let's verify count!
    # Let's inspect what we have in QUESTIONS right now and assign sequential numbers.
    print(f"Total questions defined: {len(QUESTIONS)}")
    for idx, item in enumerate(QUESTIONS, start=1):
        item["number"] = idx

    # Write web/questions.js
    web_dir = BASE_DIR / "web"
    web_dir.mkdir(parents=True, exist_ok=True)
    js_path = web_dir / "questions.js"
    js_content = (
        "// Auto-generated by scripts/generate_questions.py\n"
        f"window.OXBRIDGE_QUESTIONS = {json.dumps(QUESTIONS, indent=2, ensure_ascii=False)};\n"
    )
    js_path.write_text(js_content, encoding="utf-8")

    # Write src/data/questions.json
    data_dir = BASE_DIR / "src" / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    json_path = data_dir / "questions.json"
    json_path.write_text(json.dumps(QUESTIONS, indent=2, ensure_ascii=False), encoding="utf-8")

    # Print breakdown by section
    from collections import Counter
    sec_counts = Counter(item["section"] for item in QUESTIONS)
    for sec, cnt in sec_counts.items():
        print(f"  {sec}: {cnt}")
    print(f"Wrote {js_path} and {json_path}")


if __name__ == "__main__":
    main()
