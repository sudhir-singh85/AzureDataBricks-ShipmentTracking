# Databricks notebook source
dbutils.notebook.run("load_orders",60)

# COMMAND ----------

dbutils.notebook.run("load_invoices",60)

# COMMAND ----------

dbutils.notebook.run("load_transactionlineitems",60)

# COMMAND ----------

dbutils.notebook.run("load_temp_Customers",60)

# COMMAND ----------

dbutils.notebook.run("load_temp_Persons",60)

# COMMAND ----------

dbutils.notebook.run("load_shipmentdetails",60)

# COMMAND ----------

dbutils.notebook.run("load_temp_Entities",60)

# COMMAND ----------

dbutils.notebook.run("load_temp_Carriers",60)