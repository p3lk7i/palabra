# Palabra DDL Language Specification

**Author:** [Pablo427](https://github.com/palabra)  
**License:** [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)  

---

## 1. Introduction

Palabra DDL is a **hierarchical, level-based, schema-free data definition language**.  
It is designed to represent tree-structured data in a **compact, human-readable, and machine-parseable format**.  

Key features:

- **Schema-free:** Users can define any keys at any depth.  
- **Hierarchical:** Structure is determined by numeric levels.  
- **Flexible:** Works for AI tech trees, personal profiles, configurations, or any nested data.  
- **Whitespace-safe:** Numeric levels replace indentation.  

---

## 2. Syntax

Each line has the format: [level:key]value

- `level` → Numeric depth (≥1)  
- `key` → Optional identifier (can be empty)  
- `value` → Optional string  
- Level `N` must follow a parent at level `N-1`  
- Repeated keys are allowed  
- Empty values are allowed  
- Optional comments start with `//`

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
[4:Engine]Electric
[4:Battery]82 kWh
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
[3:skills]Masonry
[3:skills]Carpentry
[3:skills]Operating Heavy Machinery
[3:certifications]OSHA Safety Training
[2:contact]Phone
[3:number]+1-555-123-4567
[2:hobbies]Fishing
[2:hobbies]Basketball
```
### 3.4 Post request
```
[1:class]HTTPRequest
[2:method]POST
[2:url]https://api.example.com/users
[2:headers]
[3:Content-Type]application/json
[3:Authorization]Bearer abc123token
[2:body]
[3:name]Jan Iksiński
[3:email]jan.iksinski@example.com
[3:job]Construction Worker
[3:location]Sandomierz, Poland
[2:timeout]30
[2:retry]3
```

