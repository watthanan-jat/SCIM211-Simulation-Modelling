# SCIM211 Simulation Playground

A browser-only interactive website for **SCIM211 Simulation Modelling**. It contains two simulations designed for a first lecture:

1. Monte Carlo estimation of pi.
2. An interacting-particle SIR epidemic model on a ring.

The site uses plain HTML, CSS, and JavaScript. It has no packages, build step, backend, external API, or internet dependency.

## Files

- `index.html` contains the accessible page structure.
- `style.css` contains the responsive course design.
- `app.js` contains both simulation models, graphs, seeded random-number generator, CSV export, and copy tools.

## Run locally

The simplest method is to double-click `index.html` or drag it into a browser window. The simulations work from a `file://` address.

You can also serve the folder with any static web server, but this is optional. No installation is required.

## Publish with GitHub Pages

This folder is already inside the repository's `docs/` directory, so it is compatible with the existing GitHub Pages setup.

1. Commit and push `docs/playground/index.html`, `style.css`, `app.js`, and `README.md` to the repository's `main` branch.
2. In the GitHub repository, open **Settings > Pages**.
3. Under **Build and deployment**, select **Deploy from a branch**.
4. Select the `main` branch and the `/docs` folder, then save.
5. After deployment, open:
   `https://<github-username>.github.io/<repository-name>/playground/`

For this course repository, the expected address is:
`https://watthanan-jat.github.io/SCIM211-Simulation-Modelling/playground/`

## Mathematical rules

### 1. Monte Carlo estimation of pi

Generate independent points `(X, Y)` uniformly from the square `[-1, 1] x [-1, 1]`. A point is inside the unit circle when

```text
X^2 + Y^2 <= 1.
```

If `N` is the total number of points and `H` is the number inside the circle, the estimate is

```text
pi_hat = 4H/N.
```

This works because the unit circle has area `pi` and the surrounding square has area `4`, so the probability that a uniformly sampled point lands inside is `pi/4`.

The graph records `pi_hat` against `N` and includes a horizontal reference line at the true value of pi. The absolute error is

```text
|pi_hat - pi|.
```

This is a **static stochastic** model. There is no simulated time or evolving system state; randomness enters through sampling.

### 2. Interacting-particle SIR epidemic

There are `N` particles on a ring. Each particle has one state:

- `S`: susceptible
- `I`: infected
- `R`: recovered

Particle `i` interacts only with particles `i-1` and `i+1`, with the first and last particles treated as neighbours.

At each synchronous discrete-time step, all new states are calculated from the states at the current time and then applied together:

- If a susceptible particle has `k` infected neighbours, where `k` is 0, 1, or 2, it becomes infected with probability

  ```text
  1 - (1 - p)^k.
  ```

- An infected particle recovers with probability `q`.
- A recovered particle remains recovered.

The simulation records `S(t)`, `I(t)`, and `R(t)`, the peak infected count, the first time that peak occurs, and epidemic duration. Epidemic duration is the first time `t` at which `I(t) = 0`.

This is a **dynamic, stochastic, discrete-time, discrete-state** model.

## Reproducibility

Both simulations use a deterministic seeded pseudo-random number generator. The same seed, inputs, and sequence of actions produce the same sample path. Changing the seed produces a different random path.

The **Copy summary** buttons capture the seed, parameters, and current results. The **Download CSV** buttons export the recorded simulation history.

## Suggested first-lecture activities

### Activity 1: Does more simulation always improve the answer?

1. Ask students to predict whether the pi estimate will move closer to pi after every new batch.
2. Run the model at `N = 10`, `100`, `1,000`, and `10,000`.
3. Compare estimates across students using different seeds.
4. Discuss convergence, sampling error, and why improvement is not monotonic.
5. Classify the model as static and stochastic.

### Activity 2: Reproducibility versus randomness

1. Give the class one common seed and ask everyone to repeat the same button sequence.
2. Confirm that the results match.
3. Change only the seed and compare results.
4. Distinguish the model's probabilistic rules from the deterministic execution of a seeded pseudo-random sequence.

### Activity 3: Local interaction and epidemic paths

1. Start with `N = 40`, two infected particles, `p = 0.30`, and `q = 0.10`.
2. Run three seeds and record peak infection and epidemic duration.
3. Reduce `p` while holding `q` fixed, then increase `q` while holding `p` fixed.
4. Ask why the same parameter values can lead to early extinction in one run and a larger epidemic in another.
5. Classify the model as dynamic, stochastic, discrete-time, and discrete-state.

### Activity 4: Question the assumptions

Ask students what is omitted by the ring model: long-range contacts, births and deaths, loss of immunity, changing behaviour, unequal infectivity, and continuous time. Discuss when a simple model is still useful.
