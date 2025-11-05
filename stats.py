def word_count(s: str) -> int:
    return len(s.split())


def char_count_grouped(s: str) -> dict[str, int]:
    res = {}

    for char in s:
        c = char.lower()
        if not res.get(c):
            res[c] = 1
        else:
            res[c] += 1

    return res


def sort_dict_vals(d: dict[str, int]) -> list[dict[str, str | int]]:
    res = []
    for key, val in d.items():
        dv = {"char": key, "count": val}
        res += [dv]

    return sorted(res, key=lambda x: x.get("count") or float("-inf"), reverse=True)
