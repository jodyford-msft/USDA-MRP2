# Databricks notebook source
# MAGIC %matplotlib inline
# MAGIC
# MAGIC import numpy as np
# MAGIC import matplotlib.pyplot as plt
# MAGIC
# MAGIC # Sample dataset
# MAGIC data = {'apple': 10, 'banana': 5, 'orange': 3}
# MAGIC
# MAGIC # Generate bar chart
# MAGIC plt.bar(data.keys(), data.values())
# MAGIC
# MAGIC # Add chart title and labels
# MAGIC plt.title('Fruit Quantities')
# MAGIC plt.xlabel('Fruit')
# MAGIC plt.ylabel('Quantity')
# MAGIC
# MAGIC # Display chart
# MAGIC plt.show()
