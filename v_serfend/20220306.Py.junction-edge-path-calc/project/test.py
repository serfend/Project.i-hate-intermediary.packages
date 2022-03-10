import utils.xlsx_handler

def get_sample_data():
    result = []
    test_headers = ['id','name']
    test_rows = 100
    for x in range(test_rows):
        item = {}
        for col in test_headers:
            item[col] = f'{col}.{x}'
        result.append(item)
    return result

def test_xls_input():
    xls = utils.xlsx_handler.XlsxHandler('./configuration/data.xlsx')
    return xls.read('edge')
    
def test_xls_output():
    xls = utils.xlsx_handler.XlsxHandler('./output/result.xlsx')
    return xls.write(get_sample_data(),'test')
    
    
if __name__ == '__main__':
    c = test_xls_output()
    # c = test_xls_input()
    print(c)
    