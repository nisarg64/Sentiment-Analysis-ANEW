library('ggplot2')
bkg.file <- "./csc791_sentiment.csv"
bkg.data <- read.csv(bkg.file, header=TRUE, sep = ",", stringsAsFactors =FALSE)
mydata <- read.csv("./csc791_sentiment.csv")
qplot(x = mydata$Valence,y = mydata$Arousal,xlab = "Valence(Pleasure)", ylab="Arousal(Activation)" , color='cyl',  geom = "point")
