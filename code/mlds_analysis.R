setwd("~/git/seminar_image_quality_and_vision/Guillermo_experiment")

library(MLDS)

## 1. Reading data
d <- read.csv('im_einstein_results.csv')

head(d)


stim <- c(0, 20, 40, 60, 80, 90, 95, 100)

## 2. Analysis with MLDS 
df <- as.mlbs.df(d, stim)


# calls MLDS routine to estimate scale
scale <- mlds(df)

# just prints the scale values in the console
print(scale) 

## 3. Plotting
plot(scale, xlab="Degradation (100 - quality)", ylab="Perceptual scale")

  
write.csv(scale$pscale,"im_einstein_scale.csv")
  

## 4. Optional: calculate CI
# obs.bt <- boot.mlds(scale, nsim=10000)
# obs.bt.res <- summary(obs.bt)
# obs.mns <- obs.bt.res[, 1]
# obs.95ci <- qnorm(0.975) * obs.bt.res[, 2]
# 
# plot(scale, standard.scale=TRUE, xlab="Degradation (100 - quality)", ylab="Perceptual scale")
# segments(scale$stimulus, obs.mns + obs.95ci, scale$stimulus, obs.mns - obs.95ci)
  
  
# END
