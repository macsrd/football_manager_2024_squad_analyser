import pandas as pd
import PySimpleGUI as sg

# GUI to select file location
## To consider changing PySimpleGUI to open source GUI as it's licensed now.

open_window = [
    [sg.Text("Please select an HTML Football Manager 2024 Export file:")],
    [sg.Input(), sg.FileBrowse(file_types=(("HTML Files", "*.html"),))],
    [sg.OK(), sg.Cancel()]
]

window = sg.Window("File Selector", open_window)

event, values = window.read()
window.close()

if event == 'OK' and values[0]:
    html_file_path = values[0]

else:
    print("No file selected or action canceled.")

# Reading HTML file in utf-8 format.
## Reading RTF file format also to be added
dfs = pd.read_html(html_file_path, encoding='utf-8')

# Reading first table in dataframe (there should be always one - just in case)
df = dfs[0] 

# Printing DataFrame (for testing)
# print(df)

# Range of columns to check for integers (columns 2 to 48 for squad view)
cols_to_check = list(range(2, 48)) 

# Function to check if a value is an integer
def is_integer(val):
    try:
        return int(val) == val 
    except (ValueError, TypeError):
        return False
    
# Function to calculate position suitability percentage
def calculate_percentage(row, cols_1, cols_05, max_values_1, max_values_05):
    sum_1 = row[cols_1].sum() # Tier 1 (Multiplier 1.0)
    sum_05 = row[cols_05].sum() * 0.5  # Tier 6 (Multiplier 0.5)
    return (sum_1 + sum_05) / (max_values_1 + max_values_05) * 100

# Function to calculate maximum column values (20 as maximum skill)
def calculate_max_values(column_list_1, column_list_05):
    max_values_1 = 20 * len(column_list_1) # Tier 1 (Multiplier 1.0)
    max_values_05 = 20 * 0.5 * len(column_list_05) # Tier 6 (Multiplier 0.5)
    return max_values_1, max_values_05

# Defining which columns are taken into account to calculate specific position 
# # Goalkeepers

goalkeeper_d_columns_1 = [4, 13, 15, 16, 28, 39, 44, 47, 48]  # Tier 1 (1.0 Multiplier)
goalkeeper_d_columns_05 = [5, 14, 24, 45]  # # Tier 6 (0.5 Multiplier)

goalkeeper_libero_d_columns_1 = [13, 14, 16, 24, 28, 39, 44, 48]  # Tier 1 (1.0 Multiplier)
goalkeeper_libero_d_columns_05 = [4, 5, 15, 19, 21, 23, 25, 26, 42, 45, 47]  # # Tier 6 (0.5 Multiplier)

goalkeeper_libero_s_columns_1 = [13, 14, 16, 19, 24, 28, 39, 42, 44, 48]  # Tier 1 (1.0 Multiplier)
goalkeeper_libero_s_columns_05 = [4, 5, 15, 21, 23, 25, 26, 45, 47]  # # Tier 6 (0.5 Multiplier)

goalkeeper_libero_a_columns_1 = [13, 14, 16, 19, 24, 28, 39, 42, 44, 48]  # Tier 1 (1.0 Multiplier)
goalkeeper_libero_a_columns_05 = [4, 5, 10, 15, 21, 23, 25, 26, 45, 47]  # # Tier 6 (0.5 Multiplier)

# # Central Defenders

libero_d_columns_1 = [5, 12, 17, 18, 19, 21, 25, 33, 34, 38, 39, 41]  # Tier 1 (1.0 Multiplier)
libero_d_columns_05 = [16, 24, 37, 40, 46]  # # Tier 6 (0.5 Multiplier)

libero_s_columns_1 = [5, 12, 17, 18, 19, 21, 25, 33, 34, 38, 39, 41]  # Tier 1 (1.0 Multiplier)
libero_s_columns_05 = [9, 16, 23, 24, 37, 40, 46]  # # Tier 6 (0.5 Multiplier)

tcd_d_columns_1 = [12, 17, 18, 33, 34, 39]  # Tier 1 (1.0 Multiplier)
tcd_d_columns_05 = [2, 16, 24, 37, 40]  # # Tier 6 (0.5 Multiplier)

tcd_s_columns_1 = [2, 12, 18, 33, 34, 39, 40]  # Tier 1 (1.0 Multiplier)
tcd_s_columns_05 = [16, 17, 24]  # # Tier 6 (0.5 Multiplier)

tcd_c_columns_1 = [16, 17, 18, 24, 37, 39]  # Tier 1 (1.0 Multiplier)
tcd_c_columns_05 = [12, 33, 34, 40]  # # Tier 6 (0.5 Multiplier)

cd_d_columns_1 = [12, 17, 18, 33, 34, 39]  # Tier 1 (1.0 Multiplier)
cd_d_columns_05 = [2, 5, 16, 19, 24, 37, 40]  # # Tier 6 (0.5 Multiplier)

cd_s_columns_1 = [2, 5, 12, 18, 33, 34, 39, 40]  # Tier 1 (1.0 Multiplier)
cd_s_columns_05 = [16, 17, 19, 24]  # # Tier 6 (0.5 Multiplier)

cd_c_columns_1 = [16, 17, 18, 24, 37, 39]  # Tier 1 (1.0 Multiplier)
cd_c_columns_05 = [12, 19, 33, 34, 40]  # # Tier 6 (0.5 Multiplier)

bpd_d_columns_1 = [12, 17, 18, 19, 21, 33, 34, 39]  # Tier 1 (1.0 Multiplier)
bpd_d_columns_05 = [2, 5, 16, 23, 24, 25, 37, 38, 40]  # # Tier 6 (0.5 Multiplier)

bpd_s_columns_1 = [2, 5, 12, 18, 19, 21, 33, 34, 39, 40]  # Tier 1 (1.0 Multiplier)
bpd_s_columns_05 = [16, 17, 23, 24, 25, 38]  # # Tier 6 (0.5 Multiplier)

bpd_c_columns_1 = [5, 16, 17, 18, 19, 21, 24, 37, 39]  # Tier 1 (1.0 Multiplier)
bpd_c_columns_05 = [12, 23, 25, 33, 34, 38, 40]  # # Tier 6 (0.5 Multiplier)

wcb_d_columns_1 = [12, 17, 18, 33, 34, 39]  # Tier 1 (1.0 Multiplier)
wcb_d_columns_05 = [2, 5, 9, 16, 19, 21, 22, 24, 25, 37, 38, 40, 48]  # # Tier 6 (0.5 Multiplier)

wcb_s_columns_1 = [9, 12, 17, 18, 33, 34, 37, 39]  # Tier 1 (1.0 Multiplier)
wcb_s_columns_05 = [2, 5, 8, 11, 16, 19, 21, 22, 24, 25, 38, 40, 46, 48]  # # Tier 6 (0.5 Multiplier)

wcb_a_columns_1 = [8, 9, 11, 12, 17, 18, 33, 34, 37, 46]  # Tier 1 (1.0 Multiplier)
wcb_a_columns_05 = [2, 5, 16, 19, 21, 22, 24, 25, 38, 39, 40, 48]  # # Tier 6 (0.5 Multiplier)

# # Wide Defenders

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

# # Midfielders

bwm_d_columns_1 = [2, 18, 22, 26, 41, 46]
bwm_d_columns_05 = [16, 17, 33, 37, 39, 40, 48]

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

am_s_columns_1 = [3, 5, 11, 21, 24, 25, 36, 38]
am_s_columns_05  = [9, 19, 23, 48]

am_a_columns_1 = [3, 5, 9, 11, 21, 24, 25, 36, 38]
am_a_columns_05  = [19, 23, 43, 48]

ss_a_columns_1 = [9, 11, 19, 24, 25, 26, 43]
ss_a_columns_05  = [5, 16, 21, 22, 29, 37, 38, 46, 48]

tre_a_columns_1 = [3, 5, 9, 11, 19, 21, 23, 25, 26, 38]
tre_a_columns_05  = [24, 29, 43, 48]

eng_s_columns_1 = [5, 19, 21, 23, 25, 38]
eng_s_columns_05  = [3, 9, 11, 24, 41, 48]

# # Wide Midfielders

iw_s_columns_1 = [8, 9, 21, 26, 38, 48]
iw_s_columns_05  = [5, 11, 19, 22, 23, 25, 29, 36, 37, 46]

iw_a_columns_1 = [8, 9, 21, 26, 38]
iw_a_columns_05  = [3, 5, 11, 19, 22, 23, 24, 25, 29, 36, 37]

wp_s_columns_1 = [5, 19, 21, 23, 25, 38, 41]
wp_s_columns_05  = [9, 11, 48]

wp_a_columns_1 = [5, 19, 21, 23, 25, 38, 41]
wp_a_columns_05  = [3, 9, 11, 24, 26, 48]

win_s_columns_1 = [8, 26, 38, 48]
win_s_columns_05  = [11, 21, 22, 25, 37, 46]

win_a_columns_1 = [8, 26, 38, 48]
win_a_columns_05  = [3, 11, 21, 22, 24, 25, 37, 46]

dwin_d_columns_1 = [11, 22, 24, 38, 39, 41, 46]
dwin_d_columns_05  = [2, 5, 8, 9, 16, 17, 18, 25, 26]

dwin_s_columns_1 = [8, 11, 22, 38, 41, 46]
dwin_s_columns_05  = [2, 5, 9, 16, 17, 18, 21, 24, 25, 26, 39]

wm_d_columns_1 = [5, 16, 18, 21, 22, 39, 41]
wm_d_columns_05  = [8, 17, 19, 24, 25, 38, 46]

wm_s_columns_1 = [5, 18, 21, 22, 41, 46]
wm_s_columns_05  = [8, 11, 16, 19, 23, 24, 25, 38, 46]

wm_a_columns_1 = [5, 8, 21, 22, 25, 41, 46]
wm_a_columns_05  = [11, 18, 19, 23, 24, 38]

if_s_columns_1 = [9, 11, 25, 26, 38, 43, 48]
if_s_columns_05  = [3, 19, 21, 22, 23, 24, 27, 29, 36, 37, 46]

if_a_columns_1 = [9, 11, 25, 26, 38, 43, 48]
if_a_columns_05  = [3, 19, 21, 22, 24, 27, 29, 36, 37, 46]

rmd_a_columns_1 = [5, 11, 16, 19, 24, 29, 43]
rmd_a_columns_05  = [22, 25, 26, 38, 46]

wtm_s_columns_1 = [12, 33, 34, 40, 41]
wtm_s_columns_05  = [8, 11, 22, 24, 25, 29, 46]

wtm_a_columns_1 = [11, 12, 33, 34, 40]
wtm_a_columns_05  = [8, 22, 24, 25, 29, 41, 43, 46]

# # Forwards

pf_d_columns_1 = [2, 5, 22, 24, 26, 37, 40, 41, 46]
pf_d_columns_05  = [16, 19, 25, 29, 33, 48]

pf_s_columns_1 = [2, 5, 22, 24, 26, 37, 40, 41, 46]
pf_s_columns_05  = [11, 16, 19, 21, 25, 29, 33, 48]

pf_a_columns_1 = [2, 11, 22, 24, 26, 37, 40, 41, 46]
pf_a_columns_05  = [5, 16, 19, 21, 25, 29, 33, 48]

dlf_s_columns_1 = [5, 11, 19, 21, 25, 38, 41]
dlf_s_columns_05  = [3, 23, 24, 29, 33, 43]

dlf_a_columns_1 = [5, 11, 19, 21, 25, 38, 41]
dlf_a_columns_05  = [3, 9, 23, 24, 29, 33, 43]

tm_s_columns_1 = [12, 29, 33, 34, 40, 41]
tm_s_columns_05  = [2, 5, 11, 19, 24, 25, 43]

tm_a_columns_1 = [11, 12, 19, 29, 33, 34, 40, 43]
tm_a_columns_05  = [2, 5, 25, 41]

af_a_columns_1 = [9, 11, 19, 25, 26, 38, 43]
af_a_columns_05  = [5, 21, 22, 24, 37, 46, 48]

poa_s_columns_1 = [11, 19, 24, 43]
poa_s_columns_05  = [5, 12, 25, 26, 38]

f9_s_columns_1 = [5, 9, 11, 19, 21, 23, 25, 26, 38, 48]
f9_s_columns_05  = [3, 24, 29, 41, 43]

cf_s_columns_1 = [5, 9, 11, 12, 19, 21, 23, 24, 25, 26, 33, 36, 38, 48]
cf_s_columns_05  = [22, 29, 34, 37, 41, 43, 46]

cf_a_columns_1 = [9, 11, 12, 19, 24, 25, 26, 33, 38, 48]
cf_a_columns_05  = [5, 21, 22, 23, 29, 34, 36, 37, 41, 46]


# Calculating maximum possible value for each column using function

# # Goalkeepers

max_values_goalkeeper_d_1, max_values_goalkeeper_d_05 = calculate_max_values(goalkeeper_d_columns_1, goalkeeper_d_columns_05)
max_values_goalkeeper_libero_d_1, max_values_goalkeeper_libero_d_05 = calculate_max_values(goalkeeper_libero_d_columns_1, goalkeeper_libero_d_columns_05)
max_values_goalkeeper_libero_s_1, max_values_goalkeeper_libero_s_05 = calculate_max_values(goalkeeper_libero_s_columns_1, goalkeeper_libero_s_columns_05)
max_values_goalkeeper_libero_a_1, max_values_goalkeeper_libero_a_05 = calculate_max_values(goalkeeper_libero_a_columns_1, goalkeeper_libero_a_columns_05)

# # Central Defenders

max_values_libero_d_1, max_values_libero_d_05 = calculate_max_values(libero_d_columns_1, libero_d_columns_05)
max_values_libero_s_1, max_values_libero_s_05 = calculate_max_values(libero_s_columns_1, libero_s_columns_05)

max_values_tcd_d_1, max_values_tcd_d_05 = calculate_max_values(tcd_d_columns_1, tcd_d_columns_05)
max_values_tcd_s_1, max_values_tcd_s_05 = calculate_max_values(tcd_s_columns_1, tcd_s_columns_05)
max_values_tcd_c_1, max_values_tcd_c_05 = calculate_max_values(tcd_c_columns_1, tcd_c_columns_05)

max_values_cd_d_1, max_values_cd_d_05 = calculate_max_values(cd_d_columns_1, cd_d_columns_05)
max_values_cd_s_1, max_values_cd_s_05 = calculate_max_values(cd_s_columns_1, cd_s_columns_05)
max_values_cd_c_1, max_values_cd_c_05 = calculate_max_values(cd_c_columns_1, cd_c_columns_05)

max_values_bpd_d_1, max_values_bpd_d_05 = calculate_max_values(bpd_d_columns_1, bpd_d_columns_05)
max_values_bpd_s_1, max_values_bpd_s_05 = calculate_max_values(bpd_s_columns_1, bpd_s_columns_05)
max_values_bpd_c_1, max_values_bpd_c_05 = calculate_max_values(bpd_c_columns_1, bpd_c_columns_05)

max_values_wcb_d_1, max_values_wcb_d_05 = calculate_max_values(wcb_d_columns_1, wcb_d_columns_05)
max_values_wcb_s_1, max_values_wcb_s_05 = calculate_max_values(wcb_s_columns_1, wcb_s_columns_05)
max_values_wcb_a_1, max_values_wcb_a_05 = calculate_max_values(wcb_a_columns_1, wcb_a_columns_05)

# # Wide Defenders

max_values_fb_d_1, max_values_fb_d_05 = calculate_max_values(fb_d_columns_1, fb_d_columns_05)
max_values_fb_s_1, max_values_fb_s_05 = calculate_max_values(fb_s_columns_1, fb_s_columns_05)
max_values_fb_a_1, max_values_fb_a_05 = calculate_max_values(fb_a_columns_1, fb_a_columns_05)

max_values_wb_d_1, max_values_wb_d_05 = calculate_max_values(wb_d_columns_1, wb_d_columns_05)
max_values_wb_s_1, max_values_wb_s_05 = calculate_max_values(wb_s_columns_1, wb_s_columns_05)
max_values_wb_a_1, max_values_wb_a_05 = calculate_max_values(wb_a_columns_1, wb_a_columns_05)

max_values_n_n_fb_1, max_values_n_n_fb_05 = calculate_max_values(n_n_fb_columns_1, n_n_fb_columns_05)

max_values_cwb_s_1, max_values_cwb_s_05 = calculate_max_values(cwb_s_columns_1, cwb_s_columns_05)
max_values_cwb_a_1, max_values_cwb_a_05 = calculate_max_values(cwb_a_columns_1, cwb_a_columns_05)

max_values_iwb_d_1, max_values_iwb_d_05 = calculate_max_values(iwb_d_columns_1, iwb_d_columns_05)
max_values_iwb_s_1, max_values_iwb_s_05 = calculate_max_values(iwb_s_columns_1, iwb_s_columns_05)
max_values_iwb_a_1, max_values_iwb_a_05 = calculate_max_values(iwb_a_columns_1, iwb_a_columns_05)

max_values_ifb_d_1, max_values_ifb_d_05 = calculate_max_values(ifb_d_columns_1, ifb_d_columns_05)

# # Midfielders

max_values_bwm_d_1, max_values_bwm_d_05 = calculate_max_values(bwm_d_columns_1, bwm_d_columns_05)
max_values_bwm_s_1, max_values_bwm_s_05 = calculate_max_values(bwm_s_columns_1, bwm_s_columns_05)

max_values_am_d_1, max_values_am_d_05 = calculate_max_values(am_d_columns_1, am_d_columns_05)

max_values_dm_d_1, max_values_dm_d_05 = calculate_max_values(dm_d_columns_1, dm_d_columns_05)
max_values_dm_s_1, max_values_dm_s_05 = calculate_max_values(dm_s_columns_1, dm_s_columns_05)

max_values_hb_d_1, max_values_hb_d_05 = calculate_max_values(hb_d_columns_1, hb_d_columns_05)

max_values_dlp_d_1, max_values_dlp_d_05 = calculate_max_values(dlp_d_columns_1, dlp_d_columns_05)
max_values_dlp_s_1, max_values_dlp_s_05 = calculate_max_values(dlp_s_columns_1, dlp_s_columns_05)

max_values_sv_s_1, max_values_sv_s_05 = calculate_max_values(sv_s_columns_1, sv_s_columns_05)
max_values_sv_a_1, max_values_sv_a_05 = calculate_max_values(sv_a_columns_1, sv_a_columns_05)

max_values_rp_s_1, max_values_rp_s_05 = calculate_max_values(rp_s_columns_1, rp_s_columns_05)

max_values_reg_s_1, max_values_reg_s_05 = calculate_max_values(reg_s_columns_1, reg_s_columns_05)

max_values_cm_d_1, max_values_cm_d_05 = calculate_max_values(cm_d_columns_1, cm_d_columns_05)
max_values_cm_s_1, max_values_cm_s_05 = calculate_max_values(cm_s_columns_1, cm_s_columns_05)
max_values_cm_a_1, max_values_cm_a_05 = calculate_max_values(cm_a_columns_1, cm_a_columns_05)

max_values_car_s_1, max_values_car_s_05 = calculate_max_values(car_s_columns_1, car_s_columns_05)

max_values_b2b_s_1, max_values_b2b_s_05 = calculate_max_values(b2b_s_columns_1, b2b_s_columns_05)

max_values_mez_s_1, max_values_mez_s_05 = calculate_max_values(mez_s_columns_1, mez_s_columns_05)
max_values_mez_a_1, max_values_mez_a_05 = calculate_max_values(mez_a_columns_1, mez_a_columns_05)

max_values_ap_s_1, max_values_ap_s_05 = calculate_max_values(ap_s_columns_1, ap_s_columns_05)
max_values_ap_a_1, max_values_ap_a_05 = calculate_max_values(ap_a_columns_1, ap_a_columns_05)

# # Wide Midfielders

max_values_am_s_1, max_values_am_s_05 = calculate_max_values(am_s_columns_1, am_s_columns_05)
max_values_am_a_1, max_values_am_a_05 = calculate_max_values(am_a_columns_1, am_a_columns_05)

max_values_ss_a_1, max_values_ss_a_05 = calculate_max_values(ss_a_columns_1, ss_a_columns_05)

max_values_tre_a_1, max_values_tre_a_05 = calculate_max_values(tre_a_columns_1, tre_a_columns_05)

max_values_eng_s_1, max_values_eng_s_05 = calculate_max_values(eng_s_columns_1, eng_s_columns_05)

max_values_iw_s_1, max_values_iw_s_05 = calculate_max_values(iw_s_columns_1, iw_s_columns_05)
max_values_iw_a_1, max_values_iw_a_05 = calculate_max_values(iw_a_columns_1, iw_a_columns_05)

max_values_wp_s_1, max_values_wp_s_05 = calculate_max_values(wp_s_columns_1, wp_s_columns_05)
max_values_wp_a_1, max_values_wp_a_05 = calculate_max_values(wp_a_columns_1, wp_a_columns_05)

max_values_win_s_1, max_values_win_s_05 = calculate_max_values(win_s_columns_1, win_s_columns_05)
max_values_win_a_1, max_values_win_a_05 = calculate_max_values(win_a_columns_1, win_a_columns_05)

max_values_dwin_d_1, max_values_dwin_d_05 = calculate_max_values(dwin_d_columns_1, dwin_d_columns_05)
max_values_dwin_s_1, max_values_dwin_s_05 = calculate_max_values(dwin_s_columns_1, dwin_s_columns_05)

max_values_wm_d_1, max_values_wm_d_05 = calculate_max_values(wm_d_columns_1, wm_d_columns_05)
max_values_wm_s_1, max_values_wm_s_05 = calculate_max_values(wm_s_columns_1, wm_s_columns_05)
max_values_wm_a_1, max_values_wm_a_05 = calculate_max_values(wm_a_columns_1, wm_a_columns_05)

max_values_if_s_1, max_values_if_s_05 = calculate_max_values(if_s_columns_1, if_s_columns_05)
max_values_if_a_1, max_values_if_a_05 = calculate_max_values(if_a_columns_1, if_a_columns_05)

max_values_rmd_a_1, max_values_rmd_a_05 = calculate_max_values(rmd_a_columns_1, rmd_a_columns_05)

max_values_wtm_s_1, max_values_wtm_s_05 = calculate_max_values(wtm_s_columns_1, wtm_s_columns_05)
max_values_wtm_a_1, max_values_wtm_a_05 = calculate_max_values(wtm_a_columns_1, wtm_a_columns_05)

# # Forwards
 
max_values_pf_d_1, max_values_pf_d_05 = calculate_max_values(pf_d_columns_1, pf_d_columns_05)
max_values_pf_s_1, max_values_pf_s_05 = calculate_max_values(pf_s_columns_1, pf_s_columns_05)
max_values_pf_a_1, max_values_pf_a_05 = calculate_max_values(pf_a_columns_1, pf_a_columns_05)

max_values_dlf_s_1, max_values_dlf_s_05 = calculate_max_values(dlf_s_columns_1, dlf_s_columns_05)
max_values_dlf_a_1, max_values_dlf_a_05 = calculate_max_values(dlf_a_columns_1, dlf_a_columns_05)

max_values_tm_s_1, max_values_tm_s_05 = calculate_max_values(tm_s_columns_1, tm_s_columns_05)
max_values_tm_a_1, max_values_tm_a_05 = calculate_max_values(tm_a_columns_1, tm_a_columns_05)

max_values_af_a_1, max_values_af_a_05 = calculate_max_values(af_a_columns_1, af_a_columns_05)

max_values_poa_s_1, max_values_poa_s_05 = calculate_max_values(poa_s_columns_1, poa_s_columns_05)

max_values_f9_s_1, max_values_f9_s_05 = calculate_max_values(f9_s_columns_1, f9_s_columns_05)

max_values_cf_s_1, max_values_cf_s_05 = calculate_max_values(cf_s_columns_1, cf_s_columns_05)
max_values_cf_a_1, max_values_cf_a_05 = calculate_max_values(cf_a_columns_1, cf_a_columns_05)

# Copying first two columns to new DataFrame
new_df = df.iloc[: , [0, 1]].copy() 

new_df['Goalkeeper (D)'] = None
new_df['Goalkeeper-libero (D)'] = None
new_df['Goalkeeper-libero (S)'] = None
new_df['Goalkeeper-libero (A)'] = None
new_df['Libero (D)'] = None
new_df['Libero (S)'] = None
new_df['TCD (D)'] = None
new_df['TCD (S)'] = None
new_df['TCD (C)'] = None
new_df['CD (D)'] = None
new_df['CD (S)'] = None
new_df['CD (C)'] = None
new_df['BPD (D)'] = None
new_df['BPD (S)'] = None
new_df['BPD (C)'] = None
new_df['WCB (D)'] = None
new_df['WCB (S)'] = None
new_df['WCB (A)'] = None
new_df['FB (D)'] = None
new_df['FB (S)']  = None
new_df['FB (A)'] = None
new_df['WB (D)'] = None
new_df['WB (S)'] = None
new_df['WB (A)'] = None
new_df['N_N FB']  = None
new_df['CWB (S)'] = None
new_df['CWB (A)']  = None
new_df['IWB (D)'] = None
new_df['IWB (S)'] = None
new_df['IWB (A)']  = None
new_df['IFB (D)']  = None
new_df['BWM (D)'] = None
new_df['BWM (S)']  = None
new_df['AM (D)'] = None
new_df['DM (D)'] = None
new_df['DM (S)']  = None
new_df['HB (D)'] = None
new_df['DLP (D)'] = None
new_df['DLP (S)'] = None
new_df['SV (S)'] = None
new_df['SV (A)'] = None
new_df['RP (S)']  = None
new_df['REG (S)'] = None
new_df['CM (D)'] = None
new_df['CM (S)']  = None
new_df['CM (A)']  = None
new_df['CAR (S)'] = None
new_df['B2B (S)']  = None
new_df['MEZ (S)'] = None
new_df['MEZ (A)'] = None
new_df['AP (S)'] = None
new_df['AP (A)'] = None
new_df['AM (S)'] = None
new_df['AM (A)'] = None
new_df['SS (A)']  = None
new_df['TRE (A)'] = None
new_df['ENG (S)']  = None
new_df['IW (S)']  = None
new_df['IW (A)']  = None
new_df['WP (S)'] = None
new_df['WP (A)'] = None
new_df['WIN (S)'] = None
new_df['WIN (A)'] = None
new_df['DWIN (D)'] = None
new_df['DWIN (S)']  = None
new_df['WM (D)']  = None
new_df['WM (S)']  = None
new_df['WM (A)']  = None
new_df['IF (S)'] = None
new_df['IF (A)'] = None
new_df['RMD (A)'] = None
new_df['WTM (S)'] = None
new_df['WTM (A)']  = None
new_df['PF (D)'] = None
new_df['PF (S)'] = None
new_df['PF (A)']  = None
new_df['DLF (S)']  = None
new_df['DLF (A)']  = None
new_df['TM (S)']  = None
new_df['TM (A)']  = None
new_df['AF (A)']  = None
new_df['POA (S)'] = None
new_df['F9 (S)']  = None
new_df['CF (S)']  = None
new_df['CF (A)'] = None

for idx, row in df.iterrows():
    if df.iloc[idx, cols_to_check].apply(is_integer).all():

        calculations = {
            'Goalkeeper (D)': (goalkeeper_d_columns_1, goalkeeper_d_columns_05, max_values_goalkeeper_d_1, max_values_goalkeeper_d_05),
            'Goalkeeper-libero (D)': (goalkeeper_libero_d_columns_1, goalkeeper_libero_d_columns_05, max_values_goalkeeper_libero_d_1, max_values_goalkeeper_libero_d_05),
            'Goalkeeper-libero (S)': (goalkeeper_libero_s_columns_1, goalkeeper_libero_s_columns_05, max_values_goalkeeper_libero_s_1, max_values_goalkeeper_libero_s_05),
            'Goalkeeper-libero (A)': (goalkeeper_libero_a_columns_1, goalkeeper_libero_a_columns_05, max_values_goalkeeper_libero_a_1, max_values_goalkeeper_libero_a_05),
            'Libero (D)': (libero_d_columns_1, libero_d_columns_05, max_values_libero_d_1, max_values_libero_d_05),
            'Libero (S)': (libero_s_columns_1, libero_s_columns_05, max_values_libero_s_1, max_values_libero_s_05),
            'TCD (D)': (tcd_d_columns_1, tcd_d_columns_05, max_values_tcd_d_1, max_values_tcd_d_05),
            'TCD (S)': (tcd_s_columns_1, tcd_s_columns_05, max_values_tcd_s_1, max_values_tcd_s_05),
            'TCD (C)': (tcd_c_columns_1, tcd_c_columns_05, max_values_tcd_c_1, max_values_tcd_c_05),
            'CD (D)': (cd_d_columns_1, cd_d_columns_05, max_values_cd_d_1, max_values_cd_d_05),
            'CD (S)': (cd_s_columns_1, cd_s_columns_05, max_values_cd_s_1, max_values_cd_s_05),
            'CD (C)': (cd_c_columns_1, cd_c_columns_05, max_values_cd_c_1, max_values_cd_c_05),
            'BPD (D)': (bpd_d_columns_1, bpd_d_columns_05, max_values_bpd_d_1, max_values_bpd_d_05),
            'BPD (S)': (bpd_s_columns_1, bpd_s_columns_05, max_values_bpd_s_1, max_values_bpd_s_05),
            'BPD (C)': (bpd_c_columns_1, bpd_c_columns_05, max_values_bpd_c_1, max_values_bpd_c_05),
            'WCB (D)': (wcb_d_columns_1, wcb_d_columns_05, max_values_wcb_d_1, max_values_wcb_d_05),
            'WCB (S)': (wcb_s_columns_1, wcb_s_columns_05, max_values_wcb_s_1, max_values_wcb_s_05),
            'WCB (A)': (wcb_a_columns_1, wcb_a_columns_05, max_values_wcb_a_1, max_values_wcb_a_05),
            'FB (D)': (fb_d_columns_1, fb_d_columns_05, max_values_fb_d_1, max_values_fb_d_05),
            'FB (S)': (fb_s_columns_1, fb_s_columns_05, max_values_fb_s_1, max_values_fb_s_05),
            'FB (A)': (fb_a_columns_1, fb_a_columns_05, max_values_fb_a_1, max_values_fb_a_05),
            'WB (D)': (wb_d_columns_1, wb_d_columns_05, max_values_wb_d_1, max_values_wb_d_05),
            'WB (S)': (wb_s_columns_1, wb_s_columns_05, max_values_wb_s_1, max_values_wb_s_05),
            'WB (A)': (wb_a_columns_1, wb_a_columns_05, max_values_wb_a_1, max_values_wb_a_05),
            'N_N FB': (n_n_fb_columns_1, n_n_fb_columns_05, max_values_n_n_fb_1, max_values_n_n_fb_05),
            'CWB (S)': (cwb_s_columns_1, cwb_s_columns_05, max_values_cwb_s_1, max_values_cwb_s_05),
            'CWB (A)': (cwb_a_columns_1, cwb_a_columns_05, max_values_cwb_a_1, max_values_cwb_a_05),
            'IWB (D)': (iwb_d_columns_1, iwb_d_columns_05, max_values_iwb_d_1, max_values_iwb_d_05),
            'IWB (S)': (iwb_s_columns_1, iwb_s_columns_05, max_values_iwb_s_1, max_values_iwb_s_05),
            'IWB (A)': (iwb_a_columns_1, iwb_a_columns_05, max_values_iwb_a_1, max_values_iwb_a_05),
            'IFB (D)': (ifb_d_columns_1, ifb_d_columns_05, max_values_ifb_d_1, max_values_ifb_d_05),
            'BWM (D)': (bwm_d_columns_1, bwm_d_columns_05, max_values_bwm_d_1, max_values_bwm_d_05),
            'BWM (S)': (bwm_s_columns_1, bwm_s_columns_05, max_values_bwm_s_1, max_values_bwm_s_05),
            'AM (D)': (am_d_columns_1, am_d_columns_05, max_values_am_d_1, max_values_am_d_05),
            'DM (D)': (dm_d_columns_1, dm_d_columns_05, max_values_dm_d_1, max_values_dm_d_05),
            'DM (S)': (dm_s_columns_1, dm_s_columns_05, max_values_dm_s_1, max_values_dm_s_05),
            'HB (D)': (hb_d_columns_1, hb_d_columns_05, max_values_hb_d_1, max_values_hb_d_05),
            'DLP (D)': (dlp_d_columns_1, dlp_d_columns_05, max_values_dlp_d_1, max_values_dlp_d_05),
            'DLP (S)': (dlp_s_columns_1, dlp_s_columns_05, max_values_dlp_s_1, max_values_dlp_s_05),
            'SV (S)': (sv_s_columns_1, sv_s_columns_05, max_values_sv_s_1, max_values_sv_s_05),
            'SV (A)': (sv_a_columns_1, sv_a_columns_05, max_values_sv_a_1, max_values_sv_a_05),
            'RP (S)': (rp_s_columns_1, rp_s_columns_05, max_values_rp_s_1, max_values_rp_s_05),
            'CM (D)': (cm_d_columns_1, cm_d_columns_05, max_values_cm_d_1, max_values_cm_d_05),
            'CM (S)': (cm_s_columns_1, cm_s_columns_05, max_values_cm_s_1, max_values_cm_s_05),
            'CM (A)': (cm_a_columns_1, cm_a_columns_05, max_values_cm_a_1, max_values_cm_a_05),
            'CAR (S)': (car_s_columns_1, car_s_columns_05, max_values_car_s_1, max_values_car_s_05),
            'B2B (S)': (b2b_s_columns_1, b2b_s_columns_05, max_values_b2b_s_1, max_values_b2b_s_05),
            'MEZ (S)': (mez_s_columns_1, mez_s_columns_05, max_values_mez_s_1, max_values_mez_s_05),
            'MEZ (A)': (mez_a_columns_1, mez_a_columns_05, max_values_mez_a_1, max_values_mez_a_05),
            'AP (S)': (ap_s_columns_1, ap_s_columns_05, max_values_ap_s_1, max_values_ap_s_05),
            'AP (A)': (ap_a_columns_1, ap_a_columns_05, max_values_ap_a_1, max_values_ap_a_05),
            'AM (S)': (am_s_columns_1, am_s_columns_05, max_values_am_s_1, max_values_am_s_05),
            'AM (A)': (am_a_columns_1, am_a_columns_05, max_values_am_a_1, max_values_am_a_05),
            'SS (A)': (ss_a_columns_1, ss_a_columns_05, max_values_ss_a_1, max_values_ss_a_05),
            'TRE (A)': (tre_a_columns_1, tre_a_columns_05, max_values_tre_a_1, max_values_tre_a_05),
            'ENG (S)': (eng_s_columns_1, eng_s_columns_05, max_values_eng_s_1, max_values_eng_s_05),
            'IW (S)': (iw_s_columns_1, iw_s_columns_05, max_values_iw_s_1, max_values_iw_s_05),
            'IW (A)': (iw_a_columns_1, iw_a_columns_05, max_values_iw_a_1, max_values_iw_a_05),
            'WP (S)': (wp_s_columns_1, wp_s_columns_05, max_values_wp_s_1, max_values_wp_s_05),
            'WP (A)': (wp_a_columns_1, wp_a_columns_05, max_values_wp_a_1, max_values_wp_a_05),
            'WIN (S)': (win_s_columns_1, win_s_columns_05, max_values_win_s_1, max_values_win_s_05),
            'WIN (A)': (win_a_columns_1, win_a_columns_05, max_values_win_a_1, max_values_win_a_05),
            'DWIN (D)': (dwin_d_columns_1, dwin_d_columns_05, max_values_dwin_d_1, max_values_dwin_d_05),
            'DWIN (S)': (dwin_s_columns_1, dwin_s_columns_05, max_values_dwin_s_1, max_values_dwin_s_05),
            'WM (D)': (wm_d_columns_1, wm_d_columns_05, max_values_wm_d_1, max_values_wm_d_05),
            'WM (S)': (wm_s_columns_1, wm_s_columns_05, max_values_wm_s_1, max_values_wm_s_05),
            'WM (A)': (wm_a_columns_1, wm_a_columns_05, max_values_wm_a_1, max_values_wm_a_05),
            'IF (S)': (if_s_columns_1, if_s_columns_05, max_values_if_s_1, max_values_if_s_05),
            'IF (A)': (if_a_columns_1, if_a_columns_05, max_values_if_a_1, max_values_if_a_05),
            'RMD (A)': (rmd_a_columns_1, rmd_a_columns_05, max_values_rmd_a_1, max_values_rmd_a_05),
            'WTM (S)': (wtm_s_columns_1, wtm_s_columns_05, max_values_wtm_s_1, max_values_wtm_s_05),
            'WTM (A)': (wtm_a_columns_1, wtm_a_columns_05, max_values_wtm_a_1, max_values_wtm_a_05),
            'PF (D)': (pf_d_columns_1, pf_d_columns_05, max_values_pf_d_1, max_values_pf_d_05),
            'PF (S)': (pf_s_columns_1, pf_s_columns_05, max_values_pf_s_1, max_values_pf_s_05),
            'PF (A)': (pf_a_columns_1, pf_a_columns_05, max_values_pf_a_1, max_values_pf_a_05),
            'DLF (S)': (dlf_s_columns_1, dlf_s_columns_05, max_values_dlf_s_1, max_values_dlf_s_05),
            'DLF (A)': (dlf_a_columns_1, dlf_a_columns_05, max_values_dlf_a_1, max_values_dlf_a_05),
            'TM (S)': (tm_s_columns_1, tm_s_columns_05, max_values_tm_s_1, max_values_tm_s_05),
            'TM (A)': (tm_a_columns_1, tm_a_columns_05, max_values_tm_a_1, max_values_tm_a_05),
            'AF (A)': (af_a_columns_1, af_a_columns_05, max_values_af_a_1, max_values_af_a_05),
            'POA (S)': (poa_s_columns_1, poa_s_columns_05, max_values_poa_s_1, max_values_poa_s_05),
            'F9 (S)': (f9_s_columns_1, f9_s_columns_05, max_values_f9_s_1, max_values_f9_s_05),
            'CF (S)': (cf_s_columns_1, cf_s_columns_05, max_values_cf_s_1, max_values_cf_s_05),
            'CF (A)': (cf_a_columns_1, cf_a_columns_05, max_values_cf_a_1, max_values_cf_a_05),
        }

        # Calculate percentages for all keys in calculations dictionary
        for key, (cols_1, cols_05, max_values_1, max_values_05) in calculations.items():
            new_df.at[idx, key] = calculate_percentage(row, cols_1, cols_05, max_values_1, max_values_05)

# Printing new DataFrame with calculations.
#print(new_df)

# GUI to select save location
## To consider changing PySimpleGUI to other open source GUI as it's licensed now.

save_window = [
    [sg.Text("Please select a location to save the file:")],
    [sg.Input(), sg.FileSaveAs(file_types=(("Excel Files", "*.xlsx"),))],
    [sg.OK(), sg.Cancel()]
]

window = sg.Window("Save File", save_window)

event, values = window.read()
window.close()

if event == 'OK' and values[0]:
    excel_file_path = values[0]
    
    # Ensure the file has the correct extension
    if not excel_file_path.endswith(".xlsx"):
        excel_file_path += ".xlsx"
    
    # Step 4: Save the dataframe to the selected Excel file
    new_df.to_excel(excel_file_path, index=False)
    sg.popup(f"File saved successfully at {excel_file_path}")
else:
    print("Save action canceled or no location selected.")