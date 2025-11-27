import json
import csv

with open('purchase_log.txt', 'r', encoding='utf-8') as purchase, open('visit_log__1_.csv') as visit, \
        open('funnel.csv', 'w', newline='') as result:
    purchase_log = {}
    for l in purchase:
        jl = json.loads(l.strip())
        user_id = jl.get("user_id")
        category = jl.get("category")
        if user_id != 'user_id':
            purchase_log[user_id] = category
    inp = csv.reader(visit)
    out = csv.writer(result)
    out.writerow(("user_id", "source", "category"))
    for i in inp:
        if i[0] in purchase_log:
            out.writerow((i[0], i[1], purchase_log[i[0]]))
