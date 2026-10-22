"""FSTTCS 2022 Section 2 H_k family; supplied paper transcription."""

def hk(k):
    # Thejaswini, Ohlmann, Jurdzinski (FSTTCS 2022), Section 2: layers L_i = {u,v,w,x,y}, i = 1..k
    idx = {(n, i): 5 * (i - 1) + j for i in range(1, k + 1) for j, n in enumerate("uvwxy")}
    succ = {key: [] for key in idx}
    for i in range(1, k + 1):
        for a, b in "uv vu vx xw wv xy yx".split():
            succ[(a, i)].append((b, i))
        if i <= k - 2: succ[("u", i)].append(("y", i + 2))
        if i > 1: succ[("v", i)].append(("v", i - 1)); succ[("y", i)].append(("y", i - 1))
    lines = [f"parity {5*k-1};"]
    for (n, i), v in sorted(idx.items(), key=lambda kv: kv[1]):
        prio = i + 2 if n == "w" else i + 1
        even_owns = {"u", "x", "w"} if i % 2 == 0 else {"v", "y", "w"}
        owner = 0 if n in even_owns else 1
        lines.append(f"{v} {prio} {owner} {','.join(str(idx[s]) for s in succ[(n, i)])} \"{n}{i}\";")
    return "\n".join(lines) + "\n"
