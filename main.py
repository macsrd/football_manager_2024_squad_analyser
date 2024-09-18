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

tcd_d_columns_1 = [12, 17, 18, 33, 34, 39]  # Multiplied by 1
tcd_d_columns_05 = [2, 16, 24, 37, 40]  # Multiplied by 0.5

tcd_s_columns_1 = [2, 12, 18, 33, 34, 39, 40]  # Multiplied by 1
tcd_s_columns_05 = [16, 17, 24]  # Multiplied by 0.5

tcd_c_columns_1 = [16, 17, 18, 24, 37, 39]  # Multiplied by 1
tcd_c_columns_05 = [12, 33, 34, 40]  # Multiplied by 0.5

cd_d_columns_1 = [12, 17, 18, 33, 34, 39]  # Multiplied by 1
cd_d_columns_05 = [2, 5, 16, 19, 24, 37, 40]  # Multiplied by 0.5

cd_s_columns_1 = [2, 5, 12, 18, 33, 34, 39, 40]  # Multiplied by 1
cd_s_columns_05 = [16, 17, 19, 24]  # Multiplied by 0.5

cd_c_columns_1 = [16, 17, 18, 24, 37, 39]  # Multiplied by 1
cd_c_columns_05 = [12, 19, 33, 34, 40]  # Multiplied by 0.5

bpd_d_columns_1 = [12, 17, 18, 19, 21, 33, 34, 39]  # Multiplied by 1
bpd_d_columns_05 = [2, 5, 16, 23, 24, 25, 37, 38, 40]  # Multiplied by 0.5

bpd_s_columns_1 = [2, 5, 12, 18, 19, 21, 33, 34, 39, 40]  # Multiplied by 1
bpd_s_columns_05 = [16, 17, 23, 24, 25, 38]  # Multiplied by 0.5

bpd_c_columns_1 = [5, 16, 17, 18, 19, 21, 24, 37, 39]  # Multiplied by 1
bpd_c_columns_05 = [12, 23, 25, 33, 34, 38, 40]  # Multiplied by 0.5

wcb_d_columns_1 = [12, 17, 18, 33, 34, 39]  # Multiplied by 1
wcb_d_columns_05 = [2, 5, 9, 16, 19, 21, 22, 24, 25, 37, 38, 40, 48]  # Multiplied by 0.5

wcb_s_columns_1 = [9, 12, 17, 18, 33, 34, 37, 39]  # Multiplied by 1
wcb_s_columns_05 = [2, 5, 8, 11, 16, 19, 21, 22, 24, 25, 38, 40, 46, 48]  # Multiplied by 0.5

wcb_a_columns_1 = [8, 9, 11, 12, 17, 18, 33, 34, 37, 46]  # Multiplied by 1
wcb_a_columns_05 = [2, 5, 16, 19, 21, 22, 24, 25, 38, 39, 40, 48]  # Multiplied by 0.5

# Wide Defenders

fb_d_columns_1 = [16, 17, 18, 24, 39]
fb_d_columns_05 = [5, 8, 21, 22, 37, 41, 46]

fb_s_columns_1 = [16, 17, 18, 24, 39]
fb_s_columns_05 = [5, 8, 9, 21, 22, 37, 38, 41, 46]

fb_a_columns_1 = [16, 17, 28, 24, 39]
fb_a_columns_05 = [5, 8, 9, 11, 21, 22, 25, 37, 38, 41, 46, 48]

wb_d_columns_1 = [17, 18, 22, 24, 26, 39, 41, 46]
wb_d_columns_05 = [5, 8, 9, 11, 16, 21, 25, 29, 37, 38, 48]

wb_s_columns_1 = [8, 9, 11, 17, 18, 22, 26, 41, 46]
wb_s_columns_05 = [5, 16, 21, 24, 25, 29, 37, 38, 39, 48]

wb_a_columns_1 = [8, 9, 11, 18, 22, 26, 37, 38, 41, 46]
wb_a_columns_05 = [3, 5, 16, 17, 21, 24, 25, 29, 39, 48]

n_n_fb_columns_1 = [17, 18, 24, 33, 39]
n_n_fb_columns_05 = [2, 12, 16, 40, 41]

cwb_s_columns_1 = [8, 9, 11, 22, 26, 38, 41, 46]
cwb_s_columns_05 = [3, 5, 17, 18, 21, 24, 25, 29, 37, 39, 48]

cwb_a_columns_1 = [3, 8, 9, 11, 22, 26, 38, 41, 46]
cwb_a_columns_05 = [5, 17, 18, 21, 24, 25, 29, 37, 39, 48]

iwb_d_columns_1 = [5, 18, 21, 24, 39, 41]
iwb_d_columns_05 = [11, 16, 17, 19, 22, 25, 26, 38, 46, 48]

iwb_s_columns_1 = [5, 18, 21, 24, 39, 41]
iwb_s_columns_05 = [11, 16, 17, 19, 22, 23, 25, 26, 38, 46, 48]

iwb_a_columns_1 = [5, 11, 18, 19, 21, 23, 26, 41]
iwb_a_columns_05 = [3, 8, 9, 16, 17, 22, 24, 25, 36, 37, 38, 39, 46, 48]

ifb_d_columns_1 = [12, 17, 18, 33, 39]
ifb_d_columns_05 = [2, 5, 9, 16, 19, 21, 22, 24, 25, 34, 37, 38, 40, 48]

# Midfielders

bwm_d_columns_1 = [2, 18, 22, 26, 41, 46]
bwm_d_columns_05 = [16, 17, 33, 37, 49, 40, 48]

bwm_s_columns_1 = [2, 18, 22, 26, 41, 46]
bwm_s_columns_05 = [16, 17, 21, 33, 37, 40, 48]

am_d_columns_1 = [5, 16, 17, 18, 24, 39] # RD(O) to confirm
am_d_columns_05 = [19, 33, 41]

dm_d_columns_1 = [16, 18 ,24, 39, 41]
dm_d_columns_05 = [2, 5, 17, 19, 21, 22, 33, 46]

dm_s_columns_1 = [16, 18, 24, 39, 41]
dm_s_columns_05 = [2, 5, 17, 19, 21, 22, 25, 33, 46]

hb_d_columns_1 = [5, 16, 17, 18, 19, 24, 39, 41]
hb_d_columns_05 = [2, 21, 22, 25, 33, 34, 40, 46]

dlp_d_columns_1 = [5, 19, 21 ,23, 25, 38, 41]
dlp_d_columns_05 = [18, 24, 29, 39]

dlp_s_columns_1 = [5, 19, 21, 23, 25, 38, 41]
dlp_s_columns_05 = [11, 24, 29, 39]

sv_s_columns_1 = [11, 17, 18, 21, 22, 37, 39, 46]
sv_s_columns_05 = [5, 16, 19, 24, 25, 26, 29, 33, 36, 43]

sv_a_columns_1 = [11, 18, 21, 22, 24, 36, 37, 39, 43, 46]
sv_a_columns_05 = [5, 16, 17, 19, 25, 26, 29, 33]

rp_s_columns_1 = [5, 11, 19, 21, 22, 23, 24, 25, 26, 38, 46]
rp_s_columns_05 = [9, 16, 29, 36, 37, 39, 48]

reg_s_columns_1 = [5, 11, 19, 21, 23, 25, 38, 41]
reg_s_columns_05 = [9, 24, 29, 36]

cm_d_columns_1 = [5, 16, 18, 39, 41]
cm_d_columns_05 = [2, 17, 19, 21, 22, 24, 25, 38, 46]

cm_s_columns_1 = [5, 18, 21, 25, 41]
cm_s_columns_05 = [11, 16, 19, 22, 23, 24, 38, 46]

cm_a_columns_1 = [5, 11, 21, 25]
cm_a_columns_05 = [18, 19, 22, 23, 24, 26, 36, 38, 41, 46]

car_s_columns_1 = [5, 18, 21, 25, 39, 41, 46]
car_s_columns_05 = [11, 16, 19, 22, 23, 24, 38]

b2b_s_columns_1 = [11, 18, 21, 22, 41, 46]
b2b_s_columns_05 = [2, 5, 9, 19, 24, 25, 26, 29, 33, 36, 37, 39]

mez_s_columns_1 = [5, 11, 21, 22, 38]
mez_s_columns_05 = [9, 18, 19, 23, 24, 25, 29, 36, 46]

mez_a_columns_1 = [5, 9, 11, 21, 22, 23, 38]
mez_a_columns_05 = [3, 19, 24, 25, 29, 36, 43, 46]

ap_s_columns_1 = [5, 11, 19, 21, 23, 25, 38, 41]
ap_s_columns_05 = [3, 9, 24, 48]

ap_a_columns_1 = [5, 11, 19, 21, 23, 25, 38, 41]
ap_a_columns_05 = [3, 9, 24, 26, 48]



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

max_values_tcd_d_1 = 20 * len(tcd_s_columns_1)
max_values_tcd_d_05 = 20 * 0.5 * len(tcd_d_columns_05)

max_values_tcd_s_1 = 20 * len(tcd_s_columns_1)
max_values_tcd_s_05 = 20 * 0.5 * len(tcd_d_columns_05)

max_values_tcd_c_1 = 20 * len(tcd_c_columns_1)
max_values_tcd_c_05 = 20 * 0.5 * len(tcd_c_columns_05)

max_values_cd_d_1 = 20 * len(cd_d_columns_1)
max_values_cd_d_05 = 20 * 0.5 * len(cd_d_columns_05)

max_values_cd_s_1 = 20 * len(cd_s_columns_1)
max_values_cd_s_05 = 20 * 0.5 * len(cd_s_columns_05)

max_values_cd_c_1 = 20 * len(cd_c_columns_1)
max_values_cd_c_05 = 20 * 0.5 * len(cd_c_columns_05)

max_values_bpd_d_1 = 20 * len(bpd_d_columns_1)
max_values_bpd_d_05 = 20 * 0.5 * len(bpd_d_columns_05)

max_values_bpd_s_1 = 20 * len(bpd_s_columns_1)
max_values_bpd_s_05 = 20 * 0.5 * len(bpd_s_columns_05)

max_values_bpd_c_1 = 20 * len(bpd_c_columns_1)
max_values_bpd_c_05 = 20 * 0.5 * len(bpd_c_columns_05)

max_values_wcb_d_1 = 20 * len(wcb_d_columns_1)
max_values_wcb_d_05 = 20 * 0.5 * len(wcb_d_columns_05)

max_values_wcb_s_1 = 20 * len(wcb_s_columns_1)
max_values_wcb_s_05 = 20 * 0.5 * len(wcb_s_columns_05)

max_values_wcb_a_1 = 20 * len(wcb_a_columns_1)
max_values_wcb_a_05 = 20 * 0.5 * len(wcb_a_columns_05)

# Wide Defenders

max_values_fb_d_1 = 20 * len(fb_d_columns_1)
max_values_fb_d_05 = 20 * 0.5 * len(fb_d_columns_05)

max_values_fb_s_1 = 20 * len(fb_s_columns_1)
max_values_fb_s_05 = 20 * 0.5 * len(fb_s_columns_05)

max_values_fb_a_1 = 20 * len(fb_a_columns_1)
max_values_fb_a_05 = 20 * 0.5 * len(fb_a_columns_05)

max_values_wb_d_1 = 20 * len(wb_d_columns_1)
max_values_wb_d_05 = 20 * 0.5 * len(wb_d_columns_05)

max_values_wb_s_1 = 20 * len(wb_s_columns_1)
max_values_wb_s_05 = 20 * 0.5 * len(wb_s_columns_05)

max_values_wb_a_1 = 20 * len(wb_a_columns_1)
max_values_wb_a_05 = 20 * 0.5 * len(wb_a_columns_05)

max_values_n_n_fb_1 = 20 * len(n_n_fb_columns_1)
max_values_n_n_fb_05 = 20 * 0.5 * len(n_n_fb_columns_05)

max_values_cwb_s_1 = 20 * len(cwb_s_columns_1)
max_values_cwb_s_05 = 20 * 0.5 * len(cwb_s_columns_05)

max_values_cwb_a_1 = 20 * len(cwb_a_columns_1)
max_values_cwb_a_05 = 20 * 0.5 * len(cwb_a_columns_05)

max_values_iwb_d_1 = 20 * len(iwb_d_columns_1)
max_values_iwb_d_05 = 20 * 0.5 * len(iwb_d_columns_05)

max_values_iwb_s_1 = 20 * len(iwb_s_columns_1)
max_values_iwb_s_05 = 20 * 0.5 * len(iwb_s_columns_05)

max_values_iwb_a_1 = 20 * len(iwb_a_columns_1)
max_values_iwb_a_05 = 20 * 0.5 * len(iwb_a_columns_05)

max_values_ifb_d_1 = 20 * len(ifb_d_columns_1)
max_values_ifb_d_05 = 20 * 0.5 * len(ifb_d_columns_05)

# Midfielders

max_values_bwm_d_1 = 20 * len(ifb_d_columns_1)
max_values_bwm_d_05 = 20 * 0.5 * len(ifb_d_columns_05)

max_values_bwm_s_1 = 20 * len(ifb_d_columns_1)
max_values_bwm_s_05 = 20 * 0.5 * len(ifb_d_columns_05)

max_values_am_d_1 = 20 * len(ifb_d_columns_1)
max_values_am_d_05 = 20 * 0.5 * len(ifb_d_columns_05)

max_values_dm_d_1 = 20 * len(ifb_d_columns_1)
max_values_dm_d_05 = 20 * 0.5 * len(ifb_d_columns_05)

max_values_dm_s_1 = 20 * len(ifb_d_columns_1)
max_values_dm_s_05 = 20 * 0.5 * len(ifb_d_columns_05)

max_values_hb_d_1 = 20 * len(ifb_d_columns_1)
max_values_hb_d_05 = 20 * 0.5 * len(ifb_d_columns_05)

max_values_dlp_d_1 = 20 * len(ifb_d_columns_1)
max_values_dlp_d_05 = 20 * 0.5 * len(ifb_d_columns_05)

max_values_dlp_s_1 = 20 * len(ifb_d_columns_1)
max_values_dlp_s_05 = 20 * 0.5 * len(ifb_d_columns_05)

max_values_sv_s_1 = 20 * len(ifb_d_columns_1)
max_values_sv_s_05 = 20 * 0.5 * len(ifb_d_columns_05)

max_values_sv_a_1 = 20 * len(ifb_d_columns_1)
max_values_sv_a_05 = 20 * 0.5 * len(ifb_d_columns_05)

max_values_rp_s_1 = 20 * len(ifb_d_columns_1)
max_values_rp_s_05 = 20 * 0.5 * len(ifb_d_columns_05)

max_values_reg_s_1 = 20 * len(ifb_d_columns_1)
max_values_reg_s_05 = 20 * 0.5 * len(ifb_d_columns_05)

max_values_cm_d_1 = 20 * len(ifb_d_columns_1)
max_values_cm_d_05 = 20 * 0.5 * len(ifb_d_columns_05)

max_values_cm_s_1 = 20 * len(ifb_d_columns_1)
max_values_cm_s_05 = 20 * 0.5 * len(ifb_d_columns_05)

max_values_cm_a_1 = 20 * len(ifb_d_columns_1)
max_values_cm_a_05 = 20 * 0.5 * len(ifb_d_columns_05)

max_values_car_s_1 = 20 * len(ifb_d_columns_1)
max_values_car_s_05 = 20 * 0.5 * len(ifb_d_columns_05)

max_values_b2b_s_1 = 20 * len(ifb_d_columns_1)
max_values_b2b_s_05 = 20 * 0.5 * len(ifb_d_columns_05)

max_values_mez_s_1 = 20 * len(ifb_d_columns_1)
max_values_mez_s_05 = 20 * 0.5 * len(ifb_d_columns_05)

max_values_mez_a_1 = 20 * len(ifb_d_columns_1)
max_values_mez_a_05 = 20 * 0.5 * len(ifb_d_columns_05)

max_values_ap_s_1 = 20 * len(ifb_d_columns_1)
max_values_ap_s_05 = 20 * 0.5 * len(ifb_d_columns_05)

max_values_ap_a_1 = 20 * len(ifb_d_columns_1)
max_values_ap_a_05 = 20 * 0.5 * len(ifb_d_columns_05)


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

# Calculate "TCD (D)" value
tcd_d_1_sum = df.iloc[:, tcd_d_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
tcd_d_05_sum = df.iloc[:, tcd_d_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['TCD (D)'] = (tcd_d_1_sum + tcd_d_05_sum) / (max_values_tcd_d_1 + max_values_tcd_d_05) * 100  # Calculate as percentage

# Calculate "TCD (S)" value
tcd_s_1_sum = df.iloc[:, tcd_s_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
tcd_s_05_sum = df.iloc[:, tcd_s_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['TCD (S)'] = (tcd_s_1_sum + tcd_s_05_sum) / (max_values_tcd_s_1 + max_values_tcd_s_05) * 100  # Calculate as percentage

# Calculate "TCD (C)" value
tcd_c_1_sum = df.iloc[:, tcd_c_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
tcd_c_05_sum = df.iloc[:, tcd_c_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['TCD (C)'] = (tcd_c_1_sum + tcd_c_05_sum) / (max_values_tcd_c_1 + max_values_tcd_c_05) * 100  # Calculate as percentage

# Calculate "CD (D)" value
cd_d_1_sum = df.iloc[:, cd_d_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
cd_d_05_sum = df.iloc[:, cd_d_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['CD (D)'] = (cd_d_1_sum + cd_d_05_sum) / (max_values_cd_d_1 + max_values_cd_d_05) * 100  # Calculate as percentage

# Calculate "CD (S)" value
cd_s_1_sum = df.iloc[:, cd_s_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
cd_s_05_sum = df.iloc[:, cd_s_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['CD (S)'] = (cd_s_1_sum + cd_s_05_sum) / (max_values_cd_s_1 + max_values_cd_s_05) * 100  # Calculate as percentage

# Calculate "CD (C)" value
cd_c_1_sum = df.iloc[:, cd_c_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
cd_c_05_sum = df.iloc[:, cd_c_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['CD (C)'] = (cd_c_1_sum + cd_c_05_sum) / (max_values_cd_c_1 + max_values_cd_c_05) * 100  # Calculate as percentage

# Calculate "BPD (D)" value
bpd_d_1_sum = df.iloc[:, bpd_d_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
bpd_d_05_sum = df.iloc[:, bpd_d_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['BPD (D)'] = (bpd_d_1_sum + bpd_d_05_sum) / (max_values_bpd_d_1 + max_values_bpd_d_05) * 100  # Calculate as percentage

# Calculate "BPD (S)" value
bpd_s_1_sum = df.iloc[:, bpd_s_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
bpd_s_05_sum = df.iloc[:, bpd_s_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['BPD (S)'] = (bpd_s_1_sum + bpd_s_05_sum) / (max_values_bpd_s_1 + max_values_bpd_s_05) * 100  # Calculate as percentage

# Calculate "BPD (C)" value
bpd_c_1_sum = df.iloc[:, bpd_c_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
bpd_c_05_sum = df.iloc[:, bpd_c_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['BPD (C)'] = (bpd_c_1_sum + bpd_c_05_sum) / (max_values_bpd_c_1 + max_values_bpd_c_05) * 100  # Calculate as percentage

# Calculate "WCB (D)" value
wcb_d_1_sum = df.iloc[:, wcb_d_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
wcb_d_05_sum = df.iloc[:, wcb_d_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['WCB (D)'] = (wcb_d_1_sum + wcb_d_05_sum) / (max_values_wcb_d_1 + max_values_wcb_d_05) * 100  # Calculate as percentage

# Calculate "WCB (S)" value
wcb_s_1_sum = df.iloc[:, wcb_s_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
wcb_s_05_sum = df.iloc[:, wcb_s_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['WCB (S)'] = (wcb_s_1_sum + wcb_s_05_sum) / (max_values_wcb_s_1 + max_values_wcb_s_05) * 100  # Calculate as percentage

# Calculate "WCB (A)" value
wcb_a_1_sum = df.iloc[:, wcb_a_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
wcb_a_05_sum = df.iloc[:, wcb_a_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['WCB (A)'] = (wcb_a_1_sum + wcb_a_05_sum) / (max_values_wcb_a_1 + max_values_wcb_a_05) * 100  # Calculate as percentage

# Calculate "FB (D)" value
fb_d_1_sum = df.iloc[:, fb_d_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
fb_d_05_sum = df.iloc[:, fb_d_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['FB (D)'] = (fb_d_1_sum + fb_d_05_sum) / (max_values_fb_d_1 + max_values_fb_d_05) * 100  # Calculate as percentage

# Calculate "FB (S)" value
fb_s_1_sum = df.iloc[:, fb_s_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
fb_s_05_sum = df.iloc[:, fb_s_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['FB (S)'] = (fb_s_1_sum + fb_s_05_sum) / (max_values_fb_s_1 + max_values_fb_s_05) * 100  # Calculate as percentage

# Calculate "FB (A)" value
fb_a_1_sum = df.iloc[:, fb_a_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
fb_a_05_sum = df.iloc[:, fb_a_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['FB (A)'] = (fb_a_1_sum + fb_a_05_sum) / (max_values_fb_a_1 + max_values_fb_a_05) * 100  # Calculate as percentage

# Calculate "WB (D)" value
wb_d_1_sum = df.iloc[:, wb_d_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
wb_d_05_sum = df.iloc[:, wb_d_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['WB (D)'] = (wb_d_1_sum + wb_d_05_sum) / (max_values_wb_d_1 + max_values_wb_d_05) * 100  # Calculate as percentage

# Calculate "WB (S)" value
wb_s_1_sum = df.iloc[:, wb_s_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
wb_s_05_sum = df.iloc[:, wb_s_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['WB (S)'] = (wb_s_1_sum + wb_s_05_sum) / (max_values_wb_s_1 + max_values_wb_s_05) * 100  # Calculate as percentage

# Calculate "WB (A)" value
wb_a_1_sum = df.iloc[:, wb_a_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
wb_a_05_sum = df.iloc[:, wb_a_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['WB (A)'] = (wb_a_1_sum + wb_a_05_sum) / (max_values_wb_a_1 + max_values_wb_a_05) * 100  # Calculate as percentage

# Calculate "N-N FB" value
n_n_fb_1_sum = df.iloc[:, n_n_fb_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
n_n_fb_05_sum = df.iloc[:, n_n_fb_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['N_N FB'] = (n_n_fb_1_sum + n_n_fb_05_sum) / (max_values_n_n_fb_1 + max_values_n_n_fb_05) * 100  # Calculate as percentage

# Calculate "CWB (S)" value
cwb_s_1_sum = df.iloc[:, cwb_s_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
cwb_s_05_sum = df.iloc[:, cwb_s_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['CWB (S)'] = (cwb_s_1_sum + cwb_s_05_sum) / (max_values_cwb_s_1 + max_values_cwb_s_05) * 100  # Calculate as percentage

# Calculate "CWB (A)" value
cwb_a_1_sum = df.iloc[:, cwb_a_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
cwb_a_05_sum = df.iloc[:, cwb_a_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['CWB (A)'] = (cwb_a_1_sum + cwb_a_05_sum) / (max_values_cwb_a_1 + max_values_cwb_a_05) * 100  # Calculate as percentage

# Calculate "IWB (D)" value
iwb_d_1_sum = df.iloc[:, iwb_d_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
iwb_d_05_sum = df.iloc[:, iwb_d_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['IWB (D)'] = (iwb_d_1_sum + iwb_d_05_sum) / (max_values_iwb_d_1 + max_values_iwb_d_05) * 100  # Calculate as percentage

# Calculate "IWB (S)" value
iwb_s_1_sum = df.iloc[:, iwb_s_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
iwb_s_05_sum = df.iloc[:, iwb_s_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['IWB (S)'] = (iwb_s_1_sum + iwb_s_05_sum) / (max_values_iwb_s_1 + max_values_iwb_s_05) * 100  # Calculate as percentage

# Calculate "IWB (A)" value
iwb_a_1_sum = df.iloc[:, iwb_a_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
iwb_a_05_sum = df.iloc[:, iwb_a_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['IWB (A)'] = (iwb_a_1_sum + iwb_a_05_sum) / (max_values_iwb_a_1 + max_values_iwb_a_05) * 100  # Calculate as percentage

# Calculate "IFB (D)" value
ifb_d_1_sum = df.iloc[:, ifb_d_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
ifb_d_05_sum = df.iloc[:, ifb_d_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['IFB (D)'] = (ifb_d_1_sum + ifb_d_05_sum) / (max_values_ifb_d_1 + max_values_ifb_d_05) * 100  # Calculate as percentage

# Calculate "BWM (D)" value
bwm_d_1_sum = df.iloc[:, bwm_d_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
bwm_d_05_sum = df.iloc[:, bwm_d_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['BWM (D)'] = (bwm_d_1_sum + bwm_d_05_sum) / (max_values_bwm_d_1 + max_values_bwm_d_05) * 100  # Calculate as percentage

# Calculate "BWM (S)" value
bwm_s_1_sum = df.iloc[:, bwm_s_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
bwm_s_05_sum = df.iloc[:, bwm_s_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['BWM (S)'] = (bwm_s_1_sum + bwm_s_05_sum) / (max_values_bwm_s_1 + max_values_bwm_s_05) * 100  # Calculate as percentage

# Calculate "AM (D)" value
am_d_1_sum = df.iloc[:, am_d_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
am_d_05_sum = df.iloc[:, am_d_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['AM (D)'] = (am_d_1_sum + am_d_05_sum) / (max_values_am_d_1 + max_values_am_d_05) * 100  # Calculate as percentage

# Calculate "DM (D)" value
dm_d_1_sum = df.iloc[:, dm_d_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
dm_d_05_sum = df.iloc[:, dm_d_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['DM (D)'] = (dm_d_1_sum + dm_d_05_sum) / (max_values_dm_d_1 + max_values_dm_d_05) * 100  # Calculate as percentage

# Calculate "DM (S)" value
dm_s_1_sum = df.iloc[:, dm_s_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
dm_s_05_sum = df.iloc[:, dm_s_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['DM (S)'] = (dm_s_1_sum + dm_s_05_sum) / (max_values_dm_s_1 + max_values_dm_s_05) * 100  # Calculate as percentage

# Calculate "HB (D)" value
hb_d_1_sum = df.iloc[:, hb_d_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
hb_d_05_sum = df.iloc[:, hb_d_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['HB (D)'] = (hb_d_1_sum + hb_d_05_sum) / (max_values_hb_d_1 + max_values_hb_d_05) * 100  # Calculate as percentage

# Calculate "DLP (D)" value
dlp_d_1_sum = df.iloc[:, dlp_d_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
dlp_d_05_sum = df.iloc[:, dlp_d_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['DLP (D)'] = (dlp_d_1_sum + dlp_d_05_sum) / (max_values_dlp_d_1 + max_values_dlp_d_05) * 100  # Calculate as percentage

# Calculate "DLP (S)" value
dlp_s_1_sum = df.iloc[:, dlp_s_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
dlp_s_05_sum = df.iloc[:, dlp_s_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['DLP (S)'] = (dlp_s_1_sum + dlp_s_05_sum) / (max_values_dlp_s_1 + max_values_dlp_s_05) * 100  # Calculate as percentage

# Calculate "SV (S)" value
sv_s_1_sum = df.iloc[:, sv_s_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
sv_s_05_sum = df.iloc[:, sv_s_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['SV (S)'] = (sv_s_1_sum + sv_s_05_sum) / (max_values_sv_s_1 + max_values_sv_s_05) * 100  # Calculate as percentage

# Calculate "SV (A)" value
sv_a_1_sum = df.iloc[:, sv_a_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
sv_a_05_sum = df.iloc[:, sv_a_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['SV (A)'] = (sv_a_1_sum + sv_a_05_sum) / (max_values_sv_a_1 + max_values_sv_a_05) * 100  # Calculate as percentage

# Calculate "RP (S)" value
rp_s_1_sum = df.iloc[:, rp_s_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
rp_s_05_sum = df.iloc[:, rp_s_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['RP (S)'] = (rp_s_1_sum + rp_s_05_sum) / (max_values_rp_s_1 + max_values_rp_s_05) * 100  # Calculate as percentage

# Calculate "REG (S)" value
reg_s_1_sum = df.iloc[:, reg_s_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
reg_s_05_sum = df.iloc[:, reg_s_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['REG (S)'] = (reg_s_1_sum + reg_s_05_sum) / (max_values_reg_s_1 + max_values_reg_s_05) * 100  # Calculate as percentage

# Calculate "CM (D)" value
cm_d_1_sum = df.iloc[:, cm_d_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
cm_d_05_sum = df.iloc[:, cm_d_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['CM (D)'] = (cm_d_1_sum + cm_d_05_sum) / (max_values_cm_d_1 + max_values_cm_d_05) * 100  # Calculate as percentage

# Calculate "CM (S)" value
cm_s_1_sum = df.iloc[:, cm_s_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
cm_s_05_sum = df.iloc[:, cm_s_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['CM (S)'] = (cm_s_1_sum + cm_s_05_sum) / (max_values_cm_s_1 + max_values_cm_s_05) * 100  # Calculate as percentage

# Calculate "CM (A)" value
cm_a_1_sum = df.iloc[:, cm_a_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
cm_a_05_sum = df.iloc[:, cm_a_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['CM (A)'] = (cm_a_1_sum + cm_a_05_sum) / (max_values_cm_a_1 + max_values_cm_a_05) * 100  # Calculate as percentage

# Calculate "CAR (S)" value
car_s_1_sum = df.iloc[:, car_s_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
car_s_05_sum = df.iloc[:, car_s_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['CAR (S)'] = (car_s_1_sum + car_s_05_sum) / (max_values_car_s_1 + max_values_car_s_05) * 100  # Calculate as percentage

# Calculate "B2B (S)" value
b2b_s_1_sum = df.iloc[:, b2b_s_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
b2b_s_05_sum = df.iloc[:, b2b_s_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['B2B (S)'] = (b2b_s_1_sum + b2b_s_05_sum) / (max_values_b2b_s_1 + max_values_b2b_s_05) * 100  # Calculate as percentage

# Calculate "MEZ (S)" value
mez_s_1_sum = df.iloc[:, mez_s_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
mez_s_05_sum = df.iloc[:, mez_s_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['MEZ (S)'] = (mez_s_1_sum + mez_s_05_sum) / (max_values_mez_s_1 + max_values_mez_s_05) * 100  # Calculate as percentage

# Calculate "MEZ (A)" value
mez_a_1_sum = df.iloc[:, mez_a_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
mez_a_05_sum = df.iloc[:, mez_a_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['MEZ (A)'] = (mez_a_1_sum + mez_a_05_sum) / (max_values_mez_a_1 + max_values_mez_a_05) * 100  # Calculate as percentage

# Calculate "AP (S)" value
ap_s_1_sum = df.iloc[:, ap_s_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
ap_s_05_sum = df.iloc[:, ap_s_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['AP (S)'] = (ap_s_1_sum + ap_s_05_sum) / (max_values_ap_s_1 + max_values_ap_s_05) * 100  # Calculate as percentage

# Calculate "AP (A)" value
ap_a_1_sum = df.iloc[:, ap_a_columns_1].sum(axis=1)  # Sum of columns with multiplier 1
ap_a_05_sum = df.iloc[:, ap_a_columns_05].sum(axis=1) * 0.5  # Sum of columns with multiplier 0.5
new_df['AP (A)'] = (ap_a_1_sum + ap_a_05_sum) / (max_values_ap_a_1 + max_values_ap_a_05) * 100  # Calculate as percentage

# Display the new dataframe
print(new_df)