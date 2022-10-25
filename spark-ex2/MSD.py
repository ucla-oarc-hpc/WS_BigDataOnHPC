from pyspark import SparkContext
from pyspark.sql import SparkSession
import pyspark
import json


spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext
sc.setLogLevel("ERROR")


path = "YearPredictionMSD.txt"
MSD_dd = spark.read.csv(path,inferSchema=True,header=False)


MSD_dd.count()


MSD_dd.columns



MSD_dd.select("_c0","_c1","_c2","_c3")




MSD_dd.select("_c0","_c1","_c2","_c3").show(3)



MSD_dd.printSchema()



from pyspark.ml.feature import VectorAssembler 
from pyspark.ml import Pipeline
from pyspark.ml.regression import GBTRegressor
from pyspark.ml.feature import VectorIndexer
from pyspark.ml.evaluation import RegressionEvaluator

(trainingData, testData) = MSD_dd.randomSplit([0.7, 0.3])




feature_columns = MSD_dd.columns[1:]




MSD_data = VectorAssembler(inputCols=feature_columns, outputCol="features")
gbt = GBTRegressor(featuresCol="features", labelCol="_c0", maxIter=10, maxDepth=10)
pipeline = Pipeline(stages=[MSD_data, gbt])


model = pipeline.fit(trainingData)



# Make predictions.
predictions = model.transform(testData)

# Select example rows to display.
predictions.select("prediction", "_c0", "features").show(5)

# Select (prediction, true label) and compute test error
evaluator = RegressionEvaluator(
    labelCol="_c0", predictionCol="prediction", metricName="rmse")
rmse = evaluator.evaluate(predictions)

print("Root Mean Squared Error (RMSE) on test data = %g" % rmse)


