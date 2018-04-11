# Statistical analysis and graphing of qRT-PCR data from an infection timecourse

Run on Mac rather than cluster

Each gene analysed is on a separate csv file

```bash
cd /Users/adamst/Documents/qPCR/Statistical_Analysis
```

## Run ANOVAs

### Candidate _Avr_ (g24882.t1)

```R
# Read in csv file
input <- read.csv("cAvr.csv")

# Generate frequency tables, sanity check, prints to screen
table(input$Timepoint, input$Isolate)

# Perform ANOVA
res.aov2 <- aov(Expression ~ Isolate * Timepoint, data = input)
ANOVA <- summary(res.aov2)
capture.output(ANOVA, file = "cAvr_ANOVA_reults.txt")

# Tukey multiple pairwise-comparisons
Tukey <- TukeyHSD(res.aov2)
capture.output(Tukey, file = "cAvr_Tukey_results.txt")
```

### Early RxLR (g32018.t1)

```R
# Read in csv file
input <- read.csv("Early_RxLR.csv")

# Generate frequency tables, sanity check, prints to screen
table(input$Timepoint, input$Isolate)

# Perform ANOVA
res.aov2 <- aov(Expression ~ Isolate * Timepoint, data = input)
ANOVA <- summary(res.aov2)
capture.output(ANOVA, file = "Early_RxLR_ANOVA_reults.txt")

# Tukey multiple pairwise-comparisons
Tukey <- TukeyHSD(res.aov2)
capture.output(Tukey, file = "Early_RxLR_Tukey_results.txt")
```

### Middle RxLR (g23965.t1)

```R
# Read in csv file
input <- read.csv("Middle_RxLR.csv")

# Generate frequency tables, sanity check, prints to screen
table(input$Timepoint, input$Isolate)

# Perform ANOVA
res.aov2 <- aov(Expression ~ Isolate * Timepoint, data = input)
ANOVA <- summary(res.aov2)
capture.output(ANOVA, file = "Middle_RxLR_ANOVA_reults.txt")

# Tukey multiple pairwise-comparisons
Tukey <- TukeyHSD(res.aov2)
capture.output(Tukey, file = "Middle_RxLR_Tukey_results.txt")
```
