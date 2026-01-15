# Palabra427 (PLB427) DDL Language Specification

**Author:** [Pablo427](https://github.com/palabra)  
**License:** Apache Version 2.0

---

## 1. Introduction

Palabra DDL is a **hierarchical, level-based, schema-free data definition language**. It belongs to the same family as JSON and YAML.
It is designed to represent tree-structured data in a **compact, human-readable, and machine-parseable format**. Allows mini grammar remapping.


Key features:

- **Schema-free:** Users can define any keys at any depth.  
- **Hierarchical:** Structure is determined by numeric levels.  
- **Flexible:** Works for AI tech trees, personal profiles, configurations, or any nested data.  
- **Whitespace-safe:** Numeric levels replace indentation.  

---

## 2. Syntax

Each line has the format : **[level:key]value** you can also use : **[level:key1|key2|...|keyN]value** for many keys.

- `level` → Numeric depth (≥1)  
- `key` → Optional identifier (can be empty)  
- `value` → Optional string  
- Level `N` must follow a parent at level `N-1`  
- Repeated keys are allowed  
- Empty values are allowed  
- Optional comments start with `//`

The format definition can be changed (grammar remapping). If you put first line as : (level=key1,key2,...,keyN])value format syntax changes :

e.g file exerpt : 
```
FORMAT (level=key1,key2,...,keyN)value 
(1=)Cars
  (2=Brand,Manufacutrer)Tesla
    (3=Model)Model S
```
for standard format you don't need FORMAT key word in your files.

Key on the same level can address many values. That enable you to create many to many relations :

```
[1:A,B,C] 123
[1:A] 333
  [2:B] 100
```
- A point to 123 and 333 
- B point to 123 on level 1 
- B point to 100 on level 2 

## 3. Examples

### 3.1 Describe car brands 
```
[1:]Cars
    [2:Brand]Tesla
        [3:Model]Model S
            [4:Engine]Electric
            [4:Battery]100 kWh
            [4:Autopilot]Full Self-Driving
        [3:Model]Model 3
            [4:Engine|Motor]Electric
            [4:Battery|Accumlator|Power]82 kWh
            [4:Autopilot]Partial
    [2:Brand]Toyota
        [3:Model]Corolla
            [4:Engine]Gasoline
            [4:Transmission]Automatic
            [4:Features]Lane Assist
        [3:Model]Prius
            [4:Engine]Hybrid
            [4:Battery]1.3 kWh
            [4:Features]Eco Mode
```
## Ready-to-use parsers (zero dependencies)

- Python → 47 lines → `palabra/py/parse.py`
- JavaScript → 39 lines → `palabra/js/parse.js`

Just copy the file and `parse_plb(your_text)` → proper tree.

### 3.3 Describe person 
```
[1:class]Person
[2:ident]john.doe@example.com
[2:personal]John Doe
[3:age]35
[3:gender]Male
[3:location]Dallas, USA
[2:job]Construction Worker
[3:position]Site Worker
[3:experience]12 years
[3:skills]Masonry,Carpentry,Operating Heavy Machinery
[3:certifications]OSHA Safety Training
[2:contact]Phone
[3:number]+1-555-123-4567
[2:hobbies]Fishing
[2:hobbies]Basketball
```
### 3.4 Prompt AI in structured manner 
```
[1:Task]Create a production-ready server configuration blueprint
    [2:Target]Nginx + Certbot + Node.js app behind HTTPS
    [2:OS]Ubuntu 24.04 LTS (or Debian 12)
    [2:Domain]example.com (with www redirect)
    [2:Security]A+ on SSL Labs, HSTS, basic DDoS hardening
    [2:Extras]
        [3:Feature]Automatic HTTPS with Let’s Encrypt (auto-renew)
        [3:Feature]Brotli + Zstd compression
        [3:Feature]HTTP/3 (QUIC) enabled
        [3:Feature]Rate limiting (10 r/s burst 20)
        [3:Feature]Cache static assets 30 days
        [3:Feature]Separate error pages (403, 404, 500)
        [3:Feature]Fail2ban rules for SSH + Nginx bad bots
    [2:Output format]One single nginx.conf file + short setup script
    [2:Style]Zero comments except section headers, must work copy-paste
    [2:Bonus]Include a one-liner to test the whole config with nginx -t
```
# Palabra search

For search we user Query Vector e.g : 
```
[4:CPU,RAM] - this search on level 4 for keys CPU & RAM
```
if you want search all levels : 
```
[*:CPI,RAM] search on all levels. You can use regular expessions too :
[*:\b(CPU|GPU)\b|RAM]
```

[Brand]Toyota[4:Battery].*]" // find Brand=Toyota and search on level 4 for Battery.

This way we can nest queries and combine them with reg-ex. So palabra let to describe 
the data and describe the search.

# Why Palabra (PLB) DDL is for you ?

## 1. Human-Readable
- Instead of complex braces, commas, or indentation rules, you just use `[level:key]value`.  
- Even someone new to your language can quickly understand the hierarchy.

## 2. Flexible
- You can describe anything: people, cars, AI tech trees, HTTP requests, etc.  
- Keys and values are free-form, so users can adapt it to any domain.
- The mini grammar can be remapped in line filter.
- You can use multiple keys to access your values.

## 3. Hierarchical and Structured
- Each level number clearly indicates parent-child relationships.  
- Lists are naturally represented by repeated keys at the same level.  
- It’s easy to parse and visualize.

## 4. Lightweight
- Minimal punctuation and rules.  
- Very compact compared to JSON or XML.  
- Easy to write by hand or generate programmatically.

## 5. GitHub-Friendly
- With proper code blocks and indentation, your examples render beautifully on GitHub.  
- Makes it perfect for specifications, demos, or structured examples.

and because simplicitas praevalet ...

EOF
