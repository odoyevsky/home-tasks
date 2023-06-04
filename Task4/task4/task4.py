from pyspark.sql import Row
from pyspark.sql import functions as F
from pyspark.sql import SparkSession

import findspark

findspark.init()

spark = SparkSession.builder \
    .config("spark.driver.bindAddress", "127.0.0.1") \
    .config("spark.driver.port", "8888") \
    .getOrCreate()

dates = spark.createDataFrame([
    Row(date='2022-01-20'),
    Row(date='2022-01-18'),
    Row(date='2022-01-16'),
])

calls = spark.createDataFrame([
    Row(date='2022-01-20', call_id='ERCERCER', audio_file='rec_12536123.wav', oper_id=134),
    Row(date='2022-01-20', call_id='34FEWEC3', audio_file='rec_89372934.wav', oper_id=134),
    Row(date='2022-01-20', call_id='ERC34F3E', audio_file='rec_56756775.wav', oper_id=134),
    Row(date='2022-01-20', call_id='ERCJNER8', audio_file='rec_32454565.wav', oper_id=128),
    Row(date='2022-01-20', call_id='ERLHCRE8', audio_file='rec_34545567.wav', oper_id=125),
    Row(date='2022-01-20', call_id='LKECRE9C', audio_file='rec_23434564.wav', oper_id=125),
    Row(date='2022-01-19', call_id='LJC8ER24', audio_file='rec_65778978.wav', oper_id=127),
    Row(date='2022-01-19', call_id='KJNDFC94', audio_file='rec_34545766.wav', oper_id=128),
    Row(date='2022-01-19', call_id='KJDC9833', audio_file='rec_34545656.wav', oper_id=125),
    Row(date='2022-01-19', call_id='JHB38743', audio_file='rec_23434545.wav', oper_id=125),
    Row(date='2022-01-19', call_id='U7JH76H5', audio_file='rec_56767876.wav', oper_id=127),
    Row(date='2022-01-18', call_id='34F345F4', audio_file='rec_56567678.wav', oper_id=134),
    Row(date='2022-01-18', call_id='WED34F45', audio_file='rec_34534534.wav', oper_id=134),
    Row(date='2022-01-18', call_id='W3D34F56', audio_file='rec_56756767.wav', oper_id=134),
    Row(date='2022-01-18', call_id='WF435F55', audio_file='rec_23434534.wav', oper_id=116),
    Row(date='2022-01-17', call_id='NKDBUS83', audio_file='rec_13434876.wav', oper_id=134),
    Row(date='2022-01-17', call_id='NBE83642', audio_file='rec_13434468.wav', oper_id=116),
    Row(date='2022-01-17', call_id='NVID49DF', audio_file='rec_13434111.wav', oper_id=134),
])

calls.show()
dates.show()

spark.stop()