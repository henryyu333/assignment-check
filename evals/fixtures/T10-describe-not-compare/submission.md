# Convergence Behaviour of Gradient Descent and Simulated Annealing

## 1. Introduction

This report describes two widely used optimisation methods and their convergence behaviour, and recommends one of them for a large sparse problem.

## 2. Gradient Descent

Gradient descent dates back to Cauchy (1847) and remains the default first-order method for smooth optimisation. The update is

    θ_{t+1} = θ_t − η ∇f(θ_t)

where η is the step size. Convergence depends heavily on η. If η is too large the iterates can oscillate or diverge; if η is too small progress is extremely slow. For a convex function with Lipschitz-continuous gradient, a fixed step size η ≤ 1/L gives a sublinear rate of O(1/t). Under the stronger assumption of strong convexity, the same method with a well-chosen step size converges linearly, with the rate determined by the condition number. In practice the step size is tuned by hand, by a line search, or by an adaptive schedule.

The main limitations follow from the assumptions above. On non-convex objectives the method converges to a stationary point that may be a local minimum or a saddle point. On ill-conditioned problems the iterates zig-zag along narrow valleys, so the condition number dominates the runtime. The method also requires the gradient to exist and to be computable; it is not directly applicable to non-smooth, discontinuous or discrete objectives. In modern practice the plain update is usually replaced by variants such as momentum or Adam, but these mainly change the effective step size, and the first-order convergence behaviour described above still governs the underlying iteration.

## 3. Simulated Annealing

Simulated annealing comes from the Metropolis algorithm (Metropolis et al., 1953) and was developed as an optimisation method by Kirkpatrick et al. (1983). A candidate move is always accepted if it improves the objective, and otherwise accepted with probability

    p = exp(−ΔE / T)

where T is the temperature and ΔE is the change in objective value. At high temperature the walk is almost random; as T decreases, the search becomes increasingly greedy.

Convergence depends on the cooling schedule. Under a logarithmic schedule, T_k = c / log(k) with c large enough, the algorithm converges in probability to the global optimum, but this requires an unbounded number of iterations. Practical implementations use a geometric schedule, T_{k+1} = α T_k with α close to 1, which has no comparable asymptotic guarantee. The method is also sensitive to the initial temperature, the cooling rate, and the number of moves per temperature level; a schedule that cools too quickly freezes the search into a poor region. Because the algorithm only ever evaluates the objective, it applies to black-box, discrete and combinatorial problems where the objective surface is rugged and no derivative is available.

## 4. Recommendation for a Large Sparse Problem

For the large sparse problem described in the brief, I would choose simulated annealing. Its ability to accept uphill moves means it can leave the vicinity of poor local minima, and it does not require gradient information, which matters when gradients are expensive to compute or unavailable. The trade-off is that it needs many objective evaluations, so the temperature schedule should be tuned carefully and the budget should be planned before running the experiment.

## References

- Cauchy, A. (1847). Méthode générale pour la résolution des systèmes d'équations simultanées.
- Kirkpatrick, S., Gelatt, C. D., & Vecchi, M. P. (1983). Optimization by simulated annealing. *Science*, 220(4598), 671–680.
- Metropolis, N., Rosenbluth, A. W., Rosenbluth, M. N., Teller, A. H., & Teller, E. (1953). Equation of state calculations by fast computing machines. *Journal of Chemical Physics*, 21(6), 1087–1092.
