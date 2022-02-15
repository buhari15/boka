import numpy as np
import h5py
import pandas as pd

# Nigeria Stock Exchange
path_first_st_nigeria = '/Users/buhariabubakar/PycharmProjects/boka/web_mining/web_mining/spiders/stock_ng_first.csv'
read_csv_st_ng_fr = pd.read_csv(path_first_st_nigeria)
first_data_stock_nigeria = np.array(read_csv_st_ng_fr, dtype='a25')

path_second_st_nigeria = '/Users/buhariabubakar/PycharmProjects/boka/web_mining/web_mining/spiders/stock_ng_second.csv'
read_csv_st_ng_sd = pd.read_csv(path_second_st_nigeria)
second_data_stock_nigeria = np.array(read_csv_st_ng_sd, dtype='a25')

path_third_st_nigeria = '/Users/buhariabubakar/PycharmProjects/boka/web_mining/web_mining/spiders/stock_ng_third.csv'
read_csv_st_ng_th = pd.read_csv(path_third_st_nigeria)
third_data_stock_nigeria = np.array(read_csv_st_ng_th, dtype='a25')

path_fourth_st_nigeria = '/Users/buhariabubakar/PycharmProjects/boka/web_mining/web_mining/spiders/stock_ng_fourth.csv'
read_csv_st_ng_ft = pd.read_csv(path_third_st_nigeria)
fourth_data_stock_nigeria = np.array(read_csv_st_ng_ft, dtype='a25')

# Central Bank of Nigeria
path_first_cbn_nigeria = '/Users/buhariabubakar/PycharmProjects/boka/web_mining/web_mining/spiders/cbn_rate_first.csv'
read_csv_cbn_ng_fr = pd.read_csv(path_first_cbn_nigeria)
first_data_rate_nigeria = np.array(read_csv_cbn_ng_fr, dtype='a25')

path_second_cbn_nigeria = '/Users/buhariabubakar/PycharmProjects/boka/web_mining/web_mining/spiders/cbn_rate_second.csv'
read_csv_cbn_ng_sd = pd.read_csv(path_second_cbn_nigeria)
second_data_rate_nigeria = np.array(read_csv_cbn_ng_sd, dtype='a25')

path_third_cbn_nigeria = '/Users/buhariabubakar/PycharmProjects/boka/web_mining/web_mining/spiders/cbn_rate_third.csv'
read_csv_rate_ng_th = pd.read_csv(path_third_cbn_nigeria)
third_data_rate_nigeria = np.array(read_csv_rate_ng_th, dtype='a25')

path_fourth_cbn_nigeria = '/Users/buhariabubakar/PycharmProjects/boka/web_mining/web_mining/spiders/cbn_rate_fourth.csv'
read_csv_rate_ng_ft = pd.read_csv(path_fourth_cbn_nigeria)
fourth_data_rate_nigeria = np.array(read_csv_rate_ng_ft, dtype='a25')

# UAE Stock

path_first_st_uae = '/Users/buhariabubakar/PycharmProjects/boka/web_mining/web_mining/spiders/stock_uae_first.csv'
read_csv_st_uae_fr = pd.read_csv(path_first_st_uae)
first_data_stock_uae = np.array(read_csv_st_uae_fr, dtype='a25')

path_second_st_uae = '/Users/buhariabubakar/PycharmProjects/boka/web_mining/web_mining/spiders/stock_uae_second.csv'
read_csv_st_uae_sd = pd.read_csv(path_second_st_uae)
second_data_stock_uae = np.array(read_csv_st_uae_sd, dtype='a25')

path_third_st_uae = '/Users/buhariabubakar/PycharmProjects/boka/web_mining/web_mining/spiders/stock_uae_third.csv'
read_csv_st_uae_th = pd.read_csv(path_third_st_uae)
third_data_stock_uae = np.array(read_csv_st_uae_th, dtype='a25')

path_fourth_st_uae = '/Users/buhariabubakar/PycharmProjects/boka/web_mining/web_mining/spiders/stock_uae_fourth.csv'
read_csv_st_uae_ft = pd.read_csv(path_fourth_st_uae)
fourth_data_stock_uae = np.array(read_csv_st_uae_ft, dtype='a25')

# UAE Rate
path_first_rate_uae = '/Users/buhariabubakar/PycharmProjects/boka/web_mining/web_mining/spiders/rate_uae_first.csv'
read_csv_rate_uae_fr = pd.read_csv(path_first_rate_uae)
first_data_rate_uae = np.array(read_csv_rate_uae_fr, dtype='a25')

path_second_rate_uae = '/Users/buhariabubakar/PycharmProjects/boka/web_mining/web_mining/spiders/rate_uae_second.csv'
read_csv_rate_uae_sd = pd.read_csv(path_second_rate_uae)
second_data_rate_uae = np.array(read_csv_rate_uae_sd, dtype='a25')

path_third_rate_uae = '/Users/buhariabubakar/PycharmProjects/boka/web_mining/web_mining/spiders/rate_uae_third.csv'
read_csv_rate_uae_th = pd.read_csv(path_third_rate_uae)
third_data_rate_uae = np.array(read_csv_rate_uae_th, dtype='a25')

path_fourth_rate_uae = '/Users/buhariabubakar/PycharmProjects/boka/web_mining/web_mining/spiders/rate_uae_fourth.csv'
read_csv_rate_uae_ft = pd.read_csv(path_fourth_rate_uae)
fourth_data_rate_uae = np.array(read_csv_rate_uae_ft, dtype='a25')

with h5py.File('/Users/buhariabubakar/PycharmProjects/boka/web_mining/web_mining/scrape_data.h5', 'w') as hdf:
    UAECENTRALBANK = hdf.create_group('UAECentralBank')
    UAECENTRALBANK.create_dataset('ft_data_rate_uae', data=first_data_rate_uae)
    UAECENTRALBANK.create_dataset('sd_data_rate_uae', data=second_data_rate_uae)
    UAECENTRALBANK.create_dataset('td_data_rate_uae', data=third_data_rate_uae)
    UAECENTRALBANK.create_dataset('fth_data_rate_uae', data=fourth_data_rate_uae)

    UAECENTRALBANK.attrs['title'] = "The dataset in this group contain the exchange rate of UAE Central Bank"

    # UAE Stock Exchange
    UAESTOCK = hdf.create_group('UAEStockExchange')
    UAESTOCK.create_dataset('ft_data_stock_uae', data=first_data_stock_uae)
    UAESTOCK.create_dataset('sd_data_stock_uae', data=second_data_stock_uae)
    UAESTOCK.create_dataset('td_data_stock_uae', data=third_data_stock_uae)
    UAESTOCK.create_dataset('fth_data_stock_uae', data=fourth_data_stock_uae)

    UAESTOCK.attrs['title'] = "The dataset in this group contain the stock exchange of UAE"

    # Nigeria Exchange Rate
    CBNRATES = hdf.create_group('NigeriaExchangeRate')
    CBNRATES.create_dataset('ft_data_rate_cbn', data=first_data_rate_nigeria)
    CBNRATES.create_dataset('sd_data_rate_cbn', data=second_data_rate_nigeria)
    CBNRATES.create_dataset('td_data_rate_cbn', data=third_data_rate_nigeria)
    CBNRATES.create_dataset('fth_data_rate_cbn', data=fourth_data_rate_nigeria)

    CBNRATES.attrs['title'] = "The dataset in this group contain Nigerian Exchange rate"
    # Nigeria Stock Exchange
    STOCKNIGERIA = hdf.create_group('NigeriaStockExchange')
    STOCKNIGERIA.create_dataset('ft_stock_data_ng', data=first_data_stock_nigeria)
    STOCKNIGERIA.create_dataset('sd_stock_data_ng', data=second_data_stock_nigeria)
    STOCKNIGERIA.create_dataset('td_stock_data_ng', data=third_data_stock_nigeria)
    STOCKNIGERIA.create_dataset('fth_stock_data_ng', data=fourth_data_stock_nigeria)

    STOCKNIGERIA.attrs['title'] = "The dataset in this group contain Nigerian stock Exchange data"

