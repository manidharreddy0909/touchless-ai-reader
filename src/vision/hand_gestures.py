def classify(features):
    thumb_index = features["thumb_index"]
    index_middle = features["index_middle"]
    palm_size = features["palm_size"]

    # Pinch (Click)
    if thumb_index < palm_size * 0.35:
        return "PINCH"

    # Two fingers (Scroll)
    if index_middle > palm_size * 0.6:
        return "TWO_FINGERS"

    # Open palm (Resume)
    if thumb_index > palm_size * 0.8 and index_middle > palm_size * 0.8:
        return "PALM"

    # Fist (Pause)
    if thumb_index < palm_size * 0.4 and index_middle < palm_size * 0.4:
        return "FIST"

    return "INDEX"
