def parse_plb(text: str) -> list[dict]:
    """Parse Palabra (.plb) text → list of root nodes (each node is a dict with children)"""
    roots = []
    stack = [roots]  # roots is a list, everything else will be dicts with "_children"
    
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("//"):
            continue
            
        # Extract [level:key]value
        if not line.startswith("["):
            raise ValueError(f"Line must start with [: {raw_line}")
        end = line.find("]")
        if end == -1:
            raise ValueError(f"Missing ] in: {raw_line}")
        
        header = line[1:end]
        value = line[end+1:].strip()
        
        try:
            level_str, key = (header.split(":", 1) + [""])[:2]
            level = int(level_str)
        except:
            raise ValueError(f"Bad header [level:key] in: {raw_line}")
        
        node = {"_key": key, "_value": value or None, "_children": []}
        
        # Pop stack until correct parent level
        while len(stack) > level:
            stack.pop()
        if len(stack) < level:
            raise ValueError(f"Level jump too big: {level} after {len(stack)}")
        
        stack[-1].append(node)          # add to current parent
        stack.append(node["_children"]) # push children list for next level
    
    return roots
