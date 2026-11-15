# Big Data Course – Hadoop MapReduce Training

## Exercise 1: Counters and Number of Reducers

### How many files were created in each run?

In the default run, I got 3 output files, from `part-00000` to `part-00002`.

After running with 6 reducers, I got 6 output files, from `part-00000` to `part-00005`.

### Did the number of mappers change? Why?

No, both runs used 9 mappers. Hadoop determines the number of mappers based on the input splits, so changing the number of reducers did not affect it.

### Did the number of reducers change? Why?

Yes. The first run used the default setting of 3 reducers. In the second run, I requested 6 reducers using `-numReduceTasks 6`.

### Did the number of output files change? Why?

Yes, from 3 to 6. Each reducer writes its own `part-xxxxx` file, so adding more reducers also increased the number of output files.

### What does "Merged Map outputs" represent?

This counter counts the map output segments merged by the reducers during the shuffle and merge process.

In my runs, the values matched the number of mappers multiplied by the number of reducers:

- 9 mappers and 3 reducers: `9 × 3 = 27`
- 9 mappers and 6 reducers: `9 × 6 = 54`

## Exercise 2: Case-Insensitive Word Count and Punctuation Cleaning

I updated `mapper.py` to convert each token to lowercase using `.lower()` and remove trailing commas and periods using `.rstrip(',.')`.

After these changes, `Reduce input groups` dropped from **77,639** in Exercise 1 to **54,398**.

This makes sense because words like `The`, `the`, `the.` and `the,` are now counted under the same key.

## Exercise 3: Top 3 Most Frequent Words

I used the following command to combine the output files, sort the counts from highest to lowest, and show the top 3 words:

```bash
hadoop fs -cat /user/hduser/gutenberg-output/part-* | sort -k2 -n -r | head -n 3
```
