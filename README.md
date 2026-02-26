# Git Tutorial: Version Control for Researchers

Todd Gerarden is better than Ivan Rudik

This repo is a hands-on introduction to Git and GitHub for the SEERE group. It 
will be followed by a deeper dive on agentic AI tools. We'll use replication
materials from Andersson (2019, AEJ: Policy) — "Carbon Taxes and CO2 Emissions:
Sweden as a Case Study" — as a realistic research project to practice on.

## Project structure

```
data/
  analysis_data.csv      # donor pool panel: OECD countries, 1960–2005
  descriptive_data.csv   # Sweden time series: CO2, taxes, GDP, synthetic control
code/
  summarize.py           # summary statistics on the donor pool (Python)
  plot_trends.R          # Sweden vs. synthetic Sweden CO2 trends (R)
output/                  # figures and tables go here
```

Sweden introduced its carbon tax in **1991**. The key outcome is transport CO2
emissions per capita.

---

## Git Tutorial

### 1. Fork and clone the repo

On GitHub, fork this repo to your own account. Then clone your fork locally:

```bash
git clone <your-fork-url>
cd seere-git-ai-demo
git status
```

### 2. Make your first commit

Open `README.md` and add your name under a new line at the top. Then:

```bash
git status
git add README.md
git commit -m "add my name to README"
```

### 3. Make a change and inspect it

Open `code/summarize.py`. If you have python installed, run it (e.g., by typing `python3 code/summarize.py` at the command line). The script prints some tables but does not output any of them. Add `co2_by_country.to_csv("output/tables/co2_by_country.csv")` to the script to output the table and run it again. Then:

```bash
git status
git diff
git diff code/summarize.py     # diff a specific file
```

### 4. Stage selectively and review before committing

```bash
git add code/summarize.py
git diff --staged                  # review what's about to be committed
git commit -m "describe your change here"
```

### 5. Review history

```bash
git log
git log --oneline
git show                           # inspect the most recent commit
git show <commit-hash>             # inspect a specific commit
```

### 6. Undo a change

Make another small edit to a script in `code/` of your choosing and save it, but do **not** stage it. Then:

```bash
git diff                           # confirm the change you made
git restore code/summarize.py      # discard unstaged changes to a file
git diff                           # confirm the change is gone
```

To undo an entire commit (preserves history):

```bash
git revert HEAD
git log --oneline                  # confirm the revert commit was added
```

### 7. Push your changes to GitHub

```bash
git push
```

### 8. Pull in changes from others

In this case, you won't have any.

```bash
git pull
```

## Time Permitting

### 9. Edit an R script

1. Run `code/plot_trends.R` (e.g., via `Rscript --vanilla code/plot_trends.R` at the command line).
2. Check what's changed using `git status`.
3. Commit the changes.
4. Revise `plot_trends.R` to output a `.pdf` instead of `.png`. Save the change. Call the script again.
5. Remove the `.png` from the git repo and working directory using `git rm output/figures/co2_trends.png`. This will stage the file for removal.
6. Stage the code change and `.pdf` file.
7. Commit the changes.

---

## Claude Code Example

If you have Claude Code set up, you can follow along with these steps on your machine. If not, we can just work through it together.

1. Create and switch to a new branch called `did-analysis` using `git switch -c did-analysis` (`-c` creates a new branch). If you have used git before, you may be familiar with the older syntax `git checkout -b did-analysis`.
2. Use `git branch -a` to view all the branches. Note that our new branch appears locally but not on remote (i.e., GitHub).
3. While within your repo, type `claude` at the command line to launch Claude Code.
4. Prompt Claude Code with this script:
  > i want to implement a difference-in-differences research design using `data/analysis_data.csv`, comparing the outcome `CO2_transport_capita` for different countries over time, with Sweden as the treated country starting in 1991. use a two-way fixed effects regression with country and year fixed effects. standard errors should be clustered at country, since that's the level of treatment assignment. ignore the inference problem of only one treated cluster. write a script to estimate the basic regression model and output a `.tex` table with the estimated treatment effect, standard errors, and other standard info. also estimate an event study version of the research design and output a `.pdf` figure of dynamic treatment coefficients. once the code is debugged, run it to output the files. think hard about this task and ask clarifying questions as needed before getting started.
5. Type `/exit` to exit Claude Code.
6. Use `git status` to see what files Claude Code changed in the repo. Open each file to inspect the changes.
7. Commit the changes.
8. Push the new branch with changes to GitHub using `git push -u origin did-analysis` (`-u` sets the upstream so in the future you can just use `git push` and `git pull` without arguments).
9. Navigate to your repo on GitHub. Use it to view the changes and compare the branch `did-analysis` with `main`. (From here, you could merge the changes, continue to work on them in a separate branch, etc.)

Repeat the steps above in a new branch, using the prompt below, and use GitHub to see how the results compare:
  > write a script to estimate diff-in-diff and event study models of how the swedish gas tax in 1991 affected emissions per capita

---

## Key concepts to keep in mind

- **Commit early and often.** Small, focused commits are easier to review and revert.
- **Write informative commit messages.** Your future self (and collaborators) will thank you.
- **`git diff` before you commit.** Always know what you're about to commit.
- **Nothing is lost if it was committed.** Git is a safety net, not just a backup.
