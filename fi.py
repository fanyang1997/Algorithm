

def back_testing(fund_symbol, start_date, end_date):
    pass

def fund_strategy(fund_data):
    cycle_days = 7
    start_date = "2018-01-01"
    end_date = "2022-01-01"
    total_invest = 0
    invest_cycle = (end_date - start_date) // cycle_days
    const_fixed_invest = 1000
    nav = fund_nav("000001", date=start_date) # 2
    shares = const_fixed_invest // nav # 500 1000/2=500 shares
    target_invest = 1000
    nav_list = []
    nav_list.append(nav)
    total_buy = 0
    for i in range(1, invest_cycle):
        nav = fund_nav("000001", date=start_date + i * cycle_days)
        # cur_nav = 0.8
        # cur_value = 0.8 * 500 = 400
        cur_value = nav * shares
        target_invest = target_invest * i # 2000  2000-400=1600
        target_buy = target_invest - cur_value
        total_buy += target_buy
        if target_buy > 0:
            buy_funds(symbol="000001", target_buy=target_buy)
        else:
            do_nothing()
        nav_list.append(nav)


def fund_nav(fund_symbol, date):
    nav = get_fund_nav(fund_symbol, date)
    return nav

def total_revenue(fund_symbol, start_date, end_date):
    start_nav = fund_nav(fund_symbol, start_date)
    end_nav = fund_nav(fund_symbol, end_date)
    total_revenue = (end_nav - start_nav) / start_nav
    return total_revenue

# Annualized Return Rate
def annual_return_rate(total_revenue, invest_cycle):
    annual_return_rate = total_revenue ** (1 / invest_cycle) - 1
    return annual_return_rate