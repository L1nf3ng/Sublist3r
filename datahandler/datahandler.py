import collections
import re
from pyexcel_ods import get_data
from pyexcel_ods import save_data

def output_excel(data, filename):
    res = collections.OrderedDict()
    res.update({"Sheet1":data})
    save_data(filename, res)


def transform2excel(filename, outfile):
    """
    :function: txt后缀文件转换ods文档。
    :param filename: 文件名称
    """
    with open(filename) as file:
        origin = file.readlines()

    headers = ["域名" , "IP地址", "外网公开"]
    data = [ headers ]

    for line in origin:
        pattern = '(.*)\s+(.*)'
        tmp_res = re.search(pattern, line)
        domain, ip = tmp_res.group(1), tmp_res.group(2)
        data.append([domain, ip , "Yes"])

    output_excel(data, outfile)