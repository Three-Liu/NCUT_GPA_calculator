import bs4
from typing import List
import numpy as np


def load_html_table(pth = 'test.html'):
    with open(pth, 'r', encoding='utf-8') as fin:
        lines = fin.readlines()
        return ''.join(lines)


def gen_gpa_dict():
    # generate gpa mapping array
    matching = [
        [86, 100, 4],
        [81, 85, 3.7],
        [77, 80, 3.3],
        [73, 76, 3],
        [69, 72, 2.5],
        [65, 68, 2],
        [60, 64, 1],
        [0, 59, 0],
    ]

    # searching gpa score
    def _get_gpa(score):
        start = 0
        end = len(matching)
        mid = (end + start) // 2
        while start < end:
            mid_low = matching[mid][0]
            mid_high = matching[mid][1]
            if score >= mid_low and score <= mid_high:
                return matching[mid][-1]
            elif score < mid_low:
                start = mid + 1
            else:
                end = mid - 1
            mid = (end + start) // 2
        return matching[mid][-1]

    return [_get_gpa(i) for i in range(101)]


def analysis(html, gpa_table):    
    # calculate gpa for you
    soup = bs4.BeautifulSoup(html)
    summary = []
    
    # reduce the scope
    trs = soup.select("#p1 > table:nth-child(3) > tbody > tr")
    for idx, a in enumerate(trs):
        if idx == 0:
            # get title for each row
            name = a.select('td')[2].text  
            grade = a.select('td')[3].text
            score = a.select('td')[4].text
            print(f"{name:>10s}{grade:>10s}{score:>10s}")
        else:
            if a.select('td')[2].text.strip() == '':
                # row end
                break
            
            # get rest part with score in it        
            name = a.select('td')[2].text  
            grade = a.select('td')[3].text
            score = '100' if a.select('td')[4].text == '通过' else a.select('td')[4].text
            c = [name, float(grade), float(score), gpa_table[int(score)]]
            print(f"{name:>10s}{grade:>10s}{score:>10s}")
            summary.append(c)
            if a.select('td')[6].text.strip() != '':
                # one more column should be taken into account
                name = a.select('td')[7].text  
                grade = a.select('td')[8].text
                score = '100' if a.select('td')[4].text == '通过' else a.select('td')[4].text
                c = [name, float(grade), float(score), gpa_table[int(score)]]
                print(f"{name:>10s}{grade:>10s}{score:>10s}")
                summary.append(c)
    return summary

def aggregate(result):
    grade_vec = list(map(lambda c: c[1], result))
    gpa_vec = list(map(lambda c: c[-1], result))
    return np.array(grade_vec).T.dot(np.array(gpa_vec))/sum(grade_vec)

def processing(src):
    html = load_html_table(src)
    gpa_table = gen_gpa_dict()
    summary_analysis = analysis(html, gpa_table)
    result = aggregate(summary_analysis)
    print(f"result: {result}")
    
                
processing('test.html')

