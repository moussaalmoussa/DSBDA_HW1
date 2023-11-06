import matplotlib.pyplot as plt

# Sample data: data_amount in some unit, and execution_time in seconds
data_amount = [100, 200, 300, 400]  
execution_time = [30, 50, 70, 80]  

plt.plot(data_amount, execution_time, marker='o')
plt.xlabel('Data Amount (e.g., MB or GB)')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs. Data Amount')
plt.grid(True)
plt.show()
