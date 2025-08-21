# Trying to create a simple ELT pipeline

Honestly I've been pushing this around for a while, but one of the skills I've found most useful apart from R data wrangling, has been knowing and managing SQL and pushing things into a pipeline. 
As AI continues to push forth I believe analytical roles will most likely transition to calibration and use of these models. It is also likely that the datapipeline aspect of this
will pick up in value in years to come.

Anyhow, the goal of this project is to create a simple ETL pipeline in my raspberrypi, I want the full cycle, from ingestion to loading into a SQL database, all set up in my raspi. 

I will be using simple python pandas, yfinance, and some SQL libraries. I also hope to be learning more about postgres in this thing. 

1. Select and calibrate what I want from yfinance 
2. Transforming and getting exactly what I want into a writable project. 
3. Setup a postgres locally. 
4. Load the data into the postgres through a routine executable cron thing. <------------------- Currently Here.
5. Create a RShiny to read the data and use that thing, transform into a cute dashboard which lives in my RStudio test thing. 

So yeah, hopefully will learn something in the process. 





