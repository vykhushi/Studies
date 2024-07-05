from pyspark.sql import SparkSession
#creating a spark session
spark = SparkSession.builder.appName("fisrtSession").getOrCreate() 
file_path = r"C:\Users\vyask\OneDrive\Desktop\Studies\Spark\demo_csv.csv"

#creating dataframe 
df=spark.read.csv(file_path,header=True,inferSchema=True)
                  
df.show()

df.printSchema()



spark.stop()