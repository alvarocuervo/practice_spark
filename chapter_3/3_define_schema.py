from pyspark.sql import SparkSession

#Define schema for our data using DDL (Data Definition Language)
schema = "`ID` INT, `First` STRING, `Last` STRING, `Url` STRING," \
         "`Published` STRING, `Hits` INT, `Campaigns` ARRAY<STRING>"

#Create our static data
data = [[1, "Jules", "Damji", "https://tinyurl.1", "1/4/2016", 4535, ["twitter", "LinkedIn"]],
        [2, "Brooke", "Wenig", "https://tinyurl.2", "5/5/2018", 8908, ["twitter", "LinkedIn"]],
        [3, "Denny", "Lee", "https://tinyurl.3", "6/7/2019", 7659, ["web", "twitter", "FB", "LinkedIn"]],
        [4, "Tathagata", "Das", "https://tinyurl.4", "5/12/2018", 10568, ["twitter", "FB"]],
        [5, "Matei", "Zaharia", "https://tinyurl.5", "5/4/2014", 40578, ["web", "twitter", "FB", "LinkedIn"]],
        [6, "Reynold", "Xin", "https://tinyurl.6", "3/2/2015", 25568, ["twitter", "LinkedIn"]]]

# Main program
if __name__ == "__main__":
    #Create a SparkSession
    spark = (SparkSession
             .builder
             .appName("Example-3_6")
             .getOrCreate())

    #Create a DataFrame using the schema defined above
    blogs_df = spark.createDataFrame(data, schema)

    blogs_df.show()

    #Print the schema used by Spark to process the DataFrame
    print(blogs_df.printSchema())

    #In case that I want to reuse the schema elsewhere in the code... blogs_df.schema
    print(blogs_df.schema)
