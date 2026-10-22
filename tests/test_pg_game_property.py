#!/usr/bin/env python3
"""Compare normalization with an independent, seeded PGSolver parser."""

import os
from pathlib import Path
import random
import re
import shlex
import subprocess
import sys


def normalize(text):
    tokens = re.findall(r'"[^"]*"|[0-9]+|[A-Za-z]+|[,;]', text)
    position = 0

    def take(expected=None):
        nonlocal position
        value = tokens[position]
        position += 1
        assert expected is None or value == expected
        return value

    if tokens[0] == "parity":
        take("parity")
        int(take())
        take(";")
    if tokens[position] == "start":
        take("start")
        int(take())
        take(";")
    declarations = {}
    while position < len(tokens):
        vertex, priority, owner = (int(take()) for _ in range(3))
        successors = [int(take())]
        while tokens[position] == ",":
            take(",")
            successors.append(int(take()))
        name = take() if tokens[position].startswith('"') else None
        take(";")
        declarations[vertex] = priority, owner, successors, name
    lines = [f"parity {max(declarations)};\n"]
    for vertex, (priority, owner, successors, name) in sorted(declarations.items()):
        assert all(target in declarations for target in successors)
        lines.append(f"{vertex} {priority} {owner} " +
                     ",".join(map(str, successors)) +
                     (f" {name}" if name is not None else "") + ";\n")
    return "".join(lines)


def generated_games():
    rng = random.Random(685789)
    whitespace = [" ", "\t", "\r\n", "\n\t", "  ", "\v", "\f"]
    for case in range(120):
        count = rng.randint(1, 35)
        ids = list(range(count)) if case % 3 == 0 else rng.sample(range(500), count)
        if case % 5 == 0:
            ids[-1] = 2**64 - 1
        tokens = []
        if rng.randrange(2):
            tokens += ["parity", str(max(ids)), ";"]
        if rng.randrange(2):
            tokens += ["start", str(rng.choice(ids + [999])), ";"]
        declarations = ids + rng.choices(ids, k=rng.randrange(count + 1))
        if case % 4:
            rng.shuffle(declarations)
        for vertex in declarations:
            priority = rng.choice([0, 1, 2, 13, 100, 2**64 - 1])
            tokens += [str(vertex), str(priority), str(rng.randrange(2))]
            for edge in range(rng.randint(1, 8)):
                if edge:
                    tokens.append(",")
                tokens.append(str(rng.choice(ids)))
            if rng.randrange(2):
                name = "".join(rng.choices("ab ,;\\\r\n\t", k=rng.randrange(40)))
                tokens.append(f'"{name}"')
            tokens.append(";")
        text = "".join(rng.choice(whitespace) +
                       ("0" * rng.randrange(4) if token.isdigit() else "") + token
                       for token in tokens)
        if case % 2:
            text += rng.choice(whitespace)
        yield case, text


def main():
    binary = Path(sys.argv[1]).resolve()
    wrapper = shlex.split(os.environ.get("STRAHLER_TEST_WRAPPER", ""))
    for case, text in generated_games():
        result = subprocess.run([*wrapper, str(binary), "--normalize"],
                                input=text.encode("ascii"),
                                capture_output=True, timeout=30)
        assert result.returncode == 0, (case, text, result.stderr)
        expected = normalize(text).encode("ascii")
        assert result.stdout == expected, (case, text, result.stdout, expected)
        assert not result.stderr, (case, result.stderr)


if __name__ == "__main__":
    main()
