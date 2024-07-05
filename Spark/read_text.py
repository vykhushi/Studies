from pyspark.sql import SparkSession
#creating a spark session
spark = SparkSession.builder.appName("fisrtSession").getOrCreate() 
file_path = r"C:\Users\vyask\OneDrive\Desktop\Studies\Spark\demo_data.txt"


#creating rdd out of text file
rdd=spark.sparkContext.textFile(file_path) 

for i in rdd.collect():
    print(i)


count = rdd.count()
print(f"\nNumber of lines in the file: {count}")

spark.stop()

