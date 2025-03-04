#entropy calculation
def e(d, t):
    v = [r[t] for r in d]
    f = {}
    for x in v:
        f[x] = f.get(x, 0) + 1
    s = len(d)
    e = 0
    for c in f.values():
        p = c / s
        e -= p * log2(p)
    return e
#log to the base 2 calculation
def log2(x):
    from math import log
    return log(x, 2)
#splitting
def sp(d, a, v):
    return [r for r in d if r.get(a) == v]
#finding best feature using information gain
def ba(d, at, t):
    be = e(d, t)
    mg = -1
    b = None
    for a in at:
        vals = set(r.get(a) for r in d if a in r and r.get(a) is not None)
        we = 0
        for v in vals:
            sub = sp(d, a, v)
            we += (len(sub) / len(d)) * e(sub, t)
        g = be - we
        if g > mg:
            mg = g
            b = a
    return b
#Construction of decision tree
def bt(d, at, t):
    tv = [r[t] for r in d]
    if len(set(tv)) == 1:
        return tv[0]
    if not at:
        return max(set(tv), key=tv.count)
    b = ba(d, at, t)
    if b is None: 
        return max(set(tv), key=tv.count)
    tr = {b: {}}
    vals = set(r.get(b) for r in d if b in r and r.get(b) is not None)
    for v in vals:
        sub = sp(d, b, v)
        tr[b][v] = bt(sub, [x for x in at if x != b], t)
    return tr
#classification using decision tree
def cl(tr, ins):
    if type(tr) is not dict:  
        return tr
    a = list(tr.keys())[0]
    v = ins.get(a, None)
    sub = tr[a].get(v, "Unknown")
    return cl(sub, ins) if type(sub) is dict else sub
#dataset
d = [
    {"C": 10, "G": "O", "P": "Good"},
    {"C": 10, "G": "A+", "P": "Good"},
    {"C": 10, "G": "A", "P": "Good"},
    {"C": 9, "G": "O", "P": "Good"},
    {"C": 9, "G": "A+", "P": "Good"},
    {"C": 9, "G": "A", "P": "Good"},
    {"C": 8, "G": "O", "P": "Bad"},
    {"C": 8, "G": "A+", "P": "Bad"},
    {"C": 8, "G": "A", "P": "Bad"},
    {"C": 9, "G": "A", "P": "Good"},
]
a = ["C", "G"]
t = "P"
tr = bt(d, a, t)
print("Decision Tree:", tr)
# Classify
sample_instance = {"C": 10, "G": "A+"}
classification = cl(tr, sample_instance)
print("Classification for instance", sample_instance, ":", classification)