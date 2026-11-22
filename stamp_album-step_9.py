# === Stage 9: Поиск по нескольким словам ===
# Project: StampAlbum
def parse_search_terms(text):
    terms = []
    for token in text.replace("-", " -").split():
        if token.startswith("-"):
            terms.append("-" + token[1:])
        else:
            terms.append(token)
    return terms


def build_query(terms):
    if not terms:
        return None
    query = "("
    for term in terms:
        if not term:
            continue
        if term.startswith("-"):
            query += "(NOT " + term[1:] + ")"
        else:
            query += "(" + term + ")"
        query += " "
    query += ")"
    return query


def search_stamps(stamps, query):
    if not query:
        return list(stamps)
    return [stamp for stamp in stamps if query in stamp.to_string()]
