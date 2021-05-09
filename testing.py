def calculate(data_list, price):
    p_l = []
    m_l = []
    min_price = '0'
    comp_price = '0'
    comp = 'Seller name not available'
    for i in data_list:
        if i['price'] != '0':
            p_l.append(i['price'])
            m_l.append((i['merchant'], i['price']))
    try:
        p_l.sort()
        min_price = p_l[0]
        for i in m_l:
            if i[0] == min_price:
                comp = i[1]
                break
            else:
                comp = 'Seller name not available'
    except Exception as e:
        print(e)

    