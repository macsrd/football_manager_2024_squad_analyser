import pandas as pd

# Path to your HTML file
html_file_path = 'Export/FMSA.html'

# Reading the HTML file
# This will return a list of DataFrames, one for each table in the HTML file
dfs = pd.read_html(html_file_path, encoding='utf-8')

# If the HTML file contains only one table, you can get the DataFrame directly
# If there are multiple tables, you can access them by their index in the list
df = dfs[0]  # This assumes there is at least one table

# Display the DataFrame
print(df)


# Assuming 'df' is your original dataframe

# Define the column indices (adjust if you use 0-based indexing)

# Goalkeepers
goalkeeper_d_columns_1 = [4, 13, 15, 16, 28, 39, 44, 47, 48]  # Multiplied by 1
goalkeeper_d_columns_05 = [5, 14, 24, 45]  # Multiplied by 0.5

goalkeeper_libero_d_columns_1 = [13, 14, 16, 24, 28, 39, 44, 48]  # Multiplied by 1
goalkeeper_libero_d_columns_05 = [4, 5, 15, 19, 21, 23, 25, 26, 42, 45, 47]  # Multiplied by 0.5

goalkeeper_libero_s_columns_1 = [13, 14, 16, 19, 24, 28, 39, 42, 44, 48]  # Multiplied by 1
goalkeeper_libero_s_columns_05 = [4, 5, 15, 21, 23, 25, 26, 45, 47]  # Multiplied by 0.5

goalkeeper_libero_a_columns_1 = [13, 14, 16, 19, 24, 28, 39, 42, 44, 48]  # Multiplied by 1
goalkeeper_libero_a_columns_05 = [4, 5, 10, 15, 21, 23, 25, 26, 45, 47]  # Multiplied by 0.5

# Central Defenders

libero_d_columns_1 = [5, 12, 17, 18, 19, 21, 25, 33, 34, 38, 39, 41]  # Multiplied by 1
libero_d_columns_05 = [16, 24, 37, 40, 46]  # Multiplied by 0.5

libero_s_columns_1 = [5, 12, 17, 18, 19, 21, 25, 33, 34, 38, 39, 41]  # Multiplied by 1
libero_s_columns_05 = [9, 16, 23, 24, 37, 40, 46]  # Multiplied by 0.5

# Define the maximum possible values for each column (assuming 100 for simplicity, adjust as needed)

#Goalkeepers
max_values_goalkeeper_d_1 = 20 * len(goalkeeper_d_columns_1)
max_values_goalkeeper_d_05 = 20 * 0.5 * len(goalkeeper_d_columns_05)

max_values_goalkeeper_libero_d_1 = 20 * len(goalkeeper_libero_d_columns_1)
max_values_goalkeeper_libero_d_05 = 20 * 0.5 * len(goalkeeper_libero_d_columns_05)

max_values_goalkeeper_libero_s_1 = 20 * len(goalkeeper_libero_s_columns_1)
max_values_goalkeeper_libero_s_05 = 20 * 0.5 * len(goalkeeper_libero_s_columns_05)

max_values_goalkeeper_libero_a_1 = 20 * len(goalkeeper_libero_a_columns_1)
max_values_goalkeeper_libero_a_05 = 20 * 0.5 * len(goalkeeper_libero_a_columns_05)

# Central Defenders
max_values_libero_d_1 = 20 * len(libero_d_columns_1)
max_values_libero_d_05 = 20 * 0.5 * len(libero_d_columns_05)

max_values_libero_s_1 = 20 * len(libero_s_columns_1)
max_values_libero_s_05 = 20 * 0.5 * len(libero_s_columns_05)

# Create a new DataFrame with 'Name 1' and 'Name 2'
#new_df = df[['Name 1', 'Name 2']].copy()
new_df = df.iloc[: , [0, 1]].copy() 


# Calculate "Goalkeeper (D)" value
goalkeeper_d_1_sum = df.iloc[:, goalkeeper_d_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
goalkeeper_d_05_sum = df.iloc[:, goalkeeper_d_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['Goalkeeper (D)'] = (goalkeeper_d_1_sum + goalkeeper_d_05_sum) / (max_values_goalkeeper_d_1 + max_values_goalkeeper_d_05) * 100  # Calculate as percentage


# Calculate "Goalkeeper-libero (D)" value
goalkeeper_libero_d_1_sum = df.iloc[:, goalkeeper_libero_d_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
goalkeeper_libero_d_05_sum = df.iloc[:, goalkeeper_libero_d_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['Goalkeeper-libero (D)'] = (goalkeeper_libero_d_1_sum + goalkeeper_libero_d_05_sum) / (max_values_goalkeeper_libero_d_1 + max_values_goalkeeper_libero_d_05) * 100  # Calculate as percentage


# Calculate "Goalkeeper-libero (S)" value
goalkeeper_libero_s_1_sum = df.iloc[:, goalkeeper_libero_s_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
goalkeeper_libero_s_05_sum = df.iloc[:, goalkeeper_libero_s_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['Goalkeeper-libero (S)'] = (goalkeeper_libero_s_1_sum + goalkeeper_libero_s_05_sum) / (max_values_goalkeeper_libero_s_1 + max_values_goalkeeper_libero_s_05) * 100  # Calculate as percentage


# Calculate "Goalkeeper-libero (A)" value
goalkeeper_libero_a_1_sum = df.iloc[:, goalkeeper_libero_a_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
goalkeeper_libero_a_05_sum = df.iloc[:, goalkeeper_libero_a_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['Goalkeeper-libero (A)'] = (goalkeeper_libero_a_1_sum + goalkeeper_libero_a_05_sum) / (max_values_goalkeeper_libero_a_1 + max_values_goalkeeper_libero_a_05) * 100  # Calculate as percentage

# Calculate "Libero (D)" value
libero_d_1_sum = df.iloc[:, libero_d_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
libero_d_05_sum = df.iloc[:, libero_d_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['Libero (D)'] = (libero_d_1_sum + libero_d_05_sum) / (max_values_libero_d_1 + max_values_libero_d_05) * 100  # Calculate as percentage

# Calculate "Libero (S)" value
libero_s_1_sum = df.iloc[:, libero_s_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
libero_s_05_sum = df.iloc[:, libero_s_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['Libero (S)'] = (libero_s_1_sum + libero_s_05_sum) / (max_values_libero_s_1 + max_values_libero_s_05) * 100  # Calculate as percentage

# Display the new dataframe
print(new_df)