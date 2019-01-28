# Statistical analysis and graphing of qRT-PCR data from an infection timecourse

Run on Mac rather than cluster

Each gene analysed is on a separate csv file

```bash
cd /Users/adamst/Documents/qPCR/With\ A4/Statistical_Analysis
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
capture.output(ANOVA, file = "cAvr_ANOVA_results.txt")

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
capture.output(ANOVA, file = "Early_RxLR_ANOVA_results.txt")

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
capture.output(ANOVA, file = "Middle_RxLR_ANOVA_results.txt")

# Tukey multiple pairwise-comparisons
Tukey <- TukeyHSD(res.aov2)
capture.output(Tukey, file = "Middle_RxLR_Tukey_results.txt")
```

## Draw graphs

### Candidate _Avr_ (g24882.t1)

```R
# Read in csv file
input <- read.csv("cAvr_plus_SEM.csv")

# Draw graph
library(ggplot2)
input$Timepoint2 <- factor(input$Timepoint, levels = c("Mycelium", "24hpi",
"48hpi", "72hpi", "96hpi"))
plot <- ggplot(input, aes(x = Timepoint2, y = Expression, group = Isolate,
    colour = Isolate)) + geom_errorbar(aes(ymin = Expression - SEM,
        ymax = Expression + SEM), width = 0.1) + geom_line() + geom_point() +
        scale_color_brewer(palette = "Paired") + xlab("Timepoint") +
        theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(), panel.background = element_blank(),
        panel.border = element_rect(colour = "black", fill = NA, size = 1),
        axis.text = element_text(size = 14),
        axis.title = element_text(size = 18))
ggsave("cAvr.pdf", plot = plot)
```

### Early RxLR (g32018.t1)

```R
# Read in csv file
input <- read.csv("Early_RxLR_plus_SEM.csv")

# Draw graph
library(ggplot2)
input$Timepoint2 <- factor(input$Timepoint, levels = c("Mycelium", "24hpi",
"48hpi", "72hpi", "96hpi"))
plot <- ggplot(input, aes(x = Timepoint2, y = Expression, group = Isolate,
    colour = Isolate)) + geom_errorbar(aes(ymin = Expression - SEM,
        ymax = Expression + SEM), width = 0.1) + geom_line() + geom_point() +
        scale_color_brewer(palette = "Paired") + xlab("Timepoint") +
        theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(), panel.background = element_blank(),
        panel.border = element_rect(colour = "black", fill = NA, size = 1),
        axis.text = element_text(size = 14),
        axis.title = element_text(size = 18))
ggsave("Early_RxLR.pdf", plot = plot)
```

### Middle RxLR (g23965.t1)

```R
# Read in csv file
input <- read.csv("Middle_RxLR_plus_SEM.csv")

# Draw graph
library(ggplot2)
input$Timepoint2 <- factor(input$Timepoint, levels = c("Mycelium", "24hpi",
"48hpi", "72hpi", "96hpi"))
plot <- ggplot(input, aes(x = Timepoint2, y = Expression, group = Isolate,
    colour = Isolate)) + geom_errorbar(aes(ymin = Expression - SEM,
        ymax = Expression + SEM), width = 0.1) + geom_line() + geom_point() +
        scale_color_brewer(palette = "Paired") + xlab("Timepoint") +
        theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(), panel.background = element_blank(),
        panel.border = element_rect(colour = "black", fill = NA, size = 1),
        axis.text = element_text(size = 14),
        axis.title = element_text(size = 18))
ggsave("Middle_RxLR.pdf", plot = plot)
```
