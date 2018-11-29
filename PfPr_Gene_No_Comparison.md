# Assessment of numbers of genes with specific annotations between Pf & Pr (Minus BC-16)

Welch two sample t-test run on local mac (OSX version 10.13.6)

## Secreted proteins

```R
x <- c(6887, 6724, 6602, 6884, 6968, 6696, 6880, 6901, 6734, 6460)
y <- c(6262, 6566, 6309)
t.test(x,y)
```

Results:

```
	Welch Two Sample t-test

data:  x and y
t = 3.6857, df = 3.2397, p-value = 0.03039
alternative hypothesis: true difference in means is not equal to 0
95 percent confidence interval:
  67.70746 721.49254
sample estimates:
mean of x mean of y 
   6773.6    6379.0 
```

## RxLRs

```R
x <- c(950, 935, 945, 932, 961, 908, 939, 945, 913, 895)
y <- c(839, 874, 827)
t.test(x,y)
```

Results:

```
	Welch Two Sample t-test

data:  x and y
t = 5.5077, df = 2.9274, p-value = 0.01256
alternative hypothesis: true difference in means is not equal to 0
95 percent confidence interval:
  35.45213 135.81454
sample estimates:
mean of x mean of y 
 932.3000  846.6667 
```

## CRNs

```R
x <- c(68, 59, 62, 67, 61, 63, 71, 75, 74, 68)
y <- c(133, 87, 135)
t.test(x,y)
```

Results:

```
	Welch Two Sample t-test

data:  x and y
t = -3.2671, df = 2.0493, p-value = 0.07965
alternative hypothesis: true difference in means is not equal to 0
95 percent confidence interval:
 -117.85795   14.79128
sample estimates:
mean of x mean of y 
  66.8000  118.3333
```

## ApoPs

```R
x <- c(3993, 3890, 3730, 4003, 4090, 3793, 4001, 4022, 3816, 3622)
y <- c(3343, 3673, 3340)
t.test(x,y)
```

Results:

```
	Welch Two Sample t-test

data:  x and y
t = 3.6885, df = 2.7944, p-value = 0.0389
alternative hypothesis: true difference in means is not equal to 0
95 percent confidence interval:
  44.47278 843.52722
sample estimates:
mean of x mean of y 
     3896      3452 
```
