import pandas as pd
import PySimpleGUI as sg

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
dfs = pd.read_html(html_file_path, encoding='utf-8')

# Reading first table in dataframe (just in case)
df = dfs[0] 

# Printing DataFrame (for testing)
# print(df)

# Defining which columns are taken into account to calculate specific position 

# Goalkeepers

goalkeeper_d_columns_1 = [4, 13, 15, 16, 28, 39, 44, 47, 48]  # Tier 1 (1.0 Multiplier)
goalkeeper_d_columns_05 = [5, 14, 24, 45]  # # Tier 6 (0.5 Multiplier)

goalkeeper_libero_d_columns_1 = [13, 14, 16, 24, 28, 39, 44, 48]  # Tier 1 (1.0 Multiplier)
goalkeeper_libero_d_columns_05 = [4, 5, 15, 19, 21, 23, 25, 26, 42, 45, 47]  # # Tier 6 (0.5 Multiplier)

goalkeeper_libero_s_columns_1 = [13, 14, 16, 19, 24, 28, 39, 42, 44, 48]  # Tier 1 (1.0 Multiplier)
goalkeeper_libero_s_columns_05 = [4, 5, 15, 21, 23, 25, 26, 45, 47]  # # Tier 6 (0.5 Multiplier)

goalkeeper_libero_a_columns_1 = [13, 14, 16, 19, 24, 28, 39, 42, 44, 48]  # Tier 1 (1.0 Multiplier)
goalkeeper_libero_a_columns_05 = [4, 5, 10, 15, 21, 23, 25, 26, 45, 47]  # # Tier 6 (0.5 Multiplier)

# Central Defenders

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

# Wide Midfielders

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

# Forwards

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


# Calculating maximum possible value for each column

# Goalkeepers
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

max_values_bwm_d_1 = 20 * len(bwm_d_columns_1)
max_values_bwm_d_05 = 20 * 0.5 * len(bwm_d_columns_05)

max_values_bwm_s_1 = 20 * len(bwm_s_columns_1)
max_values_bwm_s_05 = 20 * 0.5 * len(bwm_s_columns_05)

max_values_am_d_1 = 20 * len(am_d_columns_1)
max_values_am_d_05 = 20 * 0.5 * len(am_d_columns_05)

max_values_dm_d_1 = 20 * len(dm_d_columns_1)
max_values_dm_d_05 = 20 * 0.5 * len(dm_d_columns_05)

max_values_dm_s_1 = 20 * len(dm_s_columns_1)
max_values_dm_s_05 = 20 * 0.5 * len(dm_s_columns_05)

max_values_hb_d_1 = 20 * len(hb_d_columns_1)
max_values_hb_d_05 = 20 * 0.5 * len(hb_d_columns_05)

max_values_dlp_d_1 = 20 * len(dlp_d_columns_1)
max_values_dlp_d_05 = 20 * 0.5 * len(dlp_d_columns_05)

max_values_dlp_s_1 = 20 * len(dlp_s_columns_1)
max_values_dlp_s_05 = 20 * 0.5 * len(dlp_s_columns_05)

max_values_sv_s_1 = 20 * len(sv_s_columns_1)
max_values_sv_s_05 = 20 * 0.5 * len(sv_s_columns_05)

max_values_sv_a_1 = 20 * len(sv_a_columns_1)
max_values_sv_a_05 = 20 * 0.5 * len(sv_a_columns_05)

max_values_rp_s_1 = 20 * len(rp_s_columns_1)
max_values_rp_s_05 = 20 * 0.5 * len(rp_s_columns_05)

max_values_reg_s_1 = 20 * len(reg_s_columns_1)
max_values_reg_s_05 = 20 * 0.5 * len(reg_s_columns_05)

max_values_cm_d_1 = 20 * len(cm_d_columns_1)
max_values_cm_d_05 = 20 * 0.5 * len(cm_d_columns_05)

max_values_cm_s_1 = 20 * len(cm_s_columns_1)
max_values_cm_s_05 = 20 * 0.5 * len(cm_s_columns_05)

max_values_cm_a_1 = 20 * len(cm_a_columns_1)
max_values_cm_a_05 = 20 * 0.5 * len(cm_a_columns_05)

max_values_car_s_1 = 20 * len(car_s_columns_1)
max_values_car_s_05 = 20 * 0.5 * len(car_s_columns_05)

max_values_b2b_s_1 = 20 * len(b2b_s_columns_1)
max_values_b2b_s_05 = 20 * 0.5 * len(b2b_s_columns_05)

max_values_mez_s_1 = 20 * len(mez_s_columns_1)
max_values_mez_s_05 = 20 * 0.5 * len(mez_s_columns_05)

max_values_mez_a_1 = 20 * len(mez_a_columns_1)
max_values_mez_a_05 = 20 * 0.5 * len(mez_a_columns_05)

max_values_ap_s_1 = 20 * len(ap_s_columns_1)
max_values_ap_s_05 = 20 * 0.5 * len(ap_s_columns_05)

max_values_ap_a_1 = 20 * len(ap_a_columns_1)
max_values_ap_a_05 = 20 * 0.5 * len(ap_a_columns_05)

# Wide Midfielders

max_values_am_s_1 = 20 * len(am_s_columns_1)
max_values_am_s_05 = 20 * 0.5 * len(am_s_columns_05)
 
max_values_am_a_1 = 20 * len(am_a_columns_1)
max_values_am_a_05 = 20 * 0.5 * len(am_a_columns_05)
 
max_values_ss_a_1 = 20 * len(ss_a_columns_1)
max_values_ss_a_05 = 20 * 0.5 * len(ss_a_columns_05)
 
max_values_tre_a_1 = 20 * len(tre_a_columns_1)
max_values_tre_a_05 = 20 * 0.5 * len(tre_a_columns_05)
 
max_values_eng_s_1 = 20 * len(eng_s_columns_1)
max_values_eng_s_05 = 20 * 0.5 * len(eng_s_columns_05)
 
max_values_iw_s_1 = 20 * len(iw_s_columns_1)
max_values_iw_s_05 = 20 * 0.5 * len(iw_s_columns_05)
 
max_values_iw_a_1 = 20 * len(iw_a_columns_1)
max_values_iw_a_05 = 20 * 0.5 * len(iw_a_columns_05)
 
max_values_wp_s_1 = 20 * len(wp_s_columns_1)
max_values_wp_s_05 = 20 * 0.5 * len(wp_s_columns_05)
 
max_values_wp_a_1 = 20 * len(wp_a_columns_1)
max_values_wp_a_05 = 20 * 0.5 * len(wp_a_columns_05)
 
max_values_win_s_1 = 20 * len(win_s_columns_1)
max_values_win_s_05 = 20 * 0.5 * len(win_s_columns_05)
 
max_values_win_a_1 = 20 * len(win_a_columns_1)
max_values_win_a_05 = 20 * 0.5 * len(win_a_columns_05)
 
max_values_dwin_d_1 = 20 * len(dwin_d_columns_1)
max_values_dwin_d_05 = 20 * 0.5 * len(dwin_d_columns_05)
 
max_values_dwin_s_1 = 20 * len(dwin_s_columns_1)
max_values_dwin_s_05 = 20 * 0.5 * len(dwin_s_columns_05)
 
max_values_wm_d_1 = 20 * len(wm_d_columns_1)
max_values_wm_d_05 = 20 * 0.5 * len(wm_d_columns_05)
 
max_values_wm_s_1 = 20 * len(wm_s_columns_1)
max_values_wm_s_05 = 20 * 0.5 * len(wm_s_columns_05)
 
max_values_wm_a_1 = 20 * len(wm_a_columns_1)
max_values_wm_a_05 = 20 * 0.5 * len(wm_a_columns_05)
 
max_values_if_s_1 = 20 * len(if_s_columns_1)
max_values_if_s_05 = 20 * 0.5 * len(if_s_columns_05)
 
max_values_if_a_1 = 20 * len(if_a_columns_1)
max_values_if_a_05 = 20 * 0.5 * len(if_a_columns_05)
 
max_values_rmd_a_1 = 20 * len(rmd_a_columns_1)
max_values_rmd_a_05 = 20 * 0.5 * len(rmd_a_columns_05)
 
max_values_wtm_s_1 = 20 * len(wtm_s_columns_1)
max_values_wtm_s_05 = 20 * 0.5 * len(wtm_s_columns_05)
 
max_values_wtm_a_1 = 20 * len(wtm_a_columns_1)
max_values_wtm_a_05 = 20 * 0.5 * len(wtm_a_columns_05)

# Forwards
 
max_values_pf_d_1 = 20 * len(pf_d_columns_1)
max_values_pf_d_05 = 20 * 0.5 * len(pf_d_columns_05)
 
max_values_pf_s_1 = 20 * len(pf_s_columns_1)
max_values_pf_s_05 = 20 * 0.5 * len(pf_s_columns_05)
 
max_values_pf_a_1 = 20 * len(pf_a_columns_1)
max_values_pf_a_05 = 20 * 0.5 * len(pf_a_columns_05)
 
max_values_dlf_s_1 = 20 * len(dlf_s_columns_1)
max_values_dlf_s_05 = 20 * 0.5 * len(dlf_s_columns_05)
 
max_values_dlf_a_1 = 20 * len(dlf_a_columns_1)
max_values_dlf_a_05 = 20 * 0.5 * len(dlf_a_columns_05)
 
max_values_tm_s_1 = 20 * len(tm_s_columns_1)
max_values_tm_s_05 = 20 * 0.5 * len(tm_s_columns_05)
 
max_values_tm_a_1 = 20 * len(tm_a_columns_1)
max_values_tm_a_05 = 20 * 0.5 * len(tm_a_columns_05)
 
max_values_af_a_1 = 20 * len(af_a_columns_1)
max_values_af_a_05 = 20 * 0.5 * len(af_a_columns_05)
 
max_values_poa_s_1 = 20 * len(poa_s_columns_1)
max_values_poa_s_05 = 20 * 0.5 * len(poa_s_columns_05)
 
max_values_f9_s_1 = 20 * len(f9_s_columns_1)
max_values_f9_s_05 = 20 * 0.5 * len(f9_s_columns_05)
 
max_values_cf_s_1 = 20 * len(cf_s_columns_1)
max_values_cf_s_05 = 20 * 0.5 * len(cf_s_columns_05)
 
max_values_cf_a_1 = 20 * len(cf_a_columns_1)
max_values_cf_a_05 = 20 * 0.5 * len(cf_a_columns_05)


# Copying first two columns to new DataFrame
new_df = df.iloc[: , [0, 1]].copy() 


# Calculating "Goalkeeper (D)" percentage value
goalkeeper_d_1_sum = df.iloc[:, goalkeeper_d_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
goalkeeper_d_05_sum = df.iloc[:, goalkeeper_d_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['Goalkeeper (D)'] = (goalkeeper_d_1_sum + goalkeeper_d_05_sum) / (max_values_goalkeeper_d_1 + max_values_goalkeeper_d_05) * 100  # Percentage calculation


# Calculating "Goalkeeper-libero (D)" percentage value
goalkeeper_libero_d_1_sum = df.iloc[:, goalkeeper_libero_d_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
goalkeeper_libero_d_05_sum = df.iloc[:, goalkeeper_libero_d_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['Goalkeeper-libero (D)'] = (goalkeeper_libero_d_1_sum + goalkeeper_libero_d_05_sum) / (max_values_goalkeeper_libero_d_1 + max_values_goalkeeper_libero_d_05) * 100  # Percentage calculation


# Calculating "Goalkeeper-libero (S)" percentage value
goalkeeper_libero_s_1_sum = df.iloc[:, goalkeeper_libero_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
goalkeeper_libero_s_05_sum = df.iloc[:, goalkeeper_libero_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['Goalkeeper-libero (S)'] = (goalkeeper_libero_s_1_sum + goalkeeper_libero_s_05_sum) / (max_values_goalkeeper_libero_s_1 + max_values_goalkeeper_libero_s_05) * 100  # Percentage calculation


# Calculating "Goalkeeper-libero (A)" percentage value
goalkeeper_libero_a_1_sum = df.iloc[:, goalkeeper_libero_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
goalkeeper_libero_a_05_sum = df.iloc[:, goalkeeper_libero_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['Goalkeeper-libero (A)'] = (goalkeeper_libero_a_1_sum + goalkeeper_libero_a_05_sum) / (max_values_goalkeeper_libero_a_1 + max_values_goalkeeper_libero_a_05) * 100  # Percentage calculation

# Calculating "Libero (D)" percentage value
libero_d_1_sum = df.iloc[:, libero_d_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
libero_d_05_sum = df.iloc[:, libero_d_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['Libero (D)'] = (libero_d_1_sum + libero_d_05_sum) / (max_values_libero_d_1 + max_values_libero_d_05) * 100  # Percentage calculation

# Calculating "Libero (S)" percentage value
libero_s_1_sum = df.iloc[:, libero_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
libero_s_05_sum = df.iloc[:, libero_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['Libero (S)'] = (libero_s_1_sum + libero_s_05_sum) / (max_values_libero_s_1 + max_values_libero_s_05) * 100  # Percentage calculation

# Calculating "TCD (D)" percentage value
tcd_d_1_sum = df.iloc[:, tcd_d_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
tcd_d_05_sum = df.iloc[:, tcd_d_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['TCD (D)'] = (tcd_d_1_sum + tcd_d_05_sum) / (max_values_tcd_d_1 + max_values_tcd_d_05) * 100  # Percentage calculation

# Calculating "TCD (S)" percentage value
tcd_s_1_sum = df.iloc[:, tcd_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
tcd_s_05_sum = df.iloc[:, tcd_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['TCD (S)'] = (tcd_s_1_sum + tcd_s_05_sum) / (max_values_tcd_s_1 + max_values_tcd_s_05) * 100  # Percentage calculation

# Calculating "TCD (C)" percentage value
tcd_c_1_sum = df.iloc[:, tcd_c_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
tcd_c_05_sum = df.iloc[:, tcd_c_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['TCD (C)'] = (tcd_c_1_sum + tcd_c_05_sum) / (max_values_tcd_c_1 + max_values_tcd_c_05) * 100  # Percentage calculation

# Calculating "CD (D)" percentage value
cd_d_1_sum = df.iloc[:, cd_d_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
cd_d_05_sum = df.iloc[:, cd_d_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['CD (D)'] = (cd_d_1_sum + cd_d_05_sum) / (max_values_cd_d_1 + max_values_cd_d_05) * 100  # Percentage calculation

# Calculating "CD (S)" percentage value
cd_s_1_sum = df.iloc[:, cd_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
cd_s_05_sum = df.iloc[:, cd_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['CD (S)'] = (cd_s_1_sum + cd_s_05_sum) / (max_values_cd_s_1 + max_values_cd_s_05) * 100  # Percentage calculation

# Calculating "CD (C)" percentage value
cd_c_1_sum = df.iloc[:, cd_c_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
cd_c_05_sum = df.iloc[:, cd_c_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['CD (C)'] = (cd_c_1_sum + cd_c_05_sum) / (max_values_cd_c_1 + max_values_cd_c_05) * 100  # Percentage calculation

# Calculating "BPD (D)" percentage value
bpd_d_1_sum = df.iloc[:, bpd_d_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
bpd_d_05_sum = df.iloc[:, bpd_d_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['BPD (D)'] = (bpd_d_1_sum + bpd_d_05_sum) / (max_values_bpd_d_1 + max_values_bpd_d_05) * 100  # Percentage calculation

# Calculating "BPD (S)" percentage value
bpd_s_1_sum = df.iloc[:, bpd_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
bpd_s_05_sum = df.iloc[:, bpd_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['BPD (S)'] = (bpd_s_1_sum + bpd_s_05_sum) / (max_values_bpd_s_1 + max_values_bpd_s_05) * 100  # Percentage calculation

# Calculating "BPD (C)" percentage value
bpd_c_1_sum = df.iloc[:, bpd_c_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
bpd_c_05_sum = df.iloc[:, bpd_c_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['BPD (C)'] = (bpd_c_1_sum + bpd_c_05_sum) / (max_values_bpd_c_1 + max_values_bpd_c_05) * 100  # Percentage calculation

# Calculating "WCB (D)" percentage value
wcb_d_1_sum = df.iloc[:, wcb_d_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
wcb_d_05_sum = df.iloc[:, wcb_d_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['WCB (D)'] = (wcb_d_1_sum + wcb_d_05_sum) / (max_values_wcb_d_1 + max_values_wcb_d_05) * 100  # Percentage calculation

# Calculating "WCB (S)" percentage value
wcb_s_1_sum = df.iloc[:, wcb_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
wcb_s_05_sum = df.iloc[:, wcb_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['WCB (S)'] = (wcb_s_1_sum + wcb_s_05_sum) / (max_values_wcb_s_1 + max_values_wcb_s_05) * 100  # Percentage calculation

# Calculating "WCB (A)" percentage value
wcb_a_1_sum = df.iloc[:, wcb_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
wcb_a_05_sum = df.iloc[:, wcb_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['WCB (A)'] = (wcb_a_1_sum + wcb_a_05_sum) / (max_values_wcb_a_1 + max_values_wcb_a_05) * 100  # Percentage calculation

# Calculating "FB (D)" percentage value
fb_d_1_sum = df.iloc[:, fb_d_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
fb_d_05_sum = df.iloc[:, fb_d_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['FB (D)'] = (fb_d_1_sum + fb_d_05_sum) / (max_values_fb_d_1 + max_values_fb_d_05) * 100  # Percentage calculation

# Calculating "FB (S)" percentage value
fb_s_1_sum = df.iloc[:, fb_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
fb_s_05_sum = df.iloc[:, fb_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['FB (S)'] = (fb_s_1_sum + fb_s_05_sum) / (max_values_fb_s_1 + max_values_fb_s_05) * 100  # Percentage calculation

# Calculating "FB (A)" percentage value
fb_a_1_sum = df.iloc[:, fb_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
fb_a_05_sum = df.iloc[:, fb_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['FB (A)'] = (fb_a_1_sum + fb_a_05_sum) / (max_values_fb_a_1 + max_values_fb_a_05) * 100  # Percentage calculation

# Calculating "WB (D)" percentage value
wb_d_1_sum = df.iloc[:, wb_d_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
wb_d_05_sum = df.iloc[:, wb_d_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['WB (D)'] = (wb_d_1_sum + wb_d_05_sum) / (max_values_wb_d_1 + max_values_wb_d_05) * 100  # Percentage calculation

# Calculating "WB (S)" percentage value
wb_s_1_sum = df.iloc[:, wb_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
wb_s_05_sum = df.iloc[:, wb_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['WB (S)'] = (wb_s_1_sum + wb_s_05_sum) / (max_values_wb_s_1 + max_values_wb_s_05) * 100  # Percentage calculation

# Calculating "WB (A)" percentage value
wb_a_1_sum = df.iloc[:, wb_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
wb_a_05_sum = df.iloc[:, wb_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['WB (A)'] = (wb_a_1_sum + wb_a_05_sum) / (max_values_wb_a_1 + max_values_wb_a_05) * 100  # Percentage calculation

# Calculating "N-N FB" percentage value
n_n_fb_1_sum = df.iloc[:, n_n_fb_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
n_n_fb_05_sum = df.iloc[:, n_n_fb_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['N_N FB'] = (n_n_fb_1_sum + n_n_fb_05_sum) / (max_values_n_n_fb_1 + max_values_n_n_fb_05) * 100  # Percentage calculation

# Calculating "CWB (S)" percentage value
cwb_s_1_sum = df.iloc[:, cwb_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
cwb_s_05_sum = df.iloc[:, cwb_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['CWB (S)'] = (cwb_s_1_sum + cwb_s_05_sum) / (max_values_cwb_s_1 + max_values_cwb_s_05) * 100  # Percentage calculation

# Calculating "CWB (A)" percentage value
cwb_a_1_sum = df.iloc[:, cwb_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
cwb_a_05_sum = df.iloc[:, cwb_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['CWB (A)'] = (cwb_a_1_sum + cwb_a_05_sum) / (max_values_cwb_a_1 + max_values_cwb_a_05) * 100  # Percentage calculation

# Calculating "IWB (D)" percentage value
iwb_d_1_sum = df.iloc[:, iwb_d_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
iwb_d_05_sum = df.iloc[:, iwb_d_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['IWB (D)'] = (iwb_d_1_sum + iwb_d_05_sum) / (max_values_iwb_d_1 + max_values_iwb_d_05) * 100  # Percentage calculation

# Calculating "IWB (S)" percentage value
iwb_s_1_sum = df.iloc[:, iwb_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
iwb_s_05_sum = df.iloc[:, iwb_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['IWB (S)'] = (iwb_s_1_sum + iwb_s_05_sum) / (max_values_iwb_s_1 + max_values_iwb_s_05) * 100  # Percentage calculation

# Calculating "IWB (A)" percentage value
iwb_a_1_sum = df.iloc[:, iwb_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
iwb_a_05_sum = df.iloc[:, iwb_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['IWB (A)'] = (iwb_a_1_sum + iwb_a_05_sum) / (max_values_iwb_a_1 + max_values_iwb_a_05) * 100  # Percentage calculation

# Calculating "IFB (D)" percentage value
ifb_d_1_sum = df.iloc[:, ifb_d_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
ifb_d_05_sum = df.iloc[:, ifb_d_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['IFB (D)'] = (ifb_d_1_sum + ifb_d_05_sum) / (max_values_ifb_d_1 + max_values_ifb_d_05) * 100  # Percentage calculation

# Calculating "BWM (D)" percentage value
bwm_d_1_sum = df.iloc[:, bwm_d_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
bwm_d_05_sum = df.iloc[:, bwm_d_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['BWM (D)'] = (bwm_d_1_sum + bwm_d_05_sum) / (max_values_bwm_d_1 + max_values_bwm_d_05) * 100  # Percentage calculation

# Calculating "BWM (S)" percentage value
bwm_s_1_sum = df.iloc[:, bwm_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
bwm_s_05_sum = df.iloc[:, bwm_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['BWM (S)'] = (bwm_s_1_sum + bwm_s_05_sum) / (max_values_bwm_s_1 + max_values_bwm_s_05) * 100  # Percentage calculation

# Calculating "AM (D)" percentage value
am_d_1_sum = df.iloc[:, am_d_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
am_d_05_sum = df.iloc[:, am_d_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['AM (D)'] = (am_d_1_sum + am_d_05_sum) / (max_values_am_d_1 + max_values_am_d_05) * 100  # Percentage calculation

# Calculating "DM (D)" percentage value
dm_d_1_sum = df.iloc[:, dm_d_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
dm_d_05_sum = df.iloc[:, dm_d_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['DM (D)'] = (dm_d_1_sum + dm_d_05_sum) / (max_values_dm_d_1 + max_values_dm_d_05) * 100  # Percentage calculation

# Calculating "DM (S)" percentage value
dm_s_1_sum = df.iloc[:, dm_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
dm_s_05_sum = df.iloc[:, dm_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['DM (S)'] = (dm_s_1_sum + dm_s_05_sum) / (max_values_dm_s_1 + max_values_dm_s_05) * 100  # Percentage calculation

# Calculating "HB (D)" percentage value
hb_d_1_sum = df.iloc[:, hb_d_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
hb_d_05_sum = df.iloc[:, hb_d_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['HB (D)'] = (hb_d_1_sum + hb_d_05_sum) / (max_values_hb_d_1 + max_values_hb_d_05) * 100  # Percentage calculation

# Calculating "DLP (D)" percentage value
dlp_d_1_sum = df.iloc[:, dlp_d_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
dlp_d_05_sum = df.iloc[:, dlp_d_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['DLP (D)'] = (dlp_d_1_sum + dlp_d_05_sum) / (max_values_dlp_d_1 + max_values_dlp_d_05) * 100  # Percentage calculation

# Calculating "DLP (S)" percentage value
dlp_s_1_sum = df.iloc[:, dlp_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
dlp_s_05_sum = df.iloc[:, dlp_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['DLP (S)'] = (dlp_s_1_sum + dlp_s_05_sum) / (max_values_dlp_s_1 + max_values_dlp_s_05) * 100  # Percentage calculation

# Calculating "SV (S)" percentage value
sv_s_1_sum = df.iloc[:, sv_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
sv_s_05_sum = df.iloc[:, sv_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['SV (S)'] = (sv_s_1_sum + sv_s_05_sum) / (max_values_sv_s_1 + max_values_sv_s_05) * 100  # Percentage calculation

# Calculating "SV (A)" percentage value
sv_a_1_sum = df.iloc[:, sv_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
sv_a_05_sum = df.iloc[:, sv_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['SV (A)'] = (sv_a_1_sum + sv_a_05_sum) / (max_values_sv_a_1 + max_values_sv_a_05) * 100  # Percentage calculation

# Calculating "RP (S)" percentage value
rp_s_1_sum = df.iloc[:, rp_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
rp_s_05_sum = df.iloc[:, rp_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['RP (S)'] = (rp_s_1_sum + rp_s_05_sum) / (max_values_rp_s_1 + max_values_rp_s_05) * 100  # Percentage calculation

# Calculating "REG (S)" percentage value
reg_s_1_sum = df.iloc[:, reg_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
reg_s_05_sum = df.iloc[:, reg_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['REG (S)'] = (reg_s_1_sum + reg_s_05_sum) / (max_values_reg_s_1 + max_values_reg_s_05) * 100  # Percentage calculation

# Calculating "CM (D)" percentage value
cm_d_1_sum = df.iloc[:, cm_d_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
cm_d_05_sum = df.iloc[:, cm_d_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['CM (D)'] = (cm_d_1_sum + cm_d_05_sum) / (max_values_cm_d_1 + max_values_cm_d_05) * 100  # Percentage calculation

# Calculating "CM (S)" percentage value
cm_s_1_sum = df.iloc[:, cm_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
cm_s_05_sum = df.iloc[:, cm_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['CM (S)'] = (cm_s_1_sum + cm_s_05_sum) / (max_values_cm_s_1 + max_values_cm_s_05) * 100  # Percentage calculation

# Calculating "CM (A)" percentage value
cm_a_1_sum = df.iloc[:, cm_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
cm_a_05_sum = df.iloc[:, cm_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['CM (A)'] = (cm_a_1_sum + cm_a_05_sum) / (max_values_cm_a_1 + max_values_cm_a_05) * 100  # Percentage calculation

# Calculating "CAR (S)" percentage value
car_s_1_sum = df.iloc[:, car_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
car_s_05_sum = df.iloc[:, car_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['CAR (S)'] = (car_s_1_sum + car_s_05_sum) / (max_values_car_s_1 + max_values_car_s_05) * 100  # Percentage calculation

# Calculating "B2B (S)" percentage value
b2b_s_1_sum = df.iloc[:, b2b_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
b2b_s_05_sum = df.iloc[:, b2b_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['B2B (S)'] = (b2b_s_1_sum + b2b_s_05_sum) / (max_values_b2b_s_1 + max_values_b2b_s_05) * 100  # Percentage calculation

# Calculating "MEZ (S)" percentage value
mez_s_1_sum = df.iloc[:, mez_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
mez_s_05_sum = df.iloc[:, mez_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['MEZ (S)'] = (mez_s_1_sum + mez_s_05_sum) / (max_values_mez_s_1 + max_values_mez_s_05) * 100  # Percentage calculation

# Calculating "MEZ (A)" percentage value
mez_a_1_sum = df.iloc[:, mez_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
mez_a_05_sum = df.iloc[:, mez_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['MEZ (A)'] = (mez_a_1_sum + mez_a_05_sum) / (max_values_mez_a_1 + max_values_mez_a_05) * 100  # Percentage calculation

# Calculating "AP (S)" percentage value
ap_s_1_sum = df.iloc[:, ap_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
ap_s_05_sum = df.iloc[:, ap_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['AP (S)'] = (ap_s_1_sum + ap_s_05_sum) / (max_values_ap_s_1 + max_values_ap_s_05) * 100  # Percentage calculation

# Calculating "AP (A)" percentage value
ap_a_1_sum = df.iloc[:, ap_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
ap_a_05_sum = df.iloc[:, ap_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['AP (A)'] = (ap_a_1_sum + ap_a_05_sum) / (max_values_ap_a_1 + max_values_ap_a_05) * 100  # Percentage calculation

# Calculating "AM (S)" percentage value
am_s_1_sum = df.iloc[:, am_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
am_s_05_sum = df.iloc[:, am_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['AM (S)'] = (am_s_1_sum + am_s_05_sum) / (max_values_am_s_1 + max_values_am_s_05) * 100  # Percentage calculation

# Calculating "AM (A)" percentage value
am_a_1_sum = df.iloc[:, am_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
am_a_05_sum = df.iloc[:, am_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['AM (A)'] = (am_a_1_sum + am_a_05_sum) / (max_values_am_a_1 + max_values_am_a_05) * 100  # Percentage calculation

# Calculating "SS (A)" percentage value
ss_a_1_sum = df.iloc[:, ss_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
ss_a_05_sum = df.iloc[:, ss_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['SS (A)'] = (ss_a_1_sum + ss_a_05_sum) / (max_values_ss_a_1 + max_values_ss_a_05) * 100  # Percentage calculation

# Calculating "TRE (A)" percentage value
tre_a_1_sum = df.iloc[:, tre_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
tre_a_05_sum = df.iloc[:, tre_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['TRE (A)'] = (tre_a_1_sum + tre_a_05_sum) / (max_values_tre_a_1 + max_values_tre_a_05) * 100  # Percentage calculation

# Calculating "ENG (S)" percentage value
eng_s_1_sum = df.iloc[:, eng_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
eng_s_05_sum = df.iloc[:, eng_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['ENG (S)'] = (eng_s_1_sum + eng_s_05_sum) / (max_values_eng_s_1 + max_values_eng_s_05) * 100  # Percentage calculation

# Calculating "IW (S)" percentage value
iw_s_1_sum = df.iloc[:, iw_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
iw_s_05_sum = df.iloc[:, iw_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['IW (S)'] = (iw_s_1_sum + iw_s_05_sum) / (max_values_iw_s_1 + max_values_iw_s_05) * 100  # Percentage calculation

# Calculating "IW (A)" percentage value
iw_a_1_sum = df.iloc[:, iw_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
iw_a_05_sum = df.iloc[:, iw_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['IW (A)'] = (iw_a_1_sum + iw_a_05_sum) / (max_values_iw_a_1 + max_values_iw_a_05) * 100  # Percentage calculation

# Calculating "WP (S)" percentage value
wp_s_1_sum = df.iloc[:, wp_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
wp_s_05_sum = df.iloc[:, wp_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['WP (S)'] = (wp_s_1_sum + wp_s_05_sum) / (max_values_wp_s_1 + max_values_wp_s_05) * 100  # Percentage calculation

# Calculating "WP (A)" percentage value
wp_a_1_sum = df.iloc[:, wp_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
wp_a_05_sum = df.iloc[:, wp_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['WP (A)'] = (wp_a_1_sum + wp_a_05_sum) / (max_values_wp_a_1 + max_values_wp_a_05) * 100  # Percentage calculation

# Calculating "WIN (S)" percentage value
win_s_1_sum = df.iloc[:, win_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
win_s_05_sum = df.iloc[:, win_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['WIN (S)'] = (win_s_1_sum + win_s_05_sum) / (max_values_win_s_1 + max_values_win_s_05) * 100  # Percentage calculation

# Calculating "WIN (A)" percentage value
win_a_1_sum = df.iloc[:, win_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
win_a_05_sum = df.iloc[:, win_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['WIN (A)'] = (win_a_1_sum + win_a_05_sum) / (max_values_win_a_1 + max_values_win_a_05) * 100  # Percentage calculation

# Calculating "DWIN (D)" percentage value
dwin_d_1_sum = df.iloc[:, dwin_d_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
dwin_d_05_sum = df.iloc[:, dwin_d_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['DWIN (D)'] = (dwin_d_1_sum + dwin_d_05_sum) / (max_values_dwin_d_1 + max_values_dwin_d_05) * 100  # Percentage calculation

# Calculating "DWIN (S)" percentage value
dwin_s_1_sum = df.iloc[:, dwin_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
dwin_s_05_sum = df.iloc[:, dwin_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['DWIN (S)'] = (dwin_s_1_sum + dwin_s_05_sum) / (max_values_dwin_s_1 + max_values_dwin_s_05) * 100  # Percentage calculation

# Calculating "WM (D)" percentage value
wm_d_1_sum = df.iloc[:, wm_d_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
wm_d_05_sum = df.iloc[:, wm_d_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['WM (D)'] = (wm_d_1_sum + wm_d_05_sum) / (max_values_wm_d_1 + max_values_wm_d_05) * 100  # Percentage calculation

# Calculating "WM (S)" percentage value
wm_s_1_sum = df.iloc[:, wm_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
wm_s_05_sum = df.iloc[:, wm_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['WM (S)'] = (wm_s_1_sum + wm_s_05_sum) / (max_values_wm_s_1 + max_values_wm_s_05) * 100  # Percentage calculation

# Calculating "WM (A)" percentage value
wm_a_1_sum = df.iloc[:, wm_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
wm_a_05_sum = df.iloc[:, wm_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['WM (A)'] = (wm_a_1_sum + wm_a_05_sum) / (max_values_wm_a_1 + max_values_wm_a_05) * 100  # Percentage calculation

# Calculating "IF (S)" percentage value
if_s_1_sum = df.iloc[:, if_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
if_s_05_sum = df.iloc[:, if_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['IF (S)'] = (if_s_1_sum + if_s_05_sum) / (max_values_if_s_1 + max_values_if_s_05) * 100  # Percentage calculation

# Calculating "IF (A)" percentage value
if_a_1_sum = df.iloc[:, if_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
if_a_05_sum = df.iloc[:, if_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['IF (A)'] = (if_a_1_sum + if_a_05_sum) / (max_values_if_a_1 + max_values_if_a_05) * 100  # Percentage calculation

# Calculating "RMD (A)" percentage value
rmd_a_1_sum = df.iloc[:, rmd_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
rmd_a_05_sum = df.iloc[:, rmd_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['RMD (A)'] = (rmd_a_1_sum + rmd_a_05_sum) / (max_values_rmd_a_1 + max_values_rmd_a_05) * 100  # Percentage calculation

# Calculating "WTM (S)" percentage value
wtm_s_1_sum = df.iloc[:, wtm_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
wtm_s_05_sum = df.iloc[:, wtm_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['WTM (S)'] = (wtm_s_1_sum + wtm_s_05_sum) / (max_values_wtm_s_1 + max_values_wtm_s_05) * 100  # Percentage calculation

# Calculating "WTM (A)" percentage value
wtm_a_1_sum = df.iloc[:, wtm_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
wtm_a_05_sum = df.iloc[:, wtm_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['WTM (A)'] = (wtm_a_1_sum + wtm_a_05_sum) / (max_values_wtm_a_1 + max_values_wtm_a_05) * 100  # Percentage calculation

# Calculating "PF (D)" percentage value
pf_d_1_sum = df.iloc[:, pf_d_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
pf_d_05_sum = df.iloc[:, pf_d_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['PF (D)'] = (pf_d_1_sum + pf_d_05_sum) / (max_values_pf_d_1 + max_values_pf_d_05) * 100  # Percentage calculation

# Calculating "PF (S)" percentage value
pf_s_1_sum = df.iloc[:, pf_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
pf_s_05_sum = df.iloc[:, pf_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['PF (S)'] = (pf_s_1_sum + pf_s_05_sum) / (max_values_pf_s_1 + max_values_pf_s_05) * 100  # Percentage calculation

# Calculating "PF (A)" percentage value
pf_a_1_sum = df.iloc[:, pf_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
pf_a_05_sum = df.iloc[:, pf_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['PF (A)'] = (pf_a_1_sum + pf_a_05_sum) / (max_values_pf_a_1 + max_values_pf_a_05) * 100  # Percentage calculation

# Calculating "DLF (S)" percentage value
dlf_s_1_sum = df.iloc[:, dlf_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
dlf_s_05_sum = df.iloc[:, dlf_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['DLF (S)'] = (dlf_s_1_sum + dlf_s_05_sum) / (max_values_dlf_s_1 + max_values_dlf_s_05) * 100  # Percentage calculation

# Calculating "DLF (A)" percentage value
dlf_a_1_sum = df.iloc[:, dlf_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
dlf_a_05_sum = df.iloc[:, dlf_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['DLF (A)'] = (dlf_a_1_sum + dlf_a_05_sum) / (max_values_dlf_a_1 + max_values_dlf_a_05) * 100  # Percentage calculation

# Calculating "TM (S)" percentage value
tm_s_1_sum = df.iloc[:, tm_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
tm_s_05_sum = df.iloc[:, tm_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['TM (S)'] = (tm_s_1_sum + tm_s_05_sum) / (max_values_tm_s_1 + max_values_tm_s_05) * 100  # Percentage calculation

# Calculating "TM (A)" percentage value
tm_a_1_sum = df.iloc[:, tm_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
tm_a_05_sum = df.iloc[:, tm_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['TM (A)'] = (tm_a_1_sum + tm_a_05_sum) / (max_values_tm_a_1 + max_values_tm_a_05) * 100  # Percentage calculation

# Calculating "AF (A)" percentage value
af_a_1_sum = df.iloc[:, af_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
af_a_05_sum = df.iloc[:, af_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['AF (A)'] = (af_a_1_sum + af_a_05_sum) / (max_values_af_a_1 + max_values_af_a_05) * 100  # Percentage calculation

# Calculating "POA (S)" percentage value
poa_s_1_sum = df.iloc[:, poa_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
poa_s_05_sum = df.iloc[:, poa_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['POA (S)'] = (poa_s_1_sum + poa_s_05_sum) / (max_values_poa_s_1 + max_values_poa_s_05) * 100  # Percentage calculation

# Calculating "F9 (S)" percentage value
f9_s_1_sum = df.iloc[:, f9_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
f9_s_05_sum = df.iloc[:, f9_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['F9 (S)'] = (f9_s_1_sum + f9_s_05_sum) / (max_values_f9_s_1 + max_values_f9_s_05) * 100  # Percentage calculation

# Calculating "CF (S)" percentage value
cf_s_1_sum = df.iloc[:, cf_s_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
cf_s_05_sum = df.iloc[:, cf_s_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['CF (S)'] = (cf_s_1_sum + cf_s_05_sum) / (max_values_cf_s_1 + max_values_cf_s_05) * 100  # Percentage calculation

# Calculating "CF (A)" percentage value
cf_a_1_sum = df.iloc[:, cf_a_columns_1].sum(axis=1)  # Tier 1 (Multiplier 1.0)
cf_a_05_sum = df.iloc[:, cf_a_columns_05].sum(axis=1) * 0.5  # Tier 6 (Multiplier 0.5)
new_df['CF (A)'] = (cf_a_1_sum + cf_a_05_sum) / (max_values_cf_a_1 + max_values_cf_a_05) * 100  # Percentage calculation

# Printing new DataFrame with calculations.
print(new_df)

