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


def hk_coordinates(k):
    """Figure 2: one row per layer, columns u/v/w/x/y, w raised."""
    return {5 * (i - 1) + j: (j, k - i - (0.3 if j == 2 else 0))
            for i in range(1, k + 1) for j in range(5)}


# Figure 1, transcribed independently of the solver; ε11 is the empty child.
# Bounds are the package's normalized solver priorities (input minus two here).
PAPER_FIG1 = dict(h=4, H=[], T=[], S=[], children=[
    dict(h=2, H=[0, 1], T=[], S=[2], children=[
        dict(h=0, H=[], T=[], S=[], children=[])]),
    dict(h=2, H=[3, 4], T=[], S=[], children=[
        dict(h=0, H=[5, 6], T=[], S=[7], children=[]),
        dict(h=0, H=[8, 9], T=[], S=[], children=[])])])

EXPECTED_CALLS = {
    'zielonka': [10, 50, 218, 898, 3626, 14546, 58234, 232994],
    'zielonka-sym': [7, 23, 47, 83, 131, 191, 263, 347],
}


def count_calls(text, algorithm):
    """Count through the documented C ABI, without retaining millions of events.

    The regular Python trace deliberately retains its entire event list. This
    counting observer keeps the live H_16 table small without changing the solver.
    """
    import ctypes as C
    import strahler
    from strahler import _native

    # Reuse the package's ABI-checked loader and signatures for wheel/editable installs.
    library = _native.library()
    pointer = C.c_void_p
    game, result, error = pointer(), pointer(), pointer()
    count = 0
    errors = []

    @_native.Callback
    def observe(context, line, length):
        nonlocal count
        try:
            # shortcut: JSON writer puts event first; update if its line prefix changes.
            count += C.string_at(line, min(length, 16)) == b'{"event":"call",'
            return 1
        except BaseException as exc:
            errors.append(exc)
            return 0

    def require(status):
        if errors:
            raise errors[0]
        if status:
            message = C.string_at(error).decode('utf-8', 'replace') if error.value else 'Native allocation failure'
            if status == 6:
                raise MemoryError(message)
            raise strahler.StrahlerError(message, status)

    try:
        encoded = text.encode('utf-8')
        require(library.strahler_game_parse(encoded, len(encoded), C.byref(game), C.byref(error)))
        flags = (C.c_char_p * 2)(f'--algorithm={algorithm}'.encode(), b'--trace-limit=10000000')
        require(library.strahler_decompose(game, flags, 2, observe, None, C.byref(result), C.byref(error)))
        return count
    finally:
        library.strahler_game_free(game)
        library.strahler_free(result)
        library.strahler_free(error)
